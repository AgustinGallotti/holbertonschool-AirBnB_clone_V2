#!/usr/bin/python3
"""
    module
"""


def do_pack():
    """generate a tgz archives from contents of the web_static"""
    try:
        time= datetime.datetime.now()
        date = time.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -cfvz versions/web_static_{}.tgz web_static/".format(date))
        return("versions/web_static_{}.tgz".format(date))
    except Exception:
        return None
