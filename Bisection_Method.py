
def f(x):
    return x**3 - x - 1
def bisection_roots(a,b,error_percent):
    c=a
    P_I=0
    current_error_percent=100
    while current_error_percent>=error_percent:
        P_I=c
        c = (a+b)/2 
        if P_I != 0.0 and c != 0.0:
            current_error_percent = abs((P_I - c)/c) * 100
        if f(c)== 0:
            return c
        elif f(c) * f(a) < 0: #assuming a is +ve
            b=c
        else :
            a=c
    print(f"Overall Error : {current_error_percent} ")
    return c

if __name__ == '__main__':
    num1 = 0.0
    num2 = 1.0
    error_percent = 0.5 #Maximum Error is Here 2 decimal place
    root = 0.0
    while True:
        val1 = f(num1)
        val2 = f(num2)

        if val1 * val2 < 0 :
            print(f"Root Lies Between {val1} and {val2} ")
            root = bisection_roots(num1,num2,error_percent)
            break

        num1 = num2
        num2 += 1
    print(f"Root is {root}")

