import click
import os
import subprocess

@click.group()
def frontendcli():
    pass

@frontendcli.command()
def server():
    # command to start server
    port = int(os.environ.get("PORT", 5000))
    from app import app, socketio
    click.secho("App running at http://0.0.0.0:{}".format(port), fg='green')
    socketio.run(app, host='0.0.0.0', port=port)
