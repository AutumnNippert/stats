def mean(list):
    return sum(list) / len(list)

def std(list):
    # for each in list, (mean-val)**2
    top = []
    for num in list:
        top.append((mean(list) - num) ** 2)
    E = sum(top)
    n = len(list) - 1
    return (E / n) ** 0.5

def quartile(list, q):
    """
    q = 0-4
    """
    list.sort()
    n = len(list)
    if q == 0:
        return list[0]
    elif q == 4:
        return list[-1]
    else:
        if(n * q / 4).is_integer():
            return (list[int(n * q / 4)] + list[int(n * q / 4) - 1]) / 2
        else:
            return list[int(n * q / 4)]
        
def iqr(list):
    return quartile(list, 3) - quartile(list, 1)

def str_to_list(string, sep = ' '):
    return [eval(x) for x in string.split(sep)]

def upper_fence(list):
    return quartile(list, 3) + 1.5 * iqr(list)

def lower_fence(list):
    return quartile(list, 1) - 1.5 * iqr(list)

def outliers(list):
    uf = upper_fence(list)
    lf = lower_fence(list)
    return [x for x in list if x > uf or x < lf]

def within_range(list, lower, upper):
    return [x for x in list if x >= lower and x <= upper]

def summarize(list):
    list.sort()
    print("Min: ", list[0])
    print("Q1: ", quartile(list, 1))
    print("Q2 (Median): ", quartile(list, 2))
    print("Q3: ", quartile(list, 3))
    print()
    print("Max: ", list[-1])
    print("IQR: ", iqr(list))
    print()
    print("Mean: ", mean(list))
    print("Std: ", std(list))
    print()
    print("Range: ", list[-1] - list[0])
    print("Length: ", len(list))
    print("Sum: ", sum(list))
    print()
    print("Upper Fence: ", upper_fence(list))
    print("Lower Fence: ", lower_fence(list))
    print("Outliers: ", outliers(list))
    return {
        'min': list[0],
        'q1': quartile(list, 1),
        'q2': quartile(list, 2),
        'median': quartile(list, 2),
        'q3': quartile(list, 3),
        'max': list[-1],
        'iqr': iqr(list),
        'mean': mean(list),
        'std': std(list),
        'range': list[-1] - list[0],
        'length': len(list),
        'sum': sum(list),
        'upper_fence': upper_fence(list),
        'lower_fence': lower_fence(list),
        'outliers': outliers(list)
    }