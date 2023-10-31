import math

class Statistics:
    def mean(list):
        return sum(list) / len(list)

    def std(list):
        # for each in list, (mean-val)**2
        top = []
        for num in list:
            top.append((Statistics.mean(list) - num) ** 2)
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
        return Statistics.quartile(list, 3) - Statistics.quartile(list, 1)

    def str_to_list(string, sep = ' '):
        return [eval(x) for x in string.split(sep)]

    def upper_fence(list):
        return Statistics.quartile(list, 3) + 1.5 * Statistics.iqr(list)

    def lower_fence(list):
        return Statistics.quartile(list, 1) - 1.5 * Statistics.iqr(list)

    def outliers(list):
        uf = Statistics.upper_fence(list)
        lf = Statistics.lower_fence(list)
        return [x for x in list if x > uf or x < lf]

    def within_range(list, lower, upper):
        return [x for x in list if x >= lower and x <= upper]

    def summarize(list):
        list.sort()
        print("Min: ", list[0])
        print("Q1: ", Statistics.quartile(list, 1))
        print("Q2 (Median): ", Statistics.quartile(list, 2))
        print("Q3: ", Statistics.quartile(list, 3))
        print()
        print("Max: ", list[-1])
        print("IQR: ", Statistics.iqr(list))
        print()
        print("Mean: ", Statistics.mean(list))
        print("Std: ", Statistics.std(list))
        print()
        print("Range: ", list[-1] - list[0])
        print("Length: ", len(list))
        print("Sum: ", sum(list))
        print()
        print("Upper Fence: ", Statistics.upper_fence(list))
        print("Lower Fence: ", Statistics.lower_fence(list))
        print("Outliers: ", Statistics.outliers(list))
        return {
            'min': list[0],
            'q1': Statistics.quartile(list, 1),
            'q2': Statistics.quartile(list, 2),
            'median': Statistics.quartile(list, 2),
            'q3': Statistics.quartile(list, 3),
            'max': list[-1],
            'iqr': Statistics.iqr(list),
            'mean': Statistics.mean(list),
            'std': Statistics.std(list),
            'range': list[-1] - list[0],
            'length': len(list),
            'sum': sum(list),
            'upper_fence': Statistics.upper_fence(list),
            'lower_fence': Statistics.lower_fence(list),
            'outliers': Statistics.outliers(list)
        }

class BinomialDistribution:
    """
    Used with discrete binomial data
    """
    def mean(n, p):
        return n * p
    def std(n, p):
        return (n * p * (1 - p)) ** 0.5
    def variance(n, p):
        return n * p * (1 - p)
    def prob(min, max, n, p_succ):
        p_fail = 1 - p_succ
        sum = 0
        for x in range(min, max + 1):
            sum += math.comb(n, x) * p_succ ** x * p_fail ** (n - x)
        return sum
    def comb(n,x):
        print("Fun factorial stuff")
        math.factorial(n)/(math.factorial(n-x) * math.factorial(x))

class NormalDistribution:
    """
    Used with continuous binomial data
    Easier to approximate
    """
    def equations():
        print("mean = np")
        print("variance = np(1-p)")
        print("std = (variance)**0.5")
        print("z = (x - mean) / std")
        print("x = z * std + mean")

    def z(x, n, p):
        mean = BinomialDistribution.mean(n,p)
        std = BinomialDistribution.std(n,p)
        z = (x - mean) / std
        return z
    def z_score(x, mean, std):
        z = (x - mean) / std
        return z
    def ztab():
        # prints out a z-score probability table
        print("")
    def pdf(x, n, p): # probability density funciton
        mean = BinomialDistribution.mean(n,p)
        std = BinomialDistribution.std(n,p)
        return ((1/(2*math.pi*std)**0.5)*math.e)**((-(x-mean)**2)/2*std**2)
    def zprob(z_score):
        from scipy.stats import norm
        # Calculate the probability using the cumulative distribution function (CDF)
        probability = norm.cdf(z_score)
        return probability
    def x_from_z(z_score, mean, std):
        return z_score * std + mean
    
class Estimation:
    """
    Confidence Interval = Sample Mean ± Margin of Error
    Margin of Error = Critical Value * Standard Error of the Mean
    Standard Error of the Mean = Standard Deviation / (n ** 0.5)
    """
    def data_set(mean, std):
        return {
            'mean': mean,
            'std': std
        }
    def sample(data_set, n):
        return {
            'mean': data_set['mean'],
            'std': data_set['std'] / n ** 0.5
        }
    def prob_g(data_set, x):
        z = NormalDistribution.z(x, data_set['mean'], data_set['std'])
        return 1 - NormalDistribution.zprob(z)
    def prob_l(data_set, x):
        z = NormalDistribution.z(x, data_set['mean'], data_set['std'])
        return NormalDistribution.zprob(z)
    def prob_b(data_set, x1, x2):
        z1 = NormalDistribution.z(x1, data_set['mean'], data_set['std'])
        z2 = NormalDistribution.z(x2, data_set['mean'], data_set['std'])
        return NormalDistribution.zprob(z2) - NormalDistribution.zprob(z1)
    
    def ci(x_bar, cv, s, n):
        std_err_m = s / (n ** 0.5)
        me = cv * std_err_m
        ci = [x_bar - me, x_bar + me]
        return {
            "Confidence Interval": ci,
            "Margin of Error": me,
            "Standard Error of the Mean": std_err_m
        }

class HypothesisTesting:
    def test_statistic(x_bar, mu, std, n):
        return (x_bar - mu) / (std / (n ** 0.5))
    
    def p_value(test_statistic):
        from scipy.stats import norm
        # Calculate the probability using the cumulative distribution function (CDF)
        probability = norm.cdf(test_statistic)
        return probability
    
    def p_value_g(t, t_0):
        return 1 - HypothesisTesting.p_value(t - t_0)