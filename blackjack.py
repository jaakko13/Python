import random
import time


numberList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



money = 100
dealearList = []
playerList = []
ongoing = True
HorS = ''
bet = 0
idk = True





while idk is True:

    while ongoing is True:

        print('How much would you like to bet? Your current total is ', money)
        bet = int(input())

        for x in range(0, 2):
            dealearList.append(random.choice(numberList))

        for x in range(0, 2):
            playerList.append(random.choice(numberList))

        print('Dealers Cards:                                       Player Cards:')
        print(dealearList[0], '[]                                        ', playerList)


        while HorS != 's': 
            if sum(playerList) > 21:
                money == money - bet
                print('You lost!')
                ongoing == False

            print('Would you like to hit or stand?(h = hit, s = stand)')
            HorS = input()

            if HorS == 'h':
                playerList.append(random.choice(numberList))
                
                print('Dealers Cards:                                       Player Cards:')
                print(dealearList[0], '[]                                        ', playerList)


        print('Now the dealer goes.')
        time.sleep(2)

        if sum(dealearList) <= 16:
            playerList.append(random.choice(numberList))
                
            print('Dealers Cards:                                       Player Cards:')
            print(dealearList, '                                        ', playerList)
            break

        if sum(dealearList) > 21:
            print('Dealers Cards:                                       Player Cards:')
            print(dealearList, '                                        ', playerList)

            money == money + bet
            print('You won! Your current total is', money)
            break

        if sum(dealearList) > sum(playerList):
            print('Dealers Cards:                                       Player Cards:')
            print(dealearList, '                                        ', playerList)

            money == money - bet
            print('You lost! Your current total is', money)
            break

        if sum(dealearList) < sum(playerList):
            print('Dealers Cards:                                       Player Cards:')
            print(dealearList, '                                        ', playerList)

            money == money + bet
            print('You won! Your current total is', money)
            break

        if sum(dealearList) == sum(playerList):
            print('Dealers Cards:                                       Player Cards:')
            print(dealearList, '                                        ', playerList)

            print('Split! Your current total is', money)
            break


    print('Wanna play again?(y = yes, n = no)')
    wannaplay = input()

    if wannaplay == 'y':
        HorS = ''
        dealearList = []
        playerList = []
        continue
        

    elif wannaplay == 'n':
        ongoing = False  
         



