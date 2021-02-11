#f = open('input.txt', 'r')
#for line in f.readlines():
    

#Due to lack of time didnt complete the "Read from file" process

a = 2
b = 3
count1 = 0
count2 = 0
count3 = 0
count4 = 0
startRange = 0
finishRange = 20

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
