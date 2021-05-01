#!/usr/bin/python

import simplenote
import os
import sys

sn = simplenote.Simplenote(os.environ['USERNAME'], os.environ['PASSWORD'])

notes, status = sn.get_note_list()

for note in notes:
  if sys.argv[0] in note['tags']:
	  f = open('output.txt', 'a', encoding='UTF-8')
	  f.write(note['content'])
