from typing import Tuple
# from game_of_greed.game_logic import *

from game_logic import *


class Game():

  def  __init__(self):
      self.conter=0
      self.bank=0

      

  
  def ask_play(self):

        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        promot=input("> ").lower()

        if promot=="y" or promot=="yes":
            self.start_game()

        else:
            print("OK. Maybe another time")
    

  def start_game(self):
         self.conter+=1
         print(f'Starting round {self.conter}')
         print("Rolling 6 dice...")
         numb_dice()
         print("Enter dice to keep, or (q)uit:")
         promot_dic_num=input("> ")
         
         if promot_dic_num=="q":
             print(f'Thanks for playing. You earned {self.bank} points')
             return
         else:
            promot_dic_num=tuple(([int(i) for i in promot_dic_num]))
            ramian=6-len(promot_dic_num)
            shelf_score=GameLogic.calculate_score(promot_dic_num)
            self.bank+=shelf_score
            print(f"You have {shelf_score} unbanked points and {ramian} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            indecator=input("> ")
            if indecator=="b":
                print(f'You banked {shelf_score} points in round {self.conter}')
                print(f'Total score is {self.bank} points')
                self.start_game()
            if indecator=="q":
             print(f'Thanks for playing. You earned {self.bank} points')
             return
          
              
         
         



def numb_dice(num=6):
 dic=GameLogic.roll_dice(num)
 dic=" ".join([str(i) for i in dic])
 dic=f'*** {dic} ***'
 print(dic)

    



if __name__ == "__main__":
    game = Game()
    game.ask_play()
