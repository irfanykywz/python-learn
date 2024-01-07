nuitka --follow-imports --enable-plugin=pyside6 --standalone --disable-console --nofollow-import-to=tkinter,openpyxl app.py

nuitka --enable-plugin=pyside6 --standalone --disable-console --nofollow-import-to=tkinter,openpyxl app.py

nuitka --standalone --onefile --nofollow-import-to=numpy,openpyxl --enable-plugin=pyside6 app.py


python -m nuitka --follow-imports --onefile --standalone --windows-file-version=1.0.0.0 --windows-company-name=Test --windows-icon-from-ico=..\icon.ico ..\gen_config.py

fix openpyxl
https://stackoverflow.com/questions/74926850/how-to-solve-modulenotfounderror-no-module-named-openpyxl-cell-writer
downgrade openpyxl to version 3.0.9 will also help. it works for me.

pip unistall openpyxl
pip install openpyxl=3.0.9


pyside6 
nuitka --standalone --onefile --enable-plugin=pyside6 app.py