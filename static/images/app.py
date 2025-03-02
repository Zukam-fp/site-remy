from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
app.secret_key = "une_clé_secrète_très_sécurisée"   # Nécessaire pour Flask-WTF



tableaux = [
    {"id": 1, "titre": "Tableaux 1", "image": "1111-01 - copie 2.jpg", "description": "Description du tableau 1."},
    {"id": 2, "titre": "Tableaux 2", "image": "1111-02.jpg", "description": "Description du tableau 2."},
    {"id": 3, "titre": "Tableaux 3", "image": "AMATUNE1.jpg", "description": "Description du tableau 3."},
    {"id": 4, "titre": "Tableaux 4", "image": "B-1.jpg", "description": "Description du tableau 4."},
    {"id": 5, "titre": "Tableaux 5", "image": "BIG BUG - copie.jpg", "description": "Description du tableau 5."},
    {"id": 6, "titre": "Tableaux 6", "image": "C-2.jpg", "description": "Description du tableau 6." },
]


sculptures_plastic = [
    {"id": 1, "titre": "Sculpture Plastic 1", "image": "", "description": "Description de la sculpture 1."},
    {"id": 2, "titre": "Sculpture Plastic 2", "image": "", "description": "Description de la sculpture 2."},
    {"id": 3, "titre": "Sculpture Plastic 3", "image": "", "description": "Description de la sculpture 3."},
]


sculptures_metal = [
    {"id": 1, "titre": "Sculpture Metal 1", "image": "", "description": "Description de la sculpture 1."},
    {"id": 2, "titre": "Sculpture Metal 2", "image": "", "description": "Description de la sculpture 2."},
    {"id": 3, "titre": "Sculpture Metal 3", "image": "", "description": "Description de la sculpture 3."},
]

designs_furniture = [
    {"id": 1, "titre": "Design Furniture 1", "image": "design_furniture1.jpg", "description": "Description du design 1."},
    {"id": 2, "titre": "Design Furniture 2", "image": "design_furniture2.jpg", "description": "Description du design 2."},
    {"id": 3, "titre": "Design Furniture 3", "image": "design_furniture3.jpg", "description": "Description du design 3."},
]

designs_bike = [
    {"id": 1, "titre": "Design bike 1", "image": "design_bike1.jpg", "description": "Description du design 1."},
    {"id": 2, "titre": "Design bike 2", "image": "design_bike2.jpg", "description": "Description du design 2."},
    {"id": 3, "titre": "Design bike 3", "image": "design_bike3.jpg", "description": "Description du design 3."},
]

archis_shop = [
    {"id": 1, "titre": "Archi Shop 1", "image": "archi_shop1.jpg", "description": "Description du shop 1."},
    {"id": 2, "titre": "Archi Shop 2", "image": "archi_shop2.jpg", "description": "Description du shop 2."},
    {"id": 3, "titre": "Archi Shop 3", "image": "archi_shop3.jpg", "description": "Description du shop 3."},
]

archis_house = [
    {"id": 1, "titre": "Archi House 1", "image": "archi_house1.jpg", "description": "Description de la house 1."},
    {"id": 2, "titre": "Archi House 2", "image": "archi_house2.jpg", "description": "Description de la house 2."},
    {"id": 3, "titre": "Archi House 3", "image": "archi_house3.jpg", "description": "Description de la house 3."},
]

# Page d'accueil
@app.route("/")
def accueil():
    return render_template("index.html")



# Page Tableaux
@app.route("/tableaux")
def tableaux_view():
    return render_template("tableaux.html", tableaux=tableaux)


# Page détaillée d'un tableau
@app.route("/tableau.html/<int:tableau_id>")
def tableau(tableau_id):
    # Trouver le tableau correspondant dans la liste
    tableau = next((tableau for tableau in tableaux if tableau["id"] == tableau_id), None)
    if tableau:
        return render_template("tableau.html", tableau=tableau)
    else:
        return "Tableau non trouvée", 404

# Page sculpture plastic
@app.route("/sculptures_plastic")
def sculptures_plastic_view():
    return render_template("sculptures_plastic.html", sculptures_plastic=sculptures_plastic)


# Page détaillée d'une sculpture_plastic
@app.route("/sculpture_plastic.html/<int:sculpture_plastic_id>")
def sculpture_plastic(sculpture_plastic_id):
    # Trouver le sculpture_plastic correspondant dans la liste
    sculpture_plastic = next((sculpture_plastic for sculpture_plastic in sculptures_plastic if sculpture_plastic["id"] == sculpture_plastic_id), None)
    if sculpture_plastic:
        return render_template("sculpture_plastic.html", sculpture_plastic=sculpture_plastic)
    else:
        return "sculpture_plastic non trouvée", 404


# Page sculpture metal
@app.route("/sculptures_metal")
def sculptures_metal_view():
    return render_template("sculptures_metal.html", sculptures_metal=sculptures_metal)


# Page détaillée d'une sculpture_metal
@app.route("/sculpture_metal.html/<int:sculpture_metal_id>")
def sculpture_metal(sculpture_metal_id):
    # Trouver le sculpture_metal correspondant dans la liste
    sculpture_metal = next((sculpture_metal for sculpture_metal in sculptures_metal if sculpture_metal["id"] == sculpture_metal_id), None)
    if sculpture_metal:
        return render_template("sculpture_metal.html", sculpture_metal=sculpture_metal)
    else:
        return "sculpture_metal non trouvée", 404


# Page designs furniture
@app.route("/designs_furniture")
def designs_furniture_view():
    return render_template("designs_furniture.html", designs_furniture=designs_furniture)


# Page détaillée d'une design_furniture
@app.route("/design_furniture.html/<int:design_furniture_id>")
def design_furniture(design_furniture_id):
    # Trouver le design_furniture correspondant dans la liste
    design_furniture = next((design_furniture for design_furniture in designs_furniture if design_furniture["id"] == design_furniture_id), None)
    if design_furniture:
        return render_template("design_furniture.html", design_furniture=design_furniture)
    else:
        return "design_furniture non trouvée", 404


# Page designs bike
@app.route("/designs_bike")
def designs_bike_view():
    return render_template("designs_bike.html", designs_bike=designs_bike)


# Page détaillée d'une design_bike
@app.route("/design_bike.html/<int:design_bike_id>")
def design_bike(design_bike_id):
    # Trouver le design_bike correspondant dans la liste
    design_bike = next((design_bike for design_bike in designs_bike if design_bike["id"] == design_bike_id), None)
    if design_bike:
        return render_template("design_bike.html", design_bike=design_bike)
    else:
        return "design_bike non trouvée", 404


# Page archis shop
@app.route("/archis_shop")
def archis_shop_view():
    return render_template("archis_shop.html", archis_shop=archis_shop)


# Page détaillée d'une archi_shop
@app.route("/archi_shop.html/<int:archi_shop_id>")
def archi_shop(archi_shop_id):
    # Trouver le archi_shop correspondant dans la liste
    archi_shop = next((archi_shop for archi_shop in archis_shop if archi_shop["id"] == archi_shop_id), None)
    if archi_shop:
        return render_template("archi_shop.html", archi_shop=archi_shop)
    else:
        return "archi_shop non trouvée", 404


# Page archis house
@app.route("/archis_house")
def archis_house_view():
    return render_template("archis_house.html", archis_house=archis_house)


# Page détaillée d'une archi_house
@app.route("/archi_house.html/<int:archi_house_id>")
def archi_house(archi_house_id):
    # Trouver le archi_house correspondant dans la liste
    archi_house = next((archi_house for archi_house in archis_house if archi_house["id"] == archi_house_id), None)
    if archi_house:
        return render_template("archi_house.html", archi_house=archi_house)
    else:
        return "archi_house non trouvée", 404


# Page news
@app.route("/news")
def news():
    return render_template("news.html")

# Page Contact
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
