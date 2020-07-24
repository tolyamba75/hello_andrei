import vk_api


class VkProcess:
    def __init__(self, token, group_id):
        vk_session = vk_api.VkApi(token=token)
        self.vk = vk_session.get_api()
        self.group_id = group_id    # положительное число

    # ответ на комментарий
    def reply(self, message, post_id, num_comment):
        self.vk.wall.createComment(owner_id=-self.group_id, post_id=post_id,
                                   from_group=self.group_id, message=message,
                                   reply_to_comment=num_comment)

    # выключение комментариев
    def off_comments(self, post_id):
        self.vk.wall.closeComments(owner_id=-self.group_id, post_id=post_id)

    # проверка лайка
    def check_subscribe(self, user_id):
        subscribe = self.vk.groups.isMember(group_id=self.group_id, user_id=user_id)
        if subscribe:
            return True
        else:
            return False
    
    def check_name(self, users_id):
        name = self.vk.users.get(user_ids=users_id)[0]['first_name']
        return name

