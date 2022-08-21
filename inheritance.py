class Robot:
    def __init__(self, name,function,manufacture_year):
        self.name = name
        self.function = function
        self.manufacture_year = manufacture_year

    
    def say_hi(self):
        print("Hi, I am " + self.name)

class Perfomance:
    def __init__(self,memory,speed):
        self.memory = memory
        self.speed = speed

    def memory_test(self):
        if self.memory < 10:
            return "fast"
        elif self.memory > 20:
            return "low"
        else:
            return "average"
        
class PhysicianRobot(Robot):
    def __init__(self,name,function,manufacture_year,use):
       super().__init__(name,function,manufacture_year)
       self.use = use

class AIROBOT(Robot,Perfomance):
    def __init__(self,name,function,manufacture_year,memory,speed):
        Robot.__init__(self, name,function,manufacture_year)
        Perfomance.__init__(self,memory,speed)
       
airobot = AIROBOT("hari","work",2016,128,10)

print(airobot.memory)
print(airobot.function)
print(airobot.speed)

