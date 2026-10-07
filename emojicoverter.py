print("======================================")
print("       😎 SMART EMOJI TRANSLATOR")
print("======================================")
print("Type a message and I will convert your")
print("text emotions into emojis.")
print("Type 'exit' to close the program.")
print()

emoji_dict = {
    ":)"  : "😊",
    ":D"  : "😂",
    ":("  : "😔",
    ":|"  : "😑",
    "T_T" : "😭",
    ":P"  : "😜",
    ";)"  : "😉",
    "<3"  : "❤️",
    ":O"  : "😮",
    ">:(" : "😡",
    "B)"  : "😎",
    ":*"  : "😘",
    "^_^" : "🥰",
    "-_-" : "😐"
}

while True:

    message = input("\n> ").strip()

    # Exit program
    if message.lower() == "exit":
        print("\n👋 Goodbye! Thanks for using Smart Emoji Translator.")
        break

    # Empty message
    if message == "":
        print("⚠️ Please type something!")
        continue

    # Split message
    words = message.split()

    output = ""
    emoji_count = 0

    # Convert words
    for word in words:

        if word in emoji_dict:
            output += emoji_dict[word] + " "
            emoji_count += 1
        else:
            output += word + " "

    print("\n🤖 Converted message:")
    print(output.strip())

    # Message statistics
    print("\n------ MESSAGE INFO ------")
    print("Words:", len(words))
    print("Characters:", len(message))
    print("Emojis converted:", emoji_count)

    # Detect mood
    if any(x in message for x in [":)", ":D", ":P", ";)", "<3", "^_^"]):
        print("Mood: 😄 Happy / Positive")

    elif any(x in message for x in [":(", "T_T"]):
        print("Mood: 😢 Sad")

    elif any(x in message for x in [">:("]):
        print("Mood: 😡 Angry")

    elif any(x in message for x in [":O"]):
        print("Mood: 😮 Surprised")

    elif any(x in message for x in ["-_-", ":|"]):
        print("Mood: 😐 Neutral")

    else:
        print("Mood: 🙂 Normal")

    print("--------------------------")