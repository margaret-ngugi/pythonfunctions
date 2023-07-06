def even_numbers():
    x=range(10)
    for i in x:
        if i%2 == 0:
            print(i)

def odd_numbers():
    x=range(20)
    for i in x:
        if i%2!=0:
            print(i)

def divisible_by_five():
    x=range(50)
    for i in x:
        if i%5==0:
            print(f"{i}is divisible by 5")
        else:
            print(f"{i}is not divisible by 5")

def multiple_comparison():
    x=range(50)
    for i in x:
        if i%5==0:
            print(f"{i}is divisible by 5")
        elif i%7==0:
            print(f"{i}is divisible by 7")
        elif i%9==0:
            print(f"{i}is divisible by 9")
        else:
            print(f"{i}is not divisible by 5,7 or 9") 

def add_or_even(): 
    x=range(20)
    for i in x:
        if i%2==0 and i%3==0:
           print(f"{i}is divible by both 2 and 3")
        elif i%2==0 or i%3==0:
            print(f"{i}is divible by either 2 or 3") 
        else:
            print(f"{i}is not divible by either 2 or 3")

def while_loop():
    x=1
    while x<10:
        print("hello")
        x+=1

def break_statement():
    x=1
    while x<10:
        print("hello")
        x+=1
        if x==5:
            break

def continue_statement():
    x=0
    while x<=20:
        x+=1
        if x%3==0:
            continue
        print(x) 

#Write a function that uses while, if and continue statements to print all the even numbers 
#between 0 and 50. 
def even_number():
    x=0
    while x<=50: 
        x+=1
        if x%2!=0:
            continue
        print(x)
    
    
#Write a function that takes an integer argument and prints "Prime" if the number is prime,
# and "Not prime" if the number is not prime.
def prime_numbers(x=11):
    if(x%1==0 and x%11==0):
        print(f"{x}prime number")
    else:
        print(f"{x}not prime")    
       




#Write a function that takes a list of integers as input and prints the sum of all the
# even numbers in the list.
def sum_even():
    sum = 0
    for i in range(0,15):
        if i%2==0:
           sum=sum+1
print(sum_even)    
    


#Write a function that takes any two integers as input, and prints the sum of all the
# numbers between the two integers (inclusive) that are divisible by 3.
def divisible_three(n1,n2):
    sum=0
    for i in range(n1,n2):
      if i%3==0:
        sum+=1
    print(sum)    

    #Define a function that accepts a string as input and uses the for loop to iterate
# through the string and count the vowels

def count_vowels(name):
    count=0
    vowels=("a","e","i","o","u")
    for i in name:
        for b in vowels:
            if i==b:
                count+=1
        
    return count
print(count_vowels("margaret"))    

#or
def count_vowels(school):
    count=0
    vowels="a","e","i","o","u"
    for char in school:
        if char in vowels:
            count+=1
    return count
school="Akirachix" 
my_vowels=count_vowels(school)
print(my_vowels) 