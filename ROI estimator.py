import math

print("Pyhon program to estimate the cost of blends to produce biodiesel")

    
def dayCalc(days):
    #https://ohcanadasupply.ca/automotive/Automotive-Filters/Fuel-Filters/dut5975
    
    #filter replacement
    if(days % 12 == 0):
        return 15 * days / 12
    else:
        return 15 * (days/12 + 1)
        
    
totalCost = 0
totalCost += 20000 # cost of base machine
totalCost += 52 # cost of starting the engine (one time)

daysOfUse = float(input("Planned number of days the generator will be in use (per year): "))
dayCost = dayCalc(daysOfUse)
totalCost += dayCost

#https://www.rvheater.com/products/vvkb-diesel-filter-heater-zues-f1-12v-24v-75w-for-truck-rv-tractor-and-car
vehicles = float(input("Number of vehicles (automobiles and farming equipment) planned to be powered: "))
vehicleCost = vehicles * 82.79
totalCost += vehicleCost

teflonCost = 15.98 * vehicles
totalCost += teflonCost


print("Cost of Teflon: $" + str(teflonCost))
print("Total cost: $" + str(round(totalCost, 2)))

#interest rate: 2.8% per month

paybackDuration = float(input("How many months does the customer plan on taking to pay off the generator: "))

finalCost = totalCost * pow(1.028, paybackDuration)

perMonth = finalCost / paybackDuration

print("The final cost is: $" + str(round(finalCost, 2)))
print("The customer has to pay $" + str(round(perMonth, 2)) + " per month")

#Return on Investment

print("Return on Investment Calculator")

animalFat = float(input("How many gallons of animal fat or feedstock will be provided each week: "))
feedstockCost = float(input("Cost of potassium hydroxide ($/pound): "))
methanol = float(input("Cost of methanol ($/gallon): "))
sulfuricAcid = float(input("Cost of sulfuric acid ($/190ml): "))

costPerGallonBioDiesel = (feedstockCost*5.175 + 10*methanol + sulfuricAcid)/50
print("Cost per gallon of biodiesel production: $" + str(costPerGallonBioDiesel))

gallonCost = float(input("What is the current cost per gallon of diesel ($/gallon): "))

ROI = finalCost / (animalFat * (gallonCost - costPerGallonBioDiesel))

print("It would take " + str(round(ROI, 2)) + " weeks to pay off the initial investment")