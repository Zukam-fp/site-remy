import secrets
from flask import Flask, render_template, request, abort, send_from_directory
import os
from dotenv import load_dotenv
load_dotenv()
import logging
from logging.handlers import RotatingFileHandler
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect
from flask_sitemap import Sitemap
from datetime import datetime



app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', os.urandom(24))
app.config.update(
    SECRET_KEY=os.environ.get('FLASK_SECRET_KEY'),
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=3600,
    DEBUG=os.environ.get('FLASK_DEBUG', 'False') == 'False'
)
app.config['SERVER_NAME'] = 'www.remypagart.com'
app.config.update({
    'SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS': True,
    'SITEMAP_URL_SCHEME': 'https',
    'SITEMAP_IGNORE_ENDPOINTS': ['static']
})


sitemap = Sitemap()
sitemap.init_app(app)


csp = {
    'default-src': "'self'",
    'img-src': "'self' data: www.remypagart.com",
    'style-src': [
        "'self'",
        "'unsafe-inline'",
        "https://fonts.googleapis.com",
    ],
    'font-src': [
        "'self'",
        "https://fonts.gstatic.com",
    ],
    'script-src': [
        "'self'",
        "'unsafe-inline'",
        "https://kit.fontawesome.com",
    ],
    'connect-src': "'self'",
    'frame-src': "'none'",
    'base-uri': "'self'"
}


talisman = Talisman(
    app,
    content_security_policy=csp,
    force_https=True,
    strict_transport_security=True
)
csrf = CSRFProtect(app)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)



@app.before_request
def enforce_https_and_www():
    if app.debug or request.path.startswith('/static/'):
        return

    proto = request.headers.get('X-Forwarded-Proto', 'http')
    host = request.host.split(':')[0]

    # Redirection HTTPS
    if proto == 'http':
        return redirect(request.url.replace('http://', 'https://', 1), 301

    # Redirection www
    if host == 'remypagart.com':
        return redirect(f'https://www.remypagart.com{request.full_path}', 301)




tableaux = [
    {"id": 1, "titre": "RAW BEAT", "image": "b-1.jpg", "description": "120 x 150."},
    {"id": 2, "titre": "BIG BUG", "image": "big-bug-copie.jpg", "description": "120 x 140."},
    {"id": 3, "titre": "RAW BEAT 2", "image": "c-2.jpg", "description": "100 x 120."},
    {"id": 4, "titre": "RAW-BEAT 3", "image": "e.Raw-Beat.jpg", "description": "120 x 140."},
    {"id": 5, "titre": "RAW BEAT 4", "image": "img_5160-17-57-59.jpg", "description": "120 x 140."},
    {"id": 6, "titre": "RAW-BEAT 5", "image": "r917-1.jpg", "description": "120 x 150." },
    {"id": 7, "titre": "CALAVERA", "image": "calavera-fleurs.jpg", "description": "120 x 150."},
    {"id": 8, "titre": "DISCO MUERTE", "image": "disco-muerte-gonflée.jpg", "description": "120 x 150."},
    {"id": 9, "titre": "OLD SKULL", "image": "old-skull.jpg", "description": "120 x 140."},
    {"id": 10, "titre": "RED SKULL", "image": "red-skull.jpg", "description": "120 x 150."},
    {"id": 11, "titre": "FULL", "image": "f.jpg", "description": "120 x 120."},
    {"id": 12, "titre": "DEAD SURFER", "image": "img_5010.jpg", "description": "120 x 140." },
    {"id": 13, "titre": "MOON PA", "image": "1111-01-copie2.jpg", "description": "120 x 90."},
    {"id": 14, "titre": "PATCH-WOK", "image": "1111-02.jpg", "description": "120 x 140."},
    {"id": 15, "titre": "BOYS BAND", "image": "e.jpg", "description": "120 x 140."},
    {"id": 16, "titre": "YEAH !", "image": "d-1.jpg", "description": "90 x 120."},
    {"id": 17, "titre": "DON'T", "image": "amatune2.jpg", "description": "200 x 70." },
    {"id": 18, "titre": "ROCK !", "image": "g.jpg", "description": "120 x 140."},
    {"id": 19, "titre": "STUPID", "image": "img_8842.jpg", "description": "120 x 120." },
    {"id": 20, "titre": "BASQUIAT", "image": "dsc02125.jpg", "description": "120 x 150."},
    {"id": 21, "titre": "CRASH", "image": "crash.jpg", "description": "120 x 100."},
    {"id": 22, "titre": "IN VITRO", "image": "dscf1401-copie2.jpg", "description": "120 x 150."},
    {"id": 23, "titre": "MODERN", "image": "h.jpg", "description": "120 x 150."},
    {"id": 24, "titre": "KALASCH", "image": "img_5016.jpg", "description": "120 x 150." },
    {"id": 25, "titre": "BLOODY MARY", "image": "img_9972.jpg", "description": "100 x 140." },
    {"id": 26, "titre": "PROUT !", "image": "remy710-4.jpg", "description": "120 x 120."},
    {"id": 27, "titre": "DINSKY", "image": "remy710-6.jpg", "description": "120 x 120."},
    {"id": 28, "titre": "BIG", "image": "1111-08.jpg", "description": "120 x 90."},
    {"id": 29, "titre": "MAC", "image": "1111-09.jpg", "description": "120 x 90."},
    {"id": 30, "titre": "SHOW", "image": "1111-11-copie2.jpg", "description": ""},
    {"id": 31, "titre": "SHOW", "image": "amatune.jpg", "description": ""},
    {"id": 32, "titre": "SHOW", "image": "img_8840-copie.jpg", "description": ""},
    {"id": 33, "titre": "SHOW", "image": "img_8810-copie2.jpg", "description": ""},
]

masques = [
    {"id": 1, "titre": "Mask 1", "image": "img_0128.jpg", "description": "Mask 1."},
    {"id": 2, "titre": "Mask 2", "image": "img_0132.jpg", "description": "Mask 2."},
    {"id": 3, "titre": "Mask 3", "image": "img_0138.jpg", "description": "Mask 3."},
    {"id": 4, "titre": "Mask 4", "image": "img_0140.jpg", "description": "Mask 4."},
    {"id": 5, "titre": "Mask 5", "image": "img_0135.jpg", "description": "Mask 5."},
    {"id": 6, "titre": "Mask 6", "image": "img_0177.jpg", "description": "Mask 6."},
    {"id": 7, "titre": "Mask 7", "image": "img_0180.jpg", "description": "Mask 7."},
    {"id": 8, "titre": "Mask 8", "image": "img_0185.jpg", "description": "Mask 8."},
    {"id": 9, "titre": "Mask 9", "image": "img_0188.jpg", "description": "Mask 9."},
    {"id": 10, "titre": "Mask 10", "image": "img_0191.jpg", "description": "Mask 10."},
    {"id": 11, "titre": "Mask 11", "image": "img_0194.jpg", "description": "Mask 11."},
    {"id": 12, "titre": "Mask 12", "image": "img_0244.jpg", "description": "Mask 12."},
    {"id": 13, "titre": "Mask 13", "image": "img_0245.jpg", "description": "Mask 13."},
    {"id": 14, "titre": "Mask 14", "image": "img_1285.jpg", "description": "Mask 14."},
    {"id": 15, "titre": "Mask 15", "image": "img_1286.jpg", "description": "Mask 15."},
    {"id": 16, "titre": "Mask 16", "image": "img_1288.jpg", "description": "Mask 16."},
    {"id": 17, "titre": "Mask 17", "image": "img_1290.jpg", "description": "Mask 17."},
    {"id": 18, "titre": "Mask 18", "image": "img_1296.jpg", "description": "Mask 18."},
    {"id": 19, "titre": "Mask 19", "image": "img_1300.jpg", "description": "Mask 19."},
    {"id": 20, "titre": "Mask 20", "image": "photo-2024-01-09-22-32-43-5.jpg", "description": "Mask 20."},
    {"id": 21, "titre": "Mask 21", "image": "img_6355.jpg", "description": "Mask 21."},
    {"id": 22, "titre": "Mask 22", "image": "img_6362.jpg", "description": "Mask 22."},
    {"id": 23, "titre": "Mask 23", "image": "img_6370.jpg", "description": "Mask 23."},
    {"id": 24, "titre": "Mask 24", "image": "img_6377.jpg", "description": "Mask 24."},
    {"id": 25, "titre": "Mask 25", "image": "img_6385.jpg", "description": "Mask 25."},
    {"id": 26, "titre": "Mask 26", "image": "img_6389.jpg", "description": "Mask 26."},
    {"id": 27, "titre": "Mask 27", "image": "img_6397.jpg", "description": "Mask 27."},
    {"id": 28, "titre": "Mask 28", "image": "img_6405.jpg", "description": "Mask 28."},
    {"id": 29, "titre": "Mask 29", "image": "img_6408.jpg", "description": "Mask 29."},
    {"id": 30, "titre": "Mask 30", "image": "img_6416.jpg", "description": "Mask 30."},
    {"id": 31, "titre": "Mask 31", "image": "img_6421.jpg", "description": "Mask 31."},
    {"id": 32, "titre": "Mask 32", "image": "img_6427.jpg", "description": "Mask 32."},
    {"id": 33, "titre": "Mask 33", "image": "img_6431.jpg", "description": "Mask 33."},
    {"id": 34, "titre": "Mask 34", "image": "img_6439.jpg", "description": "Mask 34."},
    {"id": 35, "titre": "Mask 35", "image": "img_6445.jpg", "description": "Mask 35."},
    {"id": 36, "titre": "Mask 36", "image": "img_6447.jpg", "description": "Mask 36."},
    {"id": 37, "titre": "Mask 37", "image": "img_6456.jpg", "description": "Mask 37."},
    {"id": 38, "titre": "Mask 38", "image": "photo-2024-01-09-22-32-39-1.jpg", "description": "Mask 38."},
    {"id": 39, "titre": "Mask 39", "image": "photo-2024-01-09-22-32-39-5.jpg", "description": "Mask 39."},
    {"id": 40, "titre": "Mask 40", "image": "img_6337.jpg", "description": "Mask 40."},
]


@app.route('/static/<path:filename>')
@limiter.exempt
def custom_static(filename):
    if '..' in filename or filename.startswith('/'):
        app.logger.warning(f'Tentative d\'accès non autorisé à {filename}')
        abort(404)
    return send_from_directory(app.static_folder, filename)



@app.route("/")
@limiter.limit("100/hour")
def accueil():
    return render_template("index.html")




@app.route("/tableaux")
def tableaux_view():
    return render_template("tableaux.html", tableaux=tableaux)



@app.route("/tableau/<int:tableau_id>")
@limiter.limit("50/hour")
def tableau(tableau_id):
    tableau = next((tableau for tableau in tableaux if tableau["id"] == tableau_id), None)
    if tableau:
        current_index = tableaux.index(tableau)


        prev_index = current_index - 1 if current_index > 0 else len(tableaux) - 1
        next_index = current_index + 1 if current_index < len(tableaux) - 1 else 0


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


@app.route("/sculptures")
@limiter.limit("50/hour")
def sculptures_view():
    sculptures = [
    {"id": 1, "titre": "Fusos", "image": "colonne-01.jpg", "description": "Fusos"},
    {"id": 2, "titre": "Monsters", "image": "911b-10.jpg", "description": "Monsters"},
    {"id": 3, "titre": "Masks", "image": "img_0138.jpg", "description": "Masks"},
    {"id": 4, "titre": "Metals", "image": "12.jpg", "description": "Metals"},
    {"id": 5, "titre": "Motograff", "image": "img_5053.jpg", "description": "Motograff"},
]
    return render_template("sculptures.html", sculptures=sculptures)


@app.route('/fusos')
@limiter.limit("50/hour")
def fusos():
    fusos = [
        {"id": 1, "titre": "Fuso", "image": "colonne-01.jpg", "description": "Fuso."},
        {"id": 2, "titre": "Fuso", "image": "colonne-10.jpg", "description": "Fuso."},
        {"id": 3, "titre": "Fuso", "image": "colonne-02.jpg", "description": "Fuso."},
        {"id": 4, "titre": "Fuso", "image": "colonne-08.jpg", "description": "Fuso."},
        {"id": 5, "titre": "Fuso", "image": "colonne-04.jpg", "description": "Fuso."},
        {"id": 6, "titre": "Fuso", "image": "colonne-05.jpg", "description": "Fuso."},
        {"id": 7, "titre": "Fuso", "image": "colonne-03.jpg", "description": "Fuso."},
        {"id": 8, "titre": "Fuso", "image": "colonne-09.jpg", "description": "Fuso."},
    ]

    return render_template('fusos.html', fusos=fusos)




@app.route('/monsters')
@limiter.limit("50/hour")
def monsters():
    monsters = [
        {"id": 1, "titre": "Mr Bobo", "image": "mrbobo2.jpg", "description": "Mr Bobo."},
        {"id": 2, "titre": "Mr Bobo", "image": "mrbobo.jpg", "description": "Mr Bobo."},
        {"id": 3, "titre": "Mr Bobo", "image": "mrbobo-et-remy.jpg", "description": "Mr Bobo."},
        {"id": 4, "titre": "Groumph", "image": "groumph.jpg", "description": "Groumph."},
        {"id": 5, "titre": "Groumph", "image": "groumph2.jpg", "description": "Monster 5."},
        {"id": 6, "titre": "Gniap", "image": "gnap2.jpg", "description": "Gniap."},
        {"id": 7, "titre": "Gniap", "image": "gnap.jpg", "description": "Gniap."},
        {"id": 8, "titre": "Grrr 1", "image": "grrr2.jpg", "description": "Grrr 1."},
        {"id": 9, "titre": "Grrr 1", "image": "grrr.jpg", "description": "Grrr 1."},
        {"id": 10, "titre": "Grrr 2", "image": "grrr3.jpg", "description": "Grrr 2."},
        {"id": 11, "titre": "Gnnn-Gnnn", "image": "gnn.JPG", "description": "Gnnn-Gnnn."},
        {"id": 12, "titre": "Gnork", "image": "gronk.JPG", "description": "Gnork."},
        {"id": 13, "titre": "Scorpatte", "image": "scorpatte.jpg", "description": "Scorpatte."},
        {"id": 14, "titre": "Family Monster", "image": "family-monster.JPG", "description": "Family Monster."},
    ]

    return render_template('monsters.html', monsters=monsters)



@app.route('/masques')
@limiter.limit("50/hour")
def masques_view():
    return render_template('masques.html', masques=masques)


@app.route("/masque/<int:masque_id>")
@limiter.limit("50/hour")
def masque(masque_id):

    masque = next((masque for masque in masques if masque["id"] == masque_id), None)
    if masque:
        current_index = masques.index(masque)


        prev_index = current_index - 1 if current_index > 0 else len(masques) - 1
        next_index = current_index + 1 if current_index < len(masques) - 1 else 0


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


@app.route('/creations')
@limiter.limit("50/hour")
def creations():
    creations = [
        {"id": 1, "titre": "Metal 1", "image": "12.jpg", "description": "Metal 1."},
        {"id": 2, "titre": "Metal 2", "image": "18.jpg", "description": "Metal 2."},
        {"id": 3, "titre": "Metal 3", "image": "j.jpg", "description": "Metal 3."},
        {"id": 4, "titre": "Metal 3", "image": "j-2.jpg", "description": "Metal 3."},
        {"id": 5, "titre": "Metal 3", "image": "dsc00760.jpg", "description": "Metal 3."},
        {"id": 6, "titre": "Metal 4", "image": "img_2675.jpg", "description": "Metal 4."},
        {"id": 7, "titre": "Metal 4", "image": "img_2677.jpg", "description": "Metal 4."},
        {"id": 8, "titre": "Metal 5", "image": "dsc00764.jpg", "description": "Metal 5."},
        {"id": 9, "titre": "Metal 5", "image": "dsc00765.jpg", "description": "Metal 5."},
        {"id": 10, "titre": "Metal 6", "image": "27.jpg", "description": "Metal 6."},
        {"id": 11, "titre": "Metal 6", "image": "37.jpg", "description": "Metal 6."},
        {"id": 12, "titre": "Metal 7", "image": "dsc01054.jpg", "description": "Metal 7."},
        {"id": 13, "titre": "Metal 8", "image": "rp_0502b.jpg", "description": "Metal 8."},
        {"id": 14, "titre": "Metal 8", "image": "rp_0502e.jpg", "description": "Metal 8."},
        {"id": 15, "titre": "Metal 9", "image": "sculpture-3.jpg", "description": "Metal 9."},
        {"id": 16, "titre": "Metal 10", "image": "dsc00771.jpg", "description": "Metal 10."},
    ]

    return render_template('creations.html', creations=creations)




@app.route('/bikes')
@limiter.limit("50/hour")
def bikes():
    bikes = [
        {"id": 1, "titre": "Motograff 1", "image": "img_5053.jpg", "description": "Motograff 1."},
        {"id": 2, "titre": "Motograff 1", "image": "img_5059.jpg", "description": "Motograff 1."},
        {"id": 3, "titre": "Motograff 2", "image": "img_5485.jpg", "description": "Motograff 2."},
        {"id": 4, "titre": "Motograff 2", "image": "img_5488.jpg", "description": "Motograff 2."},
        {"id": 5, "titre": "Motograff 2", "image": "img_5496.jpg", "description": "Motograff 2."},
        {"id": 6, "titre": "Motograff 2", "image": "photo-2024-01-08-21-08-01.jpg", "description": "Motograff 2."},
    ]

    return render_template('bikes.html', bikes=bikes)




@app.route('/furnitures')
@limiter.limit("50/hour")
def furnitures():
    furnitures = [
        {"id": 1, "titre": "Furniture ", "image": "armoire-metal.jpeg", "description": "Furniture."},
        {"id": 2, "titre": "Furniture ", "image": "chaise-metal.jpeg", "description": "Furniture."},
        {"id": 3, "titre": "Furniture ", "image": "chaise-metal2.JPG", "description": "Furniture."},
        {"id": 4, "titre": "Furniture ", "image": "chaise-metal3.jpg", "description": "Furniture."},
        {"id": 5, "titre": "Furniture ", "image": "fauteuil-peluche.jpg", "description": "Furniture."},
        {"id": 6, "titre": "Furniture ", "image": "fauteuil-peluche2.jpg", "description": "Furniture."},
        {"id": 7, "titre": "Furniture ", "image": "luminaire.jpg", "description": "Furniture."},
        {"id": 8, "titre": "Furniture ", "image": "luminaire2.jpg", "description": "Furniture."},
        {"id": 9, "titre": "Furniture ", "image": "luminaire3.jpg", "description": "Furniture."},
        {"id": 10, "titre": "Furniture ", "image": "chaise-moto2.jpg", "description": "Furniture."},
        {"id": 11, "titre": "Furniture ", "image": "chaise-moto.jpg", "description": "Furniture."},
        {"id": 12, "titre": "Furniture ", "image": "chaise-moto4.jpg", "description": "Furniture."},
        {"id": 13, "titre": "Furniture ", "image": "chaise-moto3.jpg", "description": "Furniture."},
    ]

    return render_template('furnitures.html', furnitures=furnitures)




@app.route('/motos')
@limiter.limit("50/hour")
def motos():
    motos = [
        {"id": 1, "titre": "Tracto", "image": "tracto.jpg", "description": "Tracto."},
        {"id": 2, "titre": "Tracto", "image": "tracto2.jpg", "description": "Tracto."},
        {"id": 3, "titre": "Tracto Red", "image": "tracto-rouge.jpg", "description": "Tracto Red."},
        {"id": 4, "titre": "Sumo", "image": "sumo.jpg", "description": "Sumo."},
        {"id": 5, "titre": "Sumo", "image": "sumo2.jpg", "description": "Sumo."},
        {"id": 6, "titre": "muto", "image": "muto.jpg", "description": "muto."},
        {"id": 7, "titre": "muto", "image": "muto2.jpg", "description": "muto."},
    ]
    return render_template('motos.html', motos=motos)






@app.route('/boutiques')
@limiter.limit("50/hour")
def boutiques():
    boutiques = [
        {"id": 1, "titre": "ILLUSTRATION", "image": "illustration3.jpeg", "description": "ILLUSTRATION."},
        {"id": 2, "titre": "IRO", "image": "iro.jpeg", "description": "IRO."},
        {"id": 3, "titre": "OSIRIS", "image": "osiris1.jpeg", "description": "OSIRIS."},
        {"id": 4, "titre": "ZABOU", "image": "zabou.jpeg", "description": "ZABOU."},
        {"id": 5, "titre": "VIRUS", "image": "virus.jpeg", "description": "VIRUS."},
    ]




    return render_template('boutiques.html', boutiques=boutiques)



@app.route('/shops')
@limiter.limit("50/hour")
def shops():
    shops = [
        {"id": 1, "titre": "ILLUSTRATION", "image": "illustration.jpeg", "description": "ILLUSTRATION."},
        {"id": 2, "titre": "ILLUSTRATION", "image": "illustration2.jpeg", "description": "ILLUSTRATION."},
        {"id": 3, "titre": "ILLUSTRATION", "image": "illustration3.jpeg", "description": "ILLUSTRATION."},
    ]

    return render_template('shops.html', shops=shops)

@app.route('/shops2')
@limiter.limit("50/hour")
def shops2():
    shops2 = [
        {"id": 1, "titre": "IRO", "image": "iro.jpeg", "description": "IRO."},
        {"id": 2, "titre": "IRO", "image": "iro2.jpeg", "description": "IRO."},
    ]

    return render_template('shops2.html', shops2=shops2)

@app.route('/shops3')
@limiter.limit("50/hour")
def shops3():

    shops3 = [
        {"id": 1, "titre": "OSIRIS", "image": "osiris1.jpeg", "description": "OSIRIS."},
        {"id": 2, "titre": "OSIRIS", "image": "osiris2.jpeg", "description": "OSIRIS."},
        {"id": 3, "titre": "OSIRIS", "image": "osiris3.jpeg", "description": "OSIRIS."},
        {"id": 4, "titre": "OSIRIS", "image": "osiris4.jpeg", "description": "OSIRIS."},
    ]

    return render_template('shops3.html', shops3=shops3)


@app.route('/shops4')
@limiter.limit("50/hour")
def shops4():
    shops4 = [
        {"id": 1, "titre": "ZABOU", "image": "zabou.jpeg", "description": "ZABOU."},
        {"id": 2, "titre": "ZABOU", "image": "zabou2.jpeg", "description": "ZABOU."},
        {"id": 3, "titre": "ZABOU", "image": "zabou3.jpeg", "description": "ZABOU."},
        {"id": 4, "titre": "ZABOU", "image": "zabou4.jpeg", "description": "ZABOU."},
    ]

    return render_template('shops4.html', shops4=shops4)


@app.route('/shops5')
@limiter.limit("50/hour")
def shops5():
    shops5 = [
        {"id": 1, "titre": "VIRUS", "image": "virus.jpeg", "description": "VIRUS."},
        {"id": 2, "titre": "VIRUS", "image": "virus2.jpeg", "description": "VIRUS."},
        {"id": 3, "titre": "VIRUS", "image": "virus3.jpeg", "description": "VIRUS."},
    ]

    return render_template('shops5.html', shops5=shops5)





@app.route('/houses')
@limiter.limit("50/hour")
def houses():
    houses = [
        {"id": 1, "titre": "Façade", "image": "facade.jpg", "description": "Façade."},
        {"id": 2, "titre": "Entrée", "image": "entre.jpeg", "description": "Engtrée."},
        {"id": 3, "titre": "Salon", "image": "salon.jpeg", "description": "Salon."},
        {"id": 4, "titre": "Salon", "image": "salon2.jpeg", "description": "Salon."},
        {"id": 5, "titre": "Salon", "image": "salon3.jpeg", "description": "Salon."},
        {"id": 6, "titre": "Patio jour", "image": "patio-jour.jpeg", "description": "Patio jour."},
        {"id": 7, "titre": "Patio nuit", "image": "patio-nuit.jpg", "description": "Patio nuit."},
    ]

    return render_template('houses.html', houses=houses)





# Page news
@app.route("/news")
@limiter.limit("50/hour")
def news():
    return render_template("news.html")

# Page Contact
@app.route("/contact")
@limiter.limit("50/hour")
def contact():
    return render_template("contact.html")

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')



# Génération du sitemap
@sitemap.register_generator
def generate_sitemap():
    endpoints = [
        ('accueil', {}),
        ('tableaux_view', {}),
        ('sculptures_view', {}),
        ('fusos', {}),
        ('monsters', {}),
        ('masques_view', {}),
        ('creations', {}),
        ('bikes', {}),
        ('furnitures', {}),
        ('motos', {}),
        ('boutiques', {}),
        ('shops', {}),
        ('shops2', {}),
        ('shops3', {}),
        ('shops4', {}),
        ('shops5', {}),
        ('houses', {}),
        ('news', {}),
        ('contact', {})
    ]

    for endpoint, params in endpoints:
        yield endpoint, params

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
