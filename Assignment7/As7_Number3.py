'''
The previous lambda program accepts a *args as paramter thereby allowing
it to accept any number of argument and print those argument.
This modified version of the code does the same thing as well but in a much
more simplified manner as it takes any number of arguments and prints them out
'''
#lambda accepts positonal argument and prints out every value
print_args = lambda *args:print (args)
#calling the lambda function
print_args('a','b','c')
