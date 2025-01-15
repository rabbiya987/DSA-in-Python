def fibo(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibo(n-1)+fibo(n-2) # The function is called in itself. 
print(fibo(5))