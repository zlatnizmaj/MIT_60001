def hotelCost(days):
    return 140*days

def planeRideCost(city):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475

def rentalCarCost(days):
    cost = days*40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

def tripCost(city, days, spendingMoney):
    print(planeRideCost(days))
    return rentalCarCost(days) + hotelCost(days) + planeRideCost(days) + spendingMoney

print(tripCost("Los Angeles", 5, 600))

