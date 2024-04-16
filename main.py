#region CONSTRUCTOR
from ascii_magic import AsciiArt
import os
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

with open('./other/trad.json', 'r', encoding='utf-8') as file:
    traductions = json.load(file)
#endregion CONSTRUCTOR

#region FUNCTIONS
def oneShelter(lang):
    chemin_dossier = os.path.expanduser("~") + "\\AppData\\Local\\FalloutShelter"
    fichiers_vault = [f for f in os.listdir(chemin_dossier) if f.startswith("Vault") and f.endswith(".sav")]

    if fichiers_vault:
        fichier_a_telecharger = os.path.join(chemin_dossier, fichiers_vault[0])
        driver = webdriver.Chrome()
        driver.get("https://falloutsheltervisualize.tsukizo.fr/")
        input_file = driver.find_element(By.ID, 'sav_file')
        input_file.send_keys(fichier_a_telecharger)
        input("\n" +  traductions[lang]["remerciement"])
    else:
        print("\n" + traductions[lang]["sauvegardePasTrouver"])

def twoShelter(lang):
    chemin_dossier = os.path.expanduser("~") + "\\AppData\\Local\\FalloutShelter"
    choix2 = input(traductions[lang]["choix2"])
    
    if choix2 == "1":
        fichiers_vault = [f for f in os.listdir(chemin_dossier) if f.startswith("Vault1") and f.endswith(".sav")]
        if fichiers_vault:
            fichier_a_telecharger = os.path.join(chemin_dossier, fichiers_vault[0])
            driver = webdriver.Chrome()
            driver.get("https://falloutsheltervisualize.tsukizo.fr/")
            input_file = driver.find_element(By.ID, 'sav_file')
            input_file.send_keys(fichier_a_telecharger)
            input(traductions[lang]["remerciement"])
        else:
            print(traductions[lang]["sauvegardePasTrouver"])
    elif choix2 == "2":
        fichiers_vault = [f for f in os.listdir(chemin_dossier) if f.startswith("Vault2") and f.endswith(".sav")]
        if fichiers_vault:
            fichier_a_telecharger = os.path.join(chemin_dossier, fichiers_vault[0])
            driver = webdriver.Chrome()
            driver.get("https://falloutsheltervisualize.tsukizo.fr/")
            input_file = driver.find_element(By.ID, 'sav_file')
            input_file.send_keys(fichier_a_telecharger)
            input(traductions[lang]["remerciement"])
        else:
            print(traductions[lang]["sauvegardePasTrouver"])
    else:
        print(traductions[lang]["erreurTape"])

def threeShelter(lang):
    chemin_dossier = os.path.expanduser("~") + "\\AppData\\Local\\FalloutShelter"
    choix3 = input(traductions[lang]["choix3"])

    if choix3 == "1":
        fichiers_vault = [f for f in os.listdir(chemin_dossier) if f.startswith("Vault1") and f.endswith(".sav")]
        if fichiers_vault:
            fichier_a_telecharger = os.path.join(chemin_dossier, fichiers_vault[0])
            driver = webdriver.Chrome()
            driver.get("https://falloutsheltervisualize.tsukizo.fr/")
            input_file = driver.find_element(By.ID, 'sav_file')
            input_file.send_keys(fichier_a_telecharger)
            input(traductions[lang]["remerciement"])
        else:
            print(traductions[lang]["sauvegardePasTrouver"])
    elif choix3 == "2":
        fichiers_vault = [f for f in os.listdir(chemin_dossier) if f.startswith("Vault2") and f.endswith(".sav")]
        if fichiers_vault:
            fichier_a_telecharger = os.path.join(chemin_dossier, fichiers_vault[0])
            driver = webdriver.Chrome()
            driver.get("https://falloutsheltervisualize.tsukizo.fr/")
            input_file = driver.find_element(By.ID, 'sav_file')
            input_file.send_keys(fichier_a_telecharger)
            input(traductions[lang]["remerciement"])
        else:
            print(traductions[lang]["sauvegardePasTrouver"])       
    elif choix3 == "3":
        fichiers_vault = [f for f in os.listdir(chemin_dossier) if f.startswith("Vault3") and f.endswith(".sav")]
        if fichiers_vault:
            fichier_a_telecharger = os.path.join(chemin_dossier, fichiers_vault[0])
            driver = webdriver.Chrome()
            driver.get("https://falloutsheltervisualize.tsukizo.fr/")
            input_file = driver.find_element(By.ID, 'sav_file')
            input_file.send_keys(fichier_a_telecharger)
            input(traductions[lang]["remerciement"])
        else:
            print(traductions[lang]["sauvegardePasTrouver"])
    else:
        print(traductions[lang]["erreurTape"])
#endregion FUNCTION

#region IMAGE
my_art = AsciiArt.from_image('./other/nukoutboy.png')
my_output = my_art.to_ascii(columns=50)
print(my_output)
#endregion IMAGE

#region ABRI
language = input("Écrivez pour choisir la langue | Write to choose language \n\n > FR \n > AN")

if language == 'FR' or "fr":
    abri = input("Combien avez vous d'abri ?")
    if abri == "1":
        oneShelter("FR")
    elif abri == "2":
        twoShelter("FR")
    elif abri == "3":
        twoShelter("FR")
    else:
        print("Le nombre est invalide. Il y a seulement 3 abris disponibles dans Fallout Shelter.")
        
elif language == 'AN' or "an":
    abri = input("How many shelters do you have?")
    if abri == "1":
        oneShelter("AN")
    elif abri == "2":
        twoShelter("AN")
    elif abri == "3":
        twoShelter("AN")
    else:
        print("The number is invalid. There are only 3 shelters available in Fallout Shelter.")     
else: 
    print("Vous n'avez pas choisi la langue en l'ecrivant, fermeture du terminal | You did not choose the language when writing it, closing the terminal")    
#endregion ABRI