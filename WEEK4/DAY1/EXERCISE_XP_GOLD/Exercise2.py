user_in = int(input("Please enter a month: "))
if (user_in >= 3 and user_in <= 5):
    print("Spring runs from March to May")
elif (user_in >= 6 and user_in <= 8):
    print("Summer runs from June to August")
elif (user_in >= 9 and user_in <= 11):
    print("Autumn runs from September to November")
elif (user_in >= 12 and user_in <= 2):
    print("Winter runs from December to February")
else:
    print("Selection should be between 1 to 12, invalid entry. Bye")
print("\n")
print("End of ExerciseXpGold")