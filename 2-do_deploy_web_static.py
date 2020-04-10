#!/usr/bin/python3
"""Module to create a tar pack with web static files to deploy"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['35.237.183.49', '52.201.229.129']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        name_ext = archive_path.split('/')
        name_ext = name_ext[-1]
        name = name_ext.split(".")
        name = name[0]
        path = "/data/web_static/releases/" + name
        # instructions
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(path))
        run("tar -xzf /tmp/{} -C {}/".format(name_ext, path))
        run("rm /tmp/{}".format(name_ext))
        run("mv {}/web_static/* {}/".format(path, path))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(path))
        print("New version deployed!")
        return (True)
    except:
        return (False)
