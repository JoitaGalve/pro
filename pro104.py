import csv
from collections import Counter
with open("data2.csv", newline = '') as f:
    data = csv.reader(f)
    data1 = list(data)
    #print(data1)

'''str = "abcaabnmmmyyuzz"
data2 = Counter(str)
print(data2)
print(data2.items())
print(data2.values())'''

data1.pop(0)
newData = []
for i in range(len(data1)):
    num = data1[i][1]
    newData.append(float(num))

n = len(newData)

#Calculation of median
newData.sort()
if n % 2== 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2-1])
    median = (median1+median2)/2

else:
     median = float(newData[n//2])
print("Median of height is " + str(median))

#Calculation of mode
data2 = Counter(newData)
dataRange = {
    "50-60":0, 
    "60-70":0,
    "70-80":0
}

for height, count1 in data2.items():
    if 50 < float(height) < 60:
        dataRange["50-60"] += count1
    
    elif 60 < float(height) < 70:
        dataRange["60-70"] += count1

    elif 70 < float(height) < 80:
        dataRange["70-80"] += count1

dataMode, dataCount = 0, 0
for range, count1 in dataRange.items():
    if count1 > dataCount:
        dataMode, dataCount = [int(range.split("-")[0]), int(range.split("-")[1])], count1
        mode = float((dataMode[0] + dataCount[1])/2) 
        print("Mode of height is " + str(mode))

#Calculation of mean
total = 0
for x in newData:
    total+=x

mean = total/n
print("Mean of height is " + str(mean))