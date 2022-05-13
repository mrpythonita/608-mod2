#Using native Python programming to calculate measure of central tendency
data=[i for i in range(2000)]
count=len(data)
summation= sum(data)
mean= sum(data)/len(data)
mode=max(set(data),key=data.count)
mid_value= len(data)//2
median= (data[mid]+data[~mid])/2
print('The sequence has {} numbers, the sum of all number is {}, the mean is {}, the mode is {}, and the median is {}'.format(count,summation,mean,mode,median))
