from setuptools import setup

APP = ['Laptop_System.py']
DATA_FILES = ['laptop_ids.csv']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['time', 'os', 'pickle', 'PyQt5'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['PyQt5']
)

