'''
The previous lambda function takes in two argument which are supposed
to be lists and adds them together to make one single list and passes
them to the map function which iterates over each value and adds the value
to itself and stores it in a list
'''
#first list
a=(1,2,3)
#second list
b=(4,5,6)
#combination of both list
joined=a+b
#map function that takes two argument, one is the value and
#the second is operation to performed on the values
addList=map(lambda x : x+x, joined)
#result from the map is stored in a list 
lst=list(addList)
print(lst)
