/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Vincent Olesen & Joakim Svensson
 * Creation Date: Apr 24, 2024 at 10:51:51 AM
 *********************************************/

execute {
  cplex.epgap = 0.01;
  cplex.tilim = 1800;
}

int x =  ...;
int y =  ...;
int c =  ...;

range W = 1..x;
range H = 1..y;

int n =  ...;

range P = 1..n;

int p[k in P] = ...;
int w[k in P] = ...;
int s[k in P] = ...; // Side length (square box)


// Descision variables
dvar boolean x_ijp[i in W, j in H, k in P];
dvar boolean y_ijp[i in W, j in H, k in P];

// x_ijp[i, j, k] = 1 if bottom left corner of product k is at cell (i, j)
// y_ijp[i, j, k] = 1 if cell (i, j) is occupied by product k

maximize sum(i in W, j in H, k in P) p[k] * x_ijp[i, j, k];

subject to {
	maxOneCornerPerCell:
		forall(i in W, j in H)
			sum(k in P) x_ijp[i, j, k] <= 1;
	
	maxOneCornerPerProduct:
		forall(k in P)
			sum(i in W, j in H) x_ijp[i, j, k] <= 1;

	maxOneProductPerCell:
		forall(i in W, j in H)
			sum(k in P) y_ijp[i, j, k] <= 1;

	// Link x_ijp and y_ijp
	linkXandY:
		forall(i in W, j in H, k in P)
			forall(ii in 0..s[k]-1, jj in 0..s[k]-1: i+ii <= x && j+jj <= y)
				x_ijp[i, j, k] <= y_ijp[i+ii, j+jj, k];

	// Constrain corner placement (square has to fit in the grid)
	// TODO: Why  -1: Because we start at 1
	cornerPlacement:
		forall(k in P)
			forall(i in W, j in H: i + s[k] - 1 > x || j + s[k] - 1 > y)
				x_ijp[i, j, k] == 0;

	// Maximum weight constraint
	maxWeight:
		sum(i in W, j in H, k in P) w[k] * x_ijp[i, j, k] <= c;

}


execute {
for (var i = 1; i <= x; i++) {
  for (var j = 1; j <= y; j++) {
    var found = false;
    for (var k = 1; k <= n; k++) {
      if (x_ijp[i][j][k] == 1) {
        write(k);
        found = true;
        break;
      }
    }
    if (!found) {
      write(".");
    }
  }
  writeln("");
}

}