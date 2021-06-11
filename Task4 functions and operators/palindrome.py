def palindrome(num):
    result = 0
    temp = num
    while(num>0):
        r = num % 10
        result = result*10 + r
        num = num // 10
    
    if(temp==result):
        print(f"Number({temp}) Is Palindrome!")
    else:
        print(f"Number({temp}) is Not Palindrome")
