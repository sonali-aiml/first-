# Number Guessing Game - My 3rd Python Program
# By Sonali Joshna

import random

print("=== Number Guessing Game ===")
print("Srinivasa Institute of Engineering and Technology")
print("Nenu 1 to 100 madhya oka number fix chesanu...")
print("Nuvvu guess chey! 7 chances matrame!\n")

secret = random.randint(1, 100)
chances = 7

for i in range(chances):
    guess = int(input(f"Chance {i+1}/7 - Naa number enti guess chey: "))
    
    if guess == secret:
        print(f"🎉 Correct! {secret} ne! Nuvvu gelichav!")
        break
    elif guess < secret:
        print("Chaala takkuva! Inka ekkuva number cheppu ⬆️")
    else:
        print("Chaala ekkuva! Inka takkuva number cheppu ⬇️")
else:
    print(f"\n😢 Chances aipoyayi! Naa number {secret} mama.")

print("\nGame over! Malli aadudama? - Sonali")
