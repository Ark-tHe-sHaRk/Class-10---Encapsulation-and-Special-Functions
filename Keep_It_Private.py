class private:
    
    #Private Varible
    __PrivateVar = 27;

    #Private Method
    def __PrivateMethod(self):
        print('This is a priate method inside class private')

    #Function to print value of private varible
    def PrintPrivateVar(self):
        print('Private Varible Value Name: ', self.__PrivateVar)

#Object creation and method call
obj = private()
obj.PrintPrivateVar()
obj.__PrivateMethod() #This will give error as it is private method
