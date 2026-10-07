while True:    
    try:
        x = int(input("whats x ?"))
    except ValueError:
        print("The input is not integer ") 
    else:
        print("x is ",x)
        break
