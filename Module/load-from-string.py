# https://stackoverflow.com/questions/5362771/how-to-load-a-module-from-code-in-a-string

"""
fungsi dari load module from string yaitu memisahkan kode ketika aplikasi berbentuk exe

cara ini berguna untuk memaintenance kode yang selalu berubah 


untuk lebih bagusnya kode di enkripsi dulu baru di load biar gak mudah dibaca
"""

import sys, importlib.util

def import_module_from_string(source: str):
  """
  Import module from source string.
  Example use:
  import_module_from_string("m", "f = lambda: print('hello')")
  m.f()
  """
  spec = importlib.util.spec_from_loader('jojo', loader=None)
  module = importlib.util.module_from_spec(spec)
  # exec code
  exec(source, module.__dict__)
  # merge to sys module
  sys.modules = module
  # return module
  return module
  # globals()[name] = module


# demo

# note: "if True:" allows to indent the source string
teste = import_module_from_string('''
asu = "babhi"
def hello():
	print('hello')
def printfo():
	for i in range(100):
		print(i)
''')

teste.hello()
print(teste.asu)
teste.printfo()