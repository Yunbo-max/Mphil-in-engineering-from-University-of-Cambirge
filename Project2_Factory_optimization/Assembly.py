import sys
from gurobipy import *
import numpy as np

# model
m = Model()

# create decision variables for assignment of task
assignment = m.addVars(I, J, vtype=GRB.BINARY, name="assign")
y = m.addVars(J, vtype=GRB.BINARY, name="sta_num")
# every task is assigned to only one station
m.addConstrs((assignment.sum(t, '*') == 1 for t in I), "c0")
# cycle time constraints
for j in J:
    m.addConstr(quicksum(duration[i] * assignment[i, j] for i in I) <= ct * y[j])
# precedence constraints
for i in task_P0:
    for h in Pred_imd[i]:
        m.addConstr((quicksum(g * assignment[h, g] for g in J) <= quicksum(j * assignment[i, j] for j in J)), "_")

m.setObjective(quicksum(y[j] for j in J), GRB.MINIMIZE)

m.optimize()