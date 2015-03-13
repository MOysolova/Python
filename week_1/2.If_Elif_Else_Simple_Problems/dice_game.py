from random import randint
n = input("Enter sides number: ")
n = int(n)
player_1 = input("Enter first player name: ")
player_2 = input("Enter second player name: ")
player1_roll = randint(1, n)
player2_roll = randint(1, n)
print("{} rolls: {}".format(player_1, player1_roll))
print("{} rolls: {}".format(player_2, player2_roll))
if player1_roll == player2_roll:
    print("Result is TIE.")
elif player1_roll > player2_roll:
    print("{} is winner.".format(player_1))
elif player1_roll < player2_roll:
    print("{} is winner.".format(player_2))