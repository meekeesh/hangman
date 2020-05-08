from random import shuffle


class Card:
	suits = ["пикей", "червей",
			 "бубей", "треф"]

	values = [None, None, "2",  "3",
			  "4",  "5",  "6",  "7",
			  "8",  "9",  "10", "валет",
			  "дама", "король", "туз"]

	def __init__(self, v, s):
		self.value = v
		self.suit = s

	def __lt__(self, c2):
		if self.value < c2.value:
			return True
		elif self.value == c2.value and self.suit < c2.suit:
			return True
		return False

	def __gt__(self, c2):
		if self.value > c2.value:
			return True
		elif self.value == c2.value and self.suit > c2.suit:
			return True
		return False

	def __repr__(self):
		return Card.values[self.value] + " " + Card.suits[self.suit]


class Deck:
	def __init__(self):
		self.cards = [Card(i, j) for i in range(2, 15) for j in range(4)]
		shuffle(self.cards)

	def rm_card(self):
		if len(self.cards) == 0:
			return None
		return self.cards.pop()

class Player:
	def __init__(self, name):
		self.wins = 0
		self.card = None
		self.name = name

class Game:
	def __init__(self):
		name1 = input("Имя игрока 1: ")
		name2 = input("Имя игрока 2: ")
		self.deck = Deck()
		self.player_1 = Player(name1)
		self.player_2 = Player(name2)

	def wins(self, winner):
		print(f"{winner} забирает карты")

	def winner(self, player_1, player_2):
		if player_1.wins > player_2.wins:
			return player_1.name
		elif player_1.wins < player_2.wins:
			return player_2.name
		return "Ничья!"

	def draw(self, player_1_name, player_1_card, player_2_name, player_2_card):
		print(f"{player_1_name} кладёт {player_1_card}, а {player_2_name} кладёт {player_2_card}")

	def play_game(self):
		cards = self.deck.cards
		print("Поехали!")

		while len(cards) >= 2:
			response = input("Нажмите Х для выхода или любую другую клавишу для игры.")
			if response == "Х":
				break

			player_1_card = self.deck.rm_card()
			player_2_card = self.deck.rm_card()
			player_1_name = self.player_1.name
			player_2_name = self.player_2.name
			self.draw(player_1_name, player_1_card, player_2_name, player_2_card)

			if player_1_card > player_2_card:
				self.player_1.wins += 1
				self.wins(self.player_1.name)
			else:
				self.player_2.wins += 1
				self.wins(self.player_2.name)

		print(f"Игра окончена, {self.winner(self.player_1, self.player_2)} выйграл!")


game = Game()
game.play_game()
