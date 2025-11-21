# 2021 AMC 10A Problem 4

## Problem

A cart rolls down a hill, travelling $5$ inches the first second and accelerating so that during each successive $1$ -second time interval, it travels $7$ inches more than during the previous $1$ -second interval. The cart takes $30$ seconds to reach the bottom of the hill. How far, in inches, does it travel?

$\textbf{(A)} ~215 \qquad\textbf{(B)} ~360\qquad\textbf{(C)} ~2992\qquad\textbf{(D)} ~3195\qquad\textbf{(E)} ~3242$

## Solution 1 (Arithmetic Series)
Since \[\mathrm{Distance}=\mathrm{Speed}\cdot\mathrm{Time},\] we seek the sum \[5\cdot1+12\cdot1+19\cdot1+26\cdot1+\cdots=5+12+19+26+\cdots,\] in which there are $30$ terms.
The last term is $5+7\cdot(30-1)=208.$ Therefore, the requested sum is \[5+12+19+26+\cdots+208=\frac{5+208}{2}\cdot30=\boxed{\textbf{(D)} ~3195}.\] Recall that to find the sum of an arithmetic series, we take the average of the first and last terms, then multiply by the number of terms: \[\mathrm{Sum}=\frac{\mathrm{First}+\mathrm{Last}}{2}\cdot\mathrm{Count}.\] ~MRENTHUSIASM

## Solution 2 (Arithmetic Series)
The distance (in inches) traveled within each $1$ -second interval is: \[5,5+1(7),5+2(7), \dots , 5+29(7).\] This is an arithmetic sequence so the total distance travelled, found by summing them up is: \[\text{number of terms} \cdot \text{average of terms} = \text{number of terms} \cdot \dfrac{\text{first term}+\text{last term}}{2}.\] Or, \[30 \cdot \dfrac{5+5+29(7)}{2} = 15 \cdot 213 = \boxed{\textbf{(D)} ~3195}.\] ~BakedPotato66

## Solution 3 (Answer Choices and Modular Arithmetic)
From the $30$ -term sum \[5+12+19+26+\cdots\] in Solution 1, taking modulo $10$ gives \[5+12+19+26+\cdots \equiv 3\cdot(5+2+9+6+3+0+7+4+1+8) = 3\cdot45\equiv5 \pmod{10}.\] The only answer choices congruent to $5$ modulo $10$ are $\textbf{(A)}$ and $\textbf{(D)}.$ By a quick estimation, $\textbf{(A)}$ is too small, leaving us with $\boxed{\textbf{(D)} ~3195}.$
~MRENTHUSIASM

## Solution 4 (Motion With Constant Acceleration)
This problem can be solved by physics method. This method is perhaps the quickest too and shows the beauty of the problem. The average speed increases $7 \ \text{in/s}$ per second. So, the acceleration $a=7 \ \text{in/s\textsuperscript{2}}.$ The average speed of the first second is $5 \ \text{in/s}.$ We can know the initial velocity $v_0=5-0.5\cdot7=1.5.$ (Because of the formula for the distance traveled in the $k$ th one-second interval being $\Delta x_k = v_0 + a\left(k - \tfrac{1}{2}\right)$ ). The displacement at $t=30$ is \[s=\frac{1}{2}at^2+v_0t=\frac{1}{2}\cdot7\cdot30^2+1.5\cdot30= \boxed{\textbf{(D)} ~3195}.\] ~Bran_Qin

## Video Solution by OmegaLearn
https://youtu.be/7NSfDCJFRUg
~ pi_is_3.14

## Video Solution (Simple and Quick)
https://youtu.be/qLDkSnxLvxM
~ Education, the Study of Everything

## Video Solution (Arithmetic Sequence but in a Different Way)
https://www.youtube.com/watch?v=sJa7uB-UoLc&list=PLexHyfQ8DMuKqltG3cHT7Di4jhVl6L4YJ&index=4
~ North America Math Contest Go Go Go

## Video Solution
https://youtu.be/aO-GklwkBfI
~savannahsolver

## Video Solution by TheBeautyofMath
https://youtu.be/50CThrk3RcM?t=262
~IceMatrix

## Video Solution by The Learning Royal
https://youtu.be/slVBYmcDMOI
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .