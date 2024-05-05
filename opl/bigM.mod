/*********************************************
 * OPL 22.1.1.0 Model
 * Authors: Vincent Olesen & Joakim Svensson
 * Creation Date: Apr 24, 2024 at 10:51:51 AM
 *********************************************/

execute {
  cplex.epgap = 0.01;
  cplex.tilim = 1800;
}

// Parameters
int x = ...;  // Width constraint
int y = ...;  // Height constraint
int c = ...;  // Capacity or weight limit

range W = 1..x;
range H = 1..y;

int n = ...;  // Number of items

range P = 1..n;  // Range of products

int p[i in P] = ...;  // Profit for product i
int w[i in P] = ...;  // Weight of product i
int s[i in P] = ...;  // Side length of square box i

// Decision variables
dvar boolean X[i in P]; // 1 if product i is selected, 0 otherwise
dvar int yc[i in P]; // y-coordinate of bottom left corner of product i
dvar int xc[i in P]; // x-coordinate of bottom left corner of product i

// Objective function to maximize total profit
maximize sum(i in P) p[i] * X[i];

// Constraints
subject to {
    // Ensure the total weight of selected products does not exceed the capacity
    maxWeight:
        sum(i in P) w[i] * X[i] <= c;

    // Each product (corner) must fit within the boundary when placed
    cornerPlacement:
        forall(i in P) {
            xc[i] + s[i] - 1 <= x;
            yc[i] + s[i] - 1 <= y;    
    }

    // Prevent overlapping of products
    // If two products are selected, they cannot overlap
    // That is, one product must be to the left, right, above, or below the other
    noOverlap:
        forall(i in P, j in P: i < j)
            (X[i] == 1 && X[j] == 1) =>
            ( xc[i] + s[i] <= xc[j]
            || xc[j] + s[j] <= xc[i]
            || yc[i] + s[i] <= yc[j]
            || yc[j] + s[j] <= yc[i]);
}
