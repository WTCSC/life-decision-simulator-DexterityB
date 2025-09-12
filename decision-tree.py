day = 1
deaths = 0
scenario = 0
first_day = True

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
    if first_day == True:
        print("The day is Monday")
        print("The start of just another boring, mundane day")
        first_day = False

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
            if deaths == 3:
                scenario = 25
            else:
                print('You wake up in a cold sweat. "What just happened?!?"')
                print("Do you check the weather before your day starts?")
                print("1) Yes")
                print("2) No")
                deaths += 1
                scenario = decision(0, 4)

        case 3:
            print("You choose to just wing it and not bring an umbrella or raincoat with you")
            print("Unfortunately the rain is acidic and you die\n")
            if deaths == 3:
                scenario = 25
            else:
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
            if deaths == 3:
                scenario = 25
            else:
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
            print("You choose to swerve left???")
            print("You hit oncoming traffic and your vision goes black\n")
            if deaths == 3:
                scenario = 25
            else:
                print('You wake up in a cold sweat. "What just happened?!?"')
                print("Do you check the weather before your day starts?")
                print("1) Yes")
                print("2) No")
                deaths += 1
                scenario = decision(0, 4)

        case 8:
            print("That's the correct choice")
            print("You swerve right, away from the car and away from other traffic")
            print("You continue on your way to school")
            scenario = 11

        case 9:
            print("Surprisingly, you choose to wear the appropriate clothing")
            print("Now, do want to be responsible and go to school?")
            print("1) Yes")
            print("2) No")
            scenario = decision(11, 10)

        case 10:
            print("You choose to skip school")
            print("Unforunately someone notices and you get in trouble")
            print("You pass away because of this fact\n")
            if deaths == 3:
                scenario = 25
            else:
                print('You wake up in a cold sweat. "What just happened?!?"')
                print("Do you check the weather before your day starts?")
                print("1) Yes")
                print("2) No")
                deaths += 1
                scenario = decision(0, 4)

        case 11:
            print("You make it to school")
            print("Another mundance, boring school day is over\n")
            day += 1
            scenario = 0
            if day == 4:
                scenario = 14

        case 14:
            print("Unfortunately, you woke up late today")
            print("Do you try to drive to school as fast as possible or take it slower and be late")
            print("1) Go to school fast")
            print("2) Take it slow")
            scenario = decision(15, 16)

        case 15:
            print("Like a typical teenager, you go way too fast on the highway")
            print("You crash and your vision goes black\n")

            if deaths == 3:
                scenario = 25
            else:
                print("You wake up, dizzy & confused")
                deaths += 1
                scenario = 14

        case 16:
            print("You're a little late, but you make it to school")
            print("What class are you going to?")
            print("1) Chemistry")
            print("2) English")
            scenario = decision(18, 17)

        case 17:
            print("You go to english, and die of boredom")
            print("Congratulations, you got the only instant loss!\n")
            scenario = 25

        case 18:
            print("You go to chemistry, and you guys are doing a lab today! With dangerous chemicals")
            print("Unfortunately because you arrived late, you won't finish it today")
            print("What do you do?")
            print("1) Rush to finish the lab")
            print("2) Finish it later")
            scenario = decision(19, 20)

        case 19:
            print("You go too fast, and spill deadly chemicals all over")
            print("It's very painful\n")
            if deaths == 3:
                scenario = 25
            else:
                print("You wake up, dizzy & confused")
                deaths += 1
                scenario = 14

        case 20:
            print("You decide to finish later as to not rush a dangerous lab, smart choice")
            print("What is your next class?")
            print("1) History")
            print("2) Math")
            scenario = decision(21, 24)

        case 21:
            print("Sorry to break the fourth wall here, but how emotional are you?")
            print("1) Very")
            print("2) Not that emotional")
            scenario = decision(22, 23)

        case 22:
            print("The history lesson is devasting")
            print("You die from sadness\n")
            if deaths == 3:
                scenario = 25
            else:
                print("You wake up, dizzy & confused")
                deaths += 1
                scenario = 14

        case 23:
            print("History was pretty boring, but you make through")
            print("What is your final class?")
            print("1) Math")
            print("2) English")
            scenario = decision(24, 17)

        case 24:
            print("You go to math class, it's light work")
            print("Another mundance, boring school day is over\n")
            day += 1
            scenario = 14
        
        case 25:
            print("You... lost")
            print("Would you like to play again")
            print("1) Yes")
            print("2) No")
            scenario = decision(26, 27)

        case 26:
            day = 1
            deaths = 0
            scenario = 0

        case 27:
            break

    if day == 6:
        print("Congratulations, you've made it through another week of school!\n")
        print("Would you like to play again")
        print("1) Yes")
        print("2) No")
        scenario = decision(26, 27)