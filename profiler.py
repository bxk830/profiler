import os
import requests

r = "\033[31m"
res = "\033[0m"
b = "\033[1m"
j = "\033[33m"

os.system("clear")

x = f"""
~~~~~~~~~~~~~~~~~~~~~~~
{r}
      **  **  **   **
      **  **   ** **
      ****** V  ***
      **  **   ** **
      **  **  **   **{res} {b}v0.0.1{res}
~~~~~~~~~~~~~~~~~~~~~~-------
"""
print(x)
print(f"{j}Profiler web\n [ /upload, /admin, /config, etc... ]\nTout se trouve dans le fichier {res}({b}dirlist.txt{res})\n")


url = input(f"[{r}*{res}] Entrez une {b}url{res} pour voir si les dossiers et fichiers sont dispo : ")
print("\n")
os.system("curl -I " + url)
print("\n")
if not os.path.exists("dirlist.txt"):
    print(f"{r}Erreur : le fichier 'dirlist.txt' est pas disponible !{res}")
    sys.exit()

with open("dirlist.txt", "r") as f:
    for line in f:
        directory = line.strip()
        if directory == "":
            continue

        full_url = f"{url}/{directory}"
        print(f"Test : {full_url}")
        os.system(f"curl -I {full_url}")
print("=== Terminer. ===")