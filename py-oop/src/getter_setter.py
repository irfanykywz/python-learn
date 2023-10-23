# Belajar OOP Python
# irfanykywz
# 25 September 2023
# untuk memenuhi rasa penasaran dari 7bots.dev

class Fishing:

    __pancingan = 'Iridium Rod'
    __umpan = 'Cacing Alaska'

    # mengubah method ke property
    @property
    def persiapan(self):
        pass

    @persiapan.getter
    def persiapan(self):
        print(f'akan mancing menggunakan {self.__pancingan} dengan umpan {self.__umpan}')


    @persiapan.setter
    def persiapan(self,pan):
        self.__pancingan = pan

# now method can call like a property...
Fishing().persiapan

# set value
man = Fishing()
man.persiapan = 'Golden Rod'
man.persiapan