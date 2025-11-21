# 2021 AMC 10B Problem 13

## Problem

Let $n$ be a positive integer and $d$ be a digit such that the value of the numeral $\underline{32d}$ in base $n$ equals $263$ , and the value of the numeral $\underline{324}$ in base $n$ equals the value of the numeral $\underline{11d1}$ in base six. What is $n + d ?$

$\textbf{(A)} ~10 \qquad\textbf{(B)} ~11 \qquad\textbf{(C)} ~13 \qquad\textbf{(D)} ~15 \qquad\textbf{(E)} ~16$

## Solution 1
We can start by setting up an equation to convert $\underline{32d}$ base $n$ to base 10. To convert this to base 10, it would be $3{n}^2+2n+d.$ Because it is equal to 263, we can set this equation to 263. Finally, subtract $d$ from both sides to get $3{n}^2+2n = 263-d$ .
We can also set up equations to convert $\underline{324}$ base $n$ and $\underline{11d1}$ base 6 to base 10. The equation to covert $\underline{324}$ base $n$ to base 10 is $3{n}^2+2n+4.$ The equation to convert $\underline{11d1}$ base 6 to base 10 is ${6}^3+{6}^2+6d+1.$
Simplify ${6}^3+{6}^2+6d+1$ so it becomes $6d+253.$ Setting the above equations equal to each other, we have \[3{n}^2+2n+4 = 6d+253.\] Subtracting 4 from both sides gets $3{n}^2+2n = 6d+249.$
We can then use equations \[3{n}^2+2n = 263-d\] \[3{n}^2+2n = 6d+249\] to solve for $d$ . Set $263-d$ equal to $6d+249$ and solve to find that $d=2$ .
Plug $d=2$ back into the equation $3{n}^2+2n = 263-d$ . Subtract 261 from both sides to get your final equation of $3{n}^2+2n-261 = 0.$ We solve using the quadratic formula to find that the solutions are $9$ and $-29/3.$ Because the base must be positive, $n=9.$
Adding 2 to 9 gets $\boxed{\textbf{(B)} ~11}$
-Zeusthemoose (edited for readability) -solution corrected by Billowingsweater

## Solution 2
$32d$ is greater than $263$ when both are interpreted in base 10, so $n$ is less than $10$ . Some trial and error gives $n=9$ . $263$ in base 9 is $322$ , so the answer is $9+2=\boxed{\textbf{(B)} ~11}$ .
-SmileKat32

## Solution 3
We have \[3n^2 + 2n + d = 263\] \[3n^2 + 2n + 4 = 6^3 + 6^2 + 6d + 1\] Subtracting the 2nd from the 1st equation we get \begin{align*} d-4 &= 263 - (216 + 36 + 6d + 1) \\ &= 263 - 253 - 6d \\ &= 10 - 6d \end{align*} Thus we have $d=2.$ Substituting into the first, we have $3n^2 + 2n + 2 = 263 \Rightarrow 3n^2 + 2n - 261 = 0.$ Factoring, we have $(n-9)(3n+29)=0.$ A digit cannot be negative, so we have $n=9.$ Thus, $d+n=2+9=\boxed{\textbf{(B)} ~11}$
mathboy282 signing off ~ $\LaTeX$ fixed by Lamboreghini

## Solution 4
Find that $d=2$ using one of the methods above. Then we have that $3n^2 + 2n = 261$ . We know that $n$ is an integer, so we can solve the equation $n(3n+2)=261$ (this is guaranteed to have a solution if we did this correctly). The prime factorization of $261$ is $3^2 \cdot 29$ , so the corresponding factor pairs are $(1, 261)$ , $(3,87)$ , and $(9,29)$ . If $n = 9$ , then the equation is true, so $n + d = 9 + 2 = \boxed{\textbf{(B)} ~11}$ .
Note: This solution provides an alternate way to complete the final part of the problem if, like me, you really dislike quadratics. ~ cxsmi

## Video Solution (🚀 Under 4 min 🚀)
https://youtu.be/jm2VbqRpFyI
~ Education, the Study of Everything

## Video Solution by OmegaLearn (Bases and System of Equations)
https://youtu.be/oAc3GdAm6lk
~ pi_is_3.14

## Video Solution by TheBeautyofMath
https://youtu.be/L1iW94Ue3eI?t=880
~IceMatrix

## Video Solution by Interstigation
https://youtu.be/X86a7-pSSSY
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .