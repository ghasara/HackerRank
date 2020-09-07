class A: 
  
    def func(self, arg): 
        self.arg = arg 
        print("Value of arg = ", arg) 
  
  
# Creating an instance 
obj = A()   
  
# bound method 
print(obj.func)
