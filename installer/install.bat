@echo off

:: check if python is installed
>nul 2>nul assoc .py

if errorlevel 1 (
    :: python is not installed
    echo Python not installed, downloading installer...
    powershell -c "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe' -OutFile '%USERPROFILE%\AppData\Local\Temp\python-3.13.3.exe'"
    echo Launching installer, please make sure to follow the correct setup instructions Adding python to environment variables!
    echo:

    "%USERPROFILE%\AppData\Local\Temp\python-3.13.3.exe"
    pause
    echo Please press any button once you have completed the python setup, so we can continue installing the depedencies.

) else (
    echo Python is already installed. Please make sure its of version 3.13.3 or higher, using an older version might not work
)

:: get depedencies, not worth checking worst case they are already installed.
echo Installing dependencies...
py -m pip install -r requirements.txt

echo Finished installing dependencies.
echo: 


:: check if tesseract installer is already in temp, download if its not
if not exist "%USERPROFILE%\AppData\Local\Temp\tesseract.exe" (
    echo Downloading tesseract installer because it does not yet exist.
    powershell -c "Invoke-WebRequest -Uri 'https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe' -OutFile '%USERPROFILE%\AppData\Local\Temp\tesseract.exe'"
) else (                                 
    echo Skipped downloading tesseract installer because it already exists. Project was made using version 5.5.0.20241111 and may have better results with it
)


:: check if we need to run the installer of if its already setup where it should be
if exist "C:\Program Files\Tesseract-OCR\" (
    echo Skipped executing installer because tesseract is already installed.

) else (
    echo Tesseract needs to be installed, please install it at C:\Program Files\Tesseract-OCR
    "%USERPROFILE%\AppData\Local\Temp\tesseract.exe")


echo Setup finished.
pause