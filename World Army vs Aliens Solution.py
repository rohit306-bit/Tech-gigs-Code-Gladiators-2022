import sys
import os

a,b = list(map(int,input().split()))
a1,b1=list(map(int,input().split()))
#using temporary variable
temp1=0
temp2=0
#now update the values
temp2=b+b1
#World Army follows a 24-hour time format.
temp1=(a+a1+(temp2//60))%24
#you need to find the time of blast accordingly. The time will be in the hh mm format.
temp2=temp2%60
#print the output
print(f"{temp1:02d}",f"{temp2:02d}")
