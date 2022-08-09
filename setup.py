from setuptools import setup

APP = ['main.py']
OPTIONS = OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.png'
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
