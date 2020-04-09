#!/usr/bin/env python3
"""Module to create a tar pack with web static files to deploy"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """Create pack"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        date = datetime.now()
        date_format = date.strftime("%Y%m%d%H%M%S");
        filename = "versions/web_static_" + date_format + ".tgz";
        local("tar -czvf {} web_static".format(filename))
        return filename
    except:
        return None
