print("====================================")
print("       SMART NAME CHECKER")
print("====================================")

name = input("Enter your full name: ").strip()

# Basic validation
if name == "":
    print("\n❌ You did not enter a name.")

elif len(name) < 3:
    print("\n❌ Name is too short!")
    print("   Minimum 3 characters are required.")

elif len(name) > 50:
    print("\n❌ Name is too long!")
    print("   Maximum 50 characters are allowed.")

else:
    print("\n✅ Your name looks good!")

    # Name information
    print("\n------ NAME INFORMATION ------")

    print("Your name:", name)
    print("Characters:", len(name))

    # Count words
    words = name.split()
    print("Number of words:", len(words))

    # First and last name
    print("First name:", words[0])

    if len(words) > 1:
        print("Last name:", words[-1])
    else:
        print("Last name: Not provided")

    # Check for numbers
    if any(char.isdigit() for char in name):
        print("⚠️ Warning: Your name contains numbers.")
    else:
        print("✅ No numbers found.")

    # Check for special characters
    if any(not char.isalpha() and not char.isspace() for char in name):
        print("⚠️ Special characters found.")
    else:
        print("✅ No special characters found.")

    # Create username
    username = name.lower().replace(" ", "_")

    print("\n------ USERNAME ------")
    print("Suggested username:", username)

    # Greeting
    print("\n🎉 Welcome,", name.title() + "!")
    print("Your name has been successfully registered.")

print("\n====================================")
print("             THANK YOU")
print("====================================")