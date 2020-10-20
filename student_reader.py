#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(1, os.path.split(sys.path[0])[0])

import binascii
import nfc

service_code = 0x09CB

def connected(tag):
  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
        sc = nfc.tag.tt3.ServiceCode(service_code >> 6 ,service_code & 0x3f)
        bc = nfc.tag.tt3.BlockCode(0,service=0)
        data = tag.read_without_encryption([sc],[bc])
        print data[2:10].decode("utf-8")
    except Exception as e:
      print "error: %s" % e
  else:
    print "error: tag isn't Type3Tag"

# タッチ時のハンドラを設定して待機する
clf = nfc.ContactlessFrontend('usb:054c:06c3')
clf.connect(rdwr={'on-connect': connected})