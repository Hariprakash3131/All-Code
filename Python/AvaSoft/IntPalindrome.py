def palindrome(num:int):
    s=str(num)
    if s==s[::-1]:
        print("This value is a palindrome:",s)
    else:
        print("This value is not a palindrome:",s)

palindrome(int(input("Enter the number:")))