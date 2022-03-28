import pandas as pd
import statistics

df = pd.read_csv('SOCR-HeightWeight.csv')

results = df.Weight

weightMean = statistics.mean(results)
weightMedian = statistics.median(results)
weightMode = statistics.mode(results)

print('The mean is -> ' + str(weightMean))
print('The median is -> ' + str(weightMedian))
print('The mode is -> ' + str(weightMode))
