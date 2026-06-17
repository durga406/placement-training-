def func():
    n=int(input())
    length=len(str(n))
    if length>4:
        print("f{n} is not is not a valid car number")
    s=0
    while n>0:
        d=n%10
        s+=d
        n=n//10
    if s%3 and s%5 and s%7:
        print("Lucky Number")
    else:
        print("Sorry its not my lucky number")
func()
