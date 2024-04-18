#!/usr/bin/env python
# plot ld1.x convergence of Bessel functions

import numpy as np
import matplotlib.pyplot as plt
import sys

# main
if len(sys.argv) <= 1:
    sys.stderr.write("usage: %s ld1.out\n" % (sys.argv[0]))
    sys.exit(1)

# read output file
with open(sys.argv[1]) as f:
    lines = f.readlines()

# read (AE,PS) eigenvalues
eigs_aeps = []
for i in range(len(lines)):
    if lines[i].find('De AE-PS (Ry)') >= 0:
        i += 1
        while True:
            if lines[i] == '\n':
                break
            n, l, orb = lines[i][:15].split()
            ae, ps, de = list(map(float, lines[i][28:].split()))
            eigs_aeps.append([int(n), int(l), orb, ae, ps])
            i += 1

# read output of Bessel function diagonalization
found = False
i = 0
while i < len(lines):
    if lines[i].find('Test with a basis set of Bessel') >= 0:
        found = True
        ecut, eigs = [], []
        i += 4

        while i < len(lines):
            if lines[i].find('End of Bessel') >= 0:
                 break

            if lines[i].find('Cutoff (Ry)') >= 0:
                value = float(lines[i].split()[3])
                ecut.append(value)
                i += 2  # skip line
             
            while lines[i] != '\n':
                s = lines[i].split()
                eigs.append(list(map(float, [s[2], s[4], s[6]])))
                i += 1

            i += 1
    else:
        i += 1

if not found:
    raise RuntimeError('Missing Bessel functions test!')


# reshape arrays
lmax = len(eigs)//len(ecut)
ecut = np.array(ecut)
eigs = np.array(eigs)
eigs = eigs.reshape(len(ecut), lmax, 3)

plt.close()
for l in range(lmax):
    plt.figure() 
    plt.title(sys.argv[1] + ': Bessel functions test')

    for n in range(2):
        for e in eigs_aeps:
            if e[1] == l and abs(e[3] - eigs[-1,l,n]) < 0.1:
                plt.plot(ecut, e[3]-eigs[:,l,n], label=e[2])
    plt.axhline(0, color='black', linestyle='dashed', linewidth=0.8)

    plt.xlabel('PW cutoff (Ry)')
    plt.ylabel('$\\Delta$E (Ry)')
    plt.legend()
    plt.savefig('ld1_bessel_'+str(l)+'.png', bbox_inches='tight', facecolor='white')

plt.show()

