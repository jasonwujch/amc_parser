# 2023 AIME II Problem 12

## Problem

In $\triangle ABC$ with side lengths $AB = 13,$ $BC = 14,$ and $CA = 15,$ let $M$ be the midpoint of $\overline{BC}.$ Let $P$ be the point on the circumcircle of $\triangle ABC$ such that $M$ is on $\overline{AP}.$ There exists a unique point $Q$ on segment $\overline{AM}$ such that $\angle PBQ = \angle PCQ.$ Then $AQ$ can be written as $\frac{m}{\sqrt{n}},$ where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

## Solution 1
Because $M$ is the midpoint of $BC$ , following from the Stewart's theorem, $AM = 2 \sqrt{37}$ .
Because $A$ , $B$ , $C$ , and $P$ are concyclic, $\angle BPA = \angle C$ , $\angle CPA = \angle B$ .
Denote $\theta = \angle PBQ$ .
In $\triangle BPQ$ , following from the law of sines, \[ \frac{BQ}{\sin \angle BPA} = \frac{PQ}{\sin \angle PBQ} \]
Thus, \[ \frac{BQ}{\sin C} = \frac{PQ}{\sin \theta} . \hspace{1cm} (1) \]
In $\triangle CPQ$ , following from the law of sines, \[ \frac{CQ}{\sin \angle CPA} = \frac{PQ}{\sin \angle PCQ} \]
Thus, \[ \frac{CQ}{\sin B} = \frac{PQ}{\sin \theta} . \hspace{1cm} (2) \]
Taking $\frac{(1)}{(2)}$ , we get \[ \frac{BQ}{\sin C} = \frac{CQ}{\sin B} \]
In $\triangle ABC$ , following from the law of sines, \[ \frac{AB}{\sin C} = \frac{AC}{\sin B} . \hspace{1cm} (3) \]
Thus, Equations (2) and (3) imply \begin{align*} \frac{BQ}{CQ} & = \frac{AB}{AC} \\ & = \frac{13}{15} . \hspace{1cm} (4) \end{align*}
Next, we compute $BQ$ and $CQ$ .
We have \begin{align*} BQ^2 & = AB^2 + AQ^2 - 2 AB\cdot AQ \cos \angle BAQ \\ & = AB^2 + AQ^2 - 2 AB\cdot AQ \cos \angle BAM \\ & = AB^2 + AQ^2 - 2 AB\cdot AQ \cdot \frac{AB^2 + AM^2 - BM^2}{2 AB \cdot AM} \\ & = AB^2 + AQ^2 - AQ \cdot \frac{AB^2 + AM^2 - BM^2}{AM} \\ & = 169 + AQ^2 - \frac{268}{2 \sqrt{37}} AQ . \hspace{1cm} (5) \end{align*}
We have \begin{align*} CQ^2 & = AC^2 + AQ^2 - 2 AC\cdot AQ \cos \angle CAQ \\ & = AC^2 + AQ^2 - 2 AC\cdot AQ \cos \angle CAM \\ & = AC^2 + AQ^2 - 2 AC\cdot AQ \cdot \frac{AC^2 + AM^2 - CM^2}{2 AC \cdot AM} \\ & = AC^2 + AQ^2 - AQ \cdot \frac{AC^2 + AM^2 - CM^2}{AM} \\ & = 225 + AQ^2 - \frac{324}{2 \sqrt{37}} AQ . \hspace{1cm} (6) \end{align*}
Taking (5) and (6) into (4), we get $AQ = \frac{99}{\sqrt{148}}$
Therefore, the answer is $99 + 148 = \boxed{\textbf{(247) }}$
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 2
Define $L_1$ to be the foot of the altitude from $A$ to $BC$ . Furthermore, define $L_2$ to be the foot of the altitude from $Q$ to $BC$ . From here, one can find $AL_1=12$ , either using the 13-14-15 triangle or by calculating the area of $ABC$ two ways. Then, we find $BL_1=5$ and $L_1C = 9$ using Pythagorean theorem. Let $QL_2=x$ . By AA similarity, $\triangle{AL_1M}$ and $\triangle{QL_2M}$ are similar. By similarity ratios, \[\frac{AL_1}{L_1M}=\frac{QL_2}{L_2M}\] \[\frac{12}{2}=\frac{x}{L_2M}\] \[L_2M = \frac{x}{6}\] Thus, $BL_2=BM-L_2M=7-\frac{x}{6}$ . Similarly, $CL_2=7+\frac{x}{6}$ . Now, we angle chase from our requirement to obtain new information. \[\angle{PBQ}=\angle{PCQ}\] \[\angle{QCM}+\angle{PCM}=\angle{QBM}+\angle{PBM}\] \[\angle{QCL_2}+\angle{PCM}=\angle{QBL_2}+\angle{PBM}\] \[\angle{PCM}-\angle{PBM}=\angle{QBL_2}-\angle{QCL_2}\] \[\angle{MAB}-\angle{MAC}=\angle{QBL_2}-\angle{QCL_2}\text{(By inscribed angle theorem)}\] \[(\angle{MAL_1}+\angle{L_1AB})-(\angle{CAL_1}-\angle{MAL_1})=\angle{QBL_2}-\angle{QCL_2}\] \[2\angle{MAL_1}+\angle{L_1AB}-\angle{CAL_1}=\angle{QBL_2}-\angle{QCL_2}\] Take the tangent of both sides to obtain \[\tan(2\angle{MAL_1}+\angle{L_1AB}-\angle{CAL_1})=\tan(\angle{QBL_2}-\angle{QCL_2})\] By the definition of the tangent function on right triangles, we have $\tan{MAL_1}=\frac{7-5}{12}=\frac{1}{6}$ , $\tan{CAL_1}=\frac{9}{12}=\frac{3}{4}$ , and $\tan{L_1AB}=\frac{5}{12}$ . By abusing the tangent angle addition formula, we can find that \[\tan(2\angle{MAL_1}+\angle{L_1AB}-\angle{CAL_1})=\frac{196}{2397}\] By substituting $\tan{\angle{QBL_2}}=\frac{6x}{42-x}$ , $\tan{\angle{QCL_2}}=\frac{6x}{42+x}$ and using tangent angle subtraction formula we find that \[x=\frac{147}{37}\] Finally, using similarity formulas, we can find \[\frac{AQ}{AM}=\frac{12-x}{x}\] . Plugging in $x=\frac{147}{37}$ and $AM=\sqrt{148}$ , we find that \[AQ=\frac{99}{\sqrt{148}}\] Thus, our final answer is $99+148=\boxed{247}$ . ~sigma

## Solution 3
It is clear that $BQCP$ is a parallelogram. By Stewart's Theorem, $AM=\sqrt{148}$ , POP on $M$ tells $PM=\frac{49}{\sqrt{148}}$
As $QM=PM, AQ=AM-PM=\frac{99}{\sqrt{148}}$ leads to $\boxed{247}$
~bluesoul (supplemental note: ~Mathavi)
$\textbf{NOTE: Why BQCP is a parallelogram}$
It's not actually immediately clear why this is the case. There are two ways to easily show this:
$\textbf{Competition solution:}$
Notice that the problem statement tells us that point Q is $\textit{unique.}$ EVERY piece of information in the problem statement is intentional, so we should try to use this to our benefit. None of the other solutions do, which is why they are more complicated than they need be.
Consider point Q' s.t. $Q'M = MP$ . Obviously, $\angle Q'CP$ and $\angle Q'BP$ are equal - we have perfect symmetry along line $AP$ . Moreover, $BQ'CP$ is a parallelogram as its diagonals bisect each other. Since point $Q$ is unique, we know that $Q' \textit{is } Q$ . Thus $BQCP$ is a parallelogram. $\blacksquare$ $\newline$ $\textbf{Rigorous proof (not recommended for competition scenario):}$ Consider any quadrilateral $ABCD$ whose diagonals intersect at $O$ s.t. $AO = OC$ and $\angle BAD = \angle BCD$ . We will prove that $ABCD$ is $\textit{either a \textbf{parallelogram} or a \textbf{kite}}$ .
(Note that in our problem, since $AP$ and $BC$ are not orthogonal, ( $ABC$ isn't isosceles) this is enough to show that $BQCP$ is a parallelogram). $\newline$ -- By same base/same altitude, $[ABO] = [CBO]$ and $[ADO] = [CDO] \implies [ABD] = [ABO] + [ADO] = [CBO] + [CDO] = [CBD]. \newline$
Therefore: $\frac{1}{2} sin(\angle BAD) \overline{AB} \times \overline{AD} = \frac{1}{2} sin(\angle BCD) \overline{CB} \times \overline{CD}.$ Since $\angle BAD = \angle BCD$ , this reduces to $\overline{AB} \times \overline{AD} = \overline{CB} \times \overline{CD}. (E.1) \newline$
Let $AB = x$ and $AD = y$ . Then, by $(E.1)$ , $CB = kx$ and $CD = \frac{y}{k}$ for some real $k$ . Then by LoC on $\triangle BAD$ and $\triangle BCD$ : $x^{2} + y^{2} - 2xy cos(\angle BAD) = \overline{BD} = x^{2}k^{2} + \frac{y^{2}}{k^{2}} - 2xy cos(\angle BCD) \newline \implies x^{2} + y^{2} = x^{2}k^{2} + \frac{y^{2}}{k^{2}} \newline \implies (y^{2} - x^{2}k^{2})(k^{2} - 1) = 0.\newline$
-- $y^{2} - x^{2}k^{2} = 0 \implies y = kx \implies AD = BC$ and $AB = CD \implies$ $ABCD$ is a parallelogram.
-- $k^{2} - 1 = 0 \implies k = 1$ ( $k$ cannot be $-1$ ; no negative sided polygons here!) $\implies AB = CB$ and $AD = CD \implies$ $ABCD$ is a kite. $\square$ . ~Mathavi

## Solution 4 (LOS+ coordbash)
First, note that by Law of Sines, $\frac{\sin(\angle{QBP})}{QP}=\frac{\sin(\angle{BPQ})}{BQ}$ and that $\frac{\sin(\angle{QCP})}{QP}=\frac{\sin(\angle{QPC})}{QP}$ . Equating the 2 expressions, you get that $\frac{\sin(\angle{BPQ})}{BQ}=\frac{\sin(\angle{QPC})}{QP}$ . Now drop the altitude from $A$ to $BC$ . As it is commonly known that the dropped altitude forms a $5-12-13$ and a $9-12-15$ triangle, you get the measures of $\angle{ABC}$ and $\angle{ACB}$ respectively, which are $\arcsin(\frac{12}{13})$ and $\arcsin(\frac{4}{5})$ . However, by the inscribed angle theorem, you get that $\angle{BPQ}=\arcsin(\frac{4}{5})$ and that $\angle{QPC}=\arcsin(\frac{12}{13})$ , respectively. Therefore, by Law of Sines (as previously stated) $\frac{BQ}{CQ}=\frac{13}{15}$ .
Now commence coordbashing. Let $B$ be the origin, and $A$ be the point $(5,12)$ . As $AP$ passes through $A$ , which is $(5,12)$ , and $M$ , which is $(7,0)$ , it has the equation $-6x+42$ , so therefore a point on this line can be written as $(x,42-6x)$ . As we have the ratio of the lengths, which prompts us to write the lengths in terms of the distance formula, we can just plug and chug it in to get the ratio $\frac{\sqrt{37x^2-504x+1764}}{\sqrt{37x^2-532x+1960}}=\frac{13}{15}$ . This can be squared to get $\frac{37x^2-504x+1764}{37x^2-532x+1960}=\frac{169}{225}$ . This can be solved to get a solution of $x=\frac{469}{74}$ , and an extraneous solution of $5$ which obviously doesn’t work.
Plugging $x$ into the line equation gets you $y=\frac{147}{37}$ . The distance between this point and $A$ , which is $(5,12)$ is $\sqrt{\frac{9801}{148}}$ , or simplified to $\frac{99}{\sqrt{148}}\Longrightarrow99+148=\boxed{247}$
~dragoon (minor $\LaTeX$ fixes by rhydon516)

## Solution 5 (similar to 3)
We use the law of Cosine and get \[AB^2 = AM^2 + BM^2 - 2 AM \cdot BM \cos \angle AMB,\] \[AC^2 = AM^2 + CM^2 + 2 AM \cdot CM \cos \angle AMB \implies\] \[AM^2 = \frac {AB^2 + AC^2}{2}- BM^2 = \sqrt{148} \approx 12.\] We use the power of point $M$ with respect circumcircle $\triangle ABC$ and get \[AM \cdot MP = BM \cdot CM = BM^2 \implies\] \[PM = \frac {49}{\sqrt {148}} \approx \frac {48}{12} \approx 4 < AM.\] It is clear that if $Q = P,$ then $\angle PBQ = \angle PCQ = 0 \implies$
if $Q$ is symmetric to $P$ with respect $M$ then $\angle PBQ = \angle PCQ.$
There exists a unique point $Q$ on segment $\overline{AM}, PM < AM \implies$ \[PQ = AM - PM = \frac{99}{\sqrt{148}} \implies \boxed{247}.\] vladimir.shelomovskii@gmail.com, vvsss

## Solution 6
We will first find $AM$ by Stewart's Theorem. Hence:
$15^{2} \cdot 7 + 13^{2} \cdot 7 = 14 \cdot 7 \cdot 7 + d^{2} \cdot 14$
Where $d = AM$ . Now simplifying:
$225 + 169 = 98 + 2d^{2}$
Which means:
$d^{2} = 148$ or $d = \sqrt{148}$ .
Now we need to find $PM = QM$ because $M$ is the midpoint of both $BC$ and $PQ$ . In fact, we will find $PM$ and the answer will just be $AM - PM = \sqrt{148} - PM$ .
Let $BP = x$ and $PC = y$ and $PM = z$ . Note that we can again apply Stewart's Theorem on triangle $BPC$
$7x^{2} + 7y^{2} = 14 \cdot 7 \cdot 7 + 14z^{2}$
This yields:
$x^{2} + y^{2} = 98 + 2z^{2}$
And now, it remains to find $x$ and $y$ which can easily find using similar triangles and arc lengths. We will show triangle $BPM$ is similar to triangle $AMC$ and triangle $PMC$ is similar to triangle $ABM$ . Now notice $\angle MBP = \angle MAC$ because they both intercept the same circular arc $PC$ . Next, $\angle BMP = \angle AMC$ by vertical angles. Hence, we have an Angle-Angle similarity and thus triangles $BPM$ and $AMC$ are similar. We could do the same for triangle $PMC$ . Note that $\angle MCP = \angle BAM$ because they both intercept the same circular arc $BP$ and $\angle CMP = \angle AMB$ by vertical angles. Hence, we again have Angle-Angle similarity and thus triangles $PMC$ is similar to triangle $ABM$ . Now, we bring out the similarity ratios to solve for $x$ and $y$ and finish the problem. Note that we can solve for $x$ and $y$ by noticing $\frac{BP}{AC} = \frac{BM}{AM}$ and $\frac{PC}{AB} = \frac{MC}{AM}$ . Hence, we can substitute values to get
$\frac{x}{15} = \frac{7}{\sqrt{148}}$ and $\frac{y}{13} = \frac{7}{\sqrt{148}}$ . Solving, $x = \frac{105}{\sqrt{148}}$ and $y = \frac{91}{\sqrt{148}}$ . Recall that we found $x^{2} + y^{2} = 98 + 2z^{2}$ . Now, we can solve:
$\frac{105^{2}}{148} + \frac{91^{2}}{148} = 98 + 2z^{2}$
To simplify this, note that we have to solve:
$\frac{105^{2} + 91^{2}}{148} = 98 + 2z^{2}$
Let's focus on $105^{2} + 91^{2}$ for now. Interestingly enough, both numbers are centered around $98$ which means notice $105 = 98 + 7$ and $91 = 98 - 7$ . We can simplify this expression by using this fact to get $(98 + 7)^{2} + (98 - 7)^{2} = 98^{2} + 49 + 98^{2} + 49 = 2 \cdot 98^{2} + 98$ .
Now, we have:
$\frac{2 \cdot 98^{2} + 98}{148} = 98 + 2z^{2}$
Note that now we have:
$\frac{ 2 \cdot 98 \cdot 98 + 98 - 98 \cdot 148}{148} = 2z^{2}$
This yields:
$\frac{98(196 + 1 - 148)}{148} = 2z^{2}$
Now we have:
$\frac{98 \cdot 49}{148} = 2z^{2}$
We can cancel out the 2's and simplify to be left with:
$\frac{49}{\sqrt{148}} = z = PM$ .
Finally, the answer is $AM - PM = \sqrt{148} - \frac{49}{\sqrt{148}} = \frac{148 - 49}{\sqrt{148}} = \frac{99}{\sqrt{148}}$ which yields a final answer to $99 + 148 = \boxed{247}$ .
$\textbf{Supplement: Proof of why M is also the midpoint of PQ}$
In this solution, I claimed that $M$ is also the midpoint of $PQ$ . In fact, we could prove this by noting that because $\angle CQM$ and and $\angle MBP$ share the same circular arc $PC$ , these angles are congruent. Note that $\angle BMP = \angle QMC$ by vertical angles and note that $BM = CM = 7$ . We have Angle-Side-Angle congruence that hence triangle $BMP$ is congruent to triangle $QMC$ and hence $QM = MP$ proving the claim. You could also refer to Solution 3's supplements of the proofs that $BQPC$ is actually a parallelogram.
~ilikemath247365

## Video Solution 1
https://www.youtube.com/watch?v=qm9Sg1tEJJE

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=k6hEFEVVzMI
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .