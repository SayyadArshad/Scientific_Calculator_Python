def fun(a,b,c,d):
    try:
        ans=(a+b)//(c-d)
    except:
        print("division not possible")
    else:
        print(ans)
fun(1,2,3,4)