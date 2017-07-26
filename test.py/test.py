#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------
"""

"""
#-------------------------
#
# (C) Ibrahem Qasim, 2017
#
#-------------------------
import urllib
import re
try:
    import urllib.request as GUrllib    #python 3.6
    import urllib.parse                 #python 3.6
except:
    import urllib2  as GUrllib          #python 2.7  urllib2.urlopen
#-------------------------
try:
    import sys
    reload(sys)  
    sys.setdefaultencoding('utf8')
except:
    import sys
#-------------------------
br = '''
'''
#-------------------------
def ec_de_code(tt , type):
    fao = tt
    if type == 'encode' :
        try:
            fao = urllib.parse.quote(tt)        # python 3
        except:
            fao = GUrllib.quote(tt)
    elif type == 'decode' :
        try:
            fao = urllib.parse.unquote(tt)        # python 3
        except:
            fao = GUrllib.unquote(tt).decode('utf8')
    return fao
#-------------------------
def printo(po):
    print( ec_de_code(po , 'encode') + br)
#-------------------------
def main():

    if sys.argv:
        printo(str(sys.argv) + br)
#-------------------------
if __name__ == "__main__":
    main()
#-------------------------
