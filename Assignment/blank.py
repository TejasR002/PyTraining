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


print("The GCD of Number is : {}".format(GCD(Num1,Num2)))