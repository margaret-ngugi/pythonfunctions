def year_of_birth(name,age):
    year = 2023-age
    print(f"Hello{name},you were born in{year}")


def my_country(country="Kenya"):
    print(f"Hello you are from{country}")
        

def hello(* names):
    for name in names:
        print(f"Hello{name}")

def sum(*nums):
    answer = 0
    for num in nums:
        answer += num
    return answer
      
def multiply_many(**kwargs):
    answer = 1
    for num in kwargs.values():
        answer*= num
    return answer

    
def  concatenate_arg(*string): 
     return "".join(string) 
     print(concatenate(""))


def concatenate_kwargs(**kwargs):
    result = ""
    for name in kwargs.values(): 
        result += name
        return result      
       


