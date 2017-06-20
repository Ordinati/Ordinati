import click
import json
import os

@click.command()
def show():
    '''Shows all currently saved bookmarks'''
    
    #Expand the '~' to the user's home directory
    with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'r') as f:
        objects = json.loads(f.read())
    
    #Display only the name and url
    for x in objects:
        click.echo('{0}:\t{1}'.format(x['name'], x['url']))