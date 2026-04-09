def cal_factorial(n,f):
    if n<=0:
        print("Factorial is ",f)
        return
    f = f*n
    n-=1
    cal_factorial(n,f)
num = int(input("Please enter a number "))
cal_factorial(num,1)
