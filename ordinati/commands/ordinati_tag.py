'''
Module to manipulate tags for a bookmark
'''
import click
import json
import os

'''
name is a compulsory argument
multiple = True ensures that there can be more than one flags in a command
is_flag = True helps in treating show as a boolean flag
'''
@click.command()
@click.argument('name')
@click.option('-a','--add', '-m', multiple = True, help='Add tags to a bookmark')
@click.option('-d','--delete', '-m', multiple = True, help='Delete tags from a bookmark')
@click.option('-s','--show', is_flag = True, help='Show tags of a bookmark')
def tag(name,add,delete,show):

    '''Manipulates tags for a bookmark identified using name'''

    #Expand the '~' to the user's home directory
    with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'r') as f:
        bookmarks = json.loads(f.read())

    '''Add a tag to a bookmark'''
    if add:
        for bookmark in bookmarks:
            if bookmark['name'] == name:
                for tag in add:
                    bookmark['tags'].append(tag)
                break

    '''Delete a tag from a bookmark'''
    if delete:
        for bookmark in bookmarks:
            if bookmark['name'] == name:
                for tag in delete:
                    bookmark['tags'].remove(tag)
                break

    '''If show(a flag) is present, display all tags of that bookmark'''
    if show:
        for bookmark in bookmarks:
            if bookmark['name'] == name:
                tags = bookmark['tags']    
                for tag in tags:
                    click.echo(tag)
                break

    '''Dump the bookmarks back to the JSON file'''
    with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'w') as f:
        json.dump(bookmarks, f, indent=4, separators=(',',': '))
