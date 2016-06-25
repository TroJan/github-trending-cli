import requests

import click

from .helpers import base_data

requests.packages.urllib3.disable_warnings()


def read_page(url, timeout=5):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0'}
    try:
        response = requests.get(url, timeout=timeout, headers=headers)
    except requests.exceptions.ConnectionError as e:  # noqa
        return(None, False)

    return(response, response.status_code)


@click.command()
@click.option(
    '--repo', '-r', is_flag=True,
    help="Lists the trending repositories.")
@click.option(
    '--dev', '-d', is_flag=True,
    help="Lists the trending developers.")
def cli(repo, dev):
    '''
    A command line utility to see the trending repositories
    and developers on Github
    '''
    try:
        if repo:
            base_data('REPO')
            return
        if dev:
            base_data('DEV')
            return
        # if the user does not passes any argument then list the trending repo
        if not(repo and dev):
            base_data('REPO')
            return
    except Exception as e:
        click.secho(e.message, fg="red", bold=True)

if __name__ == '__main__':
    cli()
