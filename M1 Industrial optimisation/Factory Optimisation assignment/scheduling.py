import numpy as np

# constants
Annual_production = 500000

days = 365
Defect_rate = 0.25
Capacity_per_day = 1373
Capacity_after_cleaning_per_day = 1383

Capacity_per_day = 24*3600/22
days = Annual_production /Capacity_per_day

products_list = [0]*7
sales=500000*10
machinecost = 232000
workingcost = 11
machine_number = 6
inventory_cost = 5
labour_number =3
workhours = 24
list1 = []
list2 = []
list3 = []

dayslist = []
profitslist = []
# variables
# constrains

for mouldchangingfrequency in range(1,32):
    for number in range(1,7):
# objective
        machine_number = number
        labour_number = number
        workhours_per_day = 24-6*round(1/mouldchangingfrequency)
        changetime = 6/number
        residual = 6%number
        daysshifts = (changetime+1)*6
        Capacity_per_day =7*mouldchangingfrequency*workhours_per_day*3600/22  / (daysshifts*mouldchangingfrequency)

        daysnumber = Annual_production / Capacity_per_day

        workhours = 24 * daysnumber


        profit = sales - machine_number * machinecost - labour_number * workhours * workingcost - 365/mouldchangingfrequency*5000
 # - inventory_cost*Capacity_per_day*daysshifts

        list1.append(profit)
        list2.append(daysnumber)



for i in list2:
    if i < 365:

        list3.append(list2.index(i))

print(np.unique(list3))
print(len(list2))
for j in np.unique(list3):
    profitslist.append(list1[j])
    dayslist.append(list2[j])

print('the optimization of possible scheduling cases ')
print(profitslist)
print(dayslist)
print((profitslist.index(max(profitslist))+1))

standard_profit = sales - machine_number * machinecost - labour_number * workhours * workingcost- 365/mouldchangingfrequency*5000
print('the best performance of 6 machine in 3 shifts')
print(standard_profit)
print(days)
print(Capacity_per_day)


# give a possible list and






# cycle time
#
#
# for mouldchangingfrequency in range(31):
#     for number in range(7):
#         products_list[number] = products_list[number] + 24*365-6*round(365/mouldchangingfrequency)
#
#     for j in range(round(365/mouldchangingfrequency)):
#
#
#
#     Capacity_per_day = 500000/((24*365-6*round(365/mould_changingtime))/24)
#
# for number in range(i):
#     Capacity_list[i] = Capacity_list[i] + 1


