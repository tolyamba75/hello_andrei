class WordGame:
    def __init__(self, letter):
        self.ans_opt = ['правильно.', 'слово уже было отгадано.', 'попытайся еще раз.']
        self.letter = letter.lower()
        self.lst = []

    def rules(self, word):
        if self.letter == word[:1]:
            return True
        return False

    def answer(self, word):
        word = word.lower()
        # угадал
        if self.rules(word) and not(word in self.lst):
            self.lst.append(word)
            return self.ans_opt[0]
        # слово отгадано
        elif self.rules(word):
            return self.ans_opt[1]
        # не корректный ответ
        else:
            return self.ans_opt[2]

    def game_over(self):
        self.letter = ' '
        return self.lst

