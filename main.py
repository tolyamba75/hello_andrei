from seabattle import SeaBattle
from vkprocess import VkProcess
from wordgame import WordGame


class MiniGame:
    def __init__(self, data, group_id, token):
        self.data = data
        self.group_id = group_id
        self.token = token

        self.post_id = self.data['object']['post_id']
        self.user_id = self.data['object']['from_id']
        self.num_comment = self.data['object']['id']
        self.text = self.data['object']['text']

        self.vk_tool = VkProcess(group_id, token)
        self.name = self.vk_tool.check_name(self.user_id)

    def print_comment(self):
        try:
            if self.vk_tool.check_subscribe(self.user_id):
                comment = game[self.post_id].answer(self.text, self.user_id)
                message = '[id{user_id}|{name}], {comment}.'.format(user_id=self.user_id, name=self.name,
                                                                    comment=comment)
            else:
                message = '[id{user_id}|{name}], ответ не засчитан. Подпишитесь'.format(user_id=self.user_id,
                                                                                        name=self.name)
            self.vk_tool.reply(message, self.num_comment, self.post_id)

        except KeyError as e:
            print('invalid key', e)

    def stop_game(self, post_num):
        try:
            game[post_num].game_over()
            self.vk_tool.off_comments(post_num, self.winners(post_num))
        except KeyError as e:
            print('no key', e)

    def winners(self, post_num):
        lst = list(game[post_num].win().items())
        lst.sort(key=lambda i: i[1])
        user_name = self.vk_tool.check_name(lst[-1][0])
        messages = 'Первое место: [id{user_id}|{name}],' \
                   ' количество правильных ответов: {num}'.format(user_id=lst[-1][0], name=user_name, num=lst[-1][1])
        return messages


# group_id = 51312
# token = ''
# data = {}
win_lst = ['в2', 'г3', 'д5', 'е5', 'б6']
letter = 'ф'
game = {1: SeaBattle(win_lst), 6: WordGame(letter)}

