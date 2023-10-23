# Belajar OOP Python
# irfanykywz
# 25 September 2023
# untuk memenuhi rasa penasaran dari 7bots.dev


class Crop:

    _crop = ''

    def __init__(self, val):
        self._crop = val

    def getCrop(self):
        return self._crop

class CropMutation(Crop):

    def __init__(self, val):
        super().__init__(val)
        self.__mutation = 'Golden Turnip'

    def show(self):
        print(f'crop {super().getCrop()} mutate to : {self.__mutation}')


CropMutation('Turnip').show()