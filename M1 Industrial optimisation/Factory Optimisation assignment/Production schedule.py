import numpy as np
import pandas as pd

import gurobipy as gp
from gurobipy import GRB

# Parameters

products = ["ground spike", "cone", "left side of the torch", "right side of the torch", "solar cell holder", "light holder and cap", "white upper part"]
machines = ["Setup time", "Injection time","Cooling time"]
months = ["Oct", "Nov", "Dec", "Jan", "Feb", "March"]

profit = {"ground spike":10, "cone":6, "left side of the torch":8, "right side of the torch":4, "solar cell holder":11, "light holder and cap":9, "white upper part":3}


time_req = {
    "Setup time": {    "ground spike": 4 , "cone": 4, "left side of the torch": 4,
                    "right side of the torch": 4, "solar cell holder": 4 , "light holder and cap":4, "white upper part": 5 },

    "Injection time": {    "ground spike": 0.07670535 , "cone": 0.13136855, "left side of the torch": 0.25144855,
                    "right side of the torch": 0.256784, "solar cell holder": 0.11216855 , "light holder and cap":0.10198355, "white upper part": 0.1661409 },

    "Cooling time": {"ground spike": 3.758014139, "cone": 1.467974273, "left side of the torch": 11.31246811,
                       "right side of the torch": 11.31246811, "solar cell holder": 15.03205656, "light holder and cap":15.03205656,
                       "white upper part": 3.352577152},

}

# number of machines down
down = {("Oct","Injection time"): 1, ("Oct", "Injection time"): 1, ("Dec", "Injection time"): 1,
        ("Dec", "Injection time"): 1, ("Feb", "Injection time"): 1, ("Feb", "Injection time"): 1}

# number of each machine available
installed = {"Setup time":4, "Injection time":4, "Cooling time":4}

# market limitation of sells
max_sales = {
    ("Oct", "Prod1") : 1500,
    ("Oct", "Prod2") : 3000,
    ("Oct", "Prod3") : 1000,
    ("Oct", "Prod4") : 0,
    ("Oct", "Prod5") : 2000,
    ("Oct", "Prod6") : 1000,
    ("Oct", "Prod7") : 1500,
    ("Nov", "Prod1") : 0,
    ("Nov", "Prod2") : 800,
    ("Nov", "Prod3") : 2500,
    ("Nov", "Prod4") : 3000,
    ("Nov", "Prod5") : 2000,
    ("Nov", "Prod6") : 1000,
    ("Nov", "Prod7") : 2500,
    ("Dec", "Prod1") : 3500,
    ("Dec", "Prod2") : 0,
    ("Dec", "Prod3") : 3000,
    ("Dec", "Prod4") : 0,
    ("Dec", "Prod5") : 2000,
    ("Dec", "Prod6") : 1000,
    ("Dec", "Prod7") : 3500,
    ("Jan", "Prod1") : 3000,
    ("Jan", "Prod2") : 0,
    ("Jan", "Prod3") : 2500,
    ("Jan", "Prod4") : 1000,
    ("Jan", "Prod5") : 3000,
    ("Jan", "Prod6") : 2000,
    ("Jan", "Prod7") : 3000,
    ("Feb", "Prod1") : 2500,
    ("Feb", "Prod2") : 2500,
    ("Feb", "Prod3") : 2000,
    ("Feb", "Prod4") : 0,
    ("Feb", "Prod5") : 2000,
    ("Feb", "Prod6") : 1000,
    ("Feb", "Prod7") : 2500,
    ("March", "Prod1") : 2000,
    ("March", "Prod2") : 1000,
    ("March", "Prod3") : 1500,
    ("March", "Prod4") : 0,
    ("March", "Prod5") : 1500,
    ("March", "Prod6") : 3000,
    ("March", "Prod7") : 2000,
}

holding_cost = 0.5
max_inventory = 200
store_target = 100
hours_per_month = 3*8*24

factory = gp.Model('Factory Planning I')

make = factory.addVars(months, products, name="Make") # quantity manufactured
store = factory.addVars(months, products, ub=max_inventory, name="Store") # quantity stored
sell = factory.addVars(months, products, ub=max_sales, name="Sell") # quantity sold

# 1. Initial Balance
Balance0 = factory.addConstrs((make[months[0], product] == sell[months[0], product]
                               + store[months[0], product] for product in products), name="Initial_Balance")

# 2. Balance
Balance = factory.addConstrs((store[months[months.index(month) - 1], product] +
                              make[month, product] == sell[month, product] + store[month, product]
                              for product in products for month in months
                              if month != months[0]), name="Balance")

#3. Inventory Target
TargetInv = factory.addConstrs((store[months[-1], product] == store_target for product in products),  name="End_Balance")

#4. Machine Capacity

MachineCap = factory.addConstrs((gp.quicksum(time_req[machine][product] * make[month, product]
                             for product in time_req[machine])
                    <= hours_per_month * (installed[machine] - down.get((month, machine), 0))
                    for machine in machines for month in months),
                   name = "Capacity")

#0. Objective Function
obj = gp.quicksum(profit[product] * sell[month, product] -  holding_cost * store[month, product]
               for month in months for product in products)

factory.setObjective(obj, GRB.MAXIMIZE)

factory.optimize()

rows = months.copy()
columns = products.copy()
make_plan = pd.DataFrame(columns=columns, index=rows, data=0.0)

for month, product in make.keys():
    if (abs(make[month, product].x) > 1e-9):
        make_plan.loc[month, product] = np.round(make[month, product].x, 1)


pd.set_option('display.width', None)
pd.set_option('display.max_rows', None) #

print(make_plan)