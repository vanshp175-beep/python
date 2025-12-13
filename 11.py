#Fucntion: fuction is a group of statements which returns some result.


 1. Function with paramenters and without return value
  count=0
    a=False
    for i in range(1, (num//2)+1):
        if num%i==0:
            count=count+1
    if count==1:
       a=True
    
b=isPrime1(11)
if b==True:
    print("Prime number")
else:
    print("Not a prime number")


2. Function with paramenters and with return value
    
def isPrime1(num):
    count=0
    a=False
    for i in range(1, (num//2)+1):
        if num%i==0:
            count=count+1
    if count==1:
       a=True
    return a
    
b=isPrime1(12)
if b==True:
    print("Prime number")
else:
    print("Not a prime number")

3. Function without paramenters and without return value

    def isPrime():
    num=int(input("Enter your number :"))
    count=0
    for i in range(1, (num//2)+1):
        if num%i==0:
            count=count+1
    if count==1:
        print(num," is a prime number")
    else:
        print(num," is not a prime number")

isPrime()
  

  4. Function without paramenters and wit return valuedef isPrime1(num):
 
def isPrime1():
    num=int(input("Enter your number"))
    count=0
    a=False
    for i in range(1, (num//2)+1):
        if num%i==0:
            count=count+1
    if count==1:
       a=True
    return a
    
b=isPrime1()
if b==True:
    print("Prime number")
else:
    print("Not a prime number")

    
