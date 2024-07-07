import random
import os

from day11_blackjack_logo import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user, computer):

    if user > 21 and computer > 21:
        return "You went over. You lose 😒"

    if user == computer:
        return "Draw 🙃"

    elif computer == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user == 0:
        return "win with a Blackjack 😎"
    elif user > 21:
        return "You went over. You lose 😒"
    elif computer > 21:
        return "Opponent went over. You win 😁"
    elif user > computer:
        return "You win 😁"
    else:
        return "You lose 😢"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user = calculate_score(user_cards)
        computer = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, Current score: {user}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user == 0 or computer == 0 or user > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer != 0 and computer < 17:
        computer_cards.append(deal_card())
        computer = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final_score: {user}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer}")
    print(compare(user, computer))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()