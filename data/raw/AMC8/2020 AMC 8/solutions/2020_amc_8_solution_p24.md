# 2020 AMC 8 Problem 24

## Problem

A large square region is paved with $n^2$ gray square tiles, each measuring $s$ inches on a side. A border $d$ inches wide surrounds each tile. The figure below shows the case for $n=3$ . When $n=24$ , the $576$ gray tiles cover $64\%$ of the area of the large square region. What is the ratio $\frac{d}{s}$ for this larger value of $n?$

[asy] draw((0,0)--(13,0)--(13,13)--(0,13)--cycle); filldraw((1,1)--(4,1)--(4,4)--(1,4)--cycle, mediumgray); filldraw((1,5)--(4,5)--(4,8)--(1,8)--cycle, mediumgray); filldraw((1,9)--(4,9)--(4,12)--(1,12)--cycle, mediumgray); filldraw((5,1)--(8,1)--(8,4)--(5,4)--cycle, mediumgray); filldraw((5,5)--(8,5)--(8,8)--(5,8)--cycle, mediumgray); filldraw((5,9)--(8,9)--(8,12)--(5,12)--cycle, mediumgray); filldraw((9,1)--(12,1)--(12,4)--(9,4)--cycle, mediumgray); filldraw((9,5)--(12,5)--(12,8)--(9,8)--cycle, mediumgray); filldraw((12,12)--(12,9)--(9,9)--(9,12)--cycle, mediumgray); [/asy]

$\textbf{(A) }\frac{6}{25} \qquad \textbf{(B) }\frac{1}{4} \qquad \textbf{(C) }\frac{9}{25} \qquad \textbf{(D) }\frac{7}{16} \qquad \textbf{(E) }\frac{9}{16}$

## Solution 1
The area of the shaded region is $(24s)^2$ . To find the area of the large square, we note that there is a $d$ -inch border between each of the $23$ pairs of consecutive squares, as well as from between the first/last squares and the large square, for a total of $23+2 = 25$ times the length of the border, i.e. $25d$ . Adding this to the total length of the consecutive squares, which is $24s$ , the side length of the large square is $(24s+25d)$ , yielding the equation $\frac{(24s)^2}{(24s+25d)^2}=\frac{64}{100}$ . Taking the square root of both sides (and using the fact that lengths are non-negative) gives $\frac{24s}{24s+25d}=\frac{8}{10} = \frac{4}{5}$ , and cross-multiplying now gives $120s = 96s + 100d \Rightarrow 24s = 100d \Rightarrow \frac{d}{s} = \frac{24}{100} = \boxed{\textbf{(A) }\frac{6}{25}}$ .
Note: Once we obtain $\tfrac{24s}{24s+25d} = \tfrac{4}{5},$ to ease computation, we may take the reciprocal of both sides to yield $\tfrac{24s+25d}{24s} = 1 + \tfrac{25d}{24s} = \tfrac{5}{4},$ so $\tfrac{25d}{24s} = \tfrac{1}{4}.$ Multiplying both sides by $\tfrac{24}{25}$ yields the same answer as before.
~peace09
~Minor Edits by WrenMath

## Solution 2
WLOG (Without Loss of Generality), we may let $s=1$ (since $d$ will be determined by the scale of $s$ , and we are only interested in the ratio $\frac{d}{s}$ ). Then, as the total area of the $576$ gray tiles is simply $576$ , the large square has area $\frac{576}{0.64} = 900$ , making the side of the large square $\sqrt{900}=30$ . As in Solution 1, the side length of the large square consists of the total length of the gray tiles and $25$ lots of the border, so the length of the border is $d = \frac{30-24}{25} = \frac{6}{25}$ . Since $\frac{d}{s}=d$ if $s=1$ , the answer is $\boxed{\textbf{(A) }\frac{6}{25}}$ .

## Solution 3 (using answer choices)
As in Solution 2, we let $s = 1$ without loss of generality. For sufficiently large $n$ , we can approximate the percentage of the area covered by the gray tiles by subdividing most of the region into congruent squares, as shown: [asy] draw((0,0)--(13,0)--(13,13)--(0,13)--cycle); filldraw((1,1)--(4,1)--(4,4)--(1,4)--cycle, mediumgray); filldraw((1,5)--(4,5)--(4,8)--(1,8)--cycle, mediumgray); filldraw((1,9)--(4,9)--(4,12)--(1,12)--cycle, mediumgray); filldraw((5,1)--(8,1)--(8,4)--(5,4)--cycle, mediumgray); filldraw((5,5)--(8,5)--(8,8)--(5,8)--cycle, mediumgray); filldraw((5,9)--(8,9)--(8,12)--(5,12)--cycle, mediumgray); filldraw((9,1)--(12,1)--(12,4)--(9,4)--cycle, mediumgray); filldraw((9,5)--(12,5)--(12,8)--(9,8)--cycle, mediumgray); filldraw((9,9)--(12,9)--(12,12)--(9,12)--cycle, mediumgray); for(int i = 1; i <= 13; i += 4){ draw((1,i)--(13,i), red); draw((i,1)--(i,13), red); } [/asy] Each red square has side length $(1+d)$ , so by solving $\frac{1^2}{(1+d)^2} = \frac{64}{100} \iff \frac{1}{1+d} = \frac{4}{5}$ , we obtain $d = \frac{1}{4}$ . The actual fraction of the total area covered by the gray tiles will be slightly less than $\frac{1}{(1+d)^2}$ , which implies $\frac{1}{(1+d)^2} > \frac{64}{100} \iff \frac{1}{1+d} > \frac{4}{5} \iff d < \frac{1}{4}$ . Hence $d$ (and thus $\frac{d}{s}$ , since we are assuming $s=1$ ) is less than $\frac{1}{4}$ , and the only choice that satisfies this is $\boxed{\textbf{(A) }\frac{6}{25}}$ .

## Video Solution by TheMathGeek
https://www.youtube.com/watch?v=IsqueKZCKbk&t=11s
~TheMathGeek

## Video Solution by Math-X
https://youtu.be/UnVo6jZ3Wnk?si=Qs8zS0YEfg1iP-Y2&t=5584
~Math-X

## Video Solution
https://www.youtube.com/watch?v=Vnk73Kd8t4o&list=PL73YVYWi-yG8Exr884k6y3eq8VBFMZRIF&index=24
~Education, the Study of Everything

## Video Solution
https://youtu.be/t8MVmKEyUhw

## Video Solution by OmegaLearn
https://youtu.be/UpCURw5Moig?t=31
~ pi_is_3.14

## Video Solution by WhyMath
https://youtu.be/NHYB0VI3dcY
~savannahsolver

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=1515
~Interstigation

## Video Solution by STEMbreezy
https://youtu.be/wq8EUCe5oQU?t=353
~STEMbreezy