# https://www.programiz.com/python-programming/user-defined-exception

def run(s):
    if s == 'yes':
        return True    
    raise Exception('string is different')


try:
    run('a')
except Exception as e:
    print(e)
    pass
