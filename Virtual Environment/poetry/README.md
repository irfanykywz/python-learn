init command (poetry will generate pyproject.toml)
```
poetry init
```

add dependencies command
```
poetry add seleniumbase
poetry add seleniumbase@^4.22.4
poetry add "seleniumbase>=4.22.4"
poetry add "seleniumbase==4.22.4"
poetry add seleniumbase@latest
```


install virtual environment command
```
poetry install --no-root
poetry install --no-dev
```


find virtualenvs.path and copy python.exe path for use this environment
```
poetry config --list
```

result
```
cache-dir = "C:\\Users\\WIN10\\AppData\\Local\\pypoetry\\Cache"
experimental.system-git-client = false
installer.max-workers = null
installer.modern-installation = true
installer.no-binary = null
installer.parallel = true
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.options.always-copy = false
virtualenvs.options.no-pip = false
virtualenvs.options.no-setuptools = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = "{cache-dir}\\virtualenvs"  # C:\Users\WIN10\AppData\Local\pypoetry\Cache\virtualenvs
virtualenvs.prefer-active-python = false
virtualenvs.prompt = "{project_name}-py{python_version}"
warnings.export = true
```

add python.exe virtual environment to IDE
```
C:\Users\WIN10\AppData\Local\pypoetry\Cache\virtualenvs\seleniumbase-env-5UyUZSyX-py3.10\Scripts\python.exe
```

finish...