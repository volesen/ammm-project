/*********************************************
 * OPL 22.1.1.0 Model
 * Authors: Vincent Olesen & Joakim Svensson
 * Creation Date: Apr 24, 2024 at 10:51:51 AM
 *********************************************/

execute {
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

int M = x + y;

// Decision variables
dvar boolean X[i in P]; // 1 if product i is selected, 0 otherwise
dvar int xc[i in P] in W; // x-coordinate of bottom left corner of product i
dvar int yc[i in P] in H; // y-coordinate of bottom left corner of product i

dvar boolean left[i in P, j in P];
dvar boolean below[i in P, j in P];

// Objective function to maximize total profit
maximize sum(i in P) p[i] * X[i];

// Constraints
subject to {
    // Ensure the total weight of selected products does not exceed the capacity
    maxWeight:
        sum(i in P) w[i] * X[i] <= c;

    // Each product must fit within the x-dimension boundary when placed
    cornerPlacement:
        forall(i in P) {
            xc[i] + s[i] - 1 <= x;
            yc[i] + s[i] - 1 <= y;
     	}

    // Prevent overlapping of products
    // If two products are not selected, they cannot overlap
    // That is, one product must be to the left, right, above, or below the other
    // i < j:  4611
    // i != j: 4611
    forall(i in P, j in P: i < j) {
        xc[i] + s[i] <= xc[j] + x * (1 - left[i,j]);
        xc[j] + s[j] <= xc[i] + x * (1 - left[j,i]);
        yc[i] + s[i] <= yc[j] + y * (1 - below[i,j]);
        yc[j] + s[j] <= yc[i] + y * (1 - below[j,i]);
        left[i,j] + below[i,j] + left[j,i] + below[j,i] >= X[i] + X[j] - 1;
    }
}
