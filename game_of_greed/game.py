



class Game():

  def  __ini__(self):
     pass 

  @staticmethod
  def ask_play():

        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        promot=input("> ").lower()

        if promot=="y" or promot=="yes":
            print("OK. Maybe anothersssssssssssssssssssss time")
        else:
            print("OK. Maybe another time")
    

    def start_game():
        pass

        

    



if __name__ == "__main__":
    game = Game()
    game.ask_play()
