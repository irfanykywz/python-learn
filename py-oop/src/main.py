# Belajar OOP Python
# irfanykywz
# 25 September 2023
# untuk memenuhi rasa penasaran dari 7bots.dev

class Seasons:

    # property / attribute
    data = ''

    # construct
    def __init__(self):
        # fill property
        self.data = ['spring', 'summer', 'autumn', 'winter']

    # method
    def list(self, dat = 0):
        return self.data[dat]

# call object
season = Seasons()

# call method
print(season.list(3))

print(Seasons.__dict__)