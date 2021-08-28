import math
#build this as a function
def delNan(list):
    new_list = [item for item in list if not(math.isnan(item)) == True]
    return new_list
