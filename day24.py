print("Infinity Dice🎲")
print()
def rolldice(sides):
  import random
  while True:
    dice = random.randint(1, sides)
    print("You rolled", dice)
    print()
    again = input("Roll again? ")
    if again == "yes":
      continue
    else:
      print("Thank you for playing!")
      break
sides = int(input("How many sides? "))

rolldice(sides)