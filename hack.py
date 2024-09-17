#!/usr/bin/python

FILENAME_IN  = 'track1.bin'
FILENAME_OUT = 'track1-hack.bin'

OFFSET_ISO9000_MUSIC = 0x17db92b
MUSIC_GRANNY = 0x03
MUSIC_SUBTERRANEAN = 0x0b

with open(FILENAME_IN, 'rb') as inf:
    track1 = bytearray(inf.read())

assert track1[OFFSET_ISO9000_MUSIC] == MUSIC_GRANNY
track1[OFFSET_ISO9000_MUSIC] = MUSIC_SUBTERRANEAN

with open(FILENAME_OUT, 'wb') as outf:
    outf.write(track1)
