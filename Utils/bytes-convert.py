# https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
 
def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size


print(convert_bytes(2131231))