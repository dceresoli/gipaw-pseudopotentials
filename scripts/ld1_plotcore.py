#!/usr/bin/env python
# plot ld1.x core correction

import numpy as np
import matplotlib.pyplot as plt
import sys

# main
if len(sys.argv) <= 1:
    sys.stderr.write("usage: %s element\n" % (sys.argv[0]))
    sys.exit(1)

atom = sys.argv[1]
core = np.loadtxt(atom + '.core')

plt.figure() 
plt.title(atom + ': core')

plt.plot(core[:,0], core[:,3], label='core')
plt.plot(core[:,0], core[:,2], label='valence')
plt.plot(core[:,0], core[:,1], label='NLCC')

plt.xlim(0,5)
plt.grid()
plt.legend()
plt.savefig('ld1_core.png', bbox_inches='tight', facecolor='white')

plt.show()

