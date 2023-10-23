# Belajar OOP Python
# irfanykywz
# 25 September 2023
# untuk memenuhi rasa penasaran dari 7bots.dev

# protect internal data with encapsulation

class Cuaca:
    def __init__(self):
        # define private property
        self.__today = 'cerah'
        self.__tommorow = 'hujan'

    def getToday(self):
        print(self.__today)

    def setToday(self, val):
        self.__today = val

    def getTommorow(self):
        print(self.__tommorow)

    def setTommorow(self, val):
        self.__tommorow = val


cua = Cuaca()
cua.getToday()
cua.getTommorow()

print('\n')

# change value
cua.setToday('mendung')
cua.getToday()
cua.setTommorow('badai')
cua.getTommorow()