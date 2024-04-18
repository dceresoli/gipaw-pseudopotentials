#!/usr/bin/env python
# plot ld1.x wfc and pswfc

import numpy as np
import matplotlib.pyplot as plt
import sys

# main
if len(sys.argv) <= 1:
    sys.stderr.write("usage: %s element\n" % (sys.argv[0]))
    sys.exit(1)

atom = sys.argv[1]
log = np.loadtxt(atom + '.dlog')
pslog = np.loadtxt(atom + 'ps.dlog')

plt.close()
channel = ['S', 'P', 'D', 'F']
for i in range(log.shape[1]-1):
    plt.figure()
    plt.title(atom + ': ' + channel[i] + ' channel')

    plt.plot(log[:,0], np.arctan(log[:,i+1]), label='AE')
    plt.plot(pslog[:,0], np.arctan(pslog[:,i+1]), label='PS')

    plt.legend()
    plt.savefig('ld1_dlog_'+channel[i]+'.png', bbox_inches='tight', facecolor='white')

plt.show()

