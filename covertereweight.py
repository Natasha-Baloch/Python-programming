print("========================================")
print("       ⚖️ SMART WEIGHT CONVERTER")
print("========================================")

while True:

    print("\nChoose an option:")
    print("1. Kilograms → Pounds")
    print("2. Pounds → Kilograms")
    print("3. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "3":
        print("\nThank you for using Smart Weight Converter! 👋")
        break

    if choice != "1" and choice != "2":
        print("\n❌ Invalid choice! Please enter 1, 2 or 3.")
        continue

    try:
        weight = float(input("\nEnter your weight: "))

        if weight <= 0:
            print("❌ Weight must be greater than 0.")
            continue

        if choice == "1":

            # KG → POUNDS
            pounds = weight * 2.20462

            print("\n---------- RESULT ----------")
            print("Original weight :", weight, "Kg")
            print("Converted weight:", round(pounds, 2), "Pounds")

            # Simple category
            if weight < 30:
                print("📌 Category: Very light")
            elif weight < 60:
                print("📌 Category: Light")
            elif weight < 80:
                print("📌 Category: Medium")
            elif weight < 100:
                print("📌 Category: Heavy")
            else:
                print("📌 Category: Very heavy")

        elif choice == "2":

            # POUNDS → KG
            kilograms = weight / 2.20462

            print("\n---------- RESULT ----------")
            print("Original weight :", weight, "Pounds")
            print("Converted weight:", round(kilograms, 2), "Kg")

            if kilograms < 30:
                print("📌 Category: Very light")
            elif kilograms < 60:
                print("📌 Category: Light")
            elif kilograms < 80:
                print("📌 Category: Medium")
            elif kilograms < 100:
                print("📌 Category: Heavy")
            else:
                print("📌 Category: Very heavy")

        print("----------------------------")

    except ValueError:
        print("\n❌ Please enter a valid number!")