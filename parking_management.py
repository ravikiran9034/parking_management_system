# parking_space shows the type of vechile with its cost and how many position it will take the parking space

parking_space = {
    "Bike": {
        "space_taken": {
            "Bike" : 1
        },
        "cost": 10
    },
    "Auto": {

        "space_taken": {
            "Auto":1
        },
        "cost": 20
    },
    "Car": {

        "space_taken": {
            "Car":1
        },
        "cost": 33
    }
}
profit = 0
license_plates = set() # 'license_plates = set()'stores the license palte number of vechiles
# 'avaible_space' has the availble spaces for each vechile invidually
avaible_space = {
    "Bike": 5,
    "Auto": 3,
    "Car": 2
}
def process_coins():

    print("Please insert coins")
    total = 0
    coins_five = int(input("How many 5rs Coins : "))
    coins_ten = int(input("How many 10rs Coins : "))
    coins_twenty = int(input("How many 20rs Coins : "))
    total = coins_five*5 + coins_ten*10 + coins_twenty*20
    return  total

def is_payment_sucesful(money_recived,vechile_fare):
    if money_recived >= vechile_fare:
        global profit
        profit += vechile_fare
        change = money_recived - vechile_fare
        print(f"here is your Rs{change} in change")
        return True
    else: print("sorry insuffient payment")


    # this fucn checks the available spaces for vechile to enter if space is not availble will prompt
# Not enough space is availble for your vechile
def check_resourses(Vechile_position):
    for i in Vechile_position:
        if Vechile_position[i] > avaible_space[i]:
            print(f"Not enough space is availble for your {i}")
            return False
    return True


# def exit_vechile():
#     avaible_space[choice] +=1
#     return True
# when is_on is true code will run , when it is false the code will stop and every stored recorde will be erased
is_on = True
while is_on:
    choice = input("Vechile Type? (Bike/Auto/Car) :  ") # this will take vechile type
    if choice == "Report" or choice == "report": # this will show available spaces left in the parking(avaible_space)
        print(f"Bike = {avaible_space['Bike']} Spaces left")
        print(f"Auto = {avaible_space['Auto']} Spaces left")
        print(f"Car = {avaible_space['Car']} Spaces left")
        print("vechile plate number of parked vechile",license_plates)
        print("total profit is : ",profit)

    elif choice == "Off" or choice == "off": #this will make is_on flase
        is_on = False
    # this will exit the vechile from parking and remove the plate number
    elif choice == "exit" or choice == "Exit":
        choice = input("Vechile Type for exit? (Bike/Auto/Car) :  ")
        print(f"Fare of your {parking_space[choice]['cost']}")
        plate_to_remove = input("Enter your license plate to remove :  ")
        if plate_to_remove in license_plates:
            Vechile_Type = parking_space[choice]
            Vechile_Type_exit = Vechile_Type['space_taken']
            avaible_space[choice] += 1
            payment = process_coins()
            if is_payment_sucesful(payment,Vechile_Type['cost']):
                license_plates.remove(plate_to_remove)
                print(f"{plate_to_remove} : Exit now,Thank you")


        else:
            print(f"License plate {plate_to_remove} not found. ")

    else: # this will check if space is aviable for the vechile
        Vechile_Type = parking_space[choice]
        # print(Vechile_Type)
        if check_resourses(Vechile_Type['space_taken']):
            avaible_space[choice] -=1
            plate = input("enter your linces plate number : ")
            license_plates.add(plate)
            print(license_plates)
            print("You Vechile is Parked")
