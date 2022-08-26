#!/usr/bin/python3
"""
    module
"""


from fabric.api import run, put, env, local
import datetime
from os.path import exists

env.user = "ubuntu"
env.hosts = ['34.201.147.121', '34.207.82.133']


def do_pack():
    """casddddddddd"""
    try:
        time = datetime.datetime.now()
        date = time.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(date))
        return("versions/web_static_{}.tgz".format(date))
    except exception:
        return None


def do_deploy(archive_path):
    """dddddddddddda"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[1]
        filename_no_extension = filename.split(".")[0]
        file_path = "/data/web_static/releases/" + filename_no_extension + "/"
        run("mkdir -p " + file_path)
        run("tar -xzf /tmp/" + filename + " -C " + file_path)
        run("mv " + file_path + "web_static/*" + " " + file_path)
        run("rm /tmp/{}".format(filename))
        run("rm -rf " + file_path + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + file_path + " /data/web_static/current")
        print("New version deployed!")
        return True

    except Exception:
        return False


def deploy():
    """asad"""
    path = do_pack()
    if exists(path):
        return do_deploy(path)
    else:
        return False
