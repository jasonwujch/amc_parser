# 2022 AMC 10A Problem 17

## Problem

How many three-digit positive integers $\underline{a} \ \underline{b} \ \underline{c}$ are there whose nonzero digits $a,b,$ and $c$ satisfy \[0.\overline{\underline{a}~\underline{b}~\underline{c}} = \frac{1}{3} (0.\overline{a} + 0.\overline{b} + 0.\overline{c})?\] (The bar indicates repetition, thus $0.\overline{\underline{a}~\underline{b}~\underline{c}}$ is the infinite repeating decimal $0.\underline{a}~\underline{b}~\underline{c}~\underline{a}~\underline{b}~\underline{c}~\cdots$ )

$\textbf{(A) } 9 \qquad \textbf{(B) } 10 \qquad \textbf{(C) } 11 \qquad \textbf{(D) } 13 \qquad \textbf{(E) } 14$

## Solution
We rewrite the given equation, then rearrange: \begin{align*} \frac{100a+10b+c}{999} &= \frac13\left(\frac a9 + \frac b9 + \frac c9\right) \\ 100a+10b+c &= 37a + 37b + 37c \\ 63a &= 27b+36c \\ 7a &= 3b+4c. \end{align*} Now, this problem is equivalent to counting the ordered triples $(a,b,c)$ that satisfies the equation.
Clearly, the $9$ ordered triples $(a,b,c)=(1,1,1),(2,2,2),\ldots,(9,9,9)$ are solutions to this equation.
The expression $3b+4c$ has the same value when:
- $b$ increases by $4$ as $c$ decreases by $3.$
- $b$ decreases by $4$ as $c$ increases by $3.$
We find $4$ more solutions from the $9$ solutions above: $(a,b,c)=(4,8,1),(5,1,8),(5,9,2),(6,2,9).$ Note that all solutions are symmetric about $(a,b,c)=(5,5,5).$
Together, we have $9+4=\boxed{\textbf{(D) } 13}$ ordered triples $(a,b,c).$
~MRENTHUSIASM
### Remark
One way to solve the Diophantine Equation, $7a=3b+4c$ is by taking $\pmod{7}$ , from which the equation becomes $0\equiv 3b-3c\pmod{7} \Longrightarrow b\equiv c\pmod{7}$ so either $b=c$ or WLOG $b<c, b+7=c$ .

## Video Solution 1
https://youtu.be/p6IauwE8cX8

## Video Solution (⚡️Lightning Fast⚡️)
https://youtu.be/mgcHM0ATUks
~Education, the Study of Everything

## Video Solution 2
https://www.youtube.com/watch?v=YAazoVATYQA&list=PLmpPPbOoDfgj5BlPtEAGcB7BR_UA5FgFj&index=4

## Video Solution 3 by SpreadTheMathLove
https://www.youtube.com/watch?v=yLkGjQ-atzU&list=PLmpPPbOoDfggaByZonvjv_0Wy7XftFA9L&index=63
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .