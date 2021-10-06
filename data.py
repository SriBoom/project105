import math
import csv
from types import resolve_bases

with open("data.csv", newline="") as f:
    #reading the file and listing it
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

#calculating the mean
def mean(data):
    n=len(data)
    total=0
    #we are adding all the data
    for x in data:
        total += int(x)

    mean=total/n
    return mean

#calculating the square root
squared_list=[]
for number in data:
    #for calculating the standard deviation, we are subtrating each of the data in data.csv with the mean. 
    a=int(number)-mean(data)
    #square root of the answer(a)
    a=a**2
    squared_list.append(a)

#we are adding all the square root. 
sum=0
for i in squared_list:
    sum=sum+i
 
#we are dividing the sum by the data values. 
result=sum/(len(data)-1)
std_deiveation=math.sqrt(result)
print(std_deiveation)