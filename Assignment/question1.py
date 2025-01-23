# 1. Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.

#     The program should take input from console or args and should handle unexpected inputs    

#     Constraints:

#         - For loop is not allowed

#         - input should be in words:

#             - e.g.: onetwo = 12, sixone = 61

#         - words will be within zero to nine

#         - Cannot use inbuilt methods like max, min, or any math function    

#     Example 1:

#         - Input 1: onezero

#         - Input 2: twozero

#         - Output: onezero

#     Example 2:

#         - Input 1: twosix

#         - Input 2: twofour

#         - Output: two



nums = { "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }
digits  = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}


def getnum(x):
    i = 0      
    result = ""
    ans = ""
    while i < len(x):
        ans = ans + x[i]
        if ans in nums :
            result = result + nums[ans]
            i = i+1
            ans =""
        else :
            i = i + 1
    return int(result)

x1 = input("Enter input 1: ")
x2  = input("Enter input 2: ")

Num1 = getnum(x1)
Num2 = getnum(x2)

def GCD(Num1,Num2):
    while Num2 != 0:
        Num1, Num2 = Num2, Num1 % Num2 
    return Num1

k = str(GCD(Num1,Num2))

t = 0
FinalAns = ""
while t < len(k):
    FinalAns = FinalAns + digits[k[t]]
    t = t+ 1  
print("GCD: ",FinalAns)