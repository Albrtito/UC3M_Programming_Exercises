time_of_day = input("Write time of day: Day or Night ")
number_of_soldiers = int(input("Write number of soldiers as a whole number "))
number_of_siege_engines = int(input("Write number of siege engines as a whole number "))
poison = input("Is there any poison to use: Yes or No ")
weather = input("Is it raining? : Answer with Rain or no Rain ")

#Define the time of day string given by the user as a bool value
if time_of_day == "Day":
    time_of_day = True
    #print("Day is now True")

elif time_of_day == "Night":
    time_of_day = False
    #print("Day is now False")

else:
    #If the user gave a value that is not defined warn him
    print("Time of day is undefined")


# Define the Yes and NO values of poison as a bool variable
if poison == "Yes":
    poison = True
    #print("Poison Yes is now True")
elif poison == "No":
    poison = False
    #print("Poison no is now False")
else:
    #If the user gave a value that is not defined warn him
    print("Poison is undefined")


# Define the Rain and no Rain possible inputs of wheather as a bool variable
if weather == "Rain":
    weather = True
elif weather == "no Rain":
    weather = False
else:
    #If the user gave a value that is not defined warn him
    print("weather is undefined")


# Definition as a function of each attack depending on the requisites needed for the attack.
#Each one asks for the variables needed for the attack and returns whether the attack is possible or not
def silent_attack(time_of_day_def, weather_def, number_of_soldiers_def, siege_engines_def):
   #if statement checks if all requisites for the attack are true
    if time_of_day_def == False and weather_def == False and number_of_soldiers_def >= 500 and siege_engines_def >= 50:
        print("The recommendation is Silent Attack")
    else:
        print("Silent attack is not possible")

def crossfire(time_of_day_def, weather_def, number_of_soldiers_def, number_of_siege_engines_def):
    # if statement checks if all requisites for the attack are true
    if time_of_day_def == True and number_of_soldiers_def >= 10000:
        print("The recommendation is crossfire")


def killTheKing(time_of_day_def, number_of_soldiers_def, poison_def):
    # if statement checks if all requisites for the attack are true
    if time_of_day_def == False and number_of_soldiers_def == 1 and poison_def == True:
        print("The recommendation is Kill the King")


silent_attack(time_of_day, weather, number_of_soldiers, number_of_siege_engines)
crossfire(time_of_day,weather,number_of_soldiers,number_of_siege_engines)
killTheKing(time_of_day,number_of_soldiers,poison)
