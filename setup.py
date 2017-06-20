from setuptools import setup, find_packages

setup(
    name = 'Ordinati',
    version = '0.1.0',
    author = '''
    Chintan Soni <chintan.soni4@gmail.com>,
    Husain Zafar <husainzafar1996@gmail.com>,
    Kshitija Waghurdekar <kshiti135@gmail.com>,
    Rishika Goyal <rishika7000@gmail.com>''',
    packages = find_packages(),
    license = 'LICENSE',
    description = 'Offline bookmark management command line tool',
    long_description = open('README.md').read(),
    install_requires = [
        'Click'
    ],
    entry_points = '''
        [console_scripts]
        ordinati = ordinati.ordinati:cli
        ''',
)