import os
from math import pi

digits = int(os.getenv("DIGITS") or 10)

print("%.*f" % (digits, pi))
