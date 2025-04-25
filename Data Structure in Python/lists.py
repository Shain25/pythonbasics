#1
list=[1,7,5,13,9,2,4,6,8,10]

#2
list.append(11)

for i in list:
    if i==5:
        list.pop(list.index(i))
list[1]=3

#3
sum=0
low=list[0]
high=0

for a in list: 
    sum+=a
    if a>high:
        high=a
    if a<low:
        low=a

print(f"the list: {list}")
print(f"the sum is: {sum}")
print(f"the lowest number is: {low}, and the highest number is: {high}")