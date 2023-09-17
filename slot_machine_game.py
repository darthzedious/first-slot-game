import random
print('Welcome to the Slot Machine Game!')

symbols = ['🍒', '🍐', '💎', '🍇', '🔔', '🍉']
balance = float(input('Enter your initial balance: '))
bet = 0
while balance > 0:
    print(30 * '-')
    print(f'Current balance: {balance:.2f} lv.')

    while True:
        bet = float(input('Enter your bet amount (enter 0 to exit): '))

        if bet == 0:
            break

        if bet > balance:
            print('Insufficient balance. Please make a lower bet!')
        else:
            break

    if bet == 0:
        break

    balance -= bet
    print('Spinning the reels...')
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)
    print(reel1, reel2, reel3)

    if reel1 == reel2 == reel3 and reel1 == '💎':
        winnings = bet * 50
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 and reel1 == '💎' or reel2 == reel3 and reel2 == '💎' or reel1 == reel3 and reel1 == '💎':
        winnings = bet * 25
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 == reel3 and reel1 == '🔔':
        winnings = bet * 35
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 and reel1 == '🔔' or reel2 == reel3 and reel2 == '🔔' or reel1 == reel3 and reel1 == '🔔':
        winnings = bet * 15
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 == reel3 and reel1 == '🍇':
        winnings = bet * 20
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 and reel1 == '🍇' or reel2 == reel3 and reel2 == '🍇' or reel1 == reel3 and reel1 == '🍇':
        winnings = bet * 10
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 == reel3 and reel1 == '🍉':
        winnings = bet * 10
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 and reel1 == '🍉' or reel2 == reel3 and reel2 == '🍉' or reel1 == reel3 and reel1 == '🍉':
        winnings = bet * 5
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 == reel3 and reel1 == '🍒':
        winnings = bet * 7
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 and reel1 == '🍒' or reel2 == reel3 and reel2 == '🍒' or reel1 == reel3 and reel1 == '🍒':
        winnings = bet * 3
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 == reel3 and reel1 == '🍐':
        winnings = bet * 5
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    elif reel1 == reel2 and reel1 == '🍐' or reel2 == reel3 and reel2 == '🍐' or reel1 == reel3 and reel1 == '🍐':
        winnings = bet * 2
        balance += winnings
        print(f'Congratulations! You won {winnings:.2f} money!')
    else:
        print('Sorry! No match. Better luck next time!')
print(f'Game over. Final Balance {balance:.2f} lv.')
print('Hope to see you again soon. Better luck next time!')
