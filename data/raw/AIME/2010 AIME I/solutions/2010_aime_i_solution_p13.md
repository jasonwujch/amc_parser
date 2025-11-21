# 2010 AIME I Problem 13

## Problem

Rectangle $ABCD$ and a semicircle with diameter $AB$ are coplanar and have nonoverlapping interiors. Let $\mathcal{R}$ denote the region enclosed by the semicircle and the rectangle. Line $\ell$ meets the semicircle, segment $AB$ , and segment $CD$ at distinct points $N$ , $U$ , and $T$ , respectively. Line $\ell$ divides region $\mathcal{R}$ into two regions with areas in the ratio $1: 2$ . Suppose that $AU = 84$ , $AN = 126$ , and $UB = 168$ . Then $DA$ can be represented as $m\sqrt {n}$ , where $m$ and $n$ are positive integers and $n$ is not divisible by the square of any prime. Find $m + n$ .

## Solution
### Diagram

## Solution 1
The center of the semicircle is also the midpoint of $AB$ . Let this point be O. Let $h$ be the length of $AD$ .
Rescale everything by 42, so $AU = 2, AN = 3, UB = 4$ . Then $AB = 6$ so $OA = OB = 3$ .
Since $ON$ is a radius of the semicircle, $ON = 3$ . Thus $OAN$ is an equilateral triangle.
Let $X$ , $Y$ , and $Z$ be the areas of triangle $OUN$ , sector $ONB$ , and trapezoid $UBCT$ respectively.
$X = \frac {1}{2}(UO)(NO)\sin{O} = \frac {1}{2}(1)(3)\sin{60^\circ} = \frac {3}{4}\sqrt {3}$
$Y = \frac {1}{3}\pi(3)^2 = 3\pi$
To find $Z$ we have to find the length of $TC$ . Project $T$ and $N$ onto $AB$ to get points $T'$ and $N'$ . Notice that $UNN'$ and $TUT'$ are similar. Thus:
$\frac {TT'}{UT'} = \frac {UN'}{NN'} \implies \frac {TT'}{h} = \frac {1/2}{3\sqrt {3}/2} \implies TT' = \frac {\sqrt {3}}{9}h$ .
Then $TC = T'C - T'T = UB - TT' = 4 - \frac {\sqrt {3}}{9}h$ . So:
$Z = \frac {1}{2}(BU + TC)(CB) = \frac {1}{2}\left(8 - \frac {\sqrt {3}}{9}h\right)h = 4h - \frac {\sqrt {3}}{18}h^2$
Let $L$ be the area of the side of line $l$ containing regions $X, Y, Z$ . Then
$L = X + Y + Z = \frac {3}{4}\sqrt {3} + 3\pi + 4h - \frac {\sqrt {3}}{18}h^2$
Obviously, the $L$ is greater than the area on the other side of line $l$ . This other area is equal to the total area minus $L$ . Thus:
$\frac {2}{1} = \frac {L}{6h + \frac {9}{2}{\pi} - L} \implies 12h + 9\pi = 3L$ .
Now just solve for $h$ .
\begin{align*} 12h + 9\pi & = \frac {9}{4}\sqrt {3} + 9\pi + 12h - \frac {\sqrt {3}}{6}h^2 \\ 0 & = \frac {9}{4}\sqrt {3} - \frac {\sqrt {3}}{6}h^2 \\ h^2 & = \frac {9}{4}(6) \\ h & = \frac {3}{2}\sqrt {6} \end{align*}
Don't forget to un-rescale at the end to get $AD = \frac {3}{2}\sqrt {6} \cdot 42 = 63\sqrt {6}$ .
Finally, the answer is $63 + 6 = \boxed{069}$ .

## Solution 2
Let $O$ be the center of the semicircle. It follows that $AU + UO = AN = NO = 126$ , so triangle $ANO$ is equilateral .
Let $Y$ be the foot of the altitude from $N$ , such that $NY = 63\sqrt{3}$ and $NU = 21$ .
Finally, denote $DT = a$ , and $AD = x$ . Extend $U$ to point $Z$ so that $Z$ is on $CD$ and $UZ$ is perpendicular to $CD$ . It then follows that $ZT = a-84$ . Since $NYU$ and $UZT$ are similar ,
$\frac {x}{a-84} = \frac {63\sqrt{3}}{21} = 3\sqrt{3}$
Given that line $NT$ divides $R$ into a ratio of $1:2$ , we can also say that
$(x)(\frac{84+a}{2}) + \frac {126^2\pi}{6} - (63)(21)(\sqrt{3}) = (\frac{1}{3})(252x + \frac{126^2\pi}{2})$
where the first term is the area of trapezoid $AUTD$ , the second and third terms denote the areas of $\frac{1}{6}$ a full circle, and the area of $NUO$ , respectively, and the fourth term on the right side of the equation is equal to $R$ . Cancelling out the $\frac{126^2\pi}{6}$ on both sides, we obtain
$(x)(\frac{84+a}{2}) - \frac{252x}{3} = (63)(21)(\sqrt{3})$
By adding and collecting like terms, $\frac{3ax - 252x}{6} = (63)(21)(\sqrt{3})$
$\frac{(3x)(a-84)}{6} = (63)(21)(\sqrt{3})$ .
Since $a - 84 = \frac{x}{3\sqrt{3}}$ ,
$\frac {(3x)(\frac{x}{3\sqrt{3}})}{6} = (63)(21)(\sqrt{3})$
$\frac {x^2}{\sqrt{3}} = (63)(126)(\sqrt{3})$
$x^2 = (63)(126)(3) = (2)(3^5)(7^2)$
$x = AD = (7)(3^2)(\sqrt{6}) = 63\sqrt{6}$ , so the answer is $\boxed{069}.$

## Solution 3
Note that the total area of $\mathcal{R}$ is $252DA + \frac {126^2 \pi}{2}$ and thus one of the regions has area $84DA + \frac {126^2 \pi}{6}$
As in the above solutions we discover that $\angle AON = 60^\circ$ , thus sector $ANO$ of the semicircle has $\frac{1}{3}$ of the semicircle's area.
Similarly, dropping the $N'T'$ perpendicular we observe that $[AN'T'D] = 84DA$ , which is $\frac{1}{3}$ of the total rectangle.
Denoting the region to the left of $\overline {NT}$ as $\alpha$ and to the right as $\beta$ , it becomes clear that if $[\triangle UT'T] = [\triangle NUO]$ then the regions will have the desired ratio.
Using the 30-60-90 triangle, the slope of $NT$ , is ${-3\sqrt{3}}$ , and thus $[\triangle UT'T] = \frac {DA^2}{6\sqrt{3}}$ .
$[NUO]$ is most easily found by $\frac{absin(c)}{2}$ : $[\triangle NUO] = \frac {126*42 * \frac {\sqrt{3}}{2}}{2}$
Equating, $\frac {126*42 * \frac {\sqrt{3}}{2}}{2} = \frac {DA^2}{6\sqrt{3}}$
Solving, $63 * 21 * 3 * 6 = DA^2$
$DA = 63 \sqrt{6} \longrightarrow \boxed {069}$

## Solution 4 (Coordinates)
Like above solutions, note that $ANO$ is equilateral with side length $126,$ where $O$ is the midpoint of $AB.$ Then, if we let $DA=a$ and set origin at $D=(0,0),$ we get $N=(63,a+63\sqrt{3}), U=(84,a).$ Line $NU$ is then $y-a=\sqrt{27}(x-84),$ so it intersects $CA,$ the $x$ -axis, at $x=(a/\sqrt{27}+84),$ giving us point $T.$ Now the area of region $R$ is $252a+\pi(126)^2 / 2,$ so one third of that is $84a+\pi(126)^2 / 6.$
The area of the smaller piece of $R$ is $[AUTD] + [ANU] + [\text{lune} AN] = \frac{1}{2} \cdot a(84+\frac{a}{\sqrt{27}}+84)+\frac{1}{2} \cdot 84 \cdot 63 \sqrt{3}+ \frac{\pi (126)^2}{6}-\frac{1}{2} \cdot 126 \cdot 63 \sqrt{2}$ $=\frac{a^2}{2\sqrt{27}}+84a-21\cdot 63\sqrt{2} + \frac{\pi(126)^2}{6}.$ Setting this equal to $84a+\pi(126)^2 / 6$ and canceling the $84a + \pi(126)^2$ yields $\frac{a^2}{2\sqrt{27}}=21 \cdot 63 \sqrt{3},$ so $a = 63 \sqrt{6}$ and the anser is $\boxed{069}.$ ~ rzlng

## Solution 5 (Minimal calculation)
Once we establish that $\Delta ANO$ is equilateral, we have \[[{\rm Sector } BON] = 2[{\rm Sector } AON], [BCT'U]=2[ADT'U]\] \[\Rightarrow [\overset{\large\frown}{NB} CT'UO]=2[\overset{\large\frown}{NA} DT'UO]\] On the other hand, \[[\overset{\large\frown}{NB} CT]=2[\overset{\large\frown}{NA} DT]\] Therefore, $[UT'T]=[NUO]$ .
Now, $UO=42, NU=21 \Rightarrow [UT'T]=[NUO]=2[NN'U]$ . Also $\Delta UT'T \sim \Delta NN'U$ . Therefore, \[DA=UT'=\sqrt{2} NN'=\sqrt{2} \left(\frac{\sqrt{3}}{2}\cdot 126\right)=63\sqrt{6}\longrightarrow \boxed {069}\]
~asops

## Video Solution
2010 AIME I #13
MathProblemSolvingSkills.com
### See Also
- <url>viewtopic.php?t=338915 Discussion</url>, with a Geogebra diagram.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .