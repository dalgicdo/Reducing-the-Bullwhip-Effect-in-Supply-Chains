#!/usr/bin/env python
# coding: utf-8

# In[90]:


import random
import math
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.legend_handler import HandlerLine2D

def stdCalc(orderList, average):
    std = 0
    for i in range(0,len(orderList)):
        std += (orderList[i] - average)**2
        
    std /= len(orderList)
    std = math.sqrt(std)
    return std

def meanCalc(orders):
    mean = 0
    for u in range(0,len(orders)):
        mean += orders[u]
        
    mean /= len(orders)
    return mean

def rounder(list):
    val = 0
    for i in range(0,len(list)):
        list[i] = math.ceil(list[i])
        val += list[i]
        
    return val


#--------GLOBAL VARIABLES---------
total_year_orders = 0
total_year_prod = 0
orderList = []
prodList = [0,0]
unfilled = 0
unfilledList = []
cum_unfilled = 0
#--------------------------------

guess_order = np.random.normal(15, 1, size = (3)) # the initial order for the first month
#orderList.append(rounder(first_order))
#total_year_orders += rounder(first_order) # rounding all values to the ceiling
mean1 = meanCalc(guess_order)
mean3 = rounder(guess_order)
std1 = stdCalc(guess_order, mean1)

# initial production and rounding 
first_prod = np.random.normal(mean3, std1, size = (1))
total_year_prod += rounder(first_prod)
prodList.append(rounder(first_prod))
orderList.append(rounder(np.random.normal(15,3, size = (1))))

unfilled = rounder(orderList) # fixer error
cum_unfilled += unfilled
unfilledList.append(unfilled) 
#print("unfilled: ", unfilled)

# ------------PRODUCTION STARTING FROM THE SECOND MONTH--------------
for j in range(1,51):
    unfilled = 0
    
    order = np.random.normal(15,3, size = (1))
    total_year_orders += rounder(order)
    orderList.append(rounder(order))
    mean2 = meanCalc(orderList)
    std2 = stdCalc(orderList, mean2)
    
    prod = np.random.normal(mean2, std2, size = (1))
    total_year_prod += rounder(prod)
    prodList.append(rounder(prod))
    
    if 1<=j<=2:
        unfilled = rounder(order)
    if prod < order:
        unfilled = rounder(order) - rounder(prod)
        cum_unfilled += unfilled
    unfilledList.append(unfilled) 
    #print("unfilled: ", unfilled)
    
prodList.pop(-1)
prodList.pop(-1)
    
print(total_year_orders, total_year_prod)
#print(orderList, prodList)

#--------------GRAPHING----------------------

months = []
for i in range(1,52):
    months.append(i)

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)

# ---- Formatting the Graph ----- # 
xmarks = [i for i in range(1,len(months))] # scaling X axis
plt.xticks(xmarks)
ymarks = [i for i in range(1,60,2)] # scaling Y axis
plt.yticks(ymarks)
ax.grid(color='b', ls = '-.', lw = 0.1) # enabling grid

# ---- Setting Axis Label Names ------ #
ax.set_xlabel("Weeks",fontsize=15)
ax.set_ylabel("Number of orders / production",fontsize=15)
ax.set_title("Weekly Relationship between Customer Orders and Production",fontsize=20)

# ---- Creating Plots ----- #
ax.bar(months,unfilledList, color = "green",width=0.2, label = "Unfilled Orders")
ax.plot(months, orderList, "r--",linewidth=2, label = "Customer Orders")
ax.plot(months, prodList, linewidth=2, label = "Store's Production")

plt.legend(prop = {"size": 15}) # adding legend

plt.show()

