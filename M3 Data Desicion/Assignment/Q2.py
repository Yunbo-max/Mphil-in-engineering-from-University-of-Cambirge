import numpy as np
import pandas as pd

import gurobipy as gp
from gurobipy import GRB


# Parameters

products = ["Product P", "Product Q", "Product R", "Product S"]
Labour_cost = {"Almont":30,"Berryland":30, "Charlbury":42, "Deltown":13}
Factories = ["Almont", "Berryland", "Charlbury", "Deltown"]
Customers = ["Hermon", "JPMedTech", "Lincoln Devices", "Tomographica"]
Annual_capacity = {"Almont":210000,"Berryland":120000, "Charlbury":190000, "Deltown":200000}
# machines = ["grinder", "vertDrill", "horiDrill", "borer", "planer"]
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# profit = {"Prod1":10, "Prod2":6, "Prod3":8, "Prod4":4, "Prod5":11, "Prod6":9, "Prod7":3}


time_req = {
    "Almont": { "Product P": 100, "Product Q": 200, "Product R": 100,
                    "Product S": 100 },
    "Berryland": {  "Product P": 100, "Product Q": 150, "Product R": 90,
                    "Product S": 90  },
    "Charlbury": {  "Product P": 80, "Product Q": 210, "Product R": 90,
                    "Product S": 70 },
    "Deltown": {  "Product P": 300, "Product Q": 240, "Product R": 100,
                    "Product S": 140 }
}

distance_req = {
    "Almont": { "Hermon":128, "JPMedTech":170, "Lincoln Devices":63, "Tomographica":216 },
    "Berryland": {  "Hermon":28, "JPMedTech":51, "Lincoln Devices":100, "Tomographica":85},
    "Charlbury": {  "Hermon":76, "JPMedTech":100, "Lincoln Devices":121, "Tomographica":121 },
    "Deltown": {  "Hermon":873, "JPMedTech":878, "Lincoln Devices":827, "Tomographica":913}
}

make_and_sales = {
    "Almont": { "Product P": 100, "Product Q": 200, "Product R": 100,
                    "Product S": 100 },
    "Berryland": {  "Product P": 100, "Product Q": 150, "Product R": 90,
                    "Product S": 90  },
    "Charlbury": {  "Product P": 80, "Product Q": 210, "Product R": 90,
                    "Product S": 70 },
    "Deltown": {  "Product P": 300, "Product Q": 240, "Product R": 100,
                    "Product S": 140 }
}


# # number of machines down
# down = {("Jan","grinder"): 1, ("Feb", "horiDrill"): 2, ("Mar", "borer"): 1,
#         ("Apr", "vertDrill"): 1, ("May", "grinder"): 1, ("May", "vertDrill"): 1,
#         ("Jun", "planer"): 1, ("Jun", "horiDrill"): 1}

# number of each machine available
installed = {"Almont":1, "Berryland":1, "Charlbury":1, "Deltown":1}

Shipping_cost_per_mile = 30
number_of_goods_shifted_together = 3
store_target = 50
hours_per_month = 2*8*24



factory = gp.Model('Optimization1')

make = factory.addVars(Factories, products, name="Make") # quantity manufactured


#2. Balance
Balance = factory.addConstrs((
                make[Factories, product] == sell[Customers, product]
                for product in products for month in months
                if month != months[0]), name="Balance")

#4. factory Capacity

MachineCap = factory.addConstrs((gp.quicksum(time_req[machine][product] * make[month, product]
                             for product in time_req[machine])
                    <= Annual_capacity[machine]
                    for machine in Factories),
                   name = "Capacity")

#0. Objective Function
obj = gp.quicksum(- Labour_cost[factory]* time_req[Factories,product]* make[Factories, product] - Shipping_cost_per_mile  * distance_req[Factories,product]* make[Factories, product]/number_of_goods_shifted_together
               for factory in Factories for product in products for customer in Customers)

factory.setObjective(obj, GRB.MAXIMIZE)

factory.optimize()