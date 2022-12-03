import random


def lotto_system():
    lotto_numbers = [random.randint(0, 100) for i in range(6)]

    players_numbers = input("Please enter the six numbers you wish to check, leaving a space between the numbers: ")
    players_numbers = players_numbers.split(" ")
    players_numbers_ints = []
    for element in players_numbers:
        players_numbers_ints.append(int(element))
    # print(players_numbers_ints)
    players_numbers_ints.sort()
    lotto_numbers.sort()

    if (players_numbers_ints == lotto_numbers):
        print ("You have won the lotto")
    else:
        print(f"You have not won the lotto, the winning numbers where {lotto_numbers}")

lotto_system()