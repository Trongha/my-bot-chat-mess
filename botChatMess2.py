import logging
import os
import time
from threading import Thread

from fbchat import Client
from fbchat.models import Message, ThreadType
import schedule


class Bot(Client):
    def onMessage(self, message_object, author_id, thread_id, thread_type, **kwargs):
        lst_msg = list('Chúc mừng năm mới')
        if author_id != self.uid and message_object.text in lst_msg:
            self.send(Message(text='Năm mới chúc .....'),
                      thread_id=author_id,
                      thread_type=ThreadType.USER)


    def do_something(self):
        logging.basicConfig(level=logging.INFO)
        user_ids = ['100012610305665']
        for user_id in user_ids:
            self.send(Message(text="Chúc mừng năm mới"),
                      thread_id=user_id, thread_type=ThreadType.USER)
            self.sendLocalImage('/home/dosontung007/Pictures/wallpaper.png', message=Message(text='Chúc mừng năm mới'),
                                thread_id=user_id, thread_type=ThreadType.USER)
            logging.info('Sent success to %s' % "100012610305665")


def job_that_executes_once():
    Bot(os.environ['USERNAME_'], os.environ['PASSWORD']).something()
    return schedule.CancelJob


def reply_msg():
    Bot(os.environ['USERNAME_'], os.environ['PASSWORD']).listen()


def send_msg():
    schedule.every().day.at('00:00').do(job_that_executes_once))
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    Thread(target=send_msg).start()
    Thread(target=reply_msg).start()


if __name__ == '__main__':
    main()