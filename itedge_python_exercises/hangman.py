from random import choice

categories = {
    1: ["Apple", "Banana", "Apricot", "Avocados", "Blueberry", "Cherry", "Fig", "Grapes", "Custard apple", "Dragon fruit", "Guava", "Jackfruit", "Kiwi", "Mango", "Pear", "Oranges", "Papaya", "Peach", "Pomegranate", "Pineapple", "Raspberries", "Strawberries", "Watermelon"],
    2: ["Computer", "Internet", "Engineering", "Software", "nanotechnology", "application", "system", "robotics", "electronics", "communication", "biotechnology", "automation", "information", "innovation", "game", "code", "technology", "wireless", "hardware", "virtual", "social media", "computer science", "phone", "process", "bionics", "nanotech", "digital", "radio", "value", "developer", "core", "commercial", "development", "aeronautical", "language", "cybersecurity", "methodology", "online", "technician", "consumer", "handheld devices", "machine", "protocol", "architectures", "engineer", "invention", "video"],
    3: ["Kinetic", "astronomy", "astrophysics", "atom", "beaker", "biochemistry", "biology", "botany","cell","chemical","chemistry","climate","climatologist","data","datum","electricity","electrochemist","element""energy""entomology""evolution""experiment""fossil""genetics""geology""glassware" "cylinder"gravity laboratory hypothesis magnetism mass matter measure meteorologist meteorology microbiologist microbiology microscope mineral mineralogy molecule motion observatory observe organism physical science ],
    4: ["Mumbai"]

}

print("""Choose a category: 
1)Fruits 2)Technology 3)Science 4)Places """)

while True:
    category = int(input())
    if category == 1:
        words = categories[category]
        break
    elif category == 2:
        words = categories[category]
        break
    elif category == 3:
        words = categories[category]
        break
    elif category == 4:
        words = categories[category]
        break
    else:
        print("Wrong option. Enter again:\n")
        continue

word = choice(words)

chances = 7
guessed_alphabet = []
win = False

while not win:
    for alphabet in word:
        if alphabet.lower() in guessed_alphabet:
            print(alphabet, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Chances left {chances}, Next Guess: ")
    guessed_alphabet.append(guess[0].lower())
    if guess[0].lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break

    win = True
    for alphabet in word:
        if alphabet.lower() not in guessed_alphabet:
            win = False

if win:
    print(f"You found the word! It was {word}")
else:
    print(f"Game Over! The word was {word}!")
