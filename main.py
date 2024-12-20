from unittest import skipIf

from resources import logo, letters, digits

def type_your_message ():
    return input("Type your message: ")


def choose_encode_decode ():
    choice = input("Do you want to encode or decode? ").lower()
    if choice == "encode":
        return 1
    elif choice == "decode":
        return -1
    else:
        print("You entered invalid command. Please try again. ")
        choose_encode_decode()

def type_shift_amount ():
    shift_amount = input("Type in shift amount: ")
    for item in shift_amount:
        if item not in digits:
            print("Please enter shift amount as a whole number. ")
            type_shift_amount()
    return int(shift_amount)


def ciphering (msg, shift, choice):
    coded_msg = ""
    for character in msg:
        if character not in letters and character not in digits:
            coded_character = character
        elif character in letters:
            i = letters.index(character)
            new_i = i + shift * choice
            coded_character = letters[new_i]

        else:
            i = digits.index(character)
            new_i = i + shift * choice
            coded_character = digits[new_i]
        coded_msg += coded_character
    return coded_msg

def want_go_again ():
    go_again = input("Do you want to go again? ")
    if go_again.lower() == "yes":
        return True
    elif go_again.lower() == "no":
        return False
    else:
        print('Please type in "yes" or "no". ' )
        want_go_again()

app_is_on = True
print(logo)
while app_is_on:
    print(f"Your coded message is {ciphering(type_your_message(), type_shift_amount(), choose_encode_decode())}")
    app_is_on = want_go_again()
