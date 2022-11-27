#CSE 210 W02 Hilo game. Author: David FAjardo
"""The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed. The player guesses
if the next one will be higher or lower."""
import random
beginning_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
scores = [300]
class DisplayCards:
    def __init__(self)->None:
        pass
    def first_displayed_card(self):
        self.first_card = random.choice(beginning_cards)
        print(f'The card is {self.first_card}')
    def size_card(self):
        self.choice = input(f'Higher or lower? [h/l] ').lower()
    def second_displayed_card(self):
        self.second_card = random.choice(beginning_cards)
        print(f'Next card was {self.second_card}')

class Score(DisplayCards):
    def __init__(self):
        self.first_displayed_card()
        self.size_card()
        self.second_displayed_card()
        self.points()
        self.print()

    def points(self):
        """The player earns 100 points if they guessed
        correctly.
        The player loses 75 points if they guessed
        incorrectly."""
        self.score = 0
        if self.first_card < self.second_card and self.choice == 'h':
            self.score += 100
        elif self.first_card <= self.second_card and self.choice == 'l':
            self.score += -75
        elif self.first_card > self.second_card and self.choice == 'l':
            self.score += 100
        elif self.first_card >= self.second_card and self.choice == 'h':
            self.score += -75
        scores.append(self.score)
    def print(self):
        total_score = sum(scores)
        print(f'Your score is: {total_score}')
        if total_score > 0:
            self.keep_playing = input(f'Play again? [y/n] ').lower()
            if self.keep_playing == 'y' or self.keep_playing == 'yes':
                main()
            else:
                print(f'Game over!')
                exit()
        else:
            print(f'Game over!')
            exit()
def main():
    Score()
main()
