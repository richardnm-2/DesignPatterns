class SendEmail():

    username = 'teste'
    _username = 'teste'
    __username = 'teste'

    def __call__(self, message='Default message'):
        print()
        self.__connect()
        self.__authenticate()
        print(f'Username: {self.username}')
        print(f'Username _: {self._username}')
        print(f'Username __: {self.__username}')
        print(message)
        self.__disconnect()


    def __connect(self):
        print('Connect')

    def _authenticate(self):
        print('Authenticate')

    def __disconnect(self):
        print('Disconect')
