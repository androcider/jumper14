import random


class Hidden_word:#creates the word
    def __init__(self):
        secret_word=self.word_hide
        word = self.choose_word
      
    def word_list(self,filename):#acesses my word list file and creates a list of those words
        list_of_words = []
        with open(filename) as file:
            for line in file:
                list_of_words.append(line.rstrip('\n'))
        word_list = list_of_words
        return word_list

    def choose_word(self,word_list):#chooses a random word from the list
        word = random.choice(word_list)
        self.word = word
        return word
    def word_hide(self,word):#changes the word to underscores
        self.secret_word = ''
        temp_word = word
        for l in temp_word:
            if l != ' ':
                self.secret_word = self.secret_word + '_'
            else:
                self.secret_word = self.secret_word + ' '

        return self.secret_word
    def show_letter(self, word, secret_word, letter,director):#checks if the choosen letter is in the word and then reveals it if it is, if it is not it tells the director to remove a life
        
        list_word = list(word)
        list_secret_word = list(secret_word)
        for i in range(len(list_word)):
            if letter == list_word[i]:
                list_secret_word[i] = letter
                self.secret_word = "".join(list_secret_word)
   
        if letter not in list_word:
            director.lives = 1
        return self.secret_word