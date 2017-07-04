import click
import json
import os


@click.command()
@click.option('-n','--name', type=click.STRING, help='Delete bookmark using name.')
@click.option('-i','--ID','ID', type=click.INT, help='Delete bookmark using ID.')
@click.option('-u','--url',type=click.STRING, help='Delete bookmark using URL.')

def remove(name,ID,url):

	'''Deletes bookmarks by name, id or URL'''

	#Expand the '~' to the user's home directory
	with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'r') as f:
        	objects = json.loads(f.read())

	if name:
		for i in xrange(len(objects)):
			if objects[i]['name'] == name :
				objects.pop(i)
				break

	if ID:
		for i in xrange(len(objects)):
			if objects[i]['id'] == ID :
				objects.pop(i)
				break

	if url:
		for i in xrange(len(objects)):
			if objects[i]['url'] == url:
				objects.pop(i)
				break

	length = len(objects)
	
	for i in range(length):
		objects[i]['id'] = i

	with open(os.path.expanduser('~/.ordinati/bookmarks.json'), 'w') as f:
		json.dump(objects, f,sort_keys=True, indent=4, separators=(',',': '))
		
		

