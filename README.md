# yt-description-maker
yt-description-maker is a Python 3 CLI that is used to make YouTube Descriptions

* [Customisation](#customisation)
    * [ENV Schema](#env-schema)
* [Compiling](#compiling)
    * [py2exe](#py2exe)
    * [For Windows](#for-windows)
    * [For other OS's](#for-other-os's)


# Customisation
For customisation edit ENV.py making sure to follow the schema.

Note: the ENV is [*ordinal*](https://en.wikipedia.org/wiki/Ordinal_data), each section will be printed in the order it comes up in `ENV`

## ENV Schema

```py
ENV = [

    [
        <int>TYPE,
        <str>TITLE,
        <str>NICK,
        <str>NAME_Q,
        <str>TIME_Q,
        <list>DEFLIST
    ],
    ...

    # PLAINTEXT
    [
        PLAINTEXT,
        'some plaintext to insert'
    ],
    ...

    # FORMATTED
    [
        FORMATTED,
        'Title of the section',
        'shortname for the section',
        'Enter the name of this *shortname*',
        'Enter the time that this *shortname* begins'
    ],
    ...

    # FORMATTED WITH DEFAULTS
    [
        FORMATTED | DEFAULTS,
        'Title of the section',
        'shortname for the section',
        'Enter the name of this *shortname*',
        'Enter the time that this *shortname* begins',
        DEFLIST
    ]
]
```
where `DEFLIST` is as follows:
```py
[
    <str>TITLE,
    <list>DEFAULT_VALUE,
    ...
    <list>DEFAULT_VALUE,
    <str>DEFLIST_CUSTOM_INSERT_EXPLAINER
]
```

# Compiling

## py2exe
Compilation instrutions assume you have py2exe installed, do this [here](https://pypi.org/project/py2exe/).

## For Windows
Program can be compiled for windows using `.build.win.py2exe.bat`, assuming that you have PYTHONPATH set.

## For other OS's
Running `.build.X.py2exe.py` on any OS should compile the program