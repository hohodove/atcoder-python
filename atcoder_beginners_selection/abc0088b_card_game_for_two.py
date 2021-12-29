N = input()
cards = list(map(int, input().split()))
sorted_cards = sorted(cards)[::-1]
print(sum(sorted_cards[::2]) - sum(sorted_cards[1::2]))
