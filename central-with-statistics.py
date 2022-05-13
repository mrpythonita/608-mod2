# calculating measure of central tendency with the module statistics.
import statistics
data=[i for i in range(1,2000)]
print('The sequence "data" has {} numbers, the sum of its numbers is {}, the mean is {}, the median is {}, and the mode is {}.'.format(\
    len(data),sum(data),statistics.mean(data),statistics.median(data),\
    statistics.mode(data)))
