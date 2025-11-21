# 2010 AIME I Problem 2

## Problem

Find the remainder when $9 \times 99 \times 999 \times \cdots \times \underbrace{99\cdots9}_{\text{999 9's}}$ is divided by $1000$ .

## Solution
Note that $999\equiv 9999\equiv\dots \equiv\underbrace{99\cdots9}_{\text{999 9's}}\equiv -1 \pmod{1000}$ (see modular arithmetic ). That is a total of $999 - 3 + 1 = 997$ integers, so all those integers multiplied out are congruent to $- 1\pmod{1000}$ . Thus, the entire expression is congruent to $- 1\times9\times99 = - 891\equiv\boxed{109}\pmod{1000}$ .

## Solution 2
The expression also equals $(10-1)(100-1)\dots({10^{999}}-1)$ . To find its modular 1,000, remove all terms from 1,000 and after. Then the expression becomes $(10-1)(100-1)(-1) \pmod{1000} \equiv -891 \pmod{1000} \equiv \boxed{109}\pmod{1000}$
By maxamc

## Video Solution by OmegaLearn
https://youtu.be/orrw4VydBTk?t=140
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=-GD-wvY1ADE&t=78s

## Video Solution by WhyMath
https://youtu.be/EMTcFZB9KvA
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .