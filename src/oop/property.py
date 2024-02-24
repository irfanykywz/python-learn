# Belajar OOP Python
# irfanykywz
# 25 September 2023
# untuk memenuhi rasa penasaran dari 7bots.dev

class Festival:

    # private use __[property]
    __name = 'wooly'

    # protected use _[property]
    _participant = 1000

    def __init__(self):
        print(f'{self.__name} + {self._participant}')


# access class
Festival()

# access propery
now = Festival()
print(now.__name)
# error 'AttributeError: 'Festival' object has no attribute '__name'
print(now._participant)
# result 1000