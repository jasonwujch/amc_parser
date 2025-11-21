# 2022 AIME II Problem 14

## Problem

For positive integers $a$ , $b$ , and $c$ with $a < b < c$ , consider collections of postage stamps in denominations $a$ , $b$ , and $c$ cents that contain at least one stamp of each denomination. If there exists such a collection that contains sub-collections worth every whole number of cents up to $1000$ cents, let $f(a, b, c)$ be the minimum number of stamps in such a collection. Find the sum of the three least values of $c$ such that $f(a, b, c) = 97$ for some choice of $a$ and $b$ .

## Solution
Notice that we must have $a = 1$ ; otherwise $1$ cent stamp cannot be represented. At least $b-1$ numbers of $1$ cent stamps are needed to represent the values less than $b$ . Using at most $c-1$ stamps of value $1$ and $b$ , it can have all the values from $1$ to $c-1$ cents. Plus $\lfloor \frac{999}{c} \rfloor$ stamps of value $c$ , every value up to $1000$ can be represented.
### Correction:
This should be $\lfloor \frac{1000}{c} \rfloor$ . The current function breaks when $c \mid 1000$ and $b \mid c$ . Take $c = 200$ and $b = 20$ . Then, we have $\lfloor \frac{999}{200} \rfloor = 4$ stamps of value 200, $\lfloor \frac{199}{20} \rfloor = 9$ stamps of value b, and 19 stamps of value 1. The maximum such a collection can give is $200 \cdot 4 + 20 \cdot 9 +19 \cdot 1 = 999$ , just shy of the needed 1000. As for the rest of solution, proceed similarly, except use $1000$ instead of $999$ .
Also, some explanation: $b-1$ one cent stamps cover all residues module $b$ . Having $\lfloor \frac{c-1}{b} \rfloor$ stamps of value b covers all residue classes modulo $c$ . Finally, we just need $\lfloor \frac{1000}{c} \rfloor$ to cover everything up to 1000.
In addition, note that this function sometimes may not always minimize the number of stamps required. This is due to the fact that the stamps of value $b$ and of value $1$ have the capacity to cover values greater than or equal to $c$ (which occurs when $c-1$ has a remainder less than $b-1$ when divided by $b$ ). Thus, in certain cases, not all $\lfloor \frac{1000}{c} \rfloor$ stamps of value c may be necessary, because the stamps of value $b$ and 1 can replace one $c$ .
~ CrazyVideoGamez

## Correction for the correction and the original solution:
Actually, $f(a, b, c) = b + \lceil \frac{c}{b} \rceil + \lceil \frac{1001-b \lceil \frac{c}{b} \rceil}{c} \rceil - 2$ .
This could be obtained by solving the minimum of $A+B+C$ for the system of inequalities $A \geq b-14$ , $A+Bb \geq c$ , and $A+Bb+Cc \geq 1000$ , (Using the inequality adjustment method) where $A$ , $B$ , and $C$ represent the number of $a$ , $b$ , and $c$ postage stamps used. It is possible to get that $A=b-1$ , $B=\lceil \frac{c}{b} \rceil-1$ , $C=\lceil \frac{1001-b \lceil \frac{c}{b} \rceil}{c} \rceil$ . $f(a,b,c)=A+B+C$ yields the above.
Note that in $\text{Case } 2$ , $c=88$ , for the original solution $a=1$ , $b=86$ , $c=88$ , $f(a,b,c)=96$ if the above definition is used.
When $A=85$ , $B=1$ , and $C=10$ , you can get a collection that satisfies the conditions of the problem. $A+B+C=96$ here.
Note that using the correction does not change that the original $f(1,87,88)=97$ .
Under the correction of the correction:
The actual solution could be achieved by using inequalities on the left and right of $f(a,b,c)$ to get
$b+\frac{1001}{c}-3<f(a,b,c)<c+1+\frac{1001}{c}$ .
Similar steps follow after substituting $f(a,b,c)=97$ .
However, $f(1,7,11)=f(1,87,88)=f(1,87,89)=97$ .
Therefore the answer is still $11+88+89=\boxed{188}$ .
~eric-z
————————————————————————————————————
Therefore using $\lfloor \frac{999}{c} \rfloor$ stamps of value $c$ , $\lfloor \frac{c-1}{b} \rfloor$ stamps of value $b$ , and $b-1$ stamps of value $1$ , all values up to $1000$ can be represented in sub-collections, while minimizing the number of stamps.
So, $f(a, b, c) = \lfloor \frac{999}{c} \rfloor + \lfloor \frac{c-1}{b} \rfloor + b-1$ .
$\lfloor \frac{999}{c} \rfloor + \lfloor \frac{c-1}{b} \rfloor + b-1 = 97$ . We can get the answer by solving this equation.
$c > \lfloor \frac{c-1}{b} \rfloor + b-1$
$\frac{999}{c} + c > \lfloor \frac{999}{c} \rfloor + \lfloor \frac{c-1}{b} \rfloor + b-1 = 97$
$c^2 - 97c + 999 > 0$ , $c > 85.3$ or $c < 11.7$
$\lfloor \frac{999}{c} \rfloor + \lfloor \frac{c-1}{b} \rfloor + b-1 > \frac{999}{c}$
$97 > \frac{999}{c}$ , $c>10.3$
The $3$ least values of $c$ are $11$ , $88$ , $89$ . $11 + 88+ 89 = \boxed{\textbf{188}}$
~ isabelchen ~edited by bobjoebilly

## Video Solution
https://youtu.be/jptMMVCuj34
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .