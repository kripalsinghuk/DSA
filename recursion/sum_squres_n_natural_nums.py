def sum_sq_nums(n,sum):
    if n<=0:
        print("Sum is ",sum)
        return
    sum = sum + n*n
    n-=1
    sum_sq_nums(n,sum)
num = int(input("Please enter a number "))
sum_sq_nums(num,0)
