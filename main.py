import subprocess
import imageMain

while True:
    # Demandez à l'utilisateur d'entrer une commande
    input(print(ascii_image))
    command = input("Entrez une commande (ou 'exit' pour quitter) : ")

    # Vérifiez si l'utilisateur souhaite quitter
    if command.lower() == 'exit':
        print("Programme terminé.")
        break

    try:
        # Exécutez la commande en utilisant subprocess
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, encoding='utf-8')

        # Affichez la sortie de la commande
        print("Résultat de la commande :")
        print(output)
    except subprocess.CalledProcessError as e:
        # Gérez les erreurs d'exécution de la commande
        print("Erreur lors de l'exécution de la commande :")
        print(e.output)
    except Exception as e:
        # Gérez les autres erreurs
        print("Erreur :", str(e))
