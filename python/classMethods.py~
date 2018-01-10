class Employee:
  def __init__(self, first, last, sal):
    self.first = first
    self.last = last
    self.sal =sal
  def email(self):
      return "{} {}".format(self.first, self.last)
      # return first, last


  @classmethod
  def cm(cls,emp_str):
   first,last,sal = emp_str.split('-')
   return cls(first, last, sal)
def arg(*args, **kwargs):
    print(args)
    print(kwargs)   
emp_str1 = "aamir-maqbool-7000"
newemp = Employee.cm(emp_str1)
print(newemp.last)
var=("hello")
var2={"name":"burhan","class":"high"}
#arg("hello","hii", cl=2, name=3)
arg(*var, **var2)

emp1=Employee("burhan", "aslam", 2000)

#emp1.Employee("Burhan","aslam",1000)
#print(emp1.last)
#print(emp1.email())

