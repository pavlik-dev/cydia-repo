import sys
import hashlib
import os

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

if len(sys.argv) < 3:
	raise Exception('no control or/and deb file')
	exit(255)

debfile = sys.argv[2]

with open(sys.argv[1], 'rb') as file:
	read = file.read()

ctrl = read.decode().strip()

config = dict([l.split(':', 1) for l in ctrl.splitlines() if l and ':' in l])

config['Size'] = str(os.path.getsize(debfile))
config['Filename'] = debfile

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()

with open(debfile, 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)
        sha256.update(data)

config['MD5sum'] = md5.hexdigest()
config['SHA1'] = sha1.hexdigest()
config['SHA256'] = sha256.hexdigest()

for k,v in config.items():
	print("{0}: {1}".format(k, v.strip()))

print()
