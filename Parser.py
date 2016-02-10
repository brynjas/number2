from Lexer import *

class Parser:
    def __init__(self):
        # Create a Lexer
        self.the_Lex = Lexer()
        # Calls getData() to get all of the Tokens from input
        self.statements = self.the_Lex.getData()
        # A stack that we will use to load all of the Tokens that make
        # up a single statement
        self.the_stack = []

        #self.state_pos = 0

        # Calls the statements function
        self.Statements()

    def Statements(self):
        # To make sure we dount go out of the array
        if(len(self.statements) == 0):
            return

        # Loop that loads all of the statements until then next semicolon
        # into an array that is passed down for processing
        while((self.statements[0].tCode != "SEMICOL") and (self.statements[0].tCode != "END")):
            self.the_stack.append(self.statements.pop(0))

            # To terminate ef there was an ERROR token
            if(self.statements[0].tCode == "ERROR"):
                print("Syntax error!")
                exit(0)
            # Just to make sure we dont go out of the array
            if(len(self.statements) == 0):
                print("Syntax error!")
                exit(0)

        # To stop if there are no more Tokens
        if(len(self.statements) == 0):
            return

        # Stop if last Token was END statement
        if(self.statements[0].tCode == "END"):
            return

        # Statement is called
        self.Statement()

        # Recursively call Statements if the tokens ended with a semicolon
        if(self.statements[0].tCode == "SEMICOL"):
            self.statements.pop(0)
            self.Statements()

    def Statement(self):
        if(self.the_stack[0].tCode == "ID"):
            print("PUSH", self.the_stack[0].lexeme)
            # Pop the PUSH statement from the stack
            self.the_stack.pop(0)
            if(self.the_stack[0].tCode == "ASSIGN"):
                # Pop the ASSIGN statement from the stack
                self.the_stack.pop(0)
                self.Expr()
                print("ASSIGN")

            # Throw an error if ID is not followed by ASSIGN
            else:
                print("Syntax error!")
                exit(0)

        elif(self.the_stack[0].tCode == "PRINT"):
            if(self.the_stack[1].tCode == "ID"):
                print("PUSH", self.the_stack[1].lexeme)
                # Pop the PRINT statement and the variable from the stack
                self.the_stack.pop(0)
                self.the_stack.pop(0)
                print("PRINT")
            else:
                print("Syntax error!")
                exit(0)
        # If the first token is not an ID or a PRINT statement, then its an error
        else:
            print("Syntax error!")
            exit(0)


    def Expr(self):
        self.Term()
        # just to check if the stack isnt empty
        if(len(self.the_stack) != 0):
            if(self.the_stack[0].tCode == "ADD" or self.the_stack[0].tCode == "SUB"):
                # Temporary placeholder for the ADD or SUB statement
                temp = self.the_stack[0].tCode
                # Pop the ADD or SUB statement from the stack
                self.the_stack.pop(0)
                self.Expr()
                print(temp)

    def Term(self):
        self.Factor()
        # just to check if the stack isnt empty
        if(len(self.the_stack) != 0):
            if(self.the_stack[0].tCode == "MULT"):
                # Pop the MULT command from the stack
                self.the_stack.pop(0)
                self.Term()
                print("MULT")    

    def Factor(self):
        # just to check if the stack isnt empty
        if(len(self.the_stack) != 0):
            if((self.the_stack[0].tCode == "INT") or (self.the_stack[0].tCode == "ID")):
                print("PUSH", self.the_stack[0].lexeme)
                self.the_stack.pop(0)
            
            elif(self.the_stack[0].tCode == "LPAREN"):
                # Pop the Left parentheses from the stack, dont need the print it out
                self.the_stack.pop(0)
                self.Expr()
                if(self.the_stack[0].tCode == "RPAREN"):
                    # Pop the Right parentheses from the stack, dont need the print it out
                    self.the_stack.pop(0)
                else:
                    print("Syntax error!")
                    exit(0)
            else:
                print("Syntax error!")
                exit(0)
        else:
            print("Syntax error!")
            exit(0)
