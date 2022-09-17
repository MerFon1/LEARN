"""

"""

class Application:

    def __init__(self,name,blocked=False):
        self.name = name
        self.blocked = blocked


class AppStore:
    data = {}

    def add_application(self, app):
        self.app = app
        self.data[self.app.name]= self.app.blocked

    def remove_application(self, app):
        self.app = app
        self.data.pop(self.app.name)

    def block_application(self, app):
        self.app = app
        self.app.blocked = True
        self.data[self.app.name]==self.app.blocked

    def total_apps(self):
        return len(self.data)


