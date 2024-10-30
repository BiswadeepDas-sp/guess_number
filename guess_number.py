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
               guess_num=int(input('Guess a number between 1 to 100:  '))
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
            g.game_play()
        else:
            exit()
            
class Game:
    def game_play(self):
        guess_num=0
        guess_left=5
        win=False
        number=Number()
        user=User()
        num_gen=number.generate() 
        while win==False and guess_num<5:
           guess=user.guess_input()
           if guess==999:
               print(f'The number is {num_gen}')
               cheat=True
               continue
           guess_num+=1
           guess_left-=1
           if num_gen==guess:
                    
                print()
                if cheat==False:
                    print(f'You have won in {guess_num} {'guesses' if guess_num>1 else 'guess'}')
                else:
                    print('HMMMMM. Okay!')
                win=True
           else:
                print('Wrong guess, try again!')
                print(f'You have {guess_left} guesses left')
                
        if guess_num==5:
            print('Too many guesses, Better luck next time!!')
        try: 
            if cheat==True:
             print('HMMMM. Okay!')
        except:
            pass
        user.cont_exit()
    
g=Game()
g.game_play()
