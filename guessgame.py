i = 1
correct = 9
while(i<=3):
    guess = int(input("Guess : "))
    if(correct==guess):
        print("its correct guess ",correct)
        break
    else:
        i+=1
if(i>=3):
    print("Sorry ! you failed....")
else:
    print("congrates ! you have found.....")        