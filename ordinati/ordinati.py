import click
from .commands import ordinati_show
from .commands import ordinati_remove

@click.group()
def cli():

    '''Offline bookmark management command line tool'''

    pass
    
cli.add_command(ordinati_show.show)
cli.add_command(ordinati_remove.remove)
