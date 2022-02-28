
class Parachute():#creates the parachute and controls the disapearing chute. 
    def __init__(self) :
        self.parachute = ["  ___  ", " /___\ ", " \   / ", "  \ /  ", "   O   ", "  /|\  ", "  / \  ", " ^^^^^"]

    def draw_chute(self ):#draws the chute
        
     
        for x in range(len(self.parachute)-1):
            print (self.parachute[x])
    def update_chute(self, director):#controls if the chute will disappear and kills the player when they run out of lives. 
        
        if director.lives >= 1:
            self.parachute.pop(0)
                   
        if len(self.parachute) == 4:
            self.parachute[0] = "   X   "
            for x in range(len(self.parachute)-1):
                print (self.parachute[x])
            director.game_over = 'y'   