"""Required.

Usage:
  required.py (--parametro1=<valor1>) [--parametro2=<valor2>]
"""

from docopt import docopt

args = docopt(__doc__, version="oi")

print args
