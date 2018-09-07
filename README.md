# website_blocker

## How to run?

### Command Prompt
Open command prompt and write 
```console
python website_blocker.py
```
### Using exe file

1. Install pyinstaller
```console
pip install pyinstaller
```

2.  If you are working on Windows. You might need to install PyWin32 as well!Download it from here: 
```
https://sourceforge.net/projects/pywin32/files/
```

3. If you are using different package management tool such as conda (for Anaconda) then you will have to use the following commands instead:
```console
conda install -c conda-forge pyinstaller
conda install -c anaconda pywin32
```

4. Compile the python script into executable file
```console
pyinstaller --onefile website_blocker.py
```

5. Run the `website_blocker.exe` file in the `dist` folder
