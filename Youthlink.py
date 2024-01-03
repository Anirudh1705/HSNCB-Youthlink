import tkinter as tk
from tkinter import messagebox

class ChoicesGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Mindful Maze")

        self.story_text = tk.StringVar()
        self.story_label = tk.Label(master, textvariable=self.story_text, wraplength=400)
        self.story_label.pack()

        self.choice_button_1 = tk.Button(master, text="Option 1", command=self.choice_1)
        self.choice_button_1.pack()

        self.choice_button_2 = tk.Button(master, text="Option 2", command=self.choice_2)
        self.choice_button_2.pack()

        self.lives = 5
        self.level = 1
        self.start_game()

    def start_game(self):
        self.update_story("Welcome to the Mindful Maze Game!")
        self.update_choices("Explore the dark cave", "Follow the mysterious path")

    def update_story(self, text):
        self.story_text.set(text)

    def update_choices(self, choice1, choice2):
        self.choice_button_1.config(text=choice1)
        self.choice_button_2.config(text=choice2)

    def make_choice(self, message):
        return messagebox.askquestion("Choose Your Action", message)

    def lose_life(self):
        self.lives -= 1
        messagebox.showinfo("Oops!", f"Wrong choice! You lost a life. Lives remaining: {self.lives}")

        if self.lives <= 0:
            messagebox.showinfo("Game Over", "Sorry, you ran out of lives. Game over!")
            self.master.destroy()
        else:
            self.go_back_to_previous_level()

    def go_back_to_previous_level(self):
        self.level -= 1
        if self.level < 1:
            self.level = 1
        messagebox.showinfo("Back to Previous Level", f"You're going back to Level {self.level}.")
        self.start_game()

    def choice_1(self):
        if self.level == 1:
            result = self.make_choice("You enter the dark cave...\nIt's too dark to see anything. Suddenly, you hear a strange noise.\nWhat do you want to do?")

            if result == 'yes':
                self.update_story("You move towards the noise...\nIt turns out to be just a bat. You continue deeper into the cave.")
                self.update_choices("Continue exploring the cave", "Return to the entrance")
            else:
                self.lose_life()
        elif self.level == 2:
            result = self.make_choice("You find an ancient door in the cave.\nDo you want to open it?")
            
            if result == 'yes':
                self.update_story("The door creaks open, revealing a hidden chamber with a treasure chest.")
                self.update_choices("Open the treasure chest", "Leave the chamber")
            else:
                self.lose_life()
        elif self.level == 3:
            result = self.make_choice("As you go deeper into the cave, you encounter a fork in the path.\nDo you want to go left or right?")
            
            if result == 'yes':
                self.update_story("You choose the left path and discover a glowing crystal with magical properties.")
                self.update_choices("Touch the crystal", "Continue exploring the left path")
            else:
                self.lose_life()
        elif self.level == 4:
            result = self.make_choice("You come across a rickety bridge spanning a deep chasm.\nDo you want to cross it?")
            
            if result == 'yes':
                self.update_story("You cautiously cross the bridge, narrowly avoiding a collapse.")
                self.update_choices("Explore the area on the other side", "Retrace your steps")
            else:
                self.lose_life()
        elif self.level == 5:
            result = self.make_choice("You encounter a mystical portal with shimmering lights.\nDo you want to enter it?")
            
            if result == 'yes':
                self.update_story("You step into the portal and find yourself in a surreal dimension.")
                self.update_choices("Explore the new dimension", "Try to find a way back")
            else:
                self.lose_life()
        elif self.level == 6:
            result = self.make_choice("In the surreal dimension, you meet a mysterious guide offering two paths.\nDo you choose the path of wisdom or the path of courage?")
            
            if result == 'yes':
                self.update_story("You choose the path of wisdom and gain profound insights.")
                self.update_choices("Apply the newfound wisdom", "Explore more of the surreal dimension")
            else:
                self.lose_life()
        elif self.level == 7:
            result = self.make_choice("You return to the familiar dimension and find a portal to a futuristic city.\nDo you want to enter the city?")
            
            if result == 'yes':
                self.update_story("You enter the futuristic city, amazed by advanced technology and bustling activities.")
                self.update_choices("Explore the city's technology", "Visit a local establishment")
            else:
                self.lose_life()
        elif self.level == 8:
            result = self.make_choice("You discover a hidden laboratory in the futuristic city.\nDo you want to investigate?")
            
            if result == 'yes':
                self.update_story("Inside the laboratory, you find cutting-edge experiments and technology.")
                self.update_choices("Interact with the experiments", "Leave the laboratory")
            else:
                self.lose_life()
        elif self.level == 9:
            result = self.make_choice("You stumble upon a time machine in the laboratory.\nDo you want to use it?")
            
            if result == 'yes':
                self.update_story("You activate the time machine and find yourself in a historical era.")
                self.update_choices("Interact with historical figures", "Attempt to return to your time")
            else:
                self.lose_life()
        # Add more levels as needed

    def choice_2(self):
        if self.level == 1:
            self.update_story("You follow the mysterious path...\nThe path leads you to a beautiful garden with a magical fountain.")
            self.update_choices("Drink from the fountain", "Explore the surrounding area")
        elif self.level == 2:
            self.update_story("You decide not to open the door and continue exploring the cave.")
            self.update_choices("Go deeper into the cave", "Return to the entrance")
        elif self.level == 3:
            self.update_story("You decide to continue exploring the right path and encounter a hidden treasure chest.")
            self.update_choices("Open the treasure chest", "Leave the area")
        elif self.level == 4:
            self.update_story("You choose to retrace your steps and discover a hidden cave entrance.")
            self.update_choices("Enter the hidden cave", "Continue along the current path")
        elif self.level == 5:
            self.update_story("You decide to rest for a while and regain your strength.")
            self.update_choices("Continue your journey", "Explore the nearby surroundings")
        elif self.level == 6:
            self.update_story("You choose to explore more of the surreal dimension.")
            self.update_choices("Discover hidden knowledge", "Seek a way back to your world")
        elif self.level == 7:
            self.update_story("You decide not to enter the futuristic city and seek answers about the portals in the surreal dimension.")
            self.update_choices("Consult the mysterious guide", "Explore more of the surreal dimension")
        elif self.level == 8:
            self.update_story("You decide not to investigate the hidden laboratory and explore more of the futuristic city.")
            self.update_choices("Discover other areas in the city", "Continue your exploration")
        elif self.level == 9:
            self.update_story("You decide not to use the time machine and continue exploring the historical era.")
            self.update_choices("Interact with the surroundings", "Search for a way back")
        # Add more levels as needed

def main():
    root = tk.Tk()
    game_gui = ChoicesGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
