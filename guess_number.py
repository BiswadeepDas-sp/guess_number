import random

class Number:
    def generate(self):
        num=random.randint(1,100)
        return num
    
class User:
    def guess_input(self):
        made_guess=False
        while made_guess==False:
           try:
               print()
               guess_num=int(input('Guess a number between 1 to 100:  '))
               print()
               made_guess=True
           except:
               print('Enter a valid response')
        return guess_num
    
    def cont_exit(self):
        valid=False
        while valid==False:
            try: 
                choice=int(input('Continue(0) or Exit(1)   '))
                valid=True
            except:
                print('You have entered an invalid response')
        
        if choice==0:
            game.game_play()
        else:
            exit()
            
class Game:
    def score(self):
        if self.cheat==False and self.guess_left>0:
             self.score_round=round(100-(abs(self.guess-self.num_gen)/self.num_gen*100),0)
        return self.score_round
        
    def game_play(self):
        self.guess_left=5
        win=False
        number=Number()
        user=User()
        self.num_gen=number.generate() 
        self.cheat=False
        score=0
        #print(f'The number is {self.num_gen}')
        while win==False and self.guess_left>0:
           self.guess=user.guess_input()
           if self.guess>100:
            if self.guess==999:
                print(f'The number is {self.num_gen}')
                self.cheat=True
            else:
                print('Enter a number between 1 to 100')
                print('*'*30)
            continue
           self.guess_left-=1
           if self.num_gen==self.guess:
                    
                print()
                if self.cheat==False:
                    print()
                    print(f'You have won in {5-self.guess_left} {'guesses' if 5-self.guess_left>1 else 'guess'}')
                    print('*'*30)
                    
                win=True
           else:
                print('Wrong guess, try again!')
                print()
                print(f'You have {self.guess_left} guesses left')
           score+=self.score()
           print()
           print(f'Score = {score}')
           print('*'*30)
                
        if self.guess_left==0 and win==False:
            print()
            print('Too many guesses, Better luck next time!!')
            print()
            print(f'The number was {self.num_gen}')
            print('*'*30)
        try: 
            if self.cheat==True:
                print('*'*30)
                print('HMMMM. Okay!')
                
        except:
            pass
       
        user.cont_exit() 
        print()
        print('*'*30)
    
game=Game()
game.game_play()
