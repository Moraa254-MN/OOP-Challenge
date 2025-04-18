import json
import os

class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

        self.emojis = {
            'cat': '😺',
            'dog': '🐶',
            'parrot': '🦜',
            'hamster': '🐹',
            'bunny': '🐰',
        }

    def emoji(self):
        return self.emojis.get(self.pet_type.lower(), '🐾')

    def eat(self):
        print(f"{self.emoji()} {self.name} is munching on some treats... 🍲")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(f"{self.emoji()} {self.name} is curling up for a nap... 🛏️💤")
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy < 2:
            print(f"{self.emoji()} {self.name} is too tired to play right now... 😴")
            return
        print(f"{self.emoji()} {self.name} is playing joyfully! 🎉")
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        print(f"{self.emoji()} {self.name} is learning a new trick: '{trick}'! 🧠")
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)

    def bathe(self):
        print(f"{self.emoji()} {self.name} is taking a bubbly bath... 🛁")
        self.happiness = max(0, self.happiness - 1)
        self.energy = min(10, self.energy + 1)

    def cuddle(self):
        print(f"{self.emoji()} {self.name} is cuddling with you... ❤️")
        self.happiness = min(10, self.happiness + 2)
        self.energy = min(10, self.energy + 1)

    def show_tricks(self):
        if self.tricks:
            print(f"{self.emoji()} {self.name} knows these tricks: {', '.join(self.tricks)} 🎩")
        else:
            print(f"{self.emoji()} {self.name} hasn't learned any tricks yet. 📘")

    def get_status(self):
        print(f"\n🔍 {self.name}'s Status Report ({self.pet_type.title()} {self.emoji()}):")
        print(f"🦴 Hunger:    {self.hunger}/10")
        print(f"⚡ Energy:    {self.energy}/10")
        print(f"😊 Happiness: {self.happiness}/10")
        print(f"🎓 Tricks:    {', '.join(self.tricks) if self.tricks else 'None yet.'}")
        print("-" * 40 + "\n")

    def save_pet(self, filename="luna_save.json"):
        with open(filename, "w") as f:
            json.dump(self.__dict__, f)
        print(f"🗃️ {self.name}'s progress saved!")

    @staticmethod
    def load_pet(filename="luna_save.json"):
        with open(filename, "r") as f:
            data = json.load(f)
            pet = Pet(data['name'], data['pet_type'])
            pet.__dict__.update(data)
            return pet

def show_menu(pet):
    while True:
        print("What would you like Luna to do?")
        print("1. Eat 🍲")
        print("2. Sleep 😴")
        print("3. Play 🎾")
        print("4. Train 🎓")
        print("5. Cuddle ❤️")
        print("6. Bathe 🛁")
        print("7. Show Status 📊")
        print("8. Save & Exit 💾")
        choice = input("Enter choice: ")

        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            trick = input("Enter trick name: ")
            pet.train(trick)
        elif choice == "5":
            pet.cuddle()
        elif choice == "6":
            pet.bathe()
        elif choice == "7":
            pet.get_status()
        elif choice == "8":
            pet.save_pet()
            print("Bye for now! 🐾")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    luna = Pet.load_pet() if os.path.exists("luna_save.json") else Pet("Luna", "cat")
    show_menu(luna)
