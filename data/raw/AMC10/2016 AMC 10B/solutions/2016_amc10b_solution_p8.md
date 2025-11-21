# 2016 AMC 10B Problem 8

## Problem

What is the tens digit of $2015^{2016}-2017?$

$\textbf{(A)}\ 0 \qquad \textbf{(B)}\ 1 \qquad \textbf{(C)}\ 3 \qquad \textbf{(D)}\ 5 \qquad \textbf{(E)}\ 8$

## Solution 1
Notice that, for $n\ge 2$ , $2015^n\equiv 15^n$ is congruent to $25\pmod{100}$ when $n$ is even and $75\pmod{100}$ when $n$ is odd. (Check for yourself). Since $2016$ is even, $2015^{2016} \equiv 25\pmod{100}$ and $2015^{2016}-2017 \equiv 25 - 17 \equiv \underline{0}8\pmod{100}$ .
So the answer is $\textbf{(A)}\ \boxed{0}$ .

## Solution 2
In a very similar fashion, we find that $2015^{2016} \equiv 15^{2016} \pmod{100}$ , which equals $225^{1008}$ . Next, since every power (greater than $0$ ) of every number ending in $25$ will end in $25$ (which can easily be verified), we get $225^{1008} \equiv 25 \pmod{100}$ . (In this way, we don't have to worry about the exponent very much.) Finally, $2017 \equiv 17 \pmod{100}$ , and thus $2015^{2016}-2017 \equiv 25-17 \equiv 08 \pmod{100}$ , as above.

## Solution 3 (exponent pattern)
Since we only need the tens digits, we only need to care about the multiplication of tens and ones. (If you want to use mathematical terms then we only need to look at the exponents in $mod 100$ .) We will use the " $\equiv$ " sign to denote congruence in modulus, basically taking the last two digits and ignoring everything else.
\[\begin{split} 15^{1}\equiv15 \\ 15^{2}\equiv25 \end{split}\] From here we only need to multiply $15\cdot25$ and we can ignore the hundreds digits. \[\begin{split} 15^{3}\equiv75 \\ 15^{4}\equiv25 \\ 15^{5}\equiv75 \end{split}\] Notice that for every $x\neq1$ , $15^{x}\equiv25$ if $x$ is even, and $15^{x}\equiv75$ if $x$ is odd. Since $2015^{2016}$ has an even exponent, we conclude that the last two digits will be $25$ , and subtracting $25-17=\underline{0}8 \Longrightarrow \boxed{\textbf{(A)}\ 0}$ . ~JH. L

## Video Solution (CREATIVE THINKING)
https://youtu.be/jDHIJ8o4VSA
~Education, the Study of Everything

## Video Solution
https://youtu.be/GVPF6CcCugU
~savannahsolver

## Video Solution
https://youtu.be/zfChnbMGLVQ?t=2683
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .