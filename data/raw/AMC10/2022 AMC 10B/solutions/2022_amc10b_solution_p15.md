# 2022 AMC 10B Problem 15

## Problem

Let $S_n$ be the sum of the first $n$ terms of an arithmetic sequence that has a common difference of $2$ . The quotient $\frac{S_{3n}}{S_n}$ does not depend on $n$ . What is $S_{20}$ ?

$\textbf{(A) } 340 \qquad \textbf{(B) } 360 \qquad \textbf{(C) } 380 \qquad \textbf{(D) } 400 \qquad \textbf{(E) } 420$

## Solution 1
Let's say that our sequence is \[a, a+2, a+4, a+6, a+8, a+10, \ldots.\] Then, since the value of n doesn't matter in the quotient $\frac{S_{3n}}{S_n}$ , we can say that \[\frac{S_{3}}{S_1} = \frac{S_{6}}{S_2}.\] Simplifying, we get $\frac{3a+6}{a}=\frac{6a+30}{2a+2}$ , from which \[\frac{3a+6}{a}=\frac{3a+15}{a+1}.\] \[3a^2+9a+6=3a^2+15a\] \[6a=6\] Solving for $a$ , we get that $a=1$ .
Since the sum of the first $n$ odd numbers is $n^2$ , $S_{20} = 20^2 = \boxed{\textbf{(D) } 400}$ .
Note: you could also plug in the formulas for $\frac{S_{3n}}{S_{n}}$ and simplify, getting $3+ \frac{6n}{a+n-1}$ You would then find a= $1$ ~megacleverstarfish15

## Solution 2 (Quick Insight)
Recall that the sum of the first $n$ odd numbers is $n^2$ .
Since $\frac{S_{3n}}{S_{n}} = \frac{9n^2}{n^2} = 9$ , we have $S_{20} = 20^2 = \boxed{\textbf{(D) } 400}$ .
~numerophile

## Solution 3 (I didn't know Solution 1!)
We have a slightly challenging problem :-(, but that's okay!
$\textbf{If you didn't come up with the Solution 1 intuition}$ , then here is a more direct approach.
We want \(\frac{S_{3n}}{S_n}\) to be a natural (\(\frac{S_{3n}}{S_n} > 0\); basically a whole number \(\neq 0\)) number. Then only can the progression be incremental by 2.
Assume that \(a_1 = 1\). Then, \(a_2 = 3\), \(a_3 = 5\), etc. We take the first term \(n=1\), which is 1. Then \(3n\); the next 3 terms will sum to 9. \(\frac{9}{1} = 9\), and this is an arithmetic sequence, and therefore works!
What about \(a_1 = 0\). We immediately see that this would be undefined, so we cannot have \(a_1 = 0\). So we say \(a_1 = 2\). Then the sum for \(n=1\) is 2, and for \(3n\); it is simply 6. This is \(6/2 = 3\), so it works!
Then, what about \(a_2 = 3\)? Then this means that the \(n=2\) sum is 4, and the \(3n\) sum is 36. This is \(36/4 = 9\), and this is the same as the difference before, proving that \(a_1 = 1\) is indeed correct.
And then? What about \(a_2 = 4\)? This means \(n=2\) sum is 6, and the \(3n\) sum is 42, but uh oh, the progression breaks! Therefore, the evens cannot work.
Therefore, \(a_1 = 1\), \(a_{20}\) is just the sum of the first 20 odd numbers, which is $\boxed{\textbf{(D) } 400}$
~Pinotation
### Remark 3.0.1
Hi! It me (Pinotation) again!
If you are confused about why \( a_1 \neq 3 \) or \( a_1 \neq 4 \) or something along those lines, we can prove by induction.
We have \[S_n=\frac{n}{2}\big(2a_1+(n-1)\cdot 2\big)=n(a_1+n-1).\] Then \[S_{3n}=3n(a_1+3n-1),\] so \[\frac{S_{3n}}{S_n}=\frac{3(a_1+3n-1)}{a_1+n-1}.\]
Base case \( n=1 \): \[\frac{S_3}{S_1}=\frac{3(a_1+2)}{a_1}.\]
Suppose for some \( n \) the ratio is independent of \( n \) and equal to a constant \( k \). Then \[\frac{S_{3n}}{S_n}=\frac{3(a_1+3n-1)}{a_1+n-1}=k.\] For \( n+1 \) we must also have \[\frac{S_{3(n+1)}}{S_{n+1}}=\frac{3(a_1+3n+2)}{a_1+n}=k.\] So \[\frac{3(a_1+3n-1)}{a_1+n-1}=\frac{3(a_1+3n+2)}{a_1+n}.\] Cross multiplying gives \[(a_1+3n-1)(a_1+n)=(a_1+3n+2)(a_1+n-1).\] Expanding, \[a_1^2+4na_1+a_1- n -3 = a_1^2+4na_1+a_1+2n-2.\] Simplifying, \[- n -3 = 2n -2,\] so \[3n = -1.\] This is impossible for integer \( n \). The only way the equality can hold for all \( n \) is if the proportionality factor between numerator and denominator is fixed. Comparing coefficients in \[3(a_1+3n-1)=C(a_1+n-1),\] we get \( C=9 \) and hence \[3a_1-3=9a_1-9 \implies a_1=1.\]
I hope this helped! If not, then you can check Solution 1, as it is practically the friendlier version LOL!
~Proof by Pinotation

## Solution 4 (Answer Choices)
Let $a$ be the first element. Then, $S_{20}=20(a+19)$ . Let it equal to all the answer choices respectively, we get $a=-2, -1, 0, 1, 2$ . We test $\frac{S_{3n}}{S_n}$ for each $a$ , using $n=1, 2$ . We can see that for $a=-2, -1, 0$ there exists $n$ to let $S_n=0$ , which implies they are invalid. For $a=2$ we can also see it's invalid, since $\frac{S_3}{S_1}=6\neq7=\frac{S_6}{S_2}$ . Therefore, $a=1$ , and $\boxed{\textbf{(D) } 400}$ is the correct choice.
~metrixgo

## Video Solution (🚀 Solved in 5 min 🚀)
https://youtu.be/7ztNpblm2TY
~Education, the Study of Everything

## Video Solution By SpreadTheMathLove
https://www.youtube.com/watch?v=zHJJyMlH9DA

## Video Solution by Interstigation
https://youtu.be/qkyRBpQHbOA

## Video Solution by TheBeautyofMath
https://youtu.be/Mi2AxPhnRno?t=1299
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .