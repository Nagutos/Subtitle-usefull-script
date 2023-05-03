import os 
import glob
import re
import time

inc = 1
path = input(".------------------------------------------------------------.\n|                       Resync batch                         |\n|         Quel est le chemin d'accès de tes fichiers ?       |\n'------------------------------------------------------------' \n\nAppuyez sur q pour quitter le programme. \n\nVotre entrée : ")
if path == "q":
    exit()
os.chdir(path)
path_corrceted = path+"/sous-titre_corrigés"
mkv_files = glob.glob("*.mkv")

def human_sort(files):
    try:
        files.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
    except:
        files.sort(key=lambda var:[str(int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var))])

human_sort(mkv_files)

if not os.path.exists(path_corrceted):
    os.mkdir(path_corrceted)

def fin_de_programme():
    print("Exécution terminée !")
    time.sleep(5)
    exit()

def srt_retime():
    srt_files = glob.glob("*.srt")
    human_sort(srt_files)
    global inc
    for i in mkv_files:
        print("\nCommande exécuter : \n ffs \""+ mkv_files[inc-1] +"\" -i \""+ srt_files[inc-1] +"\" -o \"" + path_corrceted +"/EP"+(str)(inc)+".srt\" \n" )
        os.system("ffs \""+ mkv_files[inc-1] +"\" -i \""+ srt_files[inc-1] +"\" -o \"" + path_corrceted +"/EP"+(str)(inc)+".srt\" \n" )
        inc = inc + 1
    fin_de_programme()

def ass_retime():
    ass_files = glob.glob("*.ass")
    human_sort(ass_files)
    global inc
    for i in mkv_files:
        print("\nCommande exécuter : \n ffs \""+ mkv_files[inc-1] +"\" -i \""+ ass_files[inc-1] +"\" -o \"" + path_corrceted +"/EP"+(str)(inc)+".ass\" \n" )
        os.system("ffs \""+ mkv_files[inc-1] +"\" -i \""+ ass_files[inc-1] +"\" -o \"" + path_corrceted +"/EP"+(str)(inc)+".ass\" \n" )
        inc = inc + 1
    fin_de_programme()

choice = int(input("Choisi le format de tes fichiers. \n 1 - Format : ASS \n 2 - Format : SRT \n 3 - Quitter \n"))
if choice == 1:
    ass_retime()
if choice == 2:
    srt_retime()
if choice == 3:
    exit()