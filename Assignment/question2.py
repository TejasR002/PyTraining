x = int(input("Enter n : "))

res = []
stack = []

def Combopara(Open,closed):
    if Open == closed == x:
        res.append("".join(stack))
        return
    if Open < x:
        stack.append('(')
        Combopara(Open+1,closed)
        stack.pop()
    if closed < Open:
        stack.append(')')
        Combopara(Open,closed+1)
        stack.pop()
Combopara(0,0)
print(res)


