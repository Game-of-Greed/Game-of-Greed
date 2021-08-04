from typing import Tuple
from game_of_greed.game_logic import *
from game_of_greed.banker import *
# from tests.flo import *

class Game():

  def  __init__(self):
      self.conter=0
      self.bank=Banker()
      self.num_r=0

  def zilch(self):
        print(
            """****************************************
**        Zilch!!! Round over         **
****************************************""")
        self.bank.clear_shelf()
        print(f'You banked 0 points in round {self.conter}')
        print(f'Total score is {self.bank.balance} points')
        self.conter+=1
        print(f'Starting round {self.conter}')


  def roll_again(self,roller,ramian,shelf_score):
      

        if ramian==0:
            self.roll_again(roller,6,shelf_score)
       
        roll=numb_dice(roller,ramian)
        print(f'Rolling {ramian} dice...')
        print(roll)
        roll = [int(char) for char in roll if char.isdigit()]
        promot_dic_num=tuple(([int(i) for i in roll]))
        shelf_score_new=GameLogic.calculate_score(promot_dic_num)
        shelf=shelf_score + GameLogic.calculate_score(promot_dic_num)

        if shelf_score_new==0:
            self.zilch()
            self.roll_again(roller,6,shelf_score)

            return

        print("Enter dice to keep, or (q)uit:")
        promot_dic_num=input("> ")

        if promot_dic_num=="q":
            print(f'Thanks for playing. You earned {self.bank.balance} points')
            return
        ramian-=len(promot_dic_num)
        # shelf_score_new=GameLogic.calculate_score(promot_dic_num)
        # shelf=shelf_score + GameLogic.calculate_score(promot_dic_num)



        # self.bank.balance+=shelf

        print(f"You have {shelf} unbanked points and {ramian} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        indecator=input("> ")
        if indecator=="b":
            self.bank.balance+=shelf
            print(f'You banked {shelf} points in round {self.conter}')
            print(f'Total score is {self.bank.balance} points')
            ramian=6
            self.start_game(roller,ramian)
        if indecator=='r':
                self.roll_again(roller,ramian,shelf)
  
  def play(self,roller=None):

        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        promot=input("> ").lower()

        if promot=="y" or promot=="yes":
            self.start_game(roller)

        else:
            print("OK. Maybe another time")
    

  def start_game(self,roller=None,remain=6,shelf_score=0):
         self.conter+=1
         shelf_score+=shelf_score
         print(f'Starting round {self.conter}')
         print("Rolling 6 dice...")
         roll=numb_dice(roller,remain)
         print(roll)
         print("Enter dice to keep, or (q)uit:")
         promot_dic_num=input("> ")
         

         if promot_dic_num=="q":
             print(f'Thanks for playing. You earned {self.bank.balance} points')
             return

         while not GameLogic.validate_keepers(promot_dic_num,roll):
             print('Cheater!!! Or possibly made a typo...')
             print(roll)
             print("Enter dice to keep, or (q)uit:")
             promot_dic_num=input("> ")
             if promot_dic_num=="q":
                print(f'Thanks for playing. You earned {self.bank.balance} points')
                return
         
         else:
            promot_dic_num=tuple(([int(i) for i in promot_dic_num if i.isdigit()]))
            
            remain-=len(promot_dic_num)
            shelf_score+=GameLogic.calculate_score(promot_dic_num)
            print(f"You have {shelf_score} unbanked points and {remain} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            indecator=input("> ")
            if indecator=="b":

                self.bank.balance+=shelf_score
                print(f'You banked {shelf_score} points in round {self.conter}')
                print(f'Total score is {self.bank.balance} points')
                self.start_game(roller)
           
            if indecator=='r':
                self.roll_again(roller,remain,shelf_score)
                
                

            if indecator=="q":
             print(f'Thanks for playing. You earned {self.bank.balance} points')
             return


 
                    



def numb_dice(roller=None,num=6):
#  print(roller)
 dic= roller(num) 
 dic=" ".join([str(i) for i in dic])
 dic=f'*** {dic} ***'
 return(dic)





if __name__ == "__main__":
    game = Game()
    game.play(GameLogic.roll_dice)
