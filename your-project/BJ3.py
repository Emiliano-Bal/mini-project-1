
import random

def main():

  restart = True

  bank_balance = 1000
  player_name = input("Please enter your name: ")
  while (bank_balance >= 25 and restart == True):

    print (f"Welcome {player_name}, your bank balance is ${bank_balance} ")
    print (f"Betting $25")
    bank_balance-=25

    deal_hand = play_hand(player_name)

    play=input("Type 'y' to play again, or type any key to quit" + '\n')

    if (play == 'y'):
      restart=True
      print('\n')
    elif (play != 'y'):
      print('Thanks for playing ')
      restart=False


def play_hand(name):

  player= []
  dealer= []

  play_again = True

  dealer.append(random.randint(1, 11))

  player.extend([random.randint(1, 11), random.randint(1, 11)])

  print ('The dealer received card of value', *dealer)
  print(name, 'received cards of value', player[0], 'and', player[-1])
  print(f'Dealer total is {sum(dealer)}')
  print(f"{name}'s total is {sum(player)}", '\n')

  stay = False
  bust = False

  while (sum(player) <= 21 and stay == False and play_again == True):
    hors= input(f"Type 'h' to hit and 's' to stay ")
    if (hors == 'h'):
      new_card= random.randint(1, 11)
      player.append(new_card)
      print(f'{name} pulled a {new_card}')

      print(f'Dealer total is {sum(dealer)}')
      print(f"{name}'s cards are", *player)
      print(f"{name}'s total is {sum(player)}", '\n') 

    elif (hors == 's'):
      stay=True
      print('stay')


  if (sum(player) > 21 ):
    bust = True
    print('You busted!')

  while (stay == True and sum(dealer) < 17 and bust == False and play_again == True):
    dealer.append(random.randint(1, 11))

    print('The dealers total is', sum(dealer), '\n')



  if (sum(dealer) <= 21 and sum(dealer) > sum(player)):
    print("The dealer wins!")
  elif (sum(player) <= 21 and sum(player) > sum(dealer)):
    print("You win!")
  if (sum(dealer) > 21):
    print ('You win! The dealer busted!')
  if (sum(dealer) == sum(player)):
    print('Its a Tie! ')

main()