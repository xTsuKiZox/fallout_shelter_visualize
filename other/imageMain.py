from PIL import Image

# Chargement de l'image
image = Image.open("../../img/nukoutboy.png")

# Convertir l'image en niveaux de gris
image_grayscale = image.convert("L")

# Définir les caractères ASCII
characters = "@%#*+=-:. "

# Redimensionner l'image pour qu'elle convienne à votre terminal
largeur, hauteur = image_grayscale.size
ratio = hauteur / largeur
nouvelle_largeur = 100
nouvelle_hauteur = int(nouvelle_largeur * ratio)
image_grayscale = image_grayscale.resize((nouvelle_largeur, nouvelle_hauteur))

# Convertir les pixels en caractères ASCII
ascii_image = ""
for pixel_value in image_grayscale.getdata():
    ascii_image += characters[int(pixel_value / 255 * (len(characters) - 1))]
