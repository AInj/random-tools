# Packaging script that adds all files within a directory into a .zip file, and ignores specifically listed entries

import os, sys, zipfile

ignore = ['.git', '.idea', 'node_modules', 'jspm_packages']


def main():
  if len(sys.argv) < 3:
    print "USAGE: {0} <src-dir> <dest>(.zip)".format(sys.argv[0])
    sys.exit(1)

  pack(sys.argv[1], '{0}.zip'.format(sys.argv[2]))
  print "> Done"


def pack(srcdir, destzip):
  print '> Packing `{0}` into {1}'.format(srcdir, destzip)

  zf = zipfile.ZipFile(destzip, "w")
  for dirname, subdirs, files in os.walk(srcdir):
    if not any(i in dirname for i in ignore):
      innerdir = os.path.relpath(dirname, srcdir)
      zf.write(dirname, innerdir)
      for filename in files:
	    zf.write(os.path.join(dirname, filename), os.path.join(innerdir, filename))
  zf.close()

if __name__ == '__main__':
    main()
