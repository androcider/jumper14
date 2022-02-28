
from hidden_word import Hidden_word
from parachute import Parachute
from jumper import Jumper
from director import Director

def main():
    jumper = Jumper()
    hidden_word = Hidden_word()
    director = Director()
    parachute = Parachute()
   
    director.start_game( jumper, hidden_word, parachute)
if __name__ == "__main__":
    main()