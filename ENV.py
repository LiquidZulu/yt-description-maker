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
        get_songs(
            'Which song is it?\n', 
            [
                [UNKNOWN_ARTIST, 'God, Syria and Bashar!'],
                ['Gunnar Olsen', 'Cold Rise'],
                ['Tailed Feature', 'Show Me Your Pizza'],
                ['Hyper', 'Spoiler'],
                ['JVH-C', 'Heads Will Roll'],
                ['Depeche Mode', 'Just Can\'t Get Enough'],
                ['John Williams', 'Duel Of The Fates'],
                ['Frédéric Chopin', 'Raindrop Prelude, Op 28, No. 15'],
                ['Gary Glitter (Nonce)', 'Rock & Roll Part II'],
                ['Martin O\'Donnell & Michael Salvatori', 'Halo: OST'],
                ['Bulent Aydin', 'I BABA'],
                ['Jacovot', 'Sneak A Peak Remix'],
                ['Yugo Kanno', 'Golden Wind: Overture - Giorno\'s Theme "Il vento d\'oro"'],
                ['Greg Guevara (Jreg)', 'Office Life'],
                ['Kane Hambly', 'Ket Donk'],
                ['Lifeformed', 'Frozen Hot Sauce (Fastfall - Dustforce OST)'],
                ['Live Without', 'Ordinary Life'],
                ['Gary Jules', 'Mad World'],
                ['Marty Robbins', 'Big Iron'],
                ['Maryanne Amacher', 'Chorale'],
                ['Jessye Norman, Wiener Philharmoniker, Herbert von Karajan', '"Mild und leise wie er lächelt" (Isoldes Liebestod)'],
                ['Hans Zimmer & Lorne Balfe', 'Call of Duty: Modern Warfare 2 OST'],
                ['Dunderpatrullen', 'Övningsköra Remix'],
                [UNKNOWN_ARTIST, '/pol/ anthem'],
                ['Praxi', 'Synthwave'],
                ['Radiohead', 'Exit Music'],
                ['Radiohead', 'Creep'],
                ['Radiohead', 'No Surprises'],
                ['Tony Bennett', 'Rags To Riches'],
                ['Righeira', 'No Tengo Dinero'],
                ['NORTHMANE', 'Sandy Freak'],
                ['John Williams', 'Schindlers List'],
                ['Sky Wikluh', 'Pazi Sta Radis'],
                ['Tessa Violet', 'Bored'],
                ['Ween', 'Ocean Man'],
                ['$atori Zoom', 'BUSTER']
            ],
            f'Please insert all details about the song in question split by {CUSTOM_DEFAULT_DELIMITER}. For example; mary{CUSTOM_DEFAULT_DELIMITER}mary\'s social media{CUSTOM_DEFAULT_DELIMITER}also she likes lambs => "mary {DESCRIPTION_DELIMITER} mary\'s social media {DESCRIPTION_DELIMITER} also she likes lambs":\n'
        )
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