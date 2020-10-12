while 1==1:
    word = input("haystack:", )
    needle = input("needle:", )
    a=len(needle)
    test1=[]
    for i in range(len(word)):
        test=word[i:i+a]
        test1= test1 + [word[i:i+a]]
        if test==needle:
            print(i)
        
    if str(needle) not in test1:
        print(-1)

   
