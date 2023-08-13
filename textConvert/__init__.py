"""
Author: 蛇道
Url: https://github.com/caminodelaserpiente
"""


from textConvert.text_to_speech.text_to_speech import *


def banner():
    banner= """
     _____              _      ____                                   _   
    |_   _|  ___ __  __| |_   / ___|  ___   _ __  __   __  ___  _ __ | |_ 
      | |   / _ \\\\ \/ /| __| | |     / _ \ | '_ \ \ \ / / / _ \| '__|| __|
      | |  |  __/ >  < | |_  | |___ | (_) || | | | \ V / |  __/| |   | |_ 
      |_|   \___|/_/\_\ \__|  \____| \___/ |_| |_|  \_/   \___||_|    \__| \n"""
    print(banner)


def option_language():
    menu = """ 
    ----------------------------------------------------
        - Select the language. (e.g. >>> 4)
            [0] Exit
            [1] Spanish
            [2] English
            [3] Italian
            [4] French 
            [5] German"""
    print(menu)
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            response = int(input("Select option.\n>>> "))
            return response
        except ValueError:
            attempts += 1
            print("Error -- Please enter a valid numerical option.")
    print("Exceeded maximum attempts. Exiting the program.")
    exit()


def option_convert():
    menu = """
    ----------------------------------------------------
        - Select option to convert text to audio. (e.g. >>> 4)
            [1] Write text
            [2] From file .txt 
            [3] From file .csv
            [4] Flash Cards for Anki"""
    print(menu)
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            response = int(input("Select option.\n>>> "))
            return response
        except ValueError:
            attempts += 1
            print("Error -- Please enter a valid numerical option.")
    print("Exceeded maximum attempts. Exiting the program.")
    exit()


def textConvert():
    banner()
    languages = {
        0: 'bye',
        1: ['es','es'],
        2: ['en','com'],
        3: ['it','it'],
        4: ['fr','fr'],
        5: ['de','de']
    }
    try:
        while True:
            response = option_language()
            if response == 0:
                print(languages[response])
                break
            elif response == 1:
                lang = languages[response][0]
                tld = languages[response][1]
                response = option_convert()
                text_convert(response, lang, tld)
            elif response == 2:
                lang = languages[response][0]
                tld = languages[response][1]
                response = option_convert()
                text_convert(response, lang, tld)
            elif response == 3:
                lang = languages[response][0]
                tld = languages[response][1]
                response = option_convert()
                text_convert(response, lang, tld)
            elif response == 4:
                lang = languages[response][0]
                tld = languages[response][1]
                response = option_convert()
                text_convert(response, lang, tld)
            elif response == 5:
                lang = languages[response][0]
                tld = languages[response][1]
                response = option_convert()
                text_convert(response, lang, tld)
            else:
                print("Error -- Please enter a valid option.")
    except KeyboardInterrupt:
        print("\ninterrupted by the user bye")
