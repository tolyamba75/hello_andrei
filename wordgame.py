class WordGame:
    def __init__(self, litter):
        self.litter = litter.lower()
        self.lst = []

    def rules(self, word):
        if self.litter == word[:1]:
            return True
        return False

    def answer(self, word):
        word = word.lower()
        # угадал
        if self.rules(word) and not(word in self.lst):
            self.lst.append(word)
            return True
        # слово отгадано
        elif self.rules(word):
            return None
        # не корректный ответ
        else:
            return False

    def game_over(self):
        self.litter = ' '
        return self.lst
