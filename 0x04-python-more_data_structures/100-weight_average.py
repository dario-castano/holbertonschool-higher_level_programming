#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        numerator = float(sum(x[0]*x[1] for x in my_list))
        denominator = float(sum(y[1] for y in my_list))
        return numerator / denominator
