import argparse
import os
import sys
import time

import os
import yaml
from termcolor import colored
import argparse
from pyfiglet import Figlet
import sys
import time
import subprocess
import random


def display_flashing_banner(text):
    color_code = '\033[1;%dm'
    reset_color = '\033[0m'
    colors = [31, 32, 33, 34, 35, 36]

    # Ajouter des bordures
    border_top = "+" + "-" * (len(text) + 2) + "+"
    border_bottom = "+" + "-" * (len(text) + 2) + "+"
    text_line = "| " + text + " |"

    # Ajouter des symboles décoratifs
    symbol_top = "/\\___/\\"
    symbol_bottom = "\\/   \\/"

    # Construire la bannière clignotante
    for _ in range(75):  # Répéter 5 fois pour créer l'effet clignotant
        banner = ""
        banner += color_code % random.choice(colors) + border_top + "\n"
        banner += color_code % random.choice(colors) + symbol_top + " " * (len(text) - 10) + symbol_top + reset_color + "\n"
        banner += color_code % random.choice(colors) + text_line + reset_color + "\n"
        banner += color_code % random.choice(colors) + symbol_bottom + " " * (len(text) - 10) + symbol_bottom + reset_color + "\n"
        banner += color_code % random.choice(colors) + border_bottom + reset_color

        print("\033c")  # Effacer l'écran pour créer un effet de clignotement
        print(banner)
        time.sleep(0.05)  # Pause de 0.5 seconde entre chaque clignotement

# Afficher la bannière clignotante
display_flashing_banner('mail spammer')

def add_color_banner():
    banner_text = "mail spammer"
    rainbow_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    colored_banner = ''.join(colored(char, random.choice(rainbow_colors)) for char in banner_text)
    return colored_banner

def display_animated_banner():
    banner = add_color_banner()
    banner_text = "by TRHACKNON"
#     cowsay_command = f"cowsay -f $(ls /usr/share/cowsay/cows/ | shuf -n 1) '{banner}' | lolcat -a"
    cowsay_command = f"cowsay -f sodomized --rainbow --super --aurora --bold -bdgpstwy '{banner_text}'"
#     cowsay_command = f"cowsay -f sodomized --rainbow --super --aurora --bold -bdgpstwy '{banner_text}' | lolcat -a"
    subprocess.run(cowsay_command, shell=True)

display_animated_banner()

try:
        os.system("python src/version.py")
        time.sleep(1)
        os.system("python src/custom_spam.cpython-310.opt-2.pyc")
except KeyboardInterrupt:
        sys.exit()
