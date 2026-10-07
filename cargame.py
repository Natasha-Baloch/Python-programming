car_diagram = r'''
       ______
      //  ||\ \
_____//___||_\ \___
 )  _          _    \
 |_/ \________/ \___|
___\_/________\_/____
'''

started = False
print(car_diagram)
print("Type 'help' for instructions.")

while True:
    car = input(">").upper()
    if car == "HELP":
        print("start - to start the car")
        print("stop  - to stop the car")
        print("quit  - to exit")    
    elif car == "START":
        if started:
            print("Car is already started...")
        else:
            started = True      
            print(car_diagram)
            print("Car started...Ready to go!")
    elif car == "STOP":
        if not started:
            print("Car is already stopped.....")
        else:
            started = False
            print("Car stopped.")
    elif car == "QUIT":
        print("Goodbye!")
        break    
    else:
        print("I don't understand that -----")

    

