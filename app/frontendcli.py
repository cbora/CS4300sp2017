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
    socketio.run(app, host='0.0.0.0', port=port)
