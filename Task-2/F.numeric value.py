def numeric_value():
    try:
        intger_num=int(input("enter a numaric value : "))
        print("Done")
    except ValueError as er:
        print(f"\n{er}")
        print("\nnot anumeric value")
    else:
        print(f"numeric num is : {intger_num}")

flag=input("are you want to cheak of your input if numeric or not (y:n)? ").lower()    
while flag=='y':
    numeric_value()
    flag=input("are you want to cheak again (y:n)? ")
