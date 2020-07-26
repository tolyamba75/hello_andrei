class WordGame:
    def __init__(self, letter):
        self.ans_opt = ['правильно.', 'слово уже было отгадано.', 'попытайся еще раз.']
        self.letter = letter.lower()
        self.lst = []
        # id: кол-во отгаданных
        self.lst_part = {}

    def rules(self, word):
        if self.letter == word[:1]:
            return True
        return False

    def answer(self, word, user_id):
        word = word.lower()
        # угадал
        if self.rules(word) and not(word in self.lst):
            self.lst.append(word)
            try:
                self.lst_part[user_id] += 1
            except KeyError:
                self.lst_part[user_id] = 1

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

    def win(self):
        return self.lst_part

