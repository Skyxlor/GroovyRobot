import threading

from sqlalchemy import Column, String

from GroovyRobot.modules.sql import BASE, SESSION


class GroovyChats(BASE):
    __tablename__ = "Groovy_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


GroovyChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_Groovy(chat_id):
    try:
        chat = SESSION.query(GroovyChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_Groovy(chat_id):
    with INSERTION_LOCK:
        Groovychat = SESSION.query(GroovyChats).get(str(chat_id))
        if not Groovychat:
            Groovychat = GroovyChats(str(chat_id))
        SESSION.add(Groovychat)
        SESSION.commit()


def rem_Groovy(chat_id):
    with INSERTION_LOCK:
        Groovychat = SESSION.query(GroovyChats).get(str(chat_id))
        if Groovychat:
            SESSION.delete(Groovychat)
        SESSION.commit()
