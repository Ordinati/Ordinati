import click
from .commands import ordinati_show

@click.group()
def cli():

    '''Offline bookmark management command line tool'''

    pass
    
cli.add_command(ordinati_show.show)