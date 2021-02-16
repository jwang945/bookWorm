import math
def bookWorm(milkType, topping, servings, goal):
    timeToMakeCocoa = hotCocoa(milkType, topping, servings)
    pagesRead = math.floor(timeToMakeCocoa/2.0)

    if pagesRead < goal:
        return "I will need to read " + goal - pagesRead + " additional pages tomorrow."
    else:
        return "I will be reading " + goal + " pages and " + goal - pagesRead + "additional pages."