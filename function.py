def getSum(num1,num2=4):
    total=num1+num2
    return total

num=getSum(3,7)
print(num)

# Lambda function: 
# It is a small anonymus function.
# A Lambda function can take number of arguments,
# but can only have one expression.

getAdd = lambda num1,num2 : num1+num2
print(getAdd(3,3))
