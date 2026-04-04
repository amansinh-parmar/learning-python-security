import statistics

class Statistics:
    def __init__(self, data):
        self.data = data
        self.sorted_data = sorted(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def mode(self):
        try:
            mode_val = statistics.mode(self.data)
            return {'mode': mode_val, 'count': self.data.count(mode_val)}
        except statistics.StatisticsError:
            return 'No unique mode'

    def std(self):
        return round(statistics.stdev(self.data), 1)

    def var(self):
        return round(statistics.variance(self.data), 1)

    def freq_dist(self):
        freq = {}
        for value in self.data:
            freq[value] = freq.get(value, 0) + 1
        return freq

# Test the Statistics class with the given data
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count())  # 25
print('Sum: ', data.sum())  # 744
print('Min: ', data.min())  # 24
print('Max: ', data.max())  # 38
print('Range: ', data.range())  # 14
print('Mean: ', data.mean())  # 30
print('Median: ', data.median())  # 29
print('Mode: ', data.mode())  # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std())  # 4.2
print('Variance: ', data.var())  # 17.5
print('Frequency Distribution: ', data.freq_dist())  # {26: 5, 27: 4, 32: 3, 31: 2, 34: 2, 37: 2, 24: 2, 33: 2, 38: 1, 25: 1, 29: 1}

