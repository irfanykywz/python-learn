"""
python memiliki banyak type data, berikut daftarnya

text : str
number : int, float, complex
sequence (urut) : list, tuple, range
mapping : dict
set type : set, frozenset
boolean : bool
binary : bytes, bytearray, memoryview
none : none
"""

# type data string
name: str = "jojo" # string multiple quote
brother = 'boby' # string single quote
hobby = """ my hobby is fishing on a river, 
i love my rod oh yeah brother : %s
""" % (brother) # string multiline
print(f"{name} {hobby} ")

# type data number
age: int = 20
numb_1: float = 1.63
numb_2: complex = 1+3j
print(f"{age} {numb_1} {numb_2}")

# boolean
rod_is_ready = True
rod_have_hook = False
print(f"{rod_is_ready} {rod_have_hook}")

# list
rod_type = ['bronze', 'silver', 'gold']
hook_size = [10, 20, 30]
print(f"my rod : {rod_type[0]} \n"
      f"hook size: {hook_size[2]}")

# tuple
musim = ('spring', 'summer', 'autumn', 'winter')
print(musim[2])

# dict
my_bag = {
    "one": "axe",
    "two": "pick-axe",
    "three": "sycle",
    "four": "waterin-can",
    "five": "hoe",
    "etc": [
        "rod",
        "berry",
        "iron"
    ]
}
print(f"my second bag item is : {my_bag['two']}")
print(f"{my_bag['etc'][2]}")

# dict multiple
menu = {
    "map": {
        "city" : "city.png",
        "valley" : "valley.png"
    },
    "valid": True
}
print(menu["map"]["city"])
print(menu["valid"])

# set
my_setup = {"laptop", "mouse", "keyboard", "music"}
print(my_setup)
