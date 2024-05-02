/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Joakim Svensson
 * Creation Date: Apr 24, 2024 at 11:09:41 AM
 *********************************************/

execute {
  cplex.epgap = 0.01;
  cplex.tilim = 1800;
}

int       x = ...;  // Height of the suitcase.
int       y = ...;  // Width of the suitcase.
int       c = ...;  // Capacity of the suitcase.

int       n = ...;  // Number of products.
int p[1..n] = ...;  // Prices of the products.
int w[1..n] = ...;  // Weights of the products.
int s[1..n] = ...;  // Sides of the boxes of the products.

// Define here your decision variables and
// any other auxiliary program variables you need.
// You can run an execute block if needed.

//>>>>>>>>>>>>>>>>
dvar boolean X[1..n];  // Decision variable for product selection.
dvar int x_pos[1..n] in 0..x; // x-coordinates of products in the suitcase, constrained within 0 to x.
dvar int y_pos[1..n] in 0..y; // y-coordinates of products in the suitcase, constrained within 0 to y.
int M = 10000;         // Large constant for the big-M method.
//<<<<<<<<<<<<<<<<

maximize  // Write here the objective function.
//>>>>>>>>>>>>>>>>
sum(i in 1..n) p[i] * X[i];
//<<<<<<<<<<<<<<<<

subject to {
    // Write here the constraints.
    //>>>>>>>>>>>>>>>>
    
    // Weight constraint
    sum(i in 1..n) w[i] * X[i] <= c;

    // Boundary constraints
    forall(i in 1..n) {
        x_pos[i] + s[i] * X[i] <= x;
        y_pos[i] + s[i] * X[i] <= y;
    }

    // Non-overlapping constraints using big-M method
    forall(i in 1..n)
        forall(j in i+1..n)
            if (i != j) {
                (x_pos[i] + s[i] <= x_pos[j] + M * (1 - X[i])) ||
                (x_pos[j] + s[j] <= x_pos[i] + M * (1 - X[j])) ||
                (y_pos[i] + s[i] <= y_pos[j] + M * (1 - X[i])) ||
                (y_pos[j] + s[j] <= y_pos[i] + M * (1 - X[j]));
            }

    //<<<<<<<<<<<<<<<<
}

// You can run an execute block if needed.

//>>>>>>>>>>>>>>>>

//<<<<<<<<<<<<<<<<


 