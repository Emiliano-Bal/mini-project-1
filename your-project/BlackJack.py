# Lo primero que haremos en este caso será import random ya la utilizaremos para mezclar la baraja. (En los juegos de cartas nunca sabes que te tocará).
import random 
import colorama 
from colorama import Fore, Back, Style

# Se crea la class Cards con los parametros de SUIT y VALUE, que son los 2 parámetros que tienen las cartas de juego. 
class Card:
	def __init__(self,s,v):
		self.suit = s
		self.value = v

	def get_value(self):
		if self.value in ['J','Q','K']:
			return 10
		return self.value

# Se crea la clase DeckOfCards sin parametros ya que todos los DeckOfCards que creemos requieren tener los mismos parámetros y mismas cartas.

class deckOfCards:
	def __init__(self):
		self.deck_of_cards = []

		for suit in ['♠','♥','♦', '♣']:
			if suit == '♥':
				suit = (Fore.RED + '♥')+ Fore.RESET
			if suit == '♦':
				suit = (Fore.RED + '♦')+ Fore.RESET
			for value in range(2,11):
				self.deck_of_cards.append(Card(suit, value))
			for value in ['J','Q','K','A']:
				self.deck_of_cards.append(Card(suit, value))
		random.shuffle(self.deck_of_cards)

	def showDeck(self):
		for c in self.deck_of_cards:
			print(str(c.value)+ c.suit)

	def deal_one_card(self, p):
		p.get_card(self.deck_of_cards[0])
		self.deck_of_cards.remove(self.deck_of_cards[0])

# Se crea la clase Player para definir las condiciones que se deben de cumplir para que el juego del player pueda llevarse a cabo. 

class Player():
	def __init__(self, n):
		self.hand = []
		self.name = n


	def get_card(self, c):
		self.hand.append(c)

	def show_hand(self):
		for c in self.hand:
			print(str(c.value) + c.suit, end = ' ')
		print('= ' + str(self.count_hand()))

	def count_hand(self):
		counter = 0
		ace = 0 

		for c in self.hand:
			if c.get_value() == 'A':
				ace += 1 
			else:
				counter += c.get_value()
		counter += ace
		used_aces = 0 
		while counter <= 11 and used_aces < ace:
			counter += 10 
			used_aces += 1 
		return counter 



# Se crea la clase dealerGame para definir las condiciones que se deben de cumplir para que el juego del Dealer pueda llevarse a cabo. 

class dealerGame():
	def __init__(self, dealer):
		self.hand = []
		self.dealer = dealer

	
	def get_card(self, c):
		self.hand.append(c)


	def show_hand(self):
		for c in self.hand:
			print(str(c.value) + c.suit, end = ' ')
		print('= ' + str(self.count_hand()))


	def count_hand(self):
		counter = 0
		ace = 0 

		for c in self.hand:
			if c.get_value() == 'A':
				ace += 1 
			else:
				counter += c.get_value()
		counter += ace
		used_aces = 0 
		while counter <= 11 and used_aces < ace:
			counter += 10 
			used_aces += 1 
		return counter 
	
# En esta sección empieza el juego y hay tomas de decisión para el jugador, las cuales afectarán el resultado del juego . 
print('How much would you like to deposit?')
player_bank = int(input())
print('\nPlayer´s game:')
player_answer = 'y'
while player_answer == 'y' and player_bank > 0:
	print(f'You have ${player_bank} in your account')
	print('How much would you like to bet?')
	
	while player_bank > 0:
		bet = int(input())
		if bet <= player_bank:
			print('here we go')
			break
		else:
			print('You don´t have enough credits for that bet\nPlease enter a valid bet:')

	p = Player('Emiliano')
	dealer = dealerGame('Dealer')
	d = deckOfCards()
	d.deal_one_card(p)
	d.deal_one_card(p)


#Player game (Se enseñan las cartas al jugador y decide si quiere pedir más o quedarse con las que tiene.)
	p.show_hand()
	while p.count_hand() < 21:
		print('Choose your next move?')
		print('1- Hit')
		print('2- Stay')
		answer = (input())
		if answer == '1':
			d.deal_one_card(p)
		elif answer == '2':
			break
		else:
			print('Select a valid option between 1 or 2')
		p.show_hand()

	print('Delaer´s game: ')
	dealer = dealerGame('Dealer')
	d = deckOfCards()
	d.deal_one_card(dealer)
	d.deal_one_card(dealer)

	dealer.show_hand()
	while p.count_hand() < 21:
		while dealer.count_hand() < 17:
			d.deal_one_card(dealer)
			if dealer.count_hand() > 17 and dealer.count_hand() <= 21:
				dealer.show_hand()
			elif dealer.count_hand() > 21:
				dealer.show_hand()
				break
		break


	#Dealer game (Se enseñan las cartas del dealer y la suma de sus cartas debe ser mayor a 17 para que ya no pida más.)

# Se muestran los resultados de la partida dependiendo de las decisiones tomadas en los pasos anteriores. 

	print(f'The player got {p.count_hand()}')
	print(f'The dealer got {dealer.count_hand()}')
	if p.count_hand() > dealer.count_hand() and dealer.count_hand() < 21 and p.count_hand() <= 21:
		print('Player Wins!')
		winnings = bet 
		player_bank += bet
		print(f'You won ${winnings}!')
	elif dealer.count_hand() > 21:
		print('Dealer busted & player wins!')
		winnings = bet
		player_bank += bet
		print(f'You won ${winnings}!')
	elif p.count_hand() == dealer.count_hand():
		print('Push!!')
	else:
		print('The house wins!')
		losses = -bet
		player_bank -= bet
		print(f'You lost ${losses}!')
	
	print('Do you want to play again? Please enter: y for yes! & any other character for no')
	player_answer = input().lower()

	if player_answer != 'y':
		print('We are sad to see you go! \nWe hope you come back soon...')
	else:
		print('Here we go again!!! \nPlayer´s hand: ')
        
