import vk_api
import wikipedia
from vk_api.longpoll import VkLongPoll, VkEventType
from scraper import Scraper
from database import DB


class VkBot:
    def __init__(self, token):
        self.token = token

    def runBot(self):
        vk = vk_api.VkApi(token=self.token)
        random_id = 1234
        longpoll = VkLongPoll(vk)
        scrap = Scraper()
        db = DB()

        def write_msg(user_id, message, random_id):
            vk.method('messages.send', {'user_id': user_id,
                                        'message': message, 'random_id': random_id})

        def write_news(user_id, array, random_id):
            text = ''
            for i in range(10):
                text += ' ' + array[i][1] + ' ' + array[i][0] + '\n '
            write_msg(user_id, text, random_id)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    request = event.text.lower()
                    if request == "википедия":
                        db.addPost(event.user_id, "Википедия")
                        write_msg(event.user_id,
                                  "Что мне найти?", random_id)
                        random_id += 1
                        for event in longpoll.listen():
                            if (event.type == VkEventType.MESSAGE_NEW) & (event.to_me):
                                request = event.text
                                try:
                                    write_msg(event.user_id, "Вот что я нашел: \n" +
                                              str(wikipedia.summary(request)), random_id)
                                except Exception:
                                    write_msg(event.user_id, "Ничего не найдено", random_id)
                                    random_id += 1
                                break
                    elif request == "привет":
                        write_msg(event.user_id,
                                  "Хай", random_id)
                        random_id += 1
                    elif request == "погода":
                        write_msg(event.user_id,
                                  "Введите ваш город", random_id)
                        random_id += 1
                        for event in longpoll.listen():
                            if (event.type == VkEventType.MESSAGE_NEW) & (event.to_me):
                                city = event.text
                                url = "https://yandex.ru/pogoda/" + city
                                info = scrap.weather(url)
                                write_msg(
                                    event.user_id, info, random_id)
                                random_id += 1
                                break
                        db.addPost(event.user_id, "Погода")
                    elif request == "новости":
                        db.addPost(event.user_id, "Новости")
                        tempArray = scrap.lastNews()
                        write_news(event.user_id, tempArray, random_id)
                        random_id += 1
                    else:
                        write_msg(
                            event.user_id, "Не понял. Доступные команды :\n 1. Погода\n 2. Новости\n 3. Википедия\n", random_id)
                        random_id += 1
