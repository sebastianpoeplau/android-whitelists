#!/usr/bin/python

import sys
import struct

if len(sys.argv) < 2:
	print "Usage: %s <hash_file>" % sys.argv[0]
	sys.exit(0)

hashes = []
hashlen = 0
with open(sys.argv[1]) as f:
	for line in f:
		line = line.strip()
		if line == '':
			continue

		# convert to string
		if hashlen == 0:
			hashlen = len(line) / 2
		hashes.append(line.decode("hex"))

outfile = sys.argv[1] + ".bin"
with open(outfile, "w") as f:
	f.write(struct.pack(">II", hashlen, len(hashes)))
	for h in hashes:
		f.write(h)

print "Wrote %d hashes of length %d to %s" % (len(hashes), hashlen, outfile)
