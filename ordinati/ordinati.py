import click
from .commands import ordinati_add
from .commands import ordinati_show
from .commands import ordinati_remove
from .commands import ordinati_tag
from .commands import ordinati_update
from .commands import ordinati_verify

@click.group()
def cli():

    '''Offline bookmark management command line tool'''

    pass
    
cli.add_command(ordinati_add.add)
cli.add_command(ordinati_show.show)
cli.add_command(ordinati_remove.remove)
cli.add_command(ordinati_tag.tag)
cli.add_command(ordinati_update.update)
cli.add_command(ordinati_verify.verify)