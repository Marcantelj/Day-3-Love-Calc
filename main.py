print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combinedName = name1 + name2
combineName = combinedName.lower()
T = combinedName.lower().count("t")
R = combinedName.lower().count("r")
U = combinedName.lower().count("u")
E = combinedName.lower().count("e")
totalTrue = str(T + R + U + E)
L = combinedName.lower().count("l")
O = combinedName.lower().count("o")
V = combinedName.lower().count("v")
E = combinedName.lower().count("e")
totalLove = str(L + O + V + E)
loveScore = totalTrue + totalLove
loveScore = int(loveScore)
if loveScore < 10 or loveScore > 90:
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}.")