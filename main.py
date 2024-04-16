#region CONSTRUCTOR
from ascii_magic import AsciiArt
import os
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#endregion CONSTRUCTOR

#region FUNCTIONS
# def oneShelter():
#     chemin_dossier = os.path.expanduser("~") + "\\AppData\\Local\\FalloutShelter"
    
#     fichiers = [f for f in os.listdir(chemin_dossier) if os.path.isfile(os.path.join(chemin_dossier, f))]
#     fichiers_vault = [f for f in fichiers if f.startswith("Vault") and f.endswith(".sav")]

#     if fichiers_vault:
#         driver = webdriver.Chrome()
#         driver.get("https://falloutsheltervisualize.tsukizo.fr/")
#         time.sleep(5)
#         sav_file_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'sav_file')))
#     if sav_file_input:
#             try:
#                 sav_file_input.click() 
#                 time.sleep(60)  
#                 driver.quit()  
#             except Exception as e:
#                 print("Erreur lors du clic sur l'élément:", e)
#             else:
#                 print("L'élément 'sav_file' n'a pas été trouvé sur la page.")
#     else:
#         print("Aucun fichier Vault n'a été trouvé dans le dossier FalloutShelter.")


def oneShelter():
    # Chemin du dossier FalloutShelter
    chemin_dossier = os.path.expanduser("~") + "\\AppData\\Local\\FalloutShelter"

    # Liste des fichiers .sav commençant par "Vault"
    fichiers_vault = [f for f in os.listdir(chemin_dossier) if f.startswith("Vault") and f.endswith(".sav")]

    if fichiers_vault:
        fichier_a_telecharger = os.path.join(chemin_dossier, fichiers_vault[0])
        driver = webdriver.Chrome()
        driver.get("https://falloutsheltervisualize.tsukizo.fr/")
        input_file = driver.find_element(By.ID, 'sav_file')
        input_file.send_keys(fichier_a_telecharger)
        # time.sleep(5)
        input("Appuyez sur Entrée pour quitter...")
        # driver.quit()
    else:
        print("Aucun fichier Vault n'a été trouvé dans le dossier FalloutShelter.")


def twoShelter():
    return 0

def threeShelter():
    return 0

#endregion FUNCTION

#region IMAGE
my_art = AsciiArt.from_image('./img/nukoutboy.png')
my_output = my_art.to_ascii(columns=50)
print(my_output)
#endregion IMAGE

#region TEXTE HOME
# with open('./txt/home.txt', 'r') as file:
#     textehome = file.read()
#endregion TEXTE HOME

#region ABRI
abri = input("Combien avez vous d'abri ?")

if abri == "1":
    oneShelter()
elif abri == "2":
    print("Vous avez 2 abris.")
elif abri == "3":
    print("Vous avez 3 abris.")
else:
    print("Le nombre est invalide. Il y a seulement 3 abris disponibles dans Fallout Shelter.")
#endregion ABRI

#region QUITTER
input("Appuyez sur Entrée pour quitter...")
#endregion QUITTER