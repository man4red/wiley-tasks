#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Egor Egorenkov"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Egor Egorenkov"
__email__ = "it.manfred@gmail.com"
__status__ = "Development"

import paramiko
import logging

# SETUP LOGGER
FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

ssh = paramiko.SSHClient()


def main():
    hosts = [
        "qaserver1", "qaserver2", "qaserver3", "qaserver4", "qaserver5",
        "qaserver6"
    ]
    username = "user"
    password = "password"
    #key = paramiko.RSAKey.from_private_key_file(keyfilename)
    #key = paramiko.DSSKey.from_private_key_file(keyfilename)
    for host in hosts:
        try:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password, timeout=2)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
                "wall $(cat /proc/cmdline)")
            logger.info("Server %s - command was sent", host)
        except:
            logger.error("Server %s is not available or wrong user/pass", host)
            pass


if __name__ == "__main__":
    main()
