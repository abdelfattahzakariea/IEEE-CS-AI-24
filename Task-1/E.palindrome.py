string= input("enter word you would to check it: ")
revstr=string[::-1]
if revstr==string:
    print(f"The word '{string}' is a palindrome.")
else:
    print(f"The word '{string}' is not a palindrome.")    
