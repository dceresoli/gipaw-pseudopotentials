# Gipaw (and other) pseudopotentials
This repo collects some pseudopotentials I've generated for Quantum ESPRESSO and QE-GIPAW.
Most of them are norm-conserving pseudos are require a very high plane wave cutoff.

*Important: always test them on simple systems before doing any serious calculation!*

<table style="width:80%" border="0" cellpadding="1" cellspacing="2">
<tbody>
<tr align="center">
<td style="width:5%;">1<br>H</td>
<td colspan="16" style="width:5%"><br></td>
<td style="width:5%">2<br>He</td>
</tr>

<tr align="center">
<td style="width:5%">3<br>Li</td>
<td style="width:5%">4<br>Be</td>
<td colspan="10" style="width:5%"><br></td>
<td style="width:5%">5<br>B</td>
<td style="width:5%">6<br>C</td>
<td style="width:5%">7<br>N</td>
<td style="width:5%">8<br>O</td>
<td style="width:5%">9<br>F</td>
<td style="width:5%">10<br>Ne</td>
</tr>

<tr align="center">
<td style="width:5%">11<br>Na</td>
<td style="width:5%">12<br>Mg</td>
<td colspan="10" style="width:5%"><br></td>
<td style="width:5%">13<br><a href="./pseudos/13-Al" title="aluminum">Al</a></td>
<td style="width:5%">14<br>Si</td>
<td style="width:5%">15<br>P</td>
<td style="width:5%">16<br>S</td>
<td style="width:5%">17<br>Cl</td>
<td style="width:5%">18<br>Ar</td>
</tr>

<tr align="center">
<td style="width:5%">19<br>K</td>
<td style="width:5%">20<br>Ca</td>
<td style="width:5%">21<br>Sc</td>
<td style="width:5%">22<br>Ti</td>
<td style="width:5%">23<br>V</td>
<td style="width:5%">24<br>Cr</td>
<td style="width:5%">25<br>Mn</td>
<td style="width:5%">26<br>Fe</td>
<td style="width:5%">27<br>Co</td>
<td style="width:5%">28<br>Ni</td>
<td style="width:5%">29<br>Cu</td>
<td style="width:5%">30<br>Zn</td>
<td style="width:5%">31<br>Ga</td>
<td style="width:5%">32<br>Ge</td>
<td style="width:5%">33<br>As</td>
<td style="width:5%">34<br>Se</td>
<td style="width:5%">35<br>Br</td>
<td style="width:5%">36<br>Kr</td>
</tr>

<tr align="center">
<td style="width:5%">37<br>Rb</td>
<td style="width:5%">38<br>Sr</td>
<td style="width:5%">39<br>Y</td>
<td style="width:5%">40<br>Zr</td>
<td style="width:5%">41<br>Nb</td>
<td style="width:5%">42<br>Mo</td>
<td style="width:5%">43<br>Tc</td>
<td style="width:5%">44<br>Ru</td>
<td style="width:5%">45<br>Rh</td>
<td style="width:5%">46<br>Pd</td>
<td style="width:5%">47<br>Ag</td>
<td style="width:5%">48<br>Cd</td>
<td style="width:5%">49<br>In</td>
<td style="width:5%">50<br>Sn</td>
<td style="width:5%">51<br>Sb</td>
<td style="width:5%">52<br>Te</td>
<td style="width:5%">53<br>I</td>
<td style="width:5%">54<br>Xe</td>
</tr>

<tr align="center">
<td style="width:5%">55<br>Cs</td>
<td style="width:5%">56<br>Ba</td>
<td style="width:5%">71<br>Lu</td>
<td style="width:5%">72<br>Hf</td>
<td style="width:5%">73<br>Ta</td>
<td style="width:5%">74<br>W</td>
<td style="width:5%">75<br>Re</td>
<td style="width:5%">76<br>Os</td>
<td style="width:5%">77<br>Ir</td>
<td style="width:5%">78<br>Pt</td>
<td style="width:5%">79<br>Au</td>
<td style="width:5%">80<br>Hg</td>
<td style="width:5%">81<br>Tl</td>
<td style="width:5%">82<br>Pb</td>
<td style="width:5%">83<br>Bi</td>
<td style="width:5%">84<br>Po</td>
<td style="width:5%">85<br>At</td>
<td style="width:5%">86<br>Rn</td>
</tr>

<tr align="center">
<td style="width:5%">87<br>Fr</td>
<td style="width:5%">88<br>Ra</td>
<td style="width:5%">103<br>Lr</td>
<td style="width:5%">104<br>Rf</td>
<td style="width:5%">105<br>Db</td>
<td style="width:5%">106<br>Sg</td>
<td style="width:5%">107<br>Bh</td>
<td style="width:5%">108<br>Hs</td>
<td style="width:5%">109<br>Mt</td>
<td style="width:5%">110<br>Ds</td>
<td style="width:5%">111<br>Rg</td>
<td colspan="7" style="width:5%"><br>
</td>
</tr>

<tr>
<td colspan="18" style="width:5%"><br></td>
</tr>

<tr align="center">
<td colspan="2" style="width:5%"><br></td>
<td style="width:5%">57<br><a href="./pseudos/57-La" title="lanthanum">La</a></td>
<td style="width:5%">58<br><a href="./pseudos/58-Ce" title="cerium">Ce</a></td>
<td style="width:5%">59<br><a href="./pseudos/59-Pr" title="praseodimium">Pr</a></td>
<td style="width:5%">60<br><a href="./pseudos/60-Nd" title="neodimium">Nd</a></td>
<td style="width:5%">61<br><a href="./pseudos/61-Pm" title="promethium">Pm</a></td>
<td style="width:5%">62<br><a href="./pseudos/62-Sm" title="samarium">Sm</a></td>
<td style="width:5%">63<br><a href="./pseudos/63-Eu" title="europium">Eu</a></td>
<td style="width:5%">64<br><a href="./pseudos/64-Gd" title="gadolinium">Gd</a></td>
<td style="width:5%">65<br><a href="./pseudos/65-Tb" title="terbium">Tb</a></td>
<td style="width:5%">66<br><a href="./pseudos/66-Dy" title="dysprosium">Dy</a></td>
<td style="width:5%">67<br><a href="./pseudos/67-Ho" title="holmium">Ho</a></td>
<td style="width:5%">68<br><a href="./pseudos/68-Er" title="erbium">Er</a></td>
<td style="width:5%">69<br><a href="./pseudos/69-Tm" title="thulium">Tm</a></td>
<td style="width:5%">70<br><a href="./pseudos/70-Yb" title="ytterbium">Yb</a></td>
</tr>

<tr align="center">
<td colspan="2" style="width:5%"><br></td>
<td style="width:5%">89<br>Ac</td>
<td style="width:5%">90<br>Th</td>
<td style="width:5%">91<br>Pa</td>
<td style="width:5%">92<br>U</td>
<td style="width:5%">93<br>Np</td>
<td style="width:5%">94<br>Pu</td>
<td style="width:5%">95<br>Am</td>
<td style="width:5%">96<br>Cm</td>
<td style="width:5%">97<br>Bk</td>
<td style="width:5%">98<br>Cf</td>
<td style="width:5%">99<br>Es</td>
<td style="width:5%">100<br>Fm</td>
<td style="width:5%">101<br>Md</td>
<td style="width:5%">102<br>No</td>
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
