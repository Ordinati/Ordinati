import click
import json
import os
import httplib2

def is_url_ok(url, h):
    try:
        resp = h.request(url, 'HEAD')
        return True
    except:
        return False

def verify_all():
    
    click.echo('This may take several minutes.')
    
    #Expand the '~' to the user's home directory
    with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'r') as f:
        objects = json.loads(f.read())

    h = httplib2.Http(timeout = 5)
    invalid = []
    for x in objects:
        if is_url_ok(x['url'], h):
            click.echo('{0}:\r\t\tOK'.format(x['name']))
        else:
            click.echo('{0}:\r\t\tNOT OK'.format(x['name']))
            invalid.append((x['name'], x['url']))
    return invalid

def verify_by_name(name):
    
    #Expand the '~' to the user's home directory
    with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'r') as f:
        objects = json.loads(f.read())

    h = httplib2.Http(timeout = 5)
    bookmark = next((x for x in objects if x['name'].lower() == name), False)
    if not bookmark:
        click.echo('Bookmark with name \'{0}\' not found.'.format(name))
    else:
        is_ok = is_url_ok(bookmark['url'], h)
        if is_ok:
            click.echo('{0}:\r\t\tOK'.format(name))
        else:
            click.echo('{0}:\r\t\tNOT OK'.format(name))

def verify_by_url(url):
    
    h = httplib2.Http(timeout = 5)
    is_ok = is_url_ok(url, h)
    if is_ok:
        click.echo('{0}:\tOK'.format(url))
    else:
        click.echo('{0}:\tNOT OK'.format(url))

@click.command()
@click.option('-a','--all', is_flag = True, help = 'Verify all saved bookmarks.')
@click.option('-n', '--name', multiple = True, type = click.STRING, help = 'Verify a single bookmark by name.')
@click.option('-u', '--url', type = click.STRING, help = 'Verify an independent url.')
def verify(all, name, url):
    
    '''Verify if the URLs bookmarked are valid'''
    
    if all:
        invalid = verify_all()
        click.echo('List of invalid bookmarks by name:')
        for i in invalid:
            click.echo('{0}'.format(i[0]))
    
    elif name:
        for x in name:
            verify_by_name(x.lower())
    
    if url:
        verify_by_url(url)