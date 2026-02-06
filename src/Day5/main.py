import math_operations
base=int(input("Enter the base:"))
exp=int(input("Enter the exp:"))
P= math_operations.power(base,exp)
print(P)

user_input=(input("Enter elements separated by sapces:"))
numbers_list= [int(x) for x in user_input.split()]
A= math_operations.average(numbers_list)
print(A)