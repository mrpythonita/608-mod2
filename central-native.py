#Using native Python programming to calculate measure of central tendency
data=[i for i in range(1,2000)]
count=len(data)
summation= sum(data)
mean= sum(data)/len(data)
mode=max(set(data),key=data.count)
mid_value= len(data)//2
median= (data[mid_value]+data[~mid_value])/2
print('The sequence "data" has {} numbers, the sum of all numbers is {}, the mean is {}, the median is {}, and the mode is {}'.format(\
    count,summation,mean,median,mode))
