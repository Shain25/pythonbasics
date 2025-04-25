#1 
numbers={1,4,7,10,3}
#2
elements=(1,16,49,100,9)
#3
#3.1
numbers=set(sorted(numbers, reverse=True))
#3.2
common_values = numbers.intersection(elements)
#3.3
print(f"The set length: {len(numbers)}")
print(f"The tuple length: {len(elements)}")
#3.4
#There is no option to add a new value to a tuple.
#3.5
print(common_values)