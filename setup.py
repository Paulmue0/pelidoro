from setuptools import setup

APP = ['main.py']
DATA_FILES = ['icons']
OPTIONS = OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {'LSUIElement': True},
}

setup(
    app=APP,
    name="pelidoro",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
