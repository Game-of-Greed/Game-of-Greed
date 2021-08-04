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
    def validate_keepers(keepers,roll)->bool:
      
     return  not Counter(keepers) - Counter(roll)
   
    @staticmethod
    def get_scorers(dice):
        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        for i in range(len(dice)):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(dice[i])

        return tuple(scorers)
        
    @staticmethod
    def roll_dice(num=6)->tuple:
        """
        function for returning a random tuple each roll_dice in range between 1 to 6
        """

        return( tuple(randint(1,6) for _ in range(0, num)))

     






if __name__=="__main__":
  pass
     
    

