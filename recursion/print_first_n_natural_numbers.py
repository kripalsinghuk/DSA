def print_natural_nums(n):
    if n<=0:
        return
    print(" ",n)
    n-=1
    print_natural_nums(n)
n = int(input("please enter number"))    
print_natural_nums(n)    

