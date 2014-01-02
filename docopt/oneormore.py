"""Oneormore.

Usage:
  oneormore.py <name>...
"""

from docopt import docopt

args = docopt(__doc__, version="oi")

nomes = args['<name>']

print "Nomes:"
for nome in nomes:
    print nome
