#!/usr/bin/python3
""" Fari script distributes archive to servers  """
from fabric.api import *
from os import path

env.hosts = ['54.160.62.128', '3.89.99.18']


def do_deploy(archive_path):
    """ Deploy archives """
    if not path.exists(archive_path) or not path.isfile(archive_path):
        return False
    ret = True

    d_folder = put(archive_path, '/tmp/')
    if d_folder.failed:
        ret = False

    archive_file = archive_path.replace(".tgz", "").replace("versions/", "")
    d_dest = run('mkdir -p /data/web_static/releases/' + archive_file + '/')
    if d_dest.failed:
        ret = False

    d_unpack = run('tar -xzf /tmp/' + archive_file + '.tgz' +
                   ' -C /data/web_static/releases/' + archive_file + '/')
    if d_unpack.failed:
        ret = False

    d_cleanfile = run('rm /tmp/' + archive_file + '.tgz')
    if d_cleanfile.failed:
        ret = False

    d_move = run('cp -R /data/web_static/releases/' + archive_file +
                 '/web_static/* /data/web_static/releases/' + archive_file +
                 '/')
    d_del = run('rm -rf /data/web_static/releases/' + archive_file +
                '/web_static')
    if d_move.failed or d_del.failed:
        ret = False

    d_cleanfolder = run('rm -rf /data/web_static/releases/' + archive_file +
                        '/web_static')
    if d_cleanfolder.failed:
        ret = False

    d_removeold = run('rm -rf /data/web_static/current')
    if d_removeold.failed:
        ret = False

    d_createnew = run('ln -sf /data/web_static/releases/' + archive_file +
                      '/' + ' /data/web_static/current')
    if d_createnew.failed:
        ret = False

    return ret
