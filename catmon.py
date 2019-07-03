#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Egor Egorenkov"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Egor Egorenkov"
__email__ = "it.manfred@gmail.com"
__status__ = "Development"

import socket
import sys
import os
import re
from datetime import datetime, timedelta
from contextlib import closing
import logging
from jmxquery import JMXConnection, JMXQuery, MetricType

# SETUP LOGGER
FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
#logging.basicConfig(format=FORMAT, filename='routine.log', level=logging.INFO)
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

def check_socket(host, port, timeout=1):
  """Check socket
  :param host: host
  :param port: port
  :param timeout: connection timeout in seconds default = 1
  :return boolean
  """
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(timeout)

  try:
    with closing(s) as sock:
      if sock.connect_ex((host, port)) == 0:
        logger.info('Server %s is available on port %d', host, port)
        return True
  except:
    logger.info('Server %s is not available on port %d', host, port)
    return False

def get_jmx(host, port, jmxQuery=None):
  """Get jmx
  :param host: host
  :param port: port
  :param jmxQuery: jmxQuery
  """
  jmxConnection = JMXConnection("service:jmx:rmi:///jndi/rmi://"+str(host)+":"+str(port)+"/jmxrmi")
  metrics = jmxConnection.query(jmxQuery)

  for metric in metrics:
    x = re.search("name=\/\/(?P<hostname>.*)\/(?!docs,|manager,)(?P<appname>[^,]+)", metric.mBeanName)
    if x is not None:
      if x.group('appname') is not None:
        appname=x.group('appname')
        now = datetime.now()
        starttime = datetime.fromtimestamp(metric.value / 1e3)
        delta = now - starttime
        logger.info('Server: %s; appname: %s; uptime: %s', host, appname, str(delta))

def main():
  hosts = ["qaserver1", "qaserver2", "qaserver3", "qaserver4", "qaserver5", "qaserver6"]
  port = 5569
  for host in hosts:
    # Check socket
    is_socket_open = check_socket(host, port, 1)

    # Check status code
    if is_socket_open:
      get_jmx(host, port, [JMXQuery("*:*/startTime")])
    else:
      logger.error('Server %s is not available on port %d', host, port)

if __name__ == '__main__':
    main()
