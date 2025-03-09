from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
app.secret_key = "une_clé_secrète_très_sécurisée"   # Nécessaire pour Flask-WTF

tableaux = [
    {"id": 1, "titre": "MOON PA", "image": "1111-01 - copie 2.jpg", "description": "120 x 150."},
    {"id": 2, "titre": "PATCH-WOk", "image": "1111-02.jpg", "description": "120 x 140."},
    {"id": 3, "titre": "DON'T", "image": "AMATUNE1.jpg", "description": "100 x 120."},
    {"id": 4, "titre": "RAW-BEAT", "image": "B-1.jpg", "description": "120 x 140."},
    {"id": 5, "titre": "BIG BUG", "image": "BIG BUG - copie.jpg", "description": "120 x 140."},
    {"id": 6, "titre": "RAW-BEAT 2", "image": "C-2.jpg", "description": "120 x 150." },
    {"id": 7, "titre": "CALAVERA", "image": "Calavera fleurs.jpg", "description": "120 x 150."},
    {"id": 8, "titre": "YEAH !", "image": "D-1.jpg", "description": "120 x 150."},
    {"id": 9, "titre": "DISCO MUERTE", "image": "DISCO MUERTE gonflée.jpg", "description": "120 x 140."},
    {"id": 10, "titre": "BASQUIAT", "image": "DSC02125.JPG", "description": "120 x 150."},
    {"id": 11, "titre": "IN VITRO", "image": "DSCF1401 - copie 2.jpg", "description": "120 x 120."},
    {"id": 12, "titre": "BOYS BAND", "image": "E.jpg", "description": "120 x 140." },
    {"id": 13, "titre": "RAW-BEAT 3", "image": "e.Raw-Beat.jpg", "description": "120 x 90."},
    {"id": 14, "titre": "FULL", "image": "F.jpg", "description": "120 x 140."},
    {"id": 15, "titre": "ROCK", "image": "G.jpg", "description": "120 x 140."},
    {"id": 16, "titre": "MODERN", "image": "H.jpg", "description": "90 x 120."},
    {"id": 17, "titre": "DEAD SURFER", "image": "IMG_5010.jpg", "description": "200 x 70." },
    {"id": 18, "titre": "KALASCH", "image": "IMG_5016.JPG", "description": "120 x 140."},
    {"id": 19, "titre": "RAW-BEAT 4", "image": "IMG_5160 17-57-59.JPG", "description": "120 x 120." },
    {"id": 20, "titre": "STUPID", "image": "IMG_8842.jpg", "description": "120 x 150."},
    {"id": 21, "titre": "BLOODY MARY", "image": "IMG_9972.JPG", "description": "120 x 100."},
    {"id": 22, "titre": "OLD SKULL", "image": "OLD SKULL.jpg", "description": "120 x 150."},
    {"id": 23, "titre": "RAW-BEAT 5", "image": "R917-1.jpg", "description": "120 x 150."},
    {"id": 24, "titre": "RED SKULL", "image": "RED SKULL.jpg", "description": "120 x 150." },
    {"id": 25, "titre": "PROUT !", "image": "Rémy710-4.jpg", "description": "100 x 140." },
    {"id": 26, "titre": "DINSKY", "image": "Rémy710-6.jpg", "description": "120 x 120."},
    {"id": 27, "titre": "CRASH", "image": "CRASH.jpg", "description": "120 x 120."},
    {"id": 28, "titre": "BIG", "image": "1111-08.jpg", "description": "120 x 90."},
    {"id": 29, "titre": "MAC", "image": "1111-09.jpg", "description": "120 x 90."},
]

masques = [
    {"id": 1, "titre": "Mask 1", "image": "IMG_0128.jpg", "description": "Mask 1."},
    {"id": 2, "titre": "Mask 2", "image": "IMG_0132.jpg", "description": "Mask 2."},
    {"id": 3, "titre": "Mask 3", "image": "IMG_0138.jpg", "description": "Mask 3."},
    {"id": 4, "titre": "Mask 4", "image": "IMG_0140.jpg", "description": "Mask 4."},
    {"id": 5, "titre": "Mask 5", "image": "IMG_0135.jpg", "description": "Mask 5."},
    {"id": 6, "titre": "Mask 6", "image": "IMG_0177.jpg", "description": "Mask 6."},
    {"id": 7, "titre": "Mask 7", "image": "IMG_0180.jpg", "description": "Mask 7."},
    {"id": 8, "titre": "Mask 8", "image": "IMG_0185.jpg", "description": "Mask 8."},
    {"id": 9, "titre": "Mask 9", "image": "IMG_0188.jpg", "description": "Mask 9."},
    {"id": 10, "titre": "Mask 10", "image": "IMG_0191.jpg", "description": "Mask 10."},
    {"id": 11, "titre": "Mask 11", "image": "IMG_0194.jpg", "description": "Mask 11."},
    {"id": 12, "titre": "Mask 12", "image": "IMG_0244.jpg", "description": "Mask 12."},
    {"id": 13, "titre": "Mask 13", "image": "IMG_0245.jpg", "description": "Mask 13."},
    {"id": 14, "titre": "Mask 14", "image": "IMG_1285.jpg", "description": "Mask 14."},
    {"id": 15, "titre": "Mask 15", "image": "IMG_1286.jpg", "description": "Mask 15."},
    {"id": 16, "titre": "Mask 16", "image": "IMG_1288.jpg", "description": "Mask 16."},
    {"id": 17, "titre": "Mask 17", "image": "IMG_1290.jpg", "description": "Mask 17."},
    {"id": 18, "titre": "Mask 18", "image": "IMG_1296.jpg", "description": "Mask 18."},
    {"id": 19, "titre": "Mask 19", "image": "IMG_1300.JPG", "description": "Mask 19."},
    {"id": 20, "titre": "Mask 20", "image": "IMG_6337.JPG", "description": "Mask 20."},
    {"id": 21, "titre": "Mask 21", "image": "IMG_6355.jpg", "description": "Mask 21."},
    {"id": 22, "titre": "Mask 22", "image": "IMG_6362.jpg", "description": "Mask 22."},
    {"id": 23, "titre": "Mask 23", "image": "IMG_6370.jpg", "description": "Mask 23."},
    {"id": 24, "titre": "Mask 24", "image": "IMG_6377.jpg", "description": "Mask 24."},
    {"id": 25, "titre": "Mask 25", "image": "IMG_6385.jpg", "description": "Mask 25."},
    {"id": 26, "titre": "Mask 26", "image": "IMG_6389.jpg", "description": "Mask 26."},
    {"id": 27, "titre": "Mask 27", "image": "IMG_6397.jpg", "description": "Mask 27."},
    {"id": 28, "titre": "Mask 28", "image": "IMG_6405.jpg", "description": "Mask 28."},
    {"id": 29, "titre": "Mask 29", "image": "IMG_6408.jpg", "description": "Mask 29."},
    {"id": 30, "titre": "Mask 30", "image": "IMG_6416.jpg", "description": "Mask 30."},
    {"id": 31, "titre": "Mask 31", "image": "IMG_6421.jpg", "description": "Mask 31."},
    {"id": 32, "titre": "Mask 32", "image": "IMG_6427.jpg", "description": "Mask 32."},
    {"id": 33, "titre": "Mask 33", "image": "IMG_6431.jpg", "description": "Mask 33."},
    {"id": 34, "titre": "Mask 34", "image": "IMG_6439.jpg", "description": "Mask 34."},
    {"id": 35, "titre": "Mask 35", "image": "IMG_6445.jpg", "description": "Mask 35."},
    {"id": 36, "titre": "Mask 36", "image": "IMG_6447.jpg", "description": "Mask 36."},
    {"id": 37, "titre": "Mask 37", "image": "IMG_6456.jpg", "description": "Mask 37."},
    {"id": 38, "titre": "Mask 38", "image": "PHOTO-2024-01-09-22-32-39-1.jpg", "description": "Mask 38."},
    {"id": 39, "titre": "Mask 39", "image": "PHOTO-2024-01-09-22-32-39-5.jpg", "description": "Mask 39."},
    {"id": 40, "titre": "Mask 40", "image": "PHOTO-2024-01-09-22-32-43-5.jpg", "description": "Mask 40."},
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
    {"id": 3, "titre": "Masks", "image": "IMG_0128.jpg", "description": "Masks"},
    {"id": 4, "titre": "Metals", "image": "12.jpg", "description": "Metals"},
    {"id": 5, "titre": "Motograff", "image": "IMG_5053.JPG", "description": "Motograff"},
]
    return render_template("sculptures.html", sculptures=sculptures)


@app.route('/fusos.html')
def fusos():
    fusos = [
        {"id": 1, "titre": "Fuso", "image": "colonne-01.jpg", "description": "Fuso."},
        {"id": 2, "titre": "Fuso", "image": "colonne-02.jpg", "description": "Fuso."},
        {"id": 3, "titre": "Fuso", "image": "colonne-03.jpg", "description": "Fuso."},
        {"id": 4, "titre": "Fuso", "image": "colonne-04.jpg", "description": "Fuso."},
        {"id": 5, "titre": "Fuso", "image": "colonne-05.jpg", "description": "Fuso."},
        {"id": 6, "titre": "Fuso", "image": "colonne-08.jpg", "description": "Fuso."},
        {"id": 7, "titre": "Fuso", "image": "IMG_3213.jpg", "description": "Fuso."},
        {"id": 8, "titre": "Fuso", "image": "JQLA8209.jpg", "description": "Fuso."},
    ]

    return render_template('fusos.html', fusos=fusos)




@app.route('/monsters.html')
def monsters():
    monsters = [
        {"id": 1, "titre": "Mr Bobo", "image": "911B-10.jpg", "description": "Mr Bobo."},
        {"id": 2, "titre": "Mr Bobo", "image": "Rémy911B-04.jpg", "description": "Mr Bobo."},
        {"id": 3, "titre": "Mr Bobo", "image": "Rémy911B-01.jpg", "description": "Mr Bobo."},
        {"id": 4, "titre": "Groumph", "image": "Colys2012-24_A4_300DPI_RVB.jpg", "description": "Groumph."},
        {"id": 5, "titre": "Groumph", "image": "Colys2012-25.jpg", "description": "Monster 5."},
        {"id": 6, "titre": "Gniap", "image": "Colys2012-28.jpg", "description": "Gniap."},
        {"id": 7, "titre": "Gniap", "image": "GNAP!- copie.jpg", "description": "Gniap."},
        {"id": 8, "titre": "Grrr 1", "image": "GRRR! 1- copie.jpg", "description": "Grrr 1."},
        {"id": 9, "titre": "Grrr 1", "image": "Colys2012-18.jpg", "description": "Grrr 1."},
        {"id": 10, "titre": "Grrr 2", "image": "GRRR! 2 - copie.jpg", "description": "Grrr 2."},
        {"id": 11, "titre": "Gnnn-Gnnn", "image": "IMG_1165.JPG", "description": "Gnnn-Gnnn."},
        {"id": 12, "titre": "Gnork", "image": "IMG_9909.JPG", "description": "Gnork."},
        {"id": 13, "titre": "Scorpatte", "image": "Colys2012-32.jpg", "description": "Scorpatte."},
        {"id": 14, "titre": "Family Monster", "image": "DSC_0231.JPG", "description": "Family Monster."},
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
        {"id": 1, "titre": "Metal 1", "image": "12.jpg", "description": "Metal 1."},
        {"id": 2, "titre": "Metal 2", "image": "18.jpg", "description": "Metal 2."},
        {"id": 3, "titre": "Metal 3", "image": "J.jpg", "description": "Metal 3."},
        {"id": 4, "titre": "Metal 4", "image": "J-2.jpg", "description": "Metal 4."},
        {"id": 5, "titre": "Metal 5", "image": "DSC00760.JPG", "description": "Metal 5."},
        {"id": 6, "titre": "Metal 6", "image": "IMG_2675.jpg", "description": "Metal 6."},
        {"id": 7, "titre": "Metal 7", "image": "IMG_2677.JPG", "description": "Metal 7."},
        {"id": 8, "titre": "Metal 8", "image": "DSC00764.JPG", "description": "Metal 8."},
        {"id": 9, "titre": "Metal 9", "image": "DSC00765.JPG", "description": "Metal 9."},
        {"id": 10, "titre": "Metal 10", "image": "27.jpg", "description": "Metal 10."},
        {"id": 11, "titre": "Metal 11", "image": "37.jpg", "description": "Metal 11."},
        {"id": 12, "titre": "Metal 12", "image": "DSC01054.JPG", "description": "Metal 12."},
        {"id": 13, "titre": "Metal 13", "image": "RP_0502B.JPG", "description": "Metal 13."},
        {"id": 14, "titre": "Metal 14", "image": "RP_0502E.JPG", "description": "Metal 14."},
        {"id": 15, "titre": "Metal 15", "image": "Sculpture-3.jpg", "description": "Metal 15."},
        {"id": 16, "titre": "Metal 16", "image": "DSC00771.JPG", "description": "Metal 16."},
    ]

    return render_template('creations.html', creations=creations)




@app.route('/bikes.html')
def bikes():
    bikes = [
        {"id": 1, "titre": "Motograff 1", "image": "IMG_5053.JPG", "description": "Motograff 1."},
        {"id": 2, "titre": "Motograff 1", "image": "IMG_5059.jpg", "description": "Motograff 1."},
        {"id": 3, "titre": "Motograff 2", "image": "IMG_5485.JPG", "description": "Motograff 2."},
        {"id": 4, "titre": "Motograff 2", "image": "IMG_5488.JPG", "description": "Motograff 2."},
        {"id": 5, "titre": "Motograff 2", "image": "IMG_5496.jpg", "description": "Motograff 2."},
        {"id": 6, "titre": "Motograff 2", "image": "PHOTO-2024-01-08-21-08-01.jpg", "description": "Motograff 2."},
    ]

    return render_template('bikes.html', bikes=bikes)




@app.route('/furnitures.html')
def furnitures():
    furnitures = [
        {"id": 1, "titre": "Furniture ", "image": "Armoire métal.jpeg", "description": "Furniture."},
        {"id": 2, "titre": "Furniture ", "image": "Chaise métal.jpeg", "description": "Furniture."},
        {"id": 3, "titre": "Furniture ", "image": "DSC00126.JPG", "description": "Furniture."},
        {"id": 4, "titre": "Furniture ", "image": "Photo REMY 012.jpg", "description": "Furniture."},
        {"id": 5, "titre": "Furniture ", "image": "DSC00031.JPG", "description": "Furniture."},
        {"id": 6, "titre": "Furniture ", "image": "Photo REMY 004.jpg", "description": "Furniture."},
        {"id": 7, "titre": "Furniture ", "image": "Photo REMY 013.jpg", "description": "Furniture."},
        {"id": 8, "titre": "Furniture ", "image": "Rémy911-03 - copie.jpg", "description": "Furniture."},
        {"id": 9, "titre": "Furniture ", "image": "Rémy911-04.jpg", "description": "Furniture."},
        {"id": 10, "titre": "Furniture ", "image": "Rémy911-6.jpg", "description": "Furniture."},
        {"id": 11, "titre": "Furniture ", "image": "Rémy911-7.jpg", "description": "Furniture."},
        {"id": 12, "titre": "Furniture ", "image": "Rémy911-8.jpg", "description": "Furniture."},
        {"id": 13, "titre": "Furniture ", "image": "Rémy911-9.jpg", "description": "Furniture."},
    ]

    return render_template('furnitures.html', furnitures=furnitures)




@app.route('/motos.html')
def motos():
    motos = [
        {"id": 1, "titre": "Tracto", "image": "30mars0004.jpg", "description": "Tracto."},
        {"id": 2, "titre": "Tracto", "image": "30mars0025.jpg", "description": "Tracto."},
        {"id": 3, "titre": "Tracto Red", "image": "tracto reservoir rouge.jpg", "description": "Tracto Red."},
        {"id": 4, "titre": "Sumo", "image": "EmptyName 36.jpg", "description": "Sumo."},
        {"id": 5, "titre": "Sumo", "image": "EmptyName 37a.jpg", "description": "Sumo."},
        {"id": 6, "titre": "muto", "image": "muto 1.jpg", "description": "muto."},
        {"id": 7, "titre": "muto", "image": "muto.jpg", "description": "muto."},
    ]
    return render_template('motos.html', motos=motos)






@app.route('/boutiques.html')
def boutiques():
    boutiques = [
        {"id": 1, "titre": "ILLUSTRATION", "image": "Bar L'Illustration Lille.jpeg", "description": "ILLUSTRATION."},
        {"id": 2, "titre": "IRO", "image": "Boutique IRO Lille +.jpeg", "description": "IRO."},
        {"id": 3, "titre": "OSIRIS", "image": "Boutique-OSIRIS-Douai-1.jpeg", "description": "OSIRIS."},
        {"id": 4, "titre": "ZABOU", "image": "Boutique ZABOU Lille 1.jpeg", "description": "ZABOU."},
        {"id": 5, "titre": "VIRUS", "image": "VIRUS boutique ARRAS 1.jpeg", "description": "VIRUS."},
    ]




    return render_template('boutiques.html', boutiques=boutiques)



@app.route('/shops.html')
def shops():
    shops = [
        {"id": 1, "titre": "ILLUSTRATION", "image": "Bar L'Illustration Lille 1.jpeg", "description": "ILLUSTRATION."},
        {"id": 2, "titre": "ILLUSTRATION", "image": "Bar L'Illustration Lille 2.jpeg", "description": "ILLUSTRATION."},
        {"id": 3, "titre": "ILLUSTRATION", "image": "Bar L'Illustration Lille.jpeg", "description": "ILLUSTRATION."},
    ]

    return render_template('shops.html', shops=shops)

@app.route('/shops2.html')
def shops2():
    shops2 = [
        {"id": 1, "titre": "IRO", "image": "Boutique IRO Lille +.jpeg", "description": "IRO."},
        {"id": 2, "titre": "IRO", "image": "Boutique IRO Lille 2.jpeg", "description": "IRO."},
    ]

    return render_template('shops2.html', shops2=shops2)

@app.route('/shops3.html')
def shops3():
    shops3 = [
        {"id": 1, "titre": "Shop 1", "image": "Boutique-OSIRIS-Douai-1.jpeg", "description": "Shop 1."},
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
        {"id": 1, "titre": "Shop 1", "image": "VIRUS boutique ARRAS 1.jpeg", "description": "Shop 1."},
        {"id": 2, "titre": "Shop 2", "image": "VIRUS boutique ARRAS 1 - copie.jpeg", "description": "Shop 2."},
        {"id": 3, "titre": "Shop 3", "image": "détails VIRUS 2.jpeg", "description": "Shop 3."},
    ]

    return render_template('shops5.html', shops5=shops5)





@app.route('/houses.html')
def houses():
    houses = [
        {"id": 1, "titre": "house 1", "image": "IMG_6532.jpg", "description": "house 1."},
        {"id": 2, "titre": "house 2", "image": "IMG_0768.jpeg", "description": "house 2."},
        {"id": 3, "titre": "house 3", "image": "IMG_0777.jpeg", "description": "house 3."},
        {"id": 4, "titre": "house 4", "image": "IMG_0715.jpeg", "description": "house 4."},
        {"id": 5, "titre": "house 5", "image": "IMG_0696.jpeg", "description": "house 5."},
        {"id": 6, "titre": "house 6", "image": "IMG_0725.jpeg", "description": "house 6."},
        {"id": 7, "titre": "house 7", "image": "HOME REMY 14.jpg", "description": "house 7."},
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
