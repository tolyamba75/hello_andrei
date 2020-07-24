from seabattle import SeaBattle
from vkprocess import VkProcess
from wordgame import WordGame


def json_data(data):
    post_id = data['object']['post_id']
    user_id = data['object']['from_id']
    comment_num = data['object']['id']
    text = data['object']['text']
    return post_id, user_id, comment_num, text


def answer_comment(ans):
    if ans and dct[0] == first_post:
        comment = 'ранил'
    elif ans and dct[0] == second_post:
        comment = 'правильно'

    elif ans is None and dct[0] == first_post:
        comment = 'мимо'
    elif ans is None and dct[0] == second_post:
        comment = 'слово засчитано + 1 балл'

    else:
        comment = 'попытайся еще раз'
    return comment


def print_comment():
    if dct[0] == first_post:
        ans = battle.answer(dct[3])
        com = answer_comment(ans)

    elif dct[0] == second_post:
        ans = word.answer((dct[3]))
        com = answer_comment(ans)

    else:
        com = ''

    user_id = dct[1]
    name = vk_tool.check_name(user_id)
    message = '[id{user_id}|{name}], {comment}.'.format(user_id=user_id, name=name, comment=com)
    if vk_tool.check_subscribe(user_id):
        message += ' Пожалуйста, подпишитесь'
    vk_tool.reply(message, dct[2], dct[0])


def stop_game(post):
    if post == first_post:
        battle.game_over()
    elif post == second_post:
        word.game_over()


group_id = 51312
token = ''
dct = {}
dct = json_data(dct)
vk_tool = VkProcess(group_id, token)

# SeaBATTLE
first_post = 1
win_lst = ['в2', 'г3', 'д5', 'е5', 'б6']
battle = SeaBattle(win_lst)

# WordGAME
second_post = 6
litter = 'ф'
word = WordGame(litter)
