#from Compiler import*
from sys import stdin

inp = stdin
the_file = inp.read()
#------------------------------
#the_f = open('sample_5.txt')
#the_file = the_f.read()
#------------------------------

# Puts the input string into objects in an array
# seperated by spaces
string1 = the_file.split()

the_size = int(len(string1))

# The main stack
the_stack = []

# The Dictionary(Map) that will hold the variable values
the_dict = {}

# the i is here because of some Python weirdness
i = 0
for b in range(the_size):
        if(i >= the_size):
            break
        if(string1[i] == "PUSH"):
            if(string1[i+1].isdigit()):
                # Numbers have to be converted to true integers
                # before being pushed to the stack
                the_stack.append(int(string1[i+1]))
                i = i + 1
            else:
                # If it was a variable name it is pushed normally
                # to the stack
                the_stack.append(string1[i+1])
                i = i + 1

        elif(string1[i] == "ASSIGN"):
            var1 = the_stack.pop()
            var2 = the_stack.pop()
            if(isinstance(var1,int)):
                the_dict[var2] = var1
            else: 
                the_dict[var2] = the_dict[var1]

        elif(string1[i] == "ADD"):
            var1 = the_stack.pop()
            # If it is not an integer then it is a variable and
            # has a value according to the dictionary(Map)
            if(not isinstance(var1,int)):
                var1 = the_dict[var1]
                
            var2 = the_stack.pop()
            if(not isinstance(var2,int)):
                var2 = the_dict[var2]

            var1 += var2
            # Once both numbers have been added together they are again
            # pushed onto the stack
            the_stack.append(var1)

        elif(string1[i] == "SUB"):
            var1 = the_stack.pop()
            if(not isinstance(var1,int)):
                var1 = the_dict[var1]
                
            var2 = the_stack.pop()
            if(not isinstance(var2,int)):
                var2 = the_dict[var2]
            
            var2 -= var1
            the_stack.append(var2)

        elif(string1[i] == "MULT"):
            var1 = the_stack.pop()
            if(not isinstance(var1,int)):
                var1 = the_dict[var1]
                
            var2 = the_stack.pop()
            if(not isinstance(var2,int)):
                var2 = the_dict[var2]
            
            var1 = var1 * var2
            the_stack.append(var1)

        elif(string1[i] == "PRINT"):
            var1 = the_stack.pop()

            if(var1 in the_dict):
                print(the_dict[var1])
            else:
                print(var1)
                
        # It is an error if the operator does not match any of the above
        else:
            print("Error for operator:",string1[i])
            break

        i += 1

