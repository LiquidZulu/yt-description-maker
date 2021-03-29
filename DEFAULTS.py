URLS = [
    'https://youtu.be/', 
    'https://soundcloud.com/'
]

YT   = 0
SC   = 1

UNKNOWN_ARTIST        = 0
ARTIST_SONG_DELIMITER = '-'

URL_KEYS = {

    UNKNOWN_ARTIST: {

        '/pol/ anthem':
            URLS[YT] + 'RhQtjOK5Qzs',

        'God, Syria and Bashar!':
            URLS[YT] + 'BQ5ax8im3Ow'
    },

    'Gunnar Olsen': {
        'Cold Rise':
            URLS[YT] + '_W9wX04sShQ'
    },

    'Tailed Feature': {

        'Show Me Your Pizza':
            URLS[SC] + 'user-416632402/show-me-your-pizza-cover-with-vocals'
    },

    'Hyper': {

        'Spoiler':
            URLS[SC] + 'hyper/hyper-spoiler'
    },

    'JVH-C': {

        'Heads Will Roll':
            URLS[SC] + 'jvh-c/a-trak-versionyeah-yeah-yeahs-heads-will-roll-jvh-c-remix'
    },

    'Depeche Mode': {

        'Just Can\'t Get Enough':
            URLS[YT] + '_6FBfAQ-NDE'
    },

    'John Williams': {

        'Duel Of The Fates':
            URLS[YT] + 'ZTg6hg1miFg',

        'Schindlers List':
            URLS[YT] + 'YqVRcFQagtI'
    },

    'Frédéric Chopin': {

        'Raindrop Prelude, Op 28, No. 15':
            URLS[YT] + '6OFHXmiZP38'
    },

    'Gary Glitter (Nonce)': {

        'Rock & Roll Part II':
            URLS[YT] + 'bW-OLcZ4tGY'
    },

    'Martin O\'Donnell & Michael Salvatori': {

        'Halo: OST':
            URLS[YT] + 'JSpK8LxBKqQ'
    },

    'Bulent Aydin': {

        'I BABA':
            URLS[YT] + 'mKg07CMQfaA'
    },

    'Jacovot': {

        'Sneak A Peak Remix':
            URLS[SC] + 'user880712462/sneak-a-peak-remix'
    },

    'Yugo Kanno': {

        'Golden Wind: Overture - Giorno\'s Theme "Il vento d\'oro"':
            URLS[YT] + '2MtOpB5LlUA'
    },

    'Greg Guevara (Jreg)': {

        'Office Life':
            URLS[YT] + 'QTZ4PhPX2NY'
    },

    'Kane Hambly': {

        'Ket Donk':
            URLS[YT] + 'NSTx31dxmgA'
    },

    'Lifeformed': {

        'Frozen Hot Sauce (Fastfall - Dustforce OST)':
            URLS[YT] + 'FxJXn1dOwGA'
    },

    'Live Without': {

        'Ordinary Life':
            URLS[YT] + 'YIjjyDFhLZM'
    },

    'Gary Jules': {

        'Mad World':
            URLS[YT] + '0Jo73WL3lgY'
    },

    'Marty Robbins': {

        'Big Iron':
            URLS[YT] + 'zzICMIu5zFY'
    },

    'Maryanne Amacher': {

        'Chorale':
            URLS[YT] + 'nAXlF0n5XAg'
    },

    'Jessye Norman, Wiener Philharmoniker, Herbert von Karajan': {

        '"Mild und leise wie er lächelt" (Isoldes Liebestod)':
            URLS[YT] + '9680zhMmIqM'
    },

    'Hans Zimmer & Lorne Balfe': {

        'Call of Duty: Modern Warfare 2 OST':
            URLS[YT] + 'Qsp3Z25u6VI-o'
    },

    'Dunderpatrullen': {

        'Övningsköra Remix':
            URLS[YT] + 'xu2OmBbOo0s'
    },

    'Praxi': {

        'Synthwave':
            URLS[SC] + 'praxior/praxi-synthwave'
    },

    'Radiohead': {

        'Exit Music':
            URLS[YT] + 'qCLPlqeWWqI',

        'Creep':
            URLS[YT] + 'XFkzRNyygfk',

        'No Surprises':
            URLS[YT] + 'u5CVsCnxyXg'
    },

    'Tony Bennett': {

        'Rags To Riches':
            URLS[YT] + 'Y22tIJ6toPY'
    },

    'Righeira': {

        'No Tengo Dinero':
            URLS[YT] + 'kwxIGe1oOJQ'
    },

    'NORTHMANE': {

        'Sandy Freak':
            URLS[YT] + 'CjMGDBDDvCY'
    },

    'Sky Wikluh': {

        'Pazi Sta Radis':
            URLS[YT] + 'O8mGkct3oys'
    },

    'Tessa Violet': {

        'Bored':
            URLS[YT] + 'tsPxaAVg584'
    },

    'Ween': {

        'Ocean Man':
            URLS[YT] + 'tkzY_VwNIek'
    },
}


def get_song(a: int or str, s: str):

    if a == UNKNOWN_ARTIST:
        return [
            f'UNKNOWN_ARTIST {ARTIST_SONG_DELIMITER} {s}', 
            URL_KEYS[a][s]
        ]

    return [
        f'{a} {ARTIST_SONG_DELIMITER} {s}', 
        URL_KEYS[a][s]
    ]


def get_songs(*args):
    
    songs = [args[0]]

    for song in args[1]:
        songs.append(get_song(song[0], song[1]))
    
    songs.append(args[2])
    return songs