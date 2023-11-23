import random

print("🌟 Welcome to the Silly Story Maker! Get ready to giggle with our Mad Libs adventure. 🎭")

themes = ["Jungle Safari 🦁", "Space Voyage 🚀", "Underwater Odyssey 🐠"]
selected_theme = random.choice(themes)
print(f"Choose your Mad Libs theme: 1) Jungle Safari, 2) Space Voyage, 3) Underwater Odyssey")

noun = input('Pick a fun object: ')
verb = input('Choose an action word: ')
adjective = input('Select a descriptive word: ')
place = input('Name a random place: ')
animal = input('Pick an animal: ')
sound = input('Choose a sound: ')

print('------------------------------------------')
print(f"🌈 Behold the whimsical world of the {selected_theme}! 🚀\n")

print(f"In a {adjective} {place}, a {noun} decided to {verb}.")
print(f"The {animal} nearby heard this and exclaimed, '{sound}!'")
print("Everyone in the neighborhood joined in, creating a symphony of silliness. 😂")
print('------------------------------------------')

print("\nNow, share your goofy story with a friend and see who can come up with the silliest Mad Libs!")

print("\nYour Mad Libs masterpiece is ready! 🎉 Let the laughter begin!")
