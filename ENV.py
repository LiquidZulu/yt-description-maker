from DEFAULTS import *

PLAINTEXT = 0
FORMATTED = 0b0000_0001
DEFAULTS  = 0b0000_0010
ALL       = 0xff

TYPE    = 0
TITLE   = 1
NICK    = 2
NAME_Q  = 3
TIME_Q  = 4
DEFLIST = 5

CAT_ARR_DATA = 0
CAT_ARR_TIME = 1

PLAINTEXT_TEXT = 1

DEFLIST_TITLE = 0

DESCRIPTION_DELIMITER    = '-'
CUSTOM_DEFAULT_DELIMITER = ','



ENV = [

    [
        FORMATTED,
        '\n\n\n\n-- Chapters --\n\n',
        'Chapter',
        'Enter the name of the chapter:\n',
        'Enter the time that this chapter begins:\n'
    ],

    [
        FORMATTED | DEFAULTS,
        '\n\n\n\n-- Music (in order of appearance --\n\n',
        'Song',
        'Enter the title of the song:\n',
        'Enter the time that this song begins:\n',
        [
            'Which song is it?\n',
            get_song(UNKNOWN_ARTIST, 'God, Syria and Bashar!'),
            get_song('Gunnar Olsen', 'Cold Rise'),
            get_song('Tailed Feature', 'Show Me Your Pizza'),
            get_song('Hyper', 'Spoiler'),
            get_song('JVH-C', 'Heads Will Roll'),
            get_song('Depeche Mode', 'Just Can\'t Get Enough'),
            get_song('John Williams', 'Duel Of The Fates'),
            get_song('Frédéric Chopin', 'Raindrop Prelude, Op 28, No. 15'),
            get_song('Gary Glitter (Nonce)', 'Rock & Roll Part II'),
            get_song('Martin O\'Donnell & Michael Salvatori', 'Halo: OST'),
            get_song('Bulent Aydin', 'I BABA'),
            get_song('Jacovot', 'Sneak A Peak Remix'),
            get_song('Yugo Kanno', 'Golden Wind: Overture - Giorno\'s Theme "Il vento d\'oro"'),
            get_song('Greg Guevara (Jreg)', 'Office Life'),
            get_song('Kane Hambly', 'Ket Donk'),
            get_song('Lifeformed', 'Frozen Hot Sauce (Fastfall - Dustforce OST)'),
            get_song('Live Without', 'Ordinary Life'),
            get_song('Gary Jules', 'Mad World'),
            get_song('Marty Robbins', 'Big Iron'),
            get_song('Maryanne Amacher', 'Chorale'),
            get_song('Jessye Norman, Wiener Philharmoniker, Herbert von Karajan', '"Mild und leise wie er lächelt" (Isoldes Liebestod)'),
            get_song('Hans Zimmer & Lorne Balfe', 'Call of Duty: Modern Warfare 2 OST'),
            get_song('Dunderpatrullen', 'Övningsköra Remix'),
            get_song(UNKNOWN_ARTIST, '/pol/ anthem'),
            get_song('Praxi', 'Synthwave'),
            get_song('Radiohead', 'Exit Music'),
            get_song('Radiohead', 'Creep'),
            get_song('Radiohead', 'No Surprises'),
            get_song('Tony Bennett', 'Rags To Riches'),
            get_song('Righeira', 'No Tengo Dinero'),
            get_song('NORTHMANE', 'Sandy Freak'),
            get_song('John Williams', 'Schindlers List'),
            get_song('Sky Wikluh', 'Pazi Sta Radis'),
            get_song('Tessa Violet', 'Bored'),
            get_song('Ween', 'Ocean Man'),
            f'Please insert all details about the song in question split by {CUSTOM_DEFAULT_DELIMITER}. For example; mary{CUSTOM_DEFAULT_DELIMITER}mary\'s social media{CUSTOM_DEFAULT_DELIMITER}also she likes lambs => "mary {DESCRIPTION_DELIMITER} mary\'s social media {DESCRIPTION_DELIMITER} also she likes lambs":\n'
        ]
    ],

    [
        FORMATTED | DEFAULTS,
        '\n\n\n\n-- People (in order of appearance --\n\n',
        'Person',
        'Enter the name of this person:\n',
        'Enter the time that this person first appears:\n',
        [
            'Who is it?\n',
            ['Scrappy', 'https://www.youtube.com/channel/UCZhKcWfYk3RVdYfsoJ7JpCA'],
            ['Campbell', 'https://www.youtube.com/channel/UCJNXGXyttBzWWnvqlgyP25g'],
            ['EternalSalt', 'https://www.twitch.tv/EternalSalt'],
            ['Joe', '\'ah i dont need no links, dw bout it\''],
            ['Daniel', 'https://www.youtube.com/channel/UC3kEl0PpjrfsYHIgvxD6yZA'],
            ['Miller', 'IDK'],
            f'Please insert all details about the person in question split by {CUSTOM_DEFAULT_DELIMITER}. For example; mary{CUSTOM_DEFAULT_DELIMITER}mary\'s social media{CUSTOM_DEFAULT_DELIMITER}also she likes lambs => "mary {DESCRIPTION_DELIMITER} mary\'s social media {DESCRIPTION_DELIMITER} also she likes lambs":\n'
        ]
    ],

    [
        PLAINTEXT,
        '\n\n\n\n-- Social media links --\n\nhttp://liquidzulu.xyz\nhttps://discord.gg/VY4XYrR\nhttps://github.com/LiquidZulu/\nhttps://soundcloud.com/liquidzulu\nhttps://gab.com/LiquidZulu\nhttps://twitter.com/LiquidZulu'
    ],

    [
        PLAINTEXT,
        '\n\n\n****************\n\n\n - https://github.com/LiquidZulu/yt-description-maker -'
    ]
]