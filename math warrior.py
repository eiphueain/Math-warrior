import random, math

player_1_dice = []
player_2_dice = []

def roll_dice():
    roll = input("Player one : press '1' to roll your dice")
    if roll == "1":
        for i in range(0,7,1):
            player_1_dice.insert(i, random.randint(1, 4+i*2))
            print("You rolled ", player_1_dice[i])
            i=i+1
        print("Here are all your numbers: ", player_1_dice)
        print("Here are your numbers sorted :")
        bubble_sort_p1()


    roll = input("Player two : press '2' to roll your dice")
    if roll == "2":
        for i in range(0,7,1):
            player_2_dice.insert(i, random.randint(1, 4+i*2))
            print("You rolled ", player_2_dice[i])
            i=i+1
        print("Here are all your numbers: ", player_2_dice)
        print("Here are your numbers sorted :")
        bubble_sort_p2()
        

def bubble_sort_p1():
    i=0
    j=0
    swapped=False
    for i in range(7):
        for j in range(6):
            if player_1_dice[j]>player_1_dice[j+1]:
                temp = player_1_dice[j]
                player_1_dice[j]=player_1_dice[j+1]
                player_1_dice[j+1]=temp
                swapped = True
        i=i+1
        if not swapped:
            print(player_1_dice)   
            break     
    print(player_1_dice)

def bubble_sort_p2():
    i=0
    j=0
    swapped=False
    for i in range(7):
        for j in range(6):
            if player_2_dice[j]>player_2_dice[j+1]:
                temp = player_2_dice[j]
                player_2_dice[j]=player_2_dice[j+1]
                player_2_dice[j+1]=temp
                swapped = True
        i=i+1
        if not swapped:
            print(player_2_dice)   
            break     
    print(player_2_dice)

if input("Type '_' to start game") == "_":
    roll_dice()
