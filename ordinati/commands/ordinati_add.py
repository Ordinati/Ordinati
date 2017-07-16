import click
import json
import time
import os

@click.command()
@click.argument('name')
@click.argument('url')
def add(name, url):
    ''' Adds the bookmark to user's collection of Bookmarks. '''
    with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'r') as f:
        objects = json.loads(f.read())
    
    name = name.lower()
    var1 = next((x for x in objects if x['name'].lower() == name), None)
    if (var1):
        click.echo("Name already exists with url: {0}".format(var1['url']))
        exit()
    url = url.lower()
    var2 = next((x for x in objects if x['url'].lower() == url), None)
    if (var2):
        click.echo("URL already exists with name: {0}".format(var2['name']))
        exit()
    
    id = len(objects)
    tags = []
    datetime = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(time.time()))
   
    entry = {'id': id, 'name': name, 'tags': tags, 'url': url, 'datetime': datetime}
    objects.append(entry)
    
    with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'w') as f:
        json.dump(objects, f, indent=4, separators=(',', ': '))
    click.echo("Bookmark added successfully!")
