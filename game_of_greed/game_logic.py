from random import randint
from collections import Counter

score={  
    (1, 1): 100,
    (1, 2): 200,
    (1, 3): 1000,
    (1, 4): 2000,
    (1, 5): 3000,
    (1, 6): 4000,
#___________________
    (2, 3): 200,
    (2, 4): 400,
    (2, 5): 600,
    (2, 6): 800,
#___________________
    (3, 3): 300,
    (3, 4): 600,
    (3, 5): 900,
    (3, 6): 1200,
#___________________  
    (4, 3): 400,
    (4, 4): 800,
    (4, 5): 1200,
    (4, 6): 1600,
#___________________   
    (5, 1): 50,
    (5, 2): 100,
    (5, 3): 500,
    (5, 4): 1000,
    (5, 5): 1500,
    (5, 6): 2000,
#___________________   
    (6, 3): 600,
    (6, 4): 1200,
    (6, 5): 1800,
    (6, 6): 2400,
    
}



class GameLogic:

    def __init__(self):
        pass


    @staticmethod
    def calculate_score(dice_roll:tuple )->int:
        """
        calculate score function do a calculation for dice roll each time take tuple as input 
        and return int
        """
        if len(dice_roll)==3:
            return 750
        try:
            if len(dice_roll[0])==2:
             return 750
        except:
            if dice_roll in score:
                return(score[dice_roll])

        if dice_roll==(0,0):
            return 0
        

        elif dice_roll==(1,2,3,4,5,6):
            return 1500
        
        
    @staticmethod
    def roll_dice(num=6)->tuple:
        """
        function for returning a random tuple each roll_dice in range between 1 to 6
        """

        return( tuple(randint(1,6) for _ in range(0, num)))

        
class Banker :
    def __init__(self):
        self.unbanked=0
        self.bank_points=0

    def shelf(self,num):
        """
        function for calculate the temporary summation of roll_dice and store it in shelf 

        """
        self.unbanked+=num
        return self.unbanked

    def bank(self):
        """
       function  for doing a summation for the shelf to bank 

        """
        self.bank_points+=self.unbanked
        self.unbanked=0
        return self.bank_points

    def clear_shelf(self):
        """
       function  for rest the shelf each roll-dice
        """
        self.unbanked=0







if __name__=="__main__":

    pass
