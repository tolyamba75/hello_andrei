import re


class SeaBattle:
    def __init__(self, win_lst):
        self.ans_opt = ['ранил.', 'мимо.', 'попытайся еще раз.']
        self.win_lst = win_lst
        self.lst_part = {}
        # range(1, 11)
        self.lst_let = list('абвгдежзик')
        self.lst_num = list(range(1, 11))
        # [i+str(j) for i in list('абвгдежзик') for j in range(1, 11)]

    def answer(self, hit, user_id):
        hit = hit.lower().split()[0]

        if hit in self.win_lst:
            self.win_lst.remove(hit)
            self.lst_part[user_id] = hit
            return self.ans_opt[0]

        else:
            try:
                re.search(r'\b{let}{one}\d\d?\b'.format(let=self.lst_let, num=self.lst_num, one='{1}'), hit).group()
                return self.ans_opt[1]
            except AttributeError:
                return self.ans_opt[2]

    def game_over(self):
        rem = self.win_lst
        self.win_lst = []
        return rem

    def win(self):
        return self.lst_part

