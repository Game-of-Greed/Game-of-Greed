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
    def calculate_score(dice_num):
        """ This Function Takes Taple  """

        if len(dice_num) > 6:
            raise Exception("Cheating Cheater! , I See you  ")

        counts = Counter(dice_num)

        if len(counts) == 6:
            return 1500

        if len(counts) == 3 and all(val == 2 for val in counts.values()):
            return 1500

        score = 0

        ones_use = fives_useds = False

        for i in range(1, 6 + 1):

            pip_count = counts[i]

            if pip_count >= 3:

                if i == 1:

                    ones_use = True

                elif i == 5:

                    fives_useds = True

                score += i * 100

                # handle 4,5,6 of a kind
                score += score * (pip_count - 3)

                # 1s are worth 10x
                if i == 1:
                    score *= 10

        if not ones_use:
            score += counts.get(1, 0) * 100

        if not fives_useds:
            score += counts.get(5, 0) * 50

        return score


        
    @staticmethod
    def roll_dice(num=6)->tuple:

     return( tuple(randint(1,6) for _ in range(0, num)))

        
class Banker :
    def __init__(self):
        self.unbanked=0
        self.bank_points=0

    def shelf(self,num):
        self.unbanked+=num
        return self.unbanked

    def bank(self):
        self.bank_points+=self.unbanked
        self.unbanked=0
        return self.bank_points

    def clear_shelf(self):
        self.unbanked=0







if __name__=="__main__":

    pass
    