from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
app.secret_key = "une_clé_secrète_très_sécurisée"   # Nécessaire pour Flask-WTF

tableaux = [
    {"id": 1, "titre": "Tableau 1", "image": "1111-01 - copie 2.jpg", "description": "Description du tableau 1."},
    {"id": 2, "titre": "Tableau 2", "image": "1111-02.jpg", "description": "Description du tableau 2."},
    {"id": 3, "titre": "Tableau 3", "image": "AMATUNE1.jpg", "description": "Description du tableau 3."},
    {"id": 4, "titre": "Tableau 4", "image": "B-1.jpg", "description": "Description du tableau 4."},
    {"id": 5, "titre": "Tableau 5", "image": "BIG BUG - copie.jpg", "description": "Description du tableau 5."},
    {"id": 6, "titre": "Tableau 6", "image": "C-2.jpg", "description": "Description du tableau 6." },
    {"id": 7, "titre": "Tableau 7", "image": "Calavera fleurs.jpg", "description": "Description du tableau 7."},
    {"id": 8, "titre": "Tableau 8", "image": "D-1.jpg", "description": "Description du tableau 8."},
    {"id": 9, "titre": "Tableau 9", "image": "DISCO MUERTE gonflée.jpg", "description": "Description du tableau 9."},
    {"id": 10, "titre": "Tableau 10", "image": "DSC02125.JPG", "description": "Description du tableau 10."},
    {"id": 11, "titre": "Tableau 11", "image": "DSCF1401 - copie 2.jpg", "description": "Description du tableau 11."},
    {"id": 12, "titre": "Tableau 12", "image": "E.jpg", "description": "Description du tableau 12." },
    {"id": 13, "titre": "Tableau 13", "image": "e.Raw-Beat.jpg", "description": "Description du tableau 13."},
    {"id": 14, "titre": "Tableau 14", "image": "F.jpg", "description": "Description du tableau 14."},
    {"id": 15, "titre": "Tableau 15", "image": "G.jpg", "description": "Description du tableau 15."},
    {"id": 16, "titre": "Tableau 16", "image": "H.jpg", "description": "Description du tableau 16."},
    {"id": 17, "titre": "Tableau 17", "image": "IMG_5010.jpg", "description": "Description du tableau 17." },
    {"id": 18, "titre": "Tableau 18", "image": "IMG_5016.JPG", "description": "Description du tableau 18."},
    {"id": 19, "titre": "Tableau 19", "image": "IMG_5160 17-57-59.JPG", "description": "Description du tableau 19." },
    {"id": 20, "titre": "Tableau 20", "image": "IMG_8842.jpg", "description": "Description du tableau 20."},
    {"id": 21, "titre": "Tableau 21", "image": "IMG_9972.JPG", "description": "Description du tableau 21."},
    {"id": 22, "titre": "Tableau 22", "image": "OLD SKULL.jpg", "description": "Description du tableau 22."},
    {"id": 23, "titre": "Tableau 23", "image": "R917-1.jpg", "description": "Description du tableau 23."},
    {"id": 24, "titre": "Tableau 24", "image": "RED SKULL.jpg", "description": "Description du tableau 24." },
    {"id": 25, "titre": "Tableau 25", "image": "Rémy710-4.jpg", "description": "Description du tableau 25." },
    {"id": 26, "titre": "Tableau 26", "image": "Rémy710-6.jpg", "description": "Description du tableau 26."},
    {"id": 27, "titre": "Tableau 27", "image": "CRASH.jpg", "description": "Description du tableau 27."},
    {"id": 28, "titre": "Tableau 28", "image": "1111-08.jpg", "description": "Description du tableau 28."},
    {"id": 29, "titre": "Tableau 27", "image": "1111-09.jpg", "description": "Description du tableau 29."},
]

masques = [
    {"id": 1, "titre": "Masque 1", "image": "IMG_0128.jpg", "description": "Masque 1."},
    {"id": 2, "titre": "Masque 2", "image": "IMG_0132.jpg", "description": "Masque 2."},
    {"id": 3, "titre": "Masque 3", "image": "IMG_0138.jpg", "description": "Masque 3."},
    {"id": 4, "titre": "Masque 4", "image": "IMG_0140.jpg", "description": "Masque 4."},
    {"id": 5, "titre": "Masque 5", "image": "IMG_0135.jpg", "description": "Masque 5."},
    {"id": 6, "titre": "Masque 6", "image": "IMG_0177.jpg", "description": "Masque 6."},
    {"id": 7, "titre": "Masque 7", "image": "IMG_0180.jpg", "description": "Masque 7."},
    {"id": 8, "titre": "Masque 8", "image": "IMG_0185.jpg", "description": "Masque 8."},
    {"id": 9, "titre": "Masque 9", "image": "IMG_0188.jpg", "description": "Masque 9."},
    {"id": 10, "titre": "Masque 10", "image": "IMG_0191.jpg", "description": "Masque 10."},
    {"id": 11, "titre": "Masque 11", "image": "IMG_0194.jpg", "description": "Masque 11."},
    {"id": 12, "titre": "Masque 12", "image": "IMG_0244.jpg", "description": "Masque 12."},
    {"id": 13, "titre": "Masque 13", "image": "IMG_0245.jpg", "description": "Masque 13."},
    {"id": 14, "titre": "Masque 14", "image": "IMG_1285.jpg", "description": "Masque 14."},
    {"id": 15, "titre": "Masque 15", "image": "IMG_1286.jpg", "description": "Masque 15."},
    {"id": 16, "titre": "Masque 16", "image": "IMG_1288.jpg", "description": "Masque 16."},
    {"id": 17, "titre": "Masque 17", "image": "IMG_1290.jpg", "description": "Masque 17."},
    {"id": 18, "titre": "Masque 18", "image": "IMG_1296.jpg", "description": "Masque 18."},
    {"id": 19, "titre": "Masque 19", "image": "IMG_1300.JPG", "description": "Masque 19."},
    {"id": 20, "titre": "Masque 20", "image": "IMG_6337.JPG", "description": "Masque 20."},
    {"id": 21, "titre": "Masque 21", "image": "IMG_6355.jpg", "description": "Masque 21."},
    {"id": 22, "titre": "Masque 22", "image": "IMG_6362.jpg", "description": "Masque 22."},
    {"id": 23, "titre": "Masque 23", "image": "IMG_6370.jpg", "description": "Masque 23."},
    {"id": 24, "titre": "Masque 24", "image": "IMG_6377.jpg", "description": "Masque 24."},
    {"id": 25, "titre": "Masque 25", "image": "IMG_6385.jpg", "description": "Masque 25."},
    {"id": 26, "titre": "Masque 26", "image": "IMG_6389.jpg", "description": "Masque 26."},
    {"id": 27, "titre": "Masque 27", "image": "IMG_6397.jpg", "description": "Masque 27."},
    {"id": 28, "titre": "Masque 28", "image": "IMG_6405.jpg", "description": "Masque 28."},
    {"id": 29, "titre": "Masque 29", "image": "IMG_6408.jpg", "description": "Masque 29."},
    {"id": 30, "titre": "Masque 30", "image": "IMG_6416.jpg", "description": "Masque 30."},
    {"id": 31, "titre": "Masque 31", "image": "IMG_6421.jpg", "description": "Masque 31."},
    {"id": 32, "titre": "Masque 32", "image": "IMG_6427.jpg", "description": "Masque 32."},
    {"id": 33, "titre": "Masque 33", "image": "IMG_6431.jpg", "description": "Masque 33."},
    {"id": 34, "titre": "Masque 34", "image": "IMG_6439.jpg", "description": "Masque 34."},
    {"id": 35, "titre": "Masque 35", "image": "IMG_6445.jpg", "description": "Masque 35."},
    {"id": 36, "titre": "Masque 36", "image": "IMG_6447.jpg", "description": "Masque 36."},
    {"id": 37, "titre": "Masque 37", "image": "IMG_6456.jpg", "description": "Masque 37."},
    {"id": 38, "titre": "Masque 38", "image": "PHOTO-2024-01-09-22-32-39-1.jpg", "description": "Masque 38."},
    {"id": 39, "titre": "Masque 39", "image": "PHOTO-2024-01-09-22-32-39-5.jpg", "description": "Masque 39."},
    {"id": 40, "titre": "Masque 40", "image": "PHOTO-2024-01-09-22-32-43-5.jpg", "description": "Masque 40."},
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
    #     return render_template("tableau.html", tableau=tableau)
    # else:
    #     return "Tableau non trouvée", 404
        # Trouver l'index du tableau actuel
        current_index = tableaux.index(tableau)

        # Calculer les index des tableaux précédents et suivants
        prev_index = current_index - 1 if current_index > 0 else len(tableaux) - 1
        next_index = current_index + 1 if current_index < len(tableaux) - 1 else 0

        # Récupérer les tableaux précédents et suivants
        prev_tableau = tableaux[prev_index]
        next_tableau = tableaux[next_index]

        return render_template(
            "tableau.html",
            tableau=tableau,
            prev_tableau_id=prev_tableau["id"],
            next_tableau_id=next_tableau["id"]
        )
    else:
        return "Tableau non trouvé", 404


@app.route("/sculptures.html")
def sculptures():
    sculptures = [
    {"id": 1, "titre": "Fusos", "image": "colonne-01.jpg", "description": "Fusos"},
    {"id": 2, "titre": "Monsters", "image": "911B-10.jpg", "description": "Monsters"},
    {"id": 3, "titre": "Masques", "image": "IMG_0128.jpg", "description": "Masques"},
    {"id": 4, "titre": "Métals", "image": "12.jpg", "description": "Métals"},
    {"id": 5, "titre": "Motograff", "image": "IMG_5053.JPG", "description": "Motograff"},
]
    return render_template("sculptures.html", sculptures=sculptures)


@app.route('/fusos.html')
def fusos():
    fusos = [
        {"id": 1, "titre": "Fuso 1", "image": "colonne-01.jpg", "description": "Fuso 1."},
        {"id": 2, "titre": "Fuso 2", "image": "colonne-02.jpg", "description": "Fuso 2."},
        {"id": 3, "titre": "Fuso 3", "image": "colonne-03.jpg", "description": "Fuso 3."},
        {"id": 4, "titre": "Fuso 4", "image": "colonne-04.jpg", "description": "Fuso 4."},
        {"id": 5, "titre": "Fuso 5", "image": "colonne-05.jpg", "description": "Fuso 5."},
        {"id": 6, "titre": "Fuso 6", "image": "colonne-08.jpg", "description": "Fuso 6."},
        {"id": 7, "titre": "Fuso 7", "image": "IMG_3213.jpg", "description": "Fuso 7."},
        {"id": 8, "titre": "Fuso 8", "image": "JQLA8209.jpg", "description": "Fuso 8."},
    ]

    return render_template('fusos.html', fusos=fusos)




@app.route('/monsters.html')
def monsters():
    monsters = [
        {"id": 1, "titre": "Monster 1", "image": "911B-10.jpg", "description": "Monster 1."},
        {"id": 2, "titre": "Monster 2", "image": "Colys2012-18.jpg", "description": "Monster 2."},
        {"id": 3, "titre": "Monster 3", "image": "Colys2012-24_A4_300DPI_RVB.jpg", "description": "Monster 3."},
        {"id": 4, "titre": "Monster 4", "image": "Colys2012-25.jpg", "description": "Monster 4."},
        {"id": 5, "titre": "Monster 5", "image": "Colys2012-32.jpg", "description": "Monster 5."},
        {"id": 6, "titre": "Monster 6", "image": "DSC_0231.JPG", "description": "Monster 6."},
        {"id": 7, "titre": "Monster 7", "image": "GRRR! 2 - copie.jpg", "description": "Monster 7."},
        {"id": 8, "titre": "Monster 8", "image": "IMG_1165.JPG", "description": "Monster 8."},
        {"id": 9, "titre": "Monster 9", "image": "IMG_9909.JPG", "description": "Monster 9."},
        {"id": 10, "titre": "Monster 10", "image": "Rémy911B-01.jpg", "description": "Monster 10."},
        {"id": 11, "titre": "Monster 11", "image": "Rémy911B-04.jpg", "description": "Monster 11."},
    ]

    return render_template('monsters.html', monsters=monsters)



@app.route('/masques.html')
def masques_view():
    return render_template('masques.html', masques=masques)


@app.route("/masque.html/<int:masque_id>")
def masque(masque_id):
    # Trouver le masque correspondant dans la liste
    masque = next((masque for masque in masques if masque["id"] == masque_id), None)
    if masque:
    #     return render_template("masque.html", masque=masque)
    # else:
    #     return "masque non trouvée", 404
        # Trouver l'index du masque actuel
        current_index = masques.index(masque)

        # Calculer les index des masques précédents et suivants
        prev_index = current_index - 1 if current_index > 0 else len(masques) - 1
        next_index = current_index + 1 if current_index < len(masques) - 1 else 0

        # Récupérer les masques précédents et suivants
        prev_masque = masques[prev_index]
        next_masque = masques[next_index]

        return render_template(
            "masque.html",
            masque=masque,
            prev_masque_id=prev_masque["id"],
            next_masque_id=next_masque["id"]
        )
    else:
        return "masque non trouvé", 404


@app.route('/creations.html')
def creations():
    creations = [
        {"id": 1, "titre": "Métal 1", "image": "12.jpg", "description": "Métal 1."},
        {"id": 2, "titre": "Métal 2", "image": "18.jpg", "description": "Métal 2."},
        {"id": 3, "titre": "Métal 3", "image": "27.jpg", "description": "Métal 3."},
        {"id": 4, "titre": "Métal 4", "image": "37.jpg", "description": "Métal 4."},
        {"id": 5, "titre": "Métal 5", "image": "DSC00764.JPG", "description": "Métal 5."},
        {"id": 6, "titre": "Métal 6", "image": "DSC00760.JPG", "description": "Métal 6."},
        {"id": 7, "titre": "Métal 7", "image": "DSC00765.JPG", "description": "Métal 7."},
        {"id": 8, "titre": "Métal 8", "image": "DSC00771.JPG", "description": "Métal 8."},
        {"id": 9, "titre": "Métal 9", "image": "DSC01054.JPG", "description": "Métal 9."},
        {"id": 10, "titre": "Métal 10", "image": "IMG_2675.jpg", "description": "Métal 10."},
        {"id": 11, "titre": "Métal 11", "image": "IMG_2677.JPG", "description": "Métal 11."},
        {"id": 12, "titre": "Métal 12", "image": "J-2.jpg", "description": "Métal 13."},
        {"id": 13, "titre": "Métal 13", "image": "J.jpg", "description": "Métal 14."},
        {"id": 14, "titre": "Métal 14", "image": "RP_0502B.JPG", "description": "Métal 15."},
        {"id": 15, "titre": "Métal 15", "image": "RP_0502E.JPG", "description": "Métal 16."},
        {"id": 16, "titre": "Métal 16", "image": "Sculpture-3.jpg", "description": "Métal 17."},
    ]

    return render_template('creations.html', creations=creations)




@app.route('/bikes.html')
def bikes():
    bikes = [
        {"id": 1, "titre": "Bike 1", "image": "IMG_5053.JPG", "description": "Bike 1."},
        {"id": 2, "titre": "Bike 2", "image": "IMG_5059.jpg", "description": "Bike 2."},
        {"id": 3, "titre": "Bike 3", "image": "IMG_5485.JPG", "description": "Bike 3."},
        {"id": 4, "titre": "Bike 4", "image": "IMG_5488.JPG", "description": "Bike 4."},
        {"id": 5, "titre": "Bike 5", "image": "IMG_5496.jpg", "description": "Bike 5."},
        {"id": 6, "titre": "Bike 6", "image": "PHOTO-2024-01-08-21-08-01.jpg", "description": "Bike 6."},
    ]

    return render_template('bikes.html', bikes=bikes)




@app.route('/furnitures.html')
def furnitures():
    furnitures = [
        {"id": 1, "titre": "Furniture 1", "image": "Armoire métal.jpeg", "description": "Furniture 1."},
        {"id": 2, "titre": "Furniture 2", "image": "Chaise métal.jpeg", "description": "Furniture 2."},
    ]

    return render_template('furnitures.html', furnitures=furnitures)

@app.route('/motos.html')
def motos():
    return render_template('motos.html')






@app.route('/boutiques.html')
def boutiques():
    boutiques = [
        {"id": 1, "titre": "Boutique 1", "image": "Bar L'Illustration Lille 1.jpeg", "description": "Boutique 1."},
        {"id": 2, "titre": "Boutique 2", "image": "Boutique IRO Lille +.jpeg", "description": "Boutique 2."},
        {"id": 3, "titre": "Boutique 3", "image": "Boutique OSIRIS Douai 1.jpeg", "description": "Boutique 3."},
        {"id": 4, "titre": "Boutique 4", "image": "Boutique ZABOU Lille 1.jpeg", "description": "Boutique 4."},
        {"id": 5, "titre": "Boutique 5", "image": "détails VIRUS 2.jpeg", "description": "Boutique 5."},
    ]




    return render_template('boutiques.html', boutiques=boutiques)



@app.route('/shops.html')
def shops():
    shops = [
        {"id": 1, "titre": "Shop 1", "image": "Bar L'Illustration Lille 1.jpeg", "description": "Shop 1."},
        {"id": 2, "titre": "Shop 2", "image": "Bar L'Illustration Lille 2.jpeg", "description": "Shop 2."},
        {"id": 3, "titre": "Shop 3", "image": "Bar L'Illustration Lille.jpeg", "description": "Shop 3."},
    ]

    return render_template('shops.html', shops=shops)

@app.route('/shops2.html')
def shops2():
    shops2 = [
        {"id": 1, "titre": "Shop 1", "image": "Boutique IRO Lille +.jpeg", "description": "Shop 1."},
        {"id": 2, "titre": "Shop 2", "image": "Boutique IRO Lille 1.jpeg", "description": "Shop 2."},
        {"id": 3, "titre": "Shop 3", "image": "Boutique IRO Lille 2.jpeg", "description": "Shop 3."},
    ]

    return render_template('shops2.html', shops2=shops2)

@app.route('/shops3.html')
def shops3():
    shops3 = [
        {"id": 1, "titre": "Shop 1", "image": "Boutique OSIRIS Douai 1.jpeg", "description": "Shop 1."},
        {"id": 2, "titre": "Shop 2", "image": "Boutique OSIRIS Douai 2.jpeg", "description": "Shop 2."},
        {"id": 3, "titre": "Shop 3", "image": "Boutique OSIRIS Douai 3.jpeg", "description": "Shop 3."},
        {"id": 4, "titre": "Shop 4", "image": "Boutique OSIRIS Douai 4.jpeg", "description": "Shop 4."},
    ]

    return render_template('shops3.html', shops3=shops3)


@app.route('/shops4.html')
def shops4():
    shops4 = [
        {"id": 1, "titre": "Shop 1", "image": "Boutique ZABOU Lille 1.jpeg", "description": "Shop 1."},
        {"id": 2, "titre": "Shop 2", "image": "Boutique ZABOU Lille 2.jpeg", "description": "Shop 2."},
        {"id": 3, "titre": "Shop 3", "image": "Boutique ZABOU Lille 3.jpeg", "description": "Shop 3."},
        {"id": 4, "titre": "Shop 4", "image": "Boutique ZABOU Lille 4.jpeg", "description": "Shop 4."},
    ]

    return render_template('shops4.html', shops4=shops4)


@app.route('/shops5.html')
def shops5():
    shops5 = [
        {"id": 1, "titre": "Shop 1", "image": "détails VIRUS 2.jpeg", "description": "Shop 1."},
        {"id": 2, "titre": "Shop 2", "image": "VIRUS boutique ARRAS 1 - copie.jpeg", "description": "Shop 2."},
        {"id": 3, "titre": "Shop 3", "image": "VIRUS boutique ARRAS 1.jpeg", "description": "Shop 3."},
    ]

    return render_template('shops5.html', shops5=shops5)





@app.route('/houses.html')
def houses():
    houses = [
        {"id": 1, "titre": "house 1", "image": "HOME REMY 14.jpg", "description": "house 1."},
        {"id": 2, "titre": "house 2", "image": "IMG_0696.jpeg", "description": "house 2."},
        {"id": 3, "titre": "house 3", "image": "IMG_0715.jpeg", "description": "house 3."},
        {"id": 4, "titre": "house 4", "image": "IMG_0725.jpeg", "description": "house 4."},
        {"id": 5, "titre": "house 5", "image": "IMG_0768.jpeg", "description": "house 5."},
        {"id": 6, "titre": "house 6", "image": "IMG_0777.jpeg", "description": "house 6."},
        {"id": 7, "titre": "house 7", "image": "IMG_6532.jpg", "description": "house 7."},
    ]

    return render_template('houses.html', houses=houses)





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
