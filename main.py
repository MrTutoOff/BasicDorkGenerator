import time, os
from time import gmtime, strftime, time
from colorama import Fore
from console import utils
from tkinter import filedialog

combo = []
keywords = []
dorks = []
genedDorks = []


logo = Fore.CYAN+'''
██╗██████╗░░█████╗░██████╗░██╗░░██╗░██████╗░███████╗███╗░░██╗██╗
╚═╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝░██╔════╝████╗░██║╚═╝
░░░██║░░██║██║░░██║██████╔╝█████═╝░██║░░██╗░█████╗░░██╔██╗██║░░░
██╗██║░░██║██║░░██║██╔══██╗██╔═██╗░██║░░╚██╗██╔══╝░░██║╚████║██╗
╚█║██████╔╝╚█████╔╝██║░░██║██║░╚██╗╚██████╔╝███████╗██║░╚███║╚█║
░╚╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝░╚╝ by MrTutoOff\n'''

def Load():
    global ComboName
    filename = filedialog.askopenfile(mode='rb', title='Choose a Keyword file',filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    ComboName = os.path.basename(filename.name)
    if filename is None:
        print(Fore.LIGHTRED_EX+"Invalid File.")
        Load()
    else:
        try:
            with open(filename.name, 'r+') as e:
                ext = e.readlines()
                for line in ext:
                    try:
                        Dump = line.replace('\n', '')
                        combo.append(Dump)
                    except: pass
            Dumped =  list(dict.fromkeys(combo))
            RemovedLines = len(combo) - len(Dumped)
            print(Fore.LIGHTBLUE_EX+f"[{RemovedLines}] Dupes Removed.")
            for lines in combo:
                try:
                    keywords.append(combo[lines])
                except: pass
            print(Fore.LIGHTBLUE_EX+f"[{len(keywords)}] Keywords Loaded.")
        except:
            print(Fore.LIGHTRED_EX+"Your file is probably harmed.")
            Load()
    with open("dorks.txt", 'r') as f:
        for line in f.readlines():
            try:
                dorks.append(dorks[line])
            except: pass



def genDorks():
    for i in range(len(keywords)):
        for a in range(len(dorks)):
            genedDorks.append(f"{keywords[i]} {dorks[a]}")
            with open("genDorks.txt", 'a') as g:
                g.write(f"{keywords[i]} {dorks[a]}")


def Main():
    print(logo)
    print("Load your Keywords...")
    Load()
    genDorks()
    print("Dorks were generated succesfully!")

Main()