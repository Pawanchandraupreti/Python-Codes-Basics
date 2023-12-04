a=int(input("Enter first no: "))
b=int(input("Enter second no: "))
try:
    c=a/b
    print(c)
except:
    print("Error Occured ")
else:
    print("No Exception Raised")
finally:
    print("This is the end of program")
#__________________________________________
a=10
b=5
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[5])
except Exception as e :
    print(e)
#__________________________________________
a=10
b=0
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[5])
except Exception as e :
    print(e)

#_______________________________________________________________
a=10
b=0
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[3])
except :
    print("Exception raised using default Denominator")
    b=1
    c=a/b
    print(c)
 #______________________________________________________________
a=10
b=0
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[5])
except (ZeroDivisionError,IndexError):
    print("Exception Raised")


#_________________________________________________________________
def number():
    x=input()
    if(x=="17"):
        raise ValueError("NOT GOOD")
number(2
       )