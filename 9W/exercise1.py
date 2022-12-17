import random
numbers = ('1','2','3','4','5','6','7','8','9','0')
symbols = ('!','@','~','$','%','&','/','(',")")
uppers =('Q','W','E','R','T','Y','U','I','O','P','A','S',
         'D','F','G','H','J','K','L','Ñ','Z','X','C','V',
         'B','N','M')
characters = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
              'q','w','e','r','t','y','u','i','o','p',
               'a','s','d','f','g','h','j',' k','l','ñ',
                'z','x','c','v','b','n','m',
                'Q','W','E','R','T','Y','U','I','O','P','A','S',
                 'D','F','G','H','J','K','L','Ñ','Z','X','C','V',
                'B','N','M',
                '!','@','~','$','%','&','/','(',")")


def password_generation ():
    password_def = []
    lenght_password = random.randint(8, 12)
    """Generate possible positions for the 1 upper, 1 number and 1 symbol that the password needs to have"""
    position_for_upper = random.randint(0,lenght_password-1)
    position_for_number = random.randint(0,lenght_password-1)
    position_for_symbol = random.randint(0,lenght_password-1)
    """Check if the positions of the number, symbol and upper are the same, if so, change them"""
    while position_for_upper == position_for_number:
        position_for_number = random.randint(0,lenght_password-1)
    while (position_for_number == position_for_symbol) or (position_for_upper == position_for_symbol):
        position_for_symbol = random.randint(0,lenght_password-1)
    """We now have 3 positions in which to put the 3 mandatory characteristics of the password"""
    """Loop for entering values in the password:"""
    for i in range(lenght_password):
        if (i != position_for_number) and (i != position_for_upper) and (i != position_for_symbol):
            password_def.append(characters[random.randint(0, len(characters) - 1)])
        if i == position_for_number:
            password_def.append(numbers[random.randint(0, len(numbers) - 1)])
        if i == position_for_symbol:
            password_def.append(symbols[random.randint(0, len(symbols) - 1)])
        if i == position_for_upper:
            password_def.append(uppers[random.randint(0, len(uppers) - 1)])

    return password_def


# Get the password into a variable and transform it into a list
password_list = password_generation()
password_string = str()
for i in range(len(password_list)):
    password_string += password_list[i]

print(password_string)