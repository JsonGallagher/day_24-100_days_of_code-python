from random import randint

print("Infinity Dice 🎲")
print()

def rollDice(sides):
  roll = randint(1,sides)
  print(f"You rolled {roll}")
  print()
  
sides = int(input("How many sides? "))

rollDice(sides)

while True:
  roll_again = input("Roll again? y or n: ")
  if roll_again == 'y':
    rollDice(sides)
  elif roll_again == 'n':
    break
  else:
    print("Enter a valid response.")
    print()

print("Game ended.")
exit()