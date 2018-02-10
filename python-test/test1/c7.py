class Student():
    a=3
    b=5
    def add(x,y):
        return (x+y)
    def print_cod(self):
        print("hello")
    def printab(self):
        print(self.a)
        print('a:  '+str(self.a))
stu=Student()
stu.print_cod()
stu.printab()
#a=stu.add(3,2)
#print(a)