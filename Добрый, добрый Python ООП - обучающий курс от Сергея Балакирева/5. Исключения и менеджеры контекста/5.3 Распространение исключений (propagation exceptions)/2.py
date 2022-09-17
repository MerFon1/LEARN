"""

"""

class ValidatorString:

    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if len(self.chars)==0:
            if self.min_length <= len(string) <= self.max_length == False:
                raise ValueError('недопустимая строка')
        else:
            if (self.min_length <= len(string) <= self.max_length and any([i in string for i in self.chars])) == False:
                raise ValueError('недопустимая строка')

class LoginForm:

    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = None
        self._password = None

    def form(self, request):
        if 'login' not in list(request.keys()) or 'password' not in list(request.keys()):
            raise TypeError('в запросе отсутствует логин или пароль')

        self.login_validator.is_valid(request['login'])
        self.password_validator.is_valid(request['password'])
        self._login = request['login']
        self._password = request['password']

login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)