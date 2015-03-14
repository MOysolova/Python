from random import randint
player1 = input("Write Player1's name: ")
player2 = input("Write Player2's name: ")

player1_start_score = 1001
player2_start_score = 1001

while True:
    count = 1
    score = 0
    while count < 6:
        roll = randint(1, 6)
        score += roll
        count += 1
        print(roll)
    print("Sum is: {}" .format(score))
    if player1_start_score > 0:
        player1_start_score -= score
    elif player1_start_score < 0:
        player1_start_score += score
    print("Player 1 roll: " + str(score) + " and has a score of: " + str(player1_start_score))
    if player1_start_score == 0:
        break
    count = 1
    score = 0
    while count < 6:
        roll = randint(1, 6)
        score += roll
        print(roll)
        count += 1
    print("Sum is: {}" .format(score))
    if player2_start_score > 0:
        player2_start_score -= score
    elif player2_start_score < 0:
        player2_start_score += score
    print("Player 2 roll: " + str(score) + " and has a score of: " + str(player2_start_score))
    if player2_start_score == 0:
        break

if player2_start_score == 0:
    print("{} is WINNER!" .format(player2))
elif player1_start_score == 0:
    print("{} is WINNER!" .format(player1))