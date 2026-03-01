import random

def main():
    deck = create_deck()
    random.shuffle(deck)
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

    print(f"Dealer shows: {dealer[0]}")
    print(f"Your hand: {player} (value: {hand_value(player)})")

    while True:
        if hand_value(player) > 21:
            print("Bust! you lose")
            return
        move = input("Hit or stand? (h/s): ").lower()
        if move == "h":
            player.append(deck.pop())
            print(f"Your hand: {player} (value: {hand_value(player)})")
        else:
            break
    print(f"Dealer hand: {dealer} (value: {hand_value(dealer)})")
    while hand_value(dealer) < 17:
        dealer.append(deck.pop())
        print(f"Dealer draws: {dealer} (value: {hand_value(dealer)})")

    p = hand_value(player)
    d = hand_value(dealer)

    if d > 21 or p > d:
        print("You win!")
    elif p < d:
        print("You lose.")
    else:
        print("Push.")

def create_deck():
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits = ["♠","♥","♦","♣"]
    return [f"{r}{s}" for r in ranks for s in suits]

def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        r = card[:-1]
        if r in ["J","Q","K"]:
            value += 10
        elif r == "A":
            value += 11
            aces += 1
        else:
            value += int(r)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def is_bust(hand):
    return hand_value(hand) > 21

if __name__ == "__main__":
    main()
