from pet import Pet, show_menu
import os

if __name__ == "__main__":
    luna = Pet.load_pet() if os.path.exists("luna_save.json") else Pet("Luna", "cat")
    show_menu(luna)
