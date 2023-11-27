class Joki:
    def __init__(self, nama, action):
        self.nama = nama
        self.action = action

    def start(self):
        print(f'{self.nama} + {self.action}')



# func
def external():
    print('hello this is call without object')