#!/usr/bin/python

import argparse
import csv
import os

from shodan import Shodan

api = Shodan('SBnsRkcwfOvHXV3aooYdR8AjGfoe5OjS')

#Looking up IP Addresses
ipinfo = api.host('8.8.8.8')
print(ipinfo)