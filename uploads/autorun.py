from cms import updatedb, fileMove
import sys

docfile = sys.argv[1]

updatedb(docfile)
fileMove()

