from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import os, json

def check_bookmarks_file():
    if not os.path.exists(os.path.expanduser('~/.ordinati')):
        os.mkdir(os.path.expanduser('~') + '/.ordinati')
    if not os.path.isfile(os.path.expanduser('~/.ordinati/bookmarks.json')):
        f = open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'w+')
        objects = []
        json.dump(objects, f, indent=4, separators=(',', ': '))

class create_bookmarks_file_develop(develop):
    """Post-installation for development mode."""
    def run(self):
        check_bookmarks_file()
        develop.run(self)

class create_bookmarks_file_install(install):
    """Post-installation for installation mode."""
    def run(self):
        check_bookmarks_file()
        install.run(self)

setup(
    name = 'Ordinati',
    version = '0.1.0',
    author = '''
    Chintan Soni <chintan.soni4@gmail.com>,
    Husain Zafar <husainzafar1996@gmail.com>,
    Kshitija Waghurdekar <kshiti135@gmail.com>,
    Rishika Goyal <rishika7000@gmail.com>''',
    packages = find_packages(),
    license = 'AGPLv3',
    description = 'Offline bookmark management command line tool',
    url = 'https://github.com/Ordinati/Ordinati',
    keyword = 'bookmarks manager command line cli',
    long_description = open('README.md').read(),
    install_requires = [
        'Click', 'httplib2'
    ],
    entry_points = '''
        [console_scripts]
        ordinati = ordinati.ordinati:cli
        ord = ordinati.ordinati:cli
        ''',
    cmdclass={
        'develop': create_bookmarks_file_develop,
        'install': create_bookmarks_file_install,
    },

)
