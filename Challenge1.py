#Update Python File after the completion of time

f = open('input.txt', 'r')
i=0
for line in f.readlines():
    if(i==0):
        inputs = [int(s) for s in line.split() if s.isdigit()]
        i=1
    else:
        rangeCount = [int(s) for s in line.split() if s.isdigit()]

a = inputs[0]
b = inputs[1]
count1 = 0
count2 = 0
count3 = 0
count4 = 0
startRange = rangeCount[0]
finishRange = rangeCount[1]

for x in range(startRange , finishRange):
   if x % a == 0:
        if x % b != 0:
            
            count1 += 1

for x in range(startRange , finishRange):
   if x % b == 0:
        if x % a != 0:
            
            count2 += 1

for x in range(startRange , finishRange):
   if x % b == 0:
        if x % a == 0: 
            count3 += 1
            
for x in range(startRange , finishRange):
   if x % b != 0:
        if x % a != 0:
            
            count4 += 1

print(count1)
print(count2)
print(count3)
print(count4)
