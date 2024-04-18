# Gipaw (and other) pseudopotentials
This repo collects some pseudopotentials I've generated for Quantum ESPRESSO and QE-GIPAW.
Most of them are norm-conserving pseudos are require a very high plane wave cutoff.

*Important: always test them on simple systems before doing any serious calculation!*

<table style="width:80%" border="0" cellpadding="1" cellspacing="2">
<tbody>
<tr align="center">
<td style="width:5%;"><small>1</small><br><a href="#Hydrogen" title="hydrogen">H</a></td>
<td colspan="16" style="width:5%"><br></td>
<td style="width:5%"><small>2</small><br><a href="He" title="helium">He</a></td>
</tr>

<tr align="center">
<td style="width:5%"><small>3</small><br><a href="Li" title="lithium">Li</a></td>
<td style="width:5%"><small>4</small><br><a href="Be" title="beryllium">Be</a></td>
<td colspan="10" style="width:5%"><br></td>
<td style="width:5%"><small>5</small><br><a href="B" title="boron">B</a></td>
<td style="width:5%"><small>6</small><br><a href="C" title="carbon">C</a></td>
<td style="width:5%"><small>7</small><br><a href="N" title="nitrogen">N</a></td>
<td style="width:5%"><small>8</small><br><a href="O" title="oxygen">O</a></td>
<td style="width:5%"><small>9</small><br><a href="F" title="fluorine">F</a></td>
<td style="width:5%"><small>10</small><br><a href="Ne" title="neon">Ne</a></td>
</tr>

<tr align="center">
<td style="width:5%"><small>11</small><br><a href="Na" title="sodium">Na</a></td>
<td style="width:5%"><small>12</small><br><a href="Mg" title="magnesium">Mg</a></td>
<td colspan="10" style="width:5%"><br></td>
<td style="width:5%"><small>13</small><br><a href="./pseudos/13-Al" title="aluminum">Al</a></td>
<td style="width:5%"><small>14</small><br><a href="Si" title="silicon">Si</a></td>
<td style="width:5%"><small>15</small><br><a href="P" title="phosphorus">P</a></td>
<td style="width:5%"><small>16</small><br><a href="S" title="sulfur">S</a></td>
<td style="width:5%"><small>17</small><br><a href="Cl" title="chlorine">Cl</a></td>
<td style="width:5%"><small>18</small><br><a href="Ar" title="argon">Ar</a></td>
</tr>

<tr align="center">
<td style="width:5%"><small>19</small><br><a href="K" title="potassium">K</a></td>
<td style="width:5%"><small>20</small><br><a href="Ca" title="calcium">Ca</a></td>
<td style="width:5%"><small>21</small><br><a href="Sc" title="scandium">Sc</a></td>
<td style="width:5%"><small>22</small><br><a href="Ti" title="titanium">Ti</a></td>
<td style="width:5%"><small>23</small><br><a href="V" title="vanadium">V</a></td>
<td style="width:5%"><small>24</small><br><a href="Cr" title="chromium">Cr</a></td>
<td style="width:5%"><small>25</small><br><a href="Mn" title="manganese">Mn</a></td>
<td style="width:5%"><small>26</small><br><a href="Fe" title="iron">Fe</a></td>
<td style="width:5%"><small>27</small><br><a href="Co" title="cobalt">Co</a></td>
<td style="width:5%"><small>28</small><br><a href="Ni" title="nickel">Ni</a></td>
<td style="width:5%"><small>29</small><br><a href="Cu" title="copper">Cu</a></td>
<td style="width:5%"><small>30</small><br><a href="Zn" title="zinc">Zn</a></td>
<td style="width:5%"><small>31</small><br><a href="Ga" title="gallium">Ga</a></td>
<td style="width:5%"><small>32</small><br><a href="Ge" title="germanium">Ge</a></td>
<td style="width:5%"><small>33</small><br><a href="As" title="arsenic">As</a></td>
<td style="width:5%"><small>34</small><br><a href="Se" title="selenium">Se</a></td>
<td style="width:5%"><small>35</small><br><a href="Br" title="bromine">Br</a></td>
<td style="width:5%"><small>36</small><br><a href="Kr" title="krypton">Kr</a></td>
</tr>

<tr align="center">
<td style="width:5%"><small>37</small><br><a href="Rb" title="rubidium">Rb</a></td>
<td style="width:5%"><small>38</small><br><a href="Sr" title="strontium">Sr</a></td>
<td style="width:5%"><small>39</small><br><a href="Y" title="yttrium">Y</a></td>
<td style="width:5%"><small>40</small><br><a href="Zr" title="zirconium">Zr</a></td>
<td style="width:5%"><small>41</small><br><a href="Nb" title="niobium">Nb</a></td>
<td style="width:5%"><small>42</small><br><a href="Mo" title="molybdenum">Mo</a></td>
<td style="width:5%"><small>43</small><br><a href="Tc" title="technetium">Tc</a></td>
<td style="width:5%"><small>44</small><br><a href="Ru" title="ruthenium">Ru</a></td>
<td style="width:5%"><small>45</small><br><a href="Rh" title="rhodium">Rh</a></td>
<td style="width:5%"><small>46</small><br><a href="Pd" title="palladium">Pd</a></td>
<td style="width:5%"><small>47</small><br><a href="Ag" title="silver">Ag</a></td>
<td style="width:5%"><small>48</small><br><a href="Cd" title="cadmium">Cd</a></td>
<td style="width:5%"><small>49</small><br><a href="In" title="indium">In</a></td>
<td style="width:5%"><small>50</small><br><a href="Sn" title="tin">Sn</a></td>
<td style="width:5%"><small>51</small><br><a href="Sb" title="antimony">Sb</a></td>
<td style="width:5%"><small>52</small><br><a href="Te" title="tellurium">Te</a></td>
<td style="width:5%"><small>53</small><br><a href="I" title="iodine">I</a></td>
<td style="width:5%"><small>54</small><br><a href="Xe" title="xenon">Xe</a></td>
</tr>

<tr align="center">
<td style="width:5%"><small>55</small><br><a href="Cs" title="cesium">Cs</a></td>
<td style="width:5%"><small>56</small><br><a href="Ba" title="barium">Ba</a></td>
<td style="width:5%"><small>71</small><br><a href="Lu" title="lutetium">Lu</a></td>
<td style="width:5%"><small>72</small><br><a href="Hf" title="hafnium">Hf</a></td>
<td style="width:5%"><small>73</small><br><a href="Ta" title="tantalum">Ta</a></td>
<td style="width:5%"><small>74</small><br><a href="W" title="tungsten">W</a></td>
<td style="width:5%"><small>75</small><br><a href="Re" title="rhenium">Re</a></td>
<td style="width:5%"><small>76</small><br><a href="Os" title="osmium">Os</a></td>
<td style="width:5%"><small>77</small><br><a href="Ir" title="iridium">Ir</a></td>
<td style="width:5%"><small>78</small><br><a href="Pt" title="platinum">Pt</a></td>
<td style="width:5%"><small>79</small><br><a href="Au" title="gold">Au</a></td>
<td style="width:5%"><small>80</small><br><a href="Hg" title="mercury">Hg</a></td>
<td style="width:5%"><small>81</small><br><a href="Tl" title="thallium">Tl</a></td>
<td style="width:5%"><small>82</small><br><a href="Pb" title="lead">Pb</a></td>
<td style="width:5%"><small>83</small><br><a href="Bi" title="bismuth">Bi</a></td>
<td style="width:5%"><small>84</small><br><a href="Po" title="polonium">Po</a></td>
<td style="width:5%"><small>85</small><br><a href="At" title="astatine">At</a></td>
<td style="width:5%"><small>86</small><br><a href="Rn" title="radon">Rn</a></td>
</tr>

<tr align="center">
<td style="width:5%"><small>87</small><br><a href="Fr" title="francium">Fr</a></td>
<td style="width:5%"><small>88</small><br><a href="Ra" title="radium">Ra</a></td>
<td style="width:5%"><small>103</small><br><a href="Lr" title="lawrentium">Lr</a></td>
<td style="width:5%"><small>104</small><br><a href="Rf" title="rutherfordium">Rf</a></td>
<td style="width:5%"><small>105</small><br><a href="Db" title="dubnium">Db</a></td>
<td style="width:5%"><small>106</small><br><a href="Sg" title="seaborgium">Sg</a></td>
<td style="width:5%"><small>107</small><br><a href="Bh" title="bohrium">Bh</a></td>
<td style="width:5%"><small>108</small><br><a href="Hs" title="hassium">Hs</a></td>
<td style="width:5%"><small>109</small><br><a href="Mt" title="meitnerium">Mt</a></td>
<td style="width:5%"><small>110</small><br><a href="Ds" title="darmstadtium">Ds</a></td>
<td style="width:5%"><small>111</small><br><a href="Rg" title="roentgenium">Rg</a></td>
<td colspan="7" style="width:5%"><br>
</td>
</tr>

<tr>
<td colspan="18" style="width:5%"><br></td>
</tr>

<tr align="center">
<td colspan="2" style="width:5%"><br></td>
<td style="width:5%"><small>57</small><br><a href="La" title="lanthanum">La</a></td>
<td style="width:5%"><small>58</small><br><a href="Ce" title="cerium">Ce</a></td>
<td style="width:5%"><small>59</small><br><a href="Pr" title="praseodymium">Pr</a></td>
<td style="width:5%"><small>60</small><br><a href="Nd" title="neodymium">Nd</a></td>
<td style="width:5%"><small>61</small><br><a href="Pm" title="promethium">Pm</a></td>
<td style="width:5%"><small>62</small><br><a href="Sm" title="samarium">Sm</a></td>
<td style="width:5%"><small>63</small><br><a href="Eu" title="europium">Eu</a></td>
<td style="width:5%"><small>64</small><br><a href="Gd" title="gadolinium">Gd</a></td>
<td style="width:5%"><small>65</small><br><a href="Tb" title="terbium">Tb</a></td>
<td style="width:5%"><small>66</small><br><a href="Dy" title="dysprosium">Dy</a></td>
<td style="width:5%"><small>67</small><br><a href="Ho" title="holmium">Ho</a></td>
<td style="width:5%"><small>68</small><br><a href="Er" title="erbium">Er</a></td>
<td style="width:5%"><small>69</small><br><a href="Tm" title="thulium">Tm</a></td>
<td style="width:5%"><small>70</small><br><a href="Yb" title="ytterbium">Yb</a></td>
</tr>

<tr align="center">
<td colspan="2" style="width:5%"><br></td>
<td style="width:5%"><small>89</small><br><a href="Ac" title="actinium">Ac</a></td>
<td style="width:5%"><small>90</small><br><a href="Th" title="thorium">Th</a></td>
<td style="width:5%"><small>91</small><br><a href="Pa" title="protactinium">Pa</a></td>
<td style="width:5%"><small>92</small><br><a href="U" title="uranium">U</a></td>
<td style="width:5%"><small>93</small><br><a href="Np" title="neptunium">Np</a></td>
<td style="width:5%"><small>94</small><br><a href="Pu" title="plutonium">Pu</a></td>
<td style="width:5%"><small>95</small><br><a href="Am" title="americium">Am</a></td>
<td style="width:5%"><small>96</small><br><a href="Cm" title="curium">Cm</a></td>
<td style="width:5%"><small>97</small><br><a href="Bk" title="berkelium">Bk</a></td>
<td style="width:5%"><small>98</small><br><a href="Cf" title="californium">Cf</a></td>
<td style="width:5%"><small>99</small><br><a href="Es" title="einsteinium">Es</a></td>
<td style="width:5%"><small>100</small><br><a href="Fm" title="fermium">Fm</a></td>
<td style="width:5%"><small>101</small><br><a href="Md" title="mendelevium">Md</a></td>
<td style="width:5%"><small>102</small><br><a href="No" title="nobelium">No</a></td>
</tr>
</tbody>
</table>

File name breakdown:
* pz, blyp, pw91, pbe: XC functional
* tm: norm-conserving, Martins Trouillier method
* rrkj: norm-conseriving, RRKJ method
*  rrkjus: ultrasoft, RRJK method
* paw: PAW
* gipaw: with GIPAW reconstruction
* semi: with semicore orbitals
* nh: generated with Nathalie Holzwarth's atompaw
