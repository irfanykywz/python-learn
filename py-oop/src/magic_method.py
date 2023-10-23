# Belajar OOP Python
# irfanykywz
# 25 September 2023
# untuk memenuhi rasa penasaran dari 7bots.dev

class BotKill:

    def __init__(self, name, count):
        self.name = name
        self.count = count

    ## magic method for print > development / test
    def __repr__(self):
        return f'repr : {self.name} + {self.count}'

    ## magic method for print > production
    def __str__(self):
        return f'str : {self.name} + {self.count}'


do = BotKill('Huba',100)
print(do)