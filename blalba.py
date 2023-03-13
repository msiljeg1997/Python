def fibonachi():
    num = int(input("dajbroj"))
    i = 1
    if num == 0:
        fib = []
    elif num ==1:
        fib = [1]
    elif num ==2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[-1] + fib[-2])
            i += 1
        return fib
print(fibonachi())
