# 2003 AIME I Problem 8

## Problem

In an increasing sequence of four positive integers, the first three terms form an arithmetic progression , the last three terms form a geometric progression , and the first and fourth terms differ by $30$ . Find the sum of the four terms.

## Solution
Denote the first term as $a$ , and the common difference between the first three terms as $d$ . The four numbers thus are in the form $a,\ a+d,\ a+2d,\ \frac{(a + 2d)^2}{a + d}$ .
Since the first and fourth terms differ by $30$ , we have that $\frac{(a + 2d)^2}{a + d} - a = 30$ . Multiplying out by the denominator, \[(a^2 + 4ad + 4d^2) - a(a + d) = 30(a + d).\] This simplifies to $3ad + 4d^2 = 30a + 30d$ , which upon rearranging yields $2d(2d - 15) = 3a(10 - d)$ .
Both $a$ and $d$ are positive integers, so $2d - 15$ and $10 - d$ must have the same sign. Try if they are both positive (notice if they are both negative , then $d > 10$ and $d < \frac{15}{2}$ , which is a contradiction). Then, $d = 8, 9$ . Directly substituting and testing shows that $d \neq 8$ , but that if $d = 9$ then $a = 18$ . Alternatively, note that $3|2d$ or $3|2d-15$ implies that $3|d$ , so only $9$ may work. Hence, the four terms are $18,\ 27,\ 36,\ 48$ , which indeed fits the given conditions. Their sum is $\boxed{129}$ .
Postscript
As another option, $3ad + 4d^2 = 30a + 30d$ could be rewritten as follows:
$d(3a + 4d) = 30(a + d)$
$d(3a + 3d)+ d^2 = 30(a + d)$
$3d(a + d)+ d^2 = 30(a + d)$
$(3d - 30)(a + d)+ d^2 = 0$
$3(d - 10)(a + d)+ d^2 = 0$
This gives another way to prove $d<10$ , and when rewritten one last time:
$3(10 -d)(a + d) = d^2$
shows that $d$ must contain a factor of 3.
-jackshi2006
EDIT by NealShrestha: Note that once we reach $3ad + 4d^2 = 30a + 30d$ this implies $3|d$ since all other terms are congruent to $0\mod 3$ .

## Solution 2
The sequence is of the form $a-d,$ $a,$ $a+d,$ $\frac{(a+d)^2}{a}$ . Since the first and last terms differ by 30, we have \[\frac{(a+d)^2}{a}-a+d=30\] \[d^2+3ad=30a\] \[d^2+3ad-30a=0\] \[d=\frac{-3a + \sqrt{9a^2+120a}}{2}.\] Let $9a^2+120a=x^2$ , where $x$ is an integer. This yields the following: \[9a^2+120a-x^2=0\] \[a=\frac{-120 + \sqrt{14400+36x^2}}{18}\] \[a=\frac{-20 + \sqrt{400+x^2}}{3}.\] We then set $400+x^2=y^2$ , where $y$ is an integer. Factoring using difference of squares, we have \[400=2^4 \cdot 5^2=(y+x)(y-x).\] Then, noticing that $y+x > y-x$ , we set up several systems of equations involving the factors of $400$ . The second system we set up in this manner, \[y+x=2^3 \cdot 5^2\] \[y-x=2,\] yields the solution $y=101, x=99$ . Plugging back in, we get that $a=27 \implies d=9$ , so the sequence is $18,$ $27,$ $36,$ $48,$ and the answer is $\boxed{129}.$
- Note: we do not have to check the other systems since the $x$ and $y$ values obtained via this system yield integers for $a$ , $d$ , and this must be the only possible answer since this is an AIME problem. We got very lucky in this sense :)
-Fasolinka

## Solution 3 (Guesswork)
We represent the values as $a-d$ , $a$ , $a+d$ , and $\frac{(a+d)^2}{a}$ Take the difference between the first and last values \[\frac{(a+d)^2}{a}-a+d=30\] Manipulating the values by expanding and then long division we see \[\frac{a^2+2ad+d^2}{a}-a+d=30\] \[\frac{(a+2d)a+d^2}{a}-a+d=30\] \[a+2d+\frac{d^2}{a}-a+d=30\] Combining like terms we get \[3d+\frac{d^2}{a}=30\] And looking at the values we know that since the second term must be positive (since both a and d are positive), $d$ must be a maximum of 9, which offers 9 possible values (since $d$ must be a positive integer.) We can resort to guesswork by this time, and thus receive the result of of $d=9$ at which $a=27$ . The solution is thus $\boxed{129}.$
- We could also lay down some further parameters for the value of $d$ . as $a$ must be greater than $d$ (for the first term to be positive), we can substitite in a "borderline" value of a=d (which itself is just over the limit). This gives us:
\[3d+\frac{d^2}{d}=30\] \[3d+d=30\] \[4d=30\] Thus, d must be greater than 7.5, which gives us only 2 values left (8 and 9). We can then plug in any of the two to see if an integer value is attainable. In the end, 8 doesn't work and 9 does, which gives the solution of $\boxed{129}.$
- Note: This solution is similar to Solution 2
-PMaldonado13
These problems are copyrighted © by the Mathematical Association of America.