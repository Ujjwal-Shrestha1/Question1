while 1==1:
    number=list(map(int,input("Enter Number list:").split()))
    num=input("Number:", )
    for i in range(len(number)):
        if int(number[i]) == int(num):
            print(i)
        
    if int(num) not in number:
        print(-1)
    
        


