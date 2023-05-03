import os 
import glob
import re
import time
import ctypes, sys

inc = 1

def human_sort(files):
    try:
        files.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
    except:
        files.sort(key=lambda var:[str(int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var))])

#  F:\Manga Anime\Koi wa Sekai Seifuku no Ato de\[ReinForce] Koi wa Sekai Seifuku no Ato de (BDRip 1920x1080 x264 FLAC)

def change_file_to_default_cr_settings():
    inc = 0
    search = ["PlayResX:", "PlayResY:", "Style: Default", "Style: Italique", "Style: TiretsItalique", "Style: TiretsDefault","Style: DefaultUP","Style: ItaliqueUP","Style: Overlap","Style: FairyTail BD"]
    replace = ["PlayResX: 1920\n", "PlayResY: 1080\n","Style: Default,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,2,3,3,75,1\n","Style: Italique,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,2,3,3,75,1\n","Style: TiretsItalique,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,1,60,6,75,1\n","Style: TiretsDefault,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,1,60,3,75,1\n","Style: DefaultUP,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,8,6,6,75,1\n","Style: ItaliqueUP,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,8,6,6,75,1\n","Style: Overlap,Verdana,65,&H00F9F9F9,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,2,9,9,75,1\n","Style: FairyTail BD,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,2,3,3,75,1\n"]
    ass_files = glob.glob("*.ass")
    human_sort(ass_files)
    for path in ass_files :
        inc += 1
        path = os.path.abspath(path)
        print(path)
        print("Progression Episode : "+str(inc))
        f = open(path, "r", encoding='utf-8')
        for line in f:
            for x in range(len(search)):
                if line.find(search[x]) != -1:
                    line = replace[x]
            fa = open(path_corrceted+"/E"+str(inc)+".ass", "a+", encoding='utf-8')
            fa.write(line)
            fa.close()
        f.close()

def change_file_to_choosen_settings():
    search = ["PlayResX:", "PlayResY:"]
    replace = ["PlayResX: 1920\n", "PlayResY: 1080\n"]
    while True:
        search_settings = input("Entrée le paramètre de qui doit être remplacée avec le nom du style ressemblant à : Style: Default \n\n")
        replace_settings = input("Entrée le paramètre de qui doit remplacer avec le nom du style ressemblant à : Style: Default,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,2,3,3,75,1 \n Il est essentiel d'ajouter un \\n à la fin de la ligne !\n\n")
        search[len(search+1)] = '"'+search_settings+'", '
        replace[len(replace+1)] = '"'+replace_settings+'", '
        if search_settings == "finish":
            break
    inc = 0
    ass_files = glob.glob("*.ass")
    human_sort(ass_files)
    for path in ass_files :
        inc += 1
        path = os.path.abspath(path)
        print(path)
        print("Progression Episode : "+str(inc))
        f = open(path, "r", encoding='utf-8')
        for line in f:
            for x in range(len(search)):
                if line.find(search[x]) != -1:
                    line = replace[x]
            fa = open(path_corrceted+"/E"+str(inc)+".ass", "a+", encoding='utf-8')
            fa.write(line)
            fa.close()
        f.close()

def change_file_to_crunchyroll_change_without_redimension():
    inc = 0
    search = ["Style: Default", "Style: Italique", "Style: TiretsItalique", "Style: TiretsDefault","Style: DefaultUP","Style: ItaliqueUP","Style: Overlap"]
    replace = ["Style: Default,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,2,3,3,75,1\n","Style: Italique,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,2,3,3,75,1\n","Style: TiretsItalique,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,1,60,6,75,1\n","Style: TiretsDefault,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,1,60,3,75,1\n","Style: DefaultUP,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,8,6,6,75,1\n","Style: ItaliqueUP,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,8,6,6,75,1\n","Style: Overlap,Verdana,65,&H00F9F9F9,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,2,9,9,75,1\n"]
    ass_files = glob.glob("*.ass")
    human_sort(ass_files)
    for path in ass_files :
        inc += 1
        path = os.path.abspath(path)
        print(path)
        print("Progression Episode : "+str(inc))
        f = open(path, "r", encoding='utf-8')
        for line in f:
            for x in range(len(search)):
                if line.find(search[x]) != -1:
                    line = replace[x]
            fa = open(path_corrceted+"/E"+str(inc)+".ass", "a+", encoding='utf-8')
            fa.write(line)
            fa.close()
        f.close()

def change_for_pysubs2():
    inc = 0
    search = ["Style: Default", "Style: Italique", "Style: TiretsItalique", "Style: TiretsDefault","Style: DefaultUP","Style: ItaliqueUP","Style: Overlap"]
    replace = ["Style: Default,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,2,3,3,75,1\n","Style: Italique,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,2,3,3,75,1\n","Style: TiretsItalique,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,1,60,6,75,1\n","Style: TiretsDefault,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,1,60,3,75,1\n","Style: DefaultUP,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,0,0,0,100,100,0,0,1,4,0,8,6,6,75,1\n","Style: ItaliqueUP,Verdana,65,&H00FFFFFF,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,8,6,6,75,1\n","Style: Overlap,Verdana,65,&H00F9F9F9,&H000000FF,&H003E3E3E,&H00000000,-1,-1,0,0,100,100,0,0,1,4,0,2,9,9,75,1\n"]
    ass_files = glob.glob("*.ass")
    human_sort(ass_files)
    for path in ass_files :
        inc += 1
        line_number = 0
        path = os.path.abspath(path)
        print(path)
        print("Progression Episode : "+str(inc))
        f = open(path, "r", encoding='utf-8')
        for line in f:
            line_number+=1
            if line_number == 8:
                line = "PlayResX: 1920 \nPlayResY: 1080 \nScaledBorderAndShadow: yes\n\n"
            for x in range(len(search)):
                if line.find(search[x]) != -1:
                    line = replace[x]
            fa = open(path_corrceted+"/E"+str(inc)+".ass", "a+", encoding='utf-8')
            fa.write(line)
            fa.close()
        f.close()

def fin_de_programme():
    print("Exécution terminée !")
    time.sleep(10)
    exit()

def start_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if start_as_admin():
    choice = int(input("Choisi le style à appliquer. \n 1 - Styles par défault de nom de Crunchyroll \n 2 - Styles choisi est modifier par le choix d'entrée \n 3 - Styles par défault de nom de Crunchyroll sans la redimsension \n 4 - Style réinitialiser pour py2subs \n 5 - Quitter \n"))
    if choice == 1:
        path = input(".------------------------------------------------------------.\n|                     ASS Default batch                      |\n|         Quel est le chemin d'accès de tes fichiers ?       |\n'------------------------------------------------------------' \n\nAppuyez sur q pour quitter le programme. \n\nVotre entrée : ")
        if path == "q":
            exit()
        os.chdir(path)
        path_corrceted = path+"/Style_corrigés"
        if not os.path.exists(path_corrceted):
            os.mkdir(path_corrceted)
        change_file_to_default_cr_settings()
    if choice == 2:
        path = input(".------------------------------------------------------------.\n|                     ASS Default batch                      |\n|         Quel est le chemin d'accès de tes fichiers ?       |\n'------------------------------------------------------------' \n\nAppuyez sur q pour quitter le programme. \n\nVotre entrée : ")
        if path == "q":
            exit()
        os.chdir(path)
        path_corrceted = path+"/Style_corrigés"
        if not os.path.exists(path_corrceted):
            os.mkdir(path_corrceted)
        change_file_to_choosen_settings()
    if choice == 3:
        path = input(".------------------------------------------------------------.\n|                     ASS Default batch                      |\n|         Quel est le chemin d'accès de tes fichiers ?       |\n'------------------------------------------------------------' \n\nAppuyez sur q pour quitter le programme. \n\nVotre entrée : ")
        if path == "q":
            exit()
        os.chdir(path)
        path_corrceted = path+"/Style_corrigés"
        if not os.path.exists(path_corrceted):
            os.mkdir(path_corrceted)
        change_file_to_crunchyroll_change_without_redimension()
    if choice == 4:
        path = input(".------------------------------------------------------------.\n|                     ASS Default batch                      |\n|         Quel est le chemin d'accès de tes fichiers ?       |\n'------------------------------------------------------------' \n\nAppuyez sur q pour quitter le programme. \n\nVotre entrée : ")
        if path == "q":
            exit()
        os.chdir(path)
        path_corrceted = path+"/Style_corrigés"
        if not os.path.exists(path_corrceted):
            os.mkdir(path_corrceted)
        change_for_pysubs2()
    if choice == 5:
        exit()
    fin_de_programme()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)