
class Viber:
    data = {}
    @classmethod
    def add_message(cls,msg):
        cls.msg = msg
        cls.data[cls.msg.text]= cls.msg.fl_like

    @classmethod
    def remove_message(cls,msg):
        cls.msg = msg
        cls.data.pop(cls.msg.text)

    @classmethod
    def set_like(cls,msg):
        cls.msg = msg
        if cls.msg.fl_like==True:
            cls.msg.fl_like = False
        else:
            cls.msg.fl_like = True

    @classmethod
    def show_last_message(cls,num):
        print(list(cls.data.keys())[-num:])

    @classmethod
    def total_messages(cls):
        return len(cls.data)

class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False

