# Belajar OOP Python
# irfanykywz
# 25 September 2023
# untuk memenuhi rasa penasaran dari 7bots.dev


class Armor:
    def setArmor(self,arm):
        print(f'set armor menjadi {arm}')

class Weapon:
    def setWeapon(self,wea):
        print(f'set weapon menjadi {wea}')

class Battle(Armor,Weapon):
    def start(self):
        print('memulai pertarungan...')

go = Battle()
go.setArmor('baju besi')
go.setWeapon('senjata api')
go.start()