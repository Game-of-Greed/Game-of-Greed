from random import randint
from collections import Counter




class GameLogic:

    def __init__(self):
        pass

    @staticmethod
    def calculate_score(dice_num):
        """ This Function Takes Tuple  """

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
    def validate_keepers(roll,keepers)->bool:
      
     return  not Counter(keepers) - Counter(roll)
   
    @staticmethod
    def get_scorers():
        
        pass
        
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
     
    