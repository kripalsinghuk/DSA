def n_natural_nums(n):
    if n<=0:
        return
    print(" ",n)
    n-=1
    n_natural_nums(n)
num = int(input("Please enter number "))
n_natural_nums(num)
