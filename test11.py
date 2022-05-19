import re
fh = open ("regex_sum_909053.txt")
sum = 0
i = 0 #Counting variable, the same for syntax
numlist = list()
for line in fh:
    i = 0
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    length = len(numbers)
    if length == 0:
        continue
    #print(numbers)
    while i < length:
        num = int(numbers[i])
        numlist.append(num)
        i = i + 1
i = 0
numle = len(numlist)
#print(numle)
while i < numle:
  sum = sum + numlist[i]
  i = i + 1
print(sum)
