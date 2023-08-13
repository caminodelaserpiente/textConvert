# Text Convert 📝🗣️
Tool for Convert Text to Speech


## Functionalities ⚙️
1. Convert input Text
2. Convert .txt file
3. Convert .csv file
4. Convert .csv file for Anki


## Install 🔧 
1. Clone this repo.<br>
    ```consol
    git clone https://github.com/caminodelaserpiente/textConvert
    ```

2. Change the working directory.<br>
    ```consol
    cd textConvert
    ```

3. Install the requirements.<br>
    ```consol
    pip install -r requirements.txt
    ```


## Play 🎮
```consol
python3 main.py
```

         _____              _      ____                                   _   
        |_   _|  ___ __  __| |_   / ___|  ___   _ __  __   __  ___  _ __ | |_ 
          | |   / _ \\ \/ /| __| | |     / _ \ | '_ \ \ \ / / / _ \| '__|| __|
          | |  |  __/ >  < | |_  | |___ | (_) || | | | \ V / |  __/| |   | |_ 
          |_|   \___|/_/\_\ \__|  \____| \___/ |_| |_|  \_/   \___||_|    \__| 

    
        ----------------------------------------------------
            - Select the language. (e.g. >>> 4)
                [0] Exit
                [1] Spanish
                [2] English
                [3] Italian
                [4] French 
                [5] German
    Select option.
    >>> 1

        ----------------------------------------------------
            - Select option to convert text to audio. (e.g. >>> 4)
                [1] Write text
                [2] From file .txt 
                [3] From file .csv
                [4] Flash Cards for Anki
    Select option.
    >>> 1 
    Write your text. 
    >>> hola

    Write audio name. 
    >>> saludo

    Your text is converting...
    ./output/input_text/saludo.mp3
 

## Saved data 💾
* The .mp3 files are saved in the `./output/` folder  📁
* The .csv for Anki are saved in the `./output/` folder  📁
