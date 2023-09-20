def help():
    print("Autumn Stats Package:")
    print("=====================================================")
    print("str_to_list(string, ?sep) - Convert string to list of numbers")
    print()
    print("mean(list) - Mean")
    print("std(list) - Standard Deviation")
    print()
    print("quartile(list, q) - 0 <= q <= 4")
    print("iqr(list) - Interquartile Range")
    print("upper_fence(list) - Upper fence for outliers")
    print("lower_fence(list) - Lower fence for outliers")
    print()
    print("outliers(list) - List of outliers")
    print("within_range(list, lower, upper) - List of values within range")
    print()
    print("histogram(list, ?buckets) - Histogram graph showing frequency of latency")
    print("scatter(list1, list2)")
    print("boxplot(list)")
    print()
    print("summarize(list)")

def mean(list = None):
    if (list == None):
        return "Usage: mean(list)"
    return sum(list) / len(list)

def std(list = None):
    if (list == None):
        return "Usage: std(list)"
    # for each in list, (mean-val)**2
    top = []
    for num in list:
        top.append((mean(list) - num) ** 2)
    E = sum(top)
    n = len(list) - 1
    return (E / n) ** 0.5

def quartile(list = None, q = None):
    if (list == None or q == None):
        return "Usage: quartile(list, q)"
    if (q < 0 or q > 4):
        return "q must be between 0 and 4"
    
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
        
def iqr(list = None):
    if (list == None):
        return "Usage: iqr(list)"
    return quartile(list, 3) - quartile(list, 1)

def str_to_list(string = None, sep = ' '):
    if (string == None):
        return "Usage: str_to_list(string, ?sep)"
    return [eval(x) for x in string.split(sep)]

def upper_fence(list = None):
    if (list == None):
        return "Usage: upper_fence(list)"
    return quartile(list, 3) + 1.5 * iqr(list)

def lower_fence(list = None):
    if (list == None):
        return "Usage: lower_fence(list)"
    return quartile(list, 1) - 1.5 * iqr(list)

def outliers(list = None):
    if (list == None):
        return "Usage: outliers(list)"
    uf = upper_fence(list)
    lf = lower_fence(list)
    return [x for x in list if x > uf or x < lf]

def within_range(list = None, lower = None, upper = None):
    if (list == None or lower == None or upper == None):
        return "Usage: within_range(list, lower, upper)"
    if (lower >= upper):
        return "lower must be less than upper"
    
    return [x for x in list if x >= lower and x <= upper]

def histogram(list = None, buckets = 10):
    if (list == None):
        return "Usage: histogram(list, ?buckets)"
    import matplotlib.pyplot as plt
    # Histogram graph showing frequency of latency
    plt.hist(list, bins=50)
    plt.title("Histogram")
    plt.xlabel("X_label")
    plt.ylabel("Frequency")
    plt.show()

def scatter(list1 = None, list2 = None):
    if (list1 == None or list2 == None):
        return "Usage: scatter(list1, list2)"
    import matplotlib.pyplot as plt
    # Scatter plot showing relationship between latency and throughput
    plt.scatter(list1, list2)
    plt.title("Scatter Plot")
    plt.xlabel("X_label")
    plt.ylabel("Y_label")
    plt.show()

def boxplot(list = None):
    if (list == None):
        return "Usage: boxplot(list)"
    import matplotlib.pyplot as plt
    # Boxplot showing latency
    plt.boxplot(list)
    plt.title("Boxplot")
    plt.xlabel("X_label")
    plt.ylabel("Y_label")
    plt.show()

def summarize(list = None):
    if (list == None):
        return "Usage: summarize(list)"
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