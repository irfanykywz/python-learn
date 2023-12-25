
def get_document_path():
	import ctypes.wintypes
	CSIDL_PERSONAL = 5       
	SHGFP_TYPE_CURRENT = 0 
	buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
	ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
	return buf.value


print(get_document_path())