"""
Author: 蛇道
Url: https://github.com/caminodelaserpiente
"""


from gtts import gTTS
import os
import shutil
import csv


import pandas as pd


def text_convert(response, lang, tld):
    if response == 1:
        text = _text_input()
        name_file = _select_name_file()
        _audio_convert('input_text', name_file, text, lang, tld)
    elif response == 2:
        text = _read_txt()
        name_file = _select_name_file()
        _audio_convert('txt_file', name_file, text, lang, tld)
    elif response == 3:
        texts = _read_csv()
        for text in texts:
            _audio_convert('csv_file', text, text, lang, tld)
    elif response == 4:
        texts = _read_csv_anki()
        for text in texts:
            _audio_convert('anki_file', text, text, lang, tld)
    else:
        print("Error -- Please enter a valid option.")


def _text_input():
    while True:    
        try:
            text = input("Write your text. \n>>> ")
            if(not(text and text.strip())):
                raise ValueError("Error -- Cannot enter an empty string")
            return text
        except ValueError as error:
            print("Error -- Cannot enter an empty string")
            continue


def _read_txt():
    path = input('Enter path file txt. \n>>> ')
    text = ""
    with open(path, "r", encoding="utf-8") as t:
        for line in t:
            print(line)
            text += line.strip("\n")
    return text


def _read_csv():
    while True:
        try:
            path = input('Enter path file txt. \n>>> ')
            df = pd.read_csv(path)
            columns = df.columns
            cont = 0
            print("\n")
            for col in columns:
                print(f"[{cont}] {col}")
                cont += 1
            while True:
                try:
                    response = int(input("Select column to transform to audio. \n>>> "))
                    text_csv = df.iloc[:, response]
                    text_csv = list(text_csv)
                    return text_csv
                except ValueError:
                    print("Error -- Please enter a valid numerical option.")
                except IndexError:
                    print("Error -- Invalid column index.")
            break
        except FileNotFoundError:
            print("Error -- No such file or directory.")


def _read_csv_anki():
    while True:
        try:
            path = input('Enter path file txt. \n>>> ')
            df = pd.read_csv(path)
            columns = df.columns
            cont = 0
            print("\n")
            for col in columns:
                print(f"[{cont}] {col}")
                cont += 1
            while True:
                try:
                    response = int(input("Select column to transform to audio. \n>>> "))
                    text_csv = df.iloc[:, response]
                    text_csv = list(text_csv)
                    break
                except ValueError:
                    print("Error -- Please enter a valid numerical option.")
                except IndexError:
                    print("Error -- Invalid column index.")
            break
        except FileNotFoundError:
            print("Error -- No such file or directory.")
    try:
        output_folder = './output/'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        wordFront = list(df.iloc[:, 0])
        wordBack = list(df.iloc[:, 1])
        with open('./output/importAnki.csv', 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['front', 'back']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for valueWF, valueWB in zip(wordFront, wordBack):
                if response == 0:
                    front = valueWF + "<br>" + f'[sound:{valueWF}.mp3]'
                    back = valueWB
                elif response == 1:
                    front = valueWF
                    back = valueWB + "<br>" + f'[sound:{valueWB}.mp3]'
                writer.writerow({'front': front, 'back': back})
        return text_csv
    except FileNotFoundError:
        print("Error -- No such file or directory.")
    except IndexError:
        print("Error -- The file must have at least two columns.")


def _select_name_file():
    while True:
        try:
            audio_name = input("\nWrite audio name. \n>>> ")
            if(not(audio_name and audio_name.strip())):
                raise ValueError("Error -- Cannot enter an empty string")
            return audio_name
        except ValueError as error:
            print("Error -- Cannot enter an empty string")
            continue


def _audio_convert(folder, audio_name, text, LANG, TLD):
    output_folder = f'./output/{folder}/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    audio_name = os.path.join(output_folder, audio_name + ".mp3")
    audio = gTTS(text, lang=LANG, tld=TLD) # Convert texto to audio
    print(f"\nYour text is converting...\n{audio_name}")
    audio.save(audio_name) # Save audio file
