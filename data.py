from flask_babel import _

_producer = _("Producer")
_mixing = _("Mixing")
_recording = _("Recording")
_mastering = _("Mastering")
_composer = _("Composer")
_player = _("Player")

ALBUMS = (
        {"artist": "aamigafea", "title": "retiro postsoviet", "year": 2023, "cover":"2bebaa181517915.651d60f42b193.jpg", "roles": [_producer]},
        {"artist": "Gabriel Altman", "title": "Samat Humae", "year": 2023, "cover":"e3a060181473401.651ca4efeed1a.jpg", "roles": [_producer]},
        {"artist": "Sadgeisha", "title": "Cliffhanger", "year": 2023, "cover":"5c4a96170371431.645cac981db8a.jpg", "roles": [_producer]},
        {"artist": "Sadgeisha & T. Pojaghi", "title": "Hands", "year": 2023, "cover":"82dadd170371705.645cad8344a5c.jpg", "roles": [_producer, _player, _mixing]},
        {"artist": "T. Pojaghi", "title": "Que buen estereo!", "year": 2023, "cover":"75f6f8170371641.645cad400c14c.jpg", "roles": [_producer, _player, _mixing, _mastering]},
        {"artist": "Emi Franji & Augusto Sinesi", "title": "Sanación", "year": 2023, "cover":"8cae80170370301.645ca8a7451be.png", "roles": [_producer]},
        {"artist": "Emily And", "title": "En Vivo en La Tangente", "year": 2023, "cover":"bdd0b3170369911.645ca7251479d.jpg", "roles": [_mixing]},
    )