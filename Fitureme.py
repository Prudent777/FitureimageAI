from PIL import Image, ImageDraw
import random

# Créer une image vierge de 800x800 pixels
img = Image.new("RGB", (800, 800), "black")

# Créer un objet ImageDraw pour dessiner sur l'image
draw = ImageDraw.Draw(img)

# Dessiner des formes aléatoires sur l'image
for i in range(20):
    x1 = random.randint(0, 800)
    y1 = random.randint(0, 800)
    x2 = random.randint(0, 800)
    y2 = random.randint(0, 800)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.line((x1, y1, x2, y2), fill=color, width=3)
    draw.rectangle((x1, y1, x2, y2), outline=color, width=3)

# Enregistrer l'image générée
img.save("image_futuriste.png")