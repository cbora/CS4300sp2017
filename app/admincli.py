import click
import os


@click.group()
def admincli():
    click.secho('Hello World!', fg='green')

