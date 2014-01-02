"""Or.

Usage:
  or.py (--parametro1|--parametro2)
"""

from docopt import docopt

args = docopt(__doc__, version="oi")

print args
