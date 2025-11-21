# 2022 AMC 10A Problem 20

## Problem

A four-term sequence is formed by adding each term of a four-term arithmetic sequence of positive integers to the corresponding term of a four-term geometric sequence of positive integers. The first three terms of the resulting four-term sequence are $57$ , $60$ , and $91$ . What is the fourth term of this sequence?

$\textbf{(A) } 190 \qquad \textbf{(B) } 194 \qquad \textbf{(C) } 198 \qquad \textbf{(D) } 202 \qquad \textbf{(E) } 206$

## Solution 1 (Algebra)
Let the arithmetic sequence be $a,a+d,a+2d,a+3d$ and the geometric sequence be $b,br,br^2,br^3.$
We are given that \begin{align*} a+b&=57, \\ a+d+br&=60, \\ a+2d+br^2&=91, \end{align*} and we wish to find $a+3d+br^3.$
Subtracting the first equation from the second and the second equation from the third, we get \begin{align*} d+b(r-1)&=3, \\ d+br(r-1)&=31. \end{align*} Subtract these results, we get \[b(r-1)^2=28.\] Note that either $(r-1)^2=1$ or $(r-1)^2=4.$ We proceed with casework:
- If $(r-1)^2=1,$ then $r=2,b=28,a=29,$ and $d=-25.$ The arithmetic sequence is $29,4,-21,-46,$ arriving at a contradiction.
- If $(r-1)^2=4,$ then $r=3,b=7,a=50,$ and $d=-11.$ The arithmetic sequence is $50,39,28,17,$ and the geometric sequence is $7,21,63,189.$ This case is valid.
Therefore, The answer is $a+3d+br^3=17+189=\boxed{\textbf{(E) } 206}.$
~mathboy282 ~MRENTHUSIASM

## Solution 2 (Answer Choices)
Start similarly to Solution 1 and deduce the three equations \begin{align*} a+b&=57, \\ a+d+br&=60, \\ a+2d+br^2&=91. \end{align*} Then, add the last two equations and take away the first equation to get $a+3d+br^2+br-b=94$ . We can solve for this in terms of what we want: $a+3d=-br^2-br+b+94$ .
We're looking for $a+3d+br^3$ . We can substitute our value of $a+3d$ in here to get \[br^3-br^2-br+b+94=b(r+1)(r-1)(r-1)+94.\] Since our sequence only has positive integers we can now check by the answer choices. For each answer choice, we can subtract $94$ and factor it to see if it has a perfect square factor and at least one other factor and those should differ by $2$ . \begin{alignat*}{8} \textbf{(A)} \ 190-94&=96&&=2^5\cdot3, \\ \textbf{(B)} \ 194-94&=100&&=2^2\cdot5^2, \\ \textbf{(C)} \ 198-94&=104&&=2^3\cdot13, \\ \textbf{(D)} \ 202-94&=108&&=2^2\cdot3^3, \\ \textbf{(E)} \ 206-94&=112&&=2^4\cdot7. \end{alignat*} From this, the only possible answer choices are $\textbf{(A)}$ and $\textbf{(E)}$ , where $r=3$ . To solve for $b$ , we look back to the given equations above.
We are looking for $a+3d+27b$ . If $\textbf{(A)}$ were the answer, then we know that $a$ would have to be divisible by $3$ and $b$ would equal $6$ . Looking at our second equation, if this were the case, then $d$ would also have to be divisible by $3$ . However, this contradicts the third equation, as all variables are divisible by $3$ , but their sum isn't. So, $\boxed{\textbf{(E) } 206}$ is our answer.

## Video Solution (🚀Just 4 min!🚀)
https://youtu.be/P13VHc26Sgo ~ Education, the Study of Everything

## Video Solution by OmegaLearn
https://youtu.be/DBHhSX8oVME
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .