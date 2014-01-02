"""Optional.

Usage:
  optional.py [--parametro=<valor>]
"""

from docopt import docopt

args = docopt(__doc__, version="oi")

print args
