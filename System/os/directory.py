import os
print(os.environ["HOMEPATH"])
print(os.path.expanduser("~"))
print(os.path.join(os.environ["HOMEPATH"], "Desktop"))
print(os.getenv('APPDATA'))
print(os.getenv('LOCALAPPDATA'))
print(os.getenv('TEMP'))
print(os.path.dirname(__file__))

print(os.path.join(os.getenv('APPDATA'), 'ykywz/'))