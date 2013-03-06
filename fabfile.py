import os
import subprocess
from StringIO import StringIO
from fabric.api import *

HOST, DIRECTORY = os.environ['TARGET'].split(':')
env['hosts'] = [HOST]
env['use_ssh_config'] = True


@task
def deploy():
    tarball = subprocess.check_output(['git', 'archive', 'HEAD'])
    with cd(DIRECTORY):
        put(StringIO(tarball), '_app.tar')
        try:
            run('bin/airship deploy _app.tar')
        finally:
            run('rm _app.tar')
