#! /usr/bin/env python3
# from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits

import string
import random

N = 6
print(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N)))
