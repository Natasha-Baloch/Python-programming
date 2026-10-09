#Check if a password is strong.
# Ask the user to enter a password.
# A strong password has at least 8 characters, one capital letter, one small letter and one digit.
# Use a loop with isupper(), islower(), isdigit() and print 'Strong' or 'Weak'.
#Try it yourself first. The full solution is in the Solutions section at the end of this book (Solution 2)

while True:
    password = input("Enter password: ")

    if (
        len(password) >= 8
        and any(char.isupper() for char in password)
        and any(char.islower() for char in password)
        and any(char.isdigit() for char in password)
    ):
        confirm = input("Want to confirm password (Y/N): ")

        if confirm.lower() == 'y':
            print("Your password is confirmed!")
            break

        elif confirm.lower() == 'n':
            print("Try another password!")
            continue

        else:
            print("Write the correct letter (Y/N)!")
            continue

    else:
        print("Try a stronger password!")
        continue
