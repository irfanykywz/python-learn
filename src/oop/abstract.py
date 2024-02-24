# Belajar OOP Python
# irfanykywz
# 25 September 2023
# untuk memenuhi rasa penasaran dari 7bots.dev

# import module abstarct
from abc import ABC,abstractmethod

class WinterBluePrint(ABC):

    @abstractmethod
    def SnowFall(self):
        pass


class Winter(WinterBluePrint):

    def SnowFall(self):
        pass


a = Winter()

# keterangan
# abstract class = blueprint dari sebuah main class
# main class harus mengimplementasikan method yang ada di class blueprint tersebut
# jika main class tidak mengimplementasikannya maka akan terjadi error
# berguna jika banyak aksi yang sama