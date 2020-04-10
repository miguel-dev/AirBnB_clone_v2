#!/usr/bin/python3
"""Module to create a tar pack with web static files to deploy"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['35.237.183.49', '52.201.229.129']
env.user = 'ubuntu'


def do_pack():
    """Create pack"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        date = datetime.now()
        date_format = date.strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_" + date_format + ".tgz"
        local("tar -czvf {} web_static".format(filename))
        return filename
    except:
        return None

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        name_ext = archive_path.split('/')
        name_ext = name_ext[-1]
        name = name_ext.split('.')
        name = name[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, name))
        run("tar -xzf /tmp/{} -C {}{}/".format(name_ext, path, name))
        run("rm /tmp/{}".format(name_ext))
        run("mv {}{}/web_static/* {}{}/".format(path, name, path, name))
        run("rm -rf {}{}/web_static".format(path, name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, name))
        print("New version deployed!")
        return (True)
    except:
        return (False)

def deploy():
    """ combines do_deploy and do_pack functions """
    path_file = do_pack()
    if path_file:
        return (do_deploy(path_file))
    else:
        return False
