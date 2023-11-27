# https://stackoverflow.com/questions/34275782/how-to-get-desktop-location

def get_desktop_path():
    import os
    import platform
    if platform.system() == 'Windows':
        try:
            import winreg
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
            desktop = winreg.QueryValueEx(reg_key, 'Desktop')[0]
            winreg.CloseKey(reg_key)
        except:
            desktop = "None"
    else:
        from pathlib import Path
        desktop = Path.home() / 'Desktop'
        if not os.path.exists(desktop):
            desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    if not os.path.exists(desktop):
        desktop = os.path.normpath(os.path.expanduser("~"))
        print(f"arsip akan disimpan ke: {desktop}")
    else:
        print(f"arsip akan disimpan ke desktop")
    return desktop

print(get_desktop_path())