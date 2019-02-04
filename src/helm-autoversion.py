#!/usr/bin/env python
import os
import re
import subprocess
import sys
from os import path


def main():
    tiller_version = None
    if 'package' not in sys.argv[1:] and 'repo' not in sys.argv[1:] and 'fetch' not in sys.argv[1:]:
        output = helm(['version', '--server'], capture_output=True)
        tiller_version = re.search(r'SemVer:"v(?P<version>[^"]*)"', output).group('version')

    helm_init()
    helm(sys.argv[1:], version=tiller_version)


def helm_init():
    helm_home = os.getenv('HELM_HOME', path.join(path.expanduser("~"), '.helm'))
    if not path.isdir(helm_home):
        helm(['init', '--client-only'], capture_output=True)


def helm(args, version=None, capture_output=False):
    zi_args = ['0install', 'run']

    if version:
        zi_args.extend(['--version', version])

    zi_args.extend(['http://repo.roscidus.com/kubernetes/helm'])
    zi_args.extend(args)

    try:
        if capture_output:
            process = subprocess.run(zi_args, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            return process.stdout
        else:
            subprocess.run(zi_args, check=True)
    except subprocess.CalledProcessError as ex:
        sys.exit(ex.returncode)


if __name__ == '__main__':
    main()
