import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

main_token = '66789f57316dd90cd3714d0b4de68d3235214ca67637b69d7891d461bb66b382e7f645aae616edd2fdd5c'

vk_session = vk_api.VkApi(token=main_token)
longpoll = VkLongPoll(vk_session)

def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message' : text, 'random_id' : 0})
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_chat:
            msg = event.text.lower()
            id = event.chat_id
            if msg == "#pokex5":
                for i in range(5):
                    sender(id, "@all, @all, @all, @all, @all. Poke Машина запущена")
            if msg == "#status":
                sender(id, "Status: Online, Dev: @rodionovd21")
