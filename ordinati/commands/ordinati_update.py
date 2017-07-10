'''
Module to update bookmark information
'''
import click
import json
import os

'''
id now refers to the serial number of the bookmark
need to replace it to a 3 character key, but only
when used in all other modules
'''
@click.command()
@click.argument('source') #can be id, name or url
@click.option('-n','--name', type = click.STRING, help='Change the name of the bookmark')
@click.option('-u','--url', type = click.STRING, help='Change the url of the bookmark')
def update(source, name, url):

    '''Update bookmark name or url'''

    #Expand the '~' to the user's home directory
    with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'r') as f:
        bookmarks = json.loads(f.read())

    if not source.isdecimal():
        source = source.lower()
    
    '''Identify the id of bookmark'''
    bid = -1
    for bookmark in bookmarks:
        if bookmark['name'].lower() == source:
            bid = bookmark['id']
        if bookmark['url'].lower() == source:
            bid = bookmark['id']
        if source.isdecimal() and bookmark['id'] == int(source):
            bid = bookmark['id']
    if bid >= 0:
        click.echo('Bookmark identified with name {0}'.format(bookmarks[bid]['name']))
        if name:
            name = name.lower()
            bookmarks[bid]['name'] = name
            click.echo('Name changed to {0}'.format(bookmarks[bid]['name']))
        if url:
            url = url.lower()
            bookmarks[bid]['url'] = url
            click.echo('Url changed to {0}'.format(bookmarks[bid]['url']))

    '''Dump the bookmarks back to the JSON file'''
    with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'w') as f:
        json.dump(bookmarks, f, indent=4, separators=(',',': '))
