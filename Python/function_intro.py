# A function is a block of code which only runs when it is called. and it follows IPO cycle.
# Function name follow snake_case for name convention

#a. Define function without argument

#b. Define function with positional argument
#first_num = 1
#second_num = 3

#c. Define function with default value assigned to argument
#def get_addition():
    #sum = first_num + second_num #process
   #return sum #output

#function initialization -- calling function
#print (get_addition())
    
#b. Define function with positional argument
#define a function

def get_subtraction(first_num, second_num):
    return first_num - second_num



#function initialization
print(get_subtraction(4, 1))

#c. Define function with default value assigned to argument
def greets(name="Unknown"):
    return f'Welcome, {name}'

print(greets("Kaze"))

### Lambda Function