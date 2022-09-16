import click

@click.group
def cli():
    """Noodle SSG: Another Static Site Generator"""

@cli.command('init')
@click.argument('DIRNAME')
@click.option('-f', '--force', is_flag=True, show_default=True, default=False)
def init(dirname, force):
    print(dirname, force)

if __name__ == '__main__':
    cli()