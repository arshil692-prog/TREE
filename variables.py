"""

variable is used to stores data in program 

ex . name = "arshil"

(name) > variable 
(arshil) > is the value that stores into variables
(=) > assignment opretor

define > a variables is named memory location to stores data that can be used and modifed during program excuation

types of variables 
> global 
> local 
> class 
> instance

local variable 

> a variable creates inside of funcation that called a local variables 
> and we can only accesed within that funcation 

def greet ():
    name = "arshil"           ( local variable )
    print (name)


global variables 
> a global variable is created outside of all funcations
> it can be accessed ffrom anywhere in the program 

name = "arshil"
def greet ():              ( global variable )
    print (name)

greet () 
print (name)

instance variable 
> an instance variable belongs to an object (instance) of class 
> is created inside the __int__() method using self.
> each object have has own copy of the variabel

class student :
    def ___int___(self,name):
        self.name = name      (instance variable)

s1 = student = ("arshil")
s2 = student = ("nishant")
 
print (s1.name)
print (s2.name)

(key point : every object stores its own valuse)


class variable

> a class variables belongs to the class but outside all methods .
> it is decleared inside the class but outside all methods 
> all object shares the same value


class student :
    school = "chh shivaji highschool"

def __int__(self,name):
    self.name = name 
    s1 = student ("arshil")
    s2 = student ("nishant")

print (s1.school)
print (s2.school)

( we can change the class variables )

student.school = "yxz school"

print (s1.school)  > yxz school
print (s2.school ) > yxz school


"""