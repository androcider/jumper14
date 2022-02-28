
class Jumper(): #starts the player
    def __init__(self) :
        letter = self.choose_letter
        self.letter_list = []
    def choose_letter(self,letter_list):#has the player choose a letter and verifies if it has been choosen before, and if it has asks again. 
        


        while True:

            try:
                letter=input("Guess a letter [a-z] " ) 
                
                if letter not in letter_list:
                    letter_list.append(letter)
                    return letter
            except:
                print("\n")
                
            print("You already picked that letter! Try again: ")


            
       
