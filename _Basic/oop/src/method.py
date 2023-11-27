# Belajar OOP Python
# irfanykywz
# 25 September 2023
# untuk memenuhi rasa penasaran dari 7bots.dev

class Crops:

    list = ['Turnip','Strawberry','Cabage']

    def __init__(self):
        print('start class crops')

    # create method
    def getCrop(self,val = 0):
        print(f'you select crop : {self.list[val]}')

    # how to create static method
    @staticmethod
    def getCropStatic():
        print(f'you select crop : {Crops.list}')

    # how to create class method
    # call class name with other name on method..
    @classmethod
    def getCropClass(asu):
        print(f'you select crop : {asu.list}')


# Crops().getCrop()
# Crops().getCropStatic()
Crops().getCropClass()