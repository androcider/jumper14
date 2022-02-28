


class Director:#controls the game
    def __init__(self):
        self.lives = 0

        self.game_over= 'n'
    def get_game_over(self, game_over):#ends the game
        return game_over
    def get_lives(self,lives):#gets if a life was lost
        self.lives = lives
        return self.lives
    def start_game(self, jumper, hidden_word, parachute):#starts the game
        
        word_list = hidden_word.word_list('word list.txt') 
        word = hidden_word.choose_word(word_list)
        secret_word = hidden_word.word_hide(word)
        
        
        while self.game_over !='y':
            self._get_inputs(hidden_word, parachute,jumper)
            self._do_updates(parachute,jumper,hidden_word)
   

    def _get_inputs(self,hidden_word,parachute,jumper):#gets the inputs from the jumper and the current status of the hiden word and parachute
       

        print(hidden_word.secret_word)
       
        parachute.draw_chute()
        jumper.letter = jumper.choose_letter(jumper.letter_list)

        
    def _do_updates(self,parachute, jumper,hidden_word):#updates the word and chute. 
        
        hidden_word.show_letter(hidden_word.word, hidden_word.secret_word, jumper.letter, self)
        parachute.update_chute(self)
        
        
    
    