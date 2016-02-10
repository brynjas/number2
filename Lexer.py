from sys import stdin
from Token import *

class Lexer:
    def __init__(self):
        self.inp = stdin
        self.the_string = self.inp.read()
        #self.the_string = str(input())
        #self.the_file = open('sample.txt')
        #self.the_string = self.the_file.read()
        self.the_size = len(self.the_string)
        self.the_pos = 0
        self.the_arr = []
        # Calls nextToken until all of the Tokens are in the array
        while(self.the_size >= self.the_pos):
            self.the_arr.append(self.nextToken(self.the_pos))
            self.the_pos += 1
        # To remove None entries in the array
        if(None in self.the_arr):
            self.the_arr.pop()

    # A function to get all the Tokens in one 
    def getData(self):
        return self.the_arr        

    def nextToken(self, the_pos):
        # To make sure we dont go out of the array
        if(self.the_pos >= self.the_size):
            return

        #----------------------------
        # Loop to skip all spaces and newlines
        while(self.the_string[self.the_pos] == " " or self.the_string[self.the_pos] == "\n"):
            self.the_pos += 1
            if(self.the_pos >= self.the_size):
                return

        if(self.the_string[self.the_pos] == "="):
            #print(the_string[self.the_pos], "->ASSIGN")
            return Token("=", "ASSIGN")

        if(self.the_string[self.the_pos] == ";"):
            #print(the_string[self.the_pos], "->SEMICOL")
            return Token(";", "SEMICOL")

        if(self.the_string[self.the_pos] == "+"):
            #print(the_string[self.the_pos], "->PLUS")
            return Token("+", "ADD")

        if(self.the_string[self.the_pos] == "-"):
            #print(the_string[self.the_pos], "->SUB")
            return Token("-", "SUB")

        if(self.the_string[self.the_pos] == "*"):
            #print(the_string[self.the_pos],"->MULT")
            return Token("*", "MULT")

        if(self.the_string[self.the_pos] == "("):
            #print(the_string[self.the_pos],"->LPAREN")
            return Token("(", "LPAREN")

        if(self.the_string[self.the_pos] == ")"):
            #print(the_string[self.the_pos],"->RPAREN")
            return Token(")", "RPAREN")

        # If its a variable
        if(self.the_string[self.the_pos].isalpha()):
        #----------------------------------------
            the_next = self.the_pos + 1
            the_var = self.the_string[self.the_pos]
            #----------------------------
            if(the_next >= self.the_size):
                return
            #----------------------------

            while((self.the_string[the_next].isalpha() or self.the_string[the_next].isdigit()) and (self.the_pos < self.the_size)):
                the_next += 1
                self.the_pos += 1
                the_var += self.the_string[self.the_pos]
                if(the_next >= self.the_size):
                    break

            if(the_var == "print"):
                #print(the_var, "->PRINT")
                return Token("print", "PRINT")

            if(the_var == "end"):
                #print(the_var, "->END")
                return Token("end", "END")

            #print(the_var, "->ID")
            return Token(the_var, "ID")

        # If its an integer
        elif(self.the_string[self.the_pos].isdigit()):
        #----------------------------------------
            the_next = self.the_pos + 1
            the_int = self.the_string[self.the_pos]

            # Just another check to make shure we dont index outside the array
            if(the_next >= self.the_size):
                return
            # To keep reading if it is a potential integer number
            while((self.the_string[the_next].isalpha() or self.the_string[the_next].isdigit()) and (self.the_pos < self.the_size)):
                the_next += 1
                if(the_next >= self.the_size):
                    break
                self.the_pos += 1
                the_int += self.the_string[self.the_pos]

            if(the_int.isdigit()):
                #print(the_int,"->INT")
                return Token(the_int, "INT")
            # If it started as an int but got messed up we return an error token
            else:
                #print(the_int, "->ERROR")
                return Token(the_int, "ERROR")

