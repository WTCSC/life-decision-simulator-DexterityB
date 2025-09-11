day = 1
deaths = 0
scenario = 0
new_day = True

def decision(yes, no):
    while True:
        yesno = input("")
        if yesno == "1":
            return_value = yes
            break
        elif yesno == "2":
            return_value = no
            break
    return return_value

while True:
    if new_day == True:
        match day:
            case 1:
                print("The day is Monday")
            case 2:
                print("The day is Tuesday")
            case 3:
                print("The day is Wednesday")
            case 4:
                print("The day is Thursday")
            case 5:
                print("The day is Friday")
        print("Just another boring, mundane, day")
        new_day = False

    match scenario:
        case 0:
            print("After waking up, you check the weather. Looks like it's going to rain")
            print("Do you bring a raincoat and umbrella?")
            print("1) Yes")
            print("2) No")
            scenario = decision(1, 3)

        case 1:
            print("Good choice, but now you have to go to school, AND it just started raining")
            print("Do you walk or drive?")
            print("1) Walk")
            print("2) Drive")
            scenario = decision(2, 6)

        case 2:
            print("While you're walking, there's a flash flood, and you drown\n")
            print('You wake up in a cold sweat. "What just happened?!?"')
            print("Do you check the weather before your day starts?")
            print("1) Yes")
            print("2) No")
            deaths += 1
            scenario = decision(0, 4)

        case 3:
            print("You choose to just wing it and not bring an umbrella or raincoat with you")
            print("Unfortunately the rain is acidic and you die\n")
            print('You wake up in a cold sweat. "What just happened?!?"')
            print("Do you check the weather before your day starts?")
            print("1) Yes")
            print("2) No")
            deaths += 1
            scenario = decision(0, 4)

        case 4:
            print("You choose not to look at the weather forecast, and instead just glance outside")
            print("It appears to be snowing, what do you wear?")
            print("1) Thick, winter clothing")
            print("2) Thin, summer clothing")
            scenario = decision(9, 5)

        case 5:
            print("For some reason, you decide to wear shorts and a t-short when it is snowing outside")
            print("To no one's surprise, you freeze to death\n")
            print('You wake up in a cold sweat. "What just happened?!?"')
            print("Do you check the weather before your day starts?")
            print("1) Yes")
            print("2) No")
            deaths += 1
            scenario = decision(0, 4)

        case 6:
            print("You choose to drive to school, which was a good choice because there's too much water on the ground")
            print("Unfortunately water on the ground also affects cars and causes a car on the otherside of the road to come careening towards you")
            print("Do you swerve left or right to avoid the car?")
            print("1) Left")
            print("2) Right")
            scenario = decision(7, 8)

        case 7:
            case = 0

        case 8:
            case = 0

        case 9:
            case = 0

        case 10:
            case = 0

        case 11:

        case 14:
            case = 0

        case 15:
            case = 0

        case 16:
            case = 0

        case 17:
            case = 0

        case 18:
            case = 0

        case 19:
            case = 0

        case 20:
            case = 0
            break