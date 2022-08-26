#!/usr/bi/python3
# create .tgz(compress) before seding

from fabric.api import local
from datetime import datetime
from os import path


def do_pack():
    """ generate compress file  """

    local("mkdir -p versions")
    fecha = datetime.now().strftime("%Y%m%d%H%M%S")
    nombre_arch = "versions/web_static_" + fecha + ".tgz"
    
    if local("sudo tar -cvzf " + nombre_arch + " ./web_static"):
        return nombre_arch
    else:
        return None
