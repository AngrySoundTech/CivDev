import json
import shutil
import click
from git import Repo
from git.remote import RemoteProgress

class Progress(RemoteProgress):
    """
    Simple implementation of progress
    """
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(self._cur_line)

# Load our config file before anything else, because I'm lazy and only writing this because I'm mad
with open('./config.json') as f:
    config = json.load(f)

@click.group()
def main():
    """
    CLI Interface for developing civ plugins
    """
    pass

@main.command()
def setup():
    """Clone all civ plugins"""

    for plugin in config['plugins']:
        Repo.clone_from(plugin['url'], 'plugins/' + plugin['name'], progress=Progress())

@main.command()
def teardown():
    """Remove all civ plugins"""

    for plugin in config['plugins']:
        shutil.rmtree('plugins/' + plugin['name'])

@main.command()
def update():
    """Update all civ plugins"""
    for plugin in config['plugins']:
        Repo('plugins/' + plugin['name']).remotes.origin.pull()

if __name__ == '__main__':
    main()

