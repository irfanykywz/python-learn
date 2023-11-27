import os
print(os.environ["HOMEPATH"])
print(os.path.expanduser("~"))
print(os.path.join(os.environ["HOMEPATH"], "Desktop"))