#!/usr/bin/env python
# plot ld1.x wfc and pswfc

import numpy as np
import matplotlib.pyplot as plt
import sys

def readwfc(filename):
    # read columns
    with open(filename, 'rt') as f:
        cols = f.readline().split()[1:]

    # map columns to orbitals
    columns = dict()
    for i, c in enumerate(cols):
        if c not in columns:
            columns[c] = i

    # read data
    data = np.loadtxt(filename, comments='#')
    return data, columns


# main
if len(sys.argv) <= 1:
    sys.stderr.write("usage: %s element orbitals\n" % (sys.argv[0]))
    sys.exit(1)

atom = sys.argv[1]
wfc, wfc_cols = readwfc(atom + '.wfc')
pswfc, pswfc_cols = readwfc(atom + 'ps.wfc')
orbitals = sys.argv[2:]

plt.close()
for orb in orbitals:
    try:
        col = pswfc_cols[orb]
        col = wfc_cols[orb]
        idx = np.argmax(np.abs(wfc[:,col]))
        if wfc[idx,col] < 0.0: wfc[:,col] = -wfc[:,col]
    except KeyError:
        sys.stderr.write('orbital %s not present\n' % (orb))
        continue

    plt.figure() 
    plt.title(atom + ': ' + orb)

    col = wfc_cols[orb]
    plt.plot(wfc[:,0], wfc[:,col], label='AE')

    col = pswfc_cols[orb]
    plt.plot(pswfc[:,0], pswfc[:,col], label='PS')

    plt.xlim(0,5)
    plt.grid()
    plt.legend()
    plt.savefig('ld1_wfc_'+orb+'.png', bbox_inches='tight', facecolor='white')


plt.show()

