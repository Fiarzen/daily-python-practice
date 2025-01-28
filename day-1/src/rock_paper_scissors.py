
def game(p1, p2):
    if p1 == p2:
        return ("Draw!")
    elif p1 - p2 == -1 or p1 - p2 == 2:
        return ("Player 1 wins!")
    elif p2 - p1 == -1 or p2 - p1 == 2:
        return ("Player 2 wins!")
    else:
        return ("Error in input")

def main():
    p1 = input("Player 1, enter 1(rock), 2(paper) or 3(scissors)")
    p2 = input("Player 2, enter 1(rock), 2(paper) or 3(scissors)")
    game(p1, p2)

if __name__ == "__main__":
    main()
