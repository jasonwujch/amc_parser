# 2021 AIME II Problem 15

## Problem

Let $f(n)$ and $g(n)$ be functions satisfying \[f(n) = \begin{cases}\sqrt{n} & \text{ if } \sqrt{n} \text{ is an integer}\\ 1 + f(n+1) & \text{ otherwise} \end{cases}\] and \[g(n) = \begin{cases}\sqrt{n} & \text{ if } \sqrt{n} \text{ is an integer}\\ 2 + g(n+2) & \text{ otherwise} \end{cases}\] for positive integers $n$ . Find the least positive integer $n$ such that $\tfrac{f(n)}{g(n)} = \tfrac{4}{7}$ .

## Solution 1
Consider what happens when we try to calculate $f(n)$ where n is not a square. If $k^2<n<(k+1)^2$ for (positive) integer k, recursively calculating the value of the function gives us $f(n)=(k+1)^2-n+f((k+1)^2)=k^2+3k+2-n$ . Note that this formula also returns the correct value when $n=(k+1)^2$ , but not when $n=k^2$ . Thus $f(n)=k^2+3k+2-n$ for $k^2<n \leq (k+1)^2$ .
If $2 \mid (k+1)^2-n$ , $g(n)$ returns the same value as $f(n)$ . This is because the recursion once again stops at $(k+1)^2$ . We seek a case in which $f(n)<g(n)$ , so obviously this is not what we want. We want $(k+1)^2,n$ to have a different parity, or $n, k$ have the same parity. When this is the case, $g(n)$ instead returns $(k+2)^2-n+g((k+2)^2)=k^2+5k+6-n$ .
Write $7f(n)=4g(n)$ , which simplifies to $3k^2+k-10=3n$ . Notice that we want the LHS expression to be divisible by 3; as a result, $k \equiv 1 \pmod{3}$ . We also want n to be strictly greater than $k^2$ , so $k-10>0, k>10$ . The LHS expression is always even (since $3k^2+k-10$ factors to $k(3k+1)-10$ , and one of $k$ and $3k+1$ will be even), so to ensure that $k$ and $n$ share the same parity, $k$ should be even. Then the least $k$ that satisfies these requirements is $k=16$ , giving $n=258$ .
Indeed - if we check our answer, it works. Therefore, the answer is $\boxed{258}$ .
-Ross Gao

## Solution 2 (Four Variables)
We consider $f(n)$ and $g(n)$ separately:
- $\boldsymbol{f(n)}$ We restrict in which for some positive integer or for some integer such that By recursion, we get
- $\boldsymbol{g(n)}$ If and have the same parity, then we get by a similar process from This contradicts the precondition Therefore, and must have different parities, from which and must have the same parity. It follows that or for some integer such that By recursion, we get
- Answer By and we have From and equating the expressions for gives Solving for produces We substitute into then simplify, cross-multiply, and rearrange: Since we know that must be divisible by and must be divisible by Recall that the restrictions on and are and respectively. Substituting into either inequality gives Combining all these results produces To minimize in either or we minimize so we minimize and in From and we construct the following table: Finally, we have Substituting this result into either or generates
- Remark We can verify that
We restrict $n$ in which $k^2<n\leq(k+1)^2$ for some positive integer $k,$ or \[n=(k+1)^2-p\hspace{40mm}(1)\] for some integer $p$ such that $0\leq p<2k+1.$ By recursion, we get \begin{align*} f\left((k+1)^2\right)&=k+1, \\ f\left((k+1)^2-1\right)&=k+2, \\ f\left((k+1)^2-2\right)&=k+3, \\ & \ \vdots \\ f\bigl(\phantom{ }\underbrace{(k+1)^2-p}_{n}\phantom{ }\bigr)&=k+p+1. \hspace{19mm}(2) \\ \end{align*}
If $n$ and $(k+1)^2$ have the same parity, then we get $g(n)=f(n)$ by a similar process from $g\left((k+1)^2\right)=k+1.$ This contradicts the precondition $\frac{f(n)}{g(n)} = \frac{4}{7}.$ Therefore, $n$ and $(k+1)^2$ must have different parities, from which $n$ and $(k+2)^2$ must have the same parity.
It follows that $k^2<n<(k+2)^2,$ or \[n=(k+2)^2-2q\hspace{38.25mm}(3)\] for some integer $q$ such that $0<q<2k+2.$ By recursion, we get \begin{align*} g\left((k+2)^2\right)&=k+2, \\ g\left((k+2)^2-2\right)&=k+4, \\ g\left((k+2)^2-4\right)&=k+6, \\ & \ \vdots \\ g\bigl(\phantom{ }\underbrace{(k+2)^2-2q}_{n}\phantom{ }\bigr)&=k+2q+2. \hspace{15.5mm}(4) \\ \end{align*}
By $(2)$ and $(4),$ we have \[\frac{f(n)}{g(n)}=\frac{k+p+1}{k+2q+2}=\frac{4}{7}. \hspace{27mm}(5)\] From $(1)$ and $(3),$ equating the expressions for $n$ gives $(k+1)^2-p=(k+2)^2-2q.$ Solving for $k$ produces \[k=\frac{2q-p-3}{2}. \hspace{41.25mm}(6)\] We substitute $(6)$ into $(5),$ then simplify, cross-multiply, and rearrange: \begin{align*} \frac{\tfrac{2q-p-3}{2}+p+1}{\tfrac{2q-p-3}{2}+2q+2}&=\frac{4}{7} \\ \frac{p+2q-1}{-p+6q+1}&=\frac{4}{7} \\ 7p+14q-7&=-4p+24q+4 \\ 11p-11&=10q \\ 11(p-1)&=10q. \hspace{29mm}(7) \end{align*} Since $\gcd(11,10)=1,$ we know that $p-1$ must be divisible by $10,$ and $q$ must be divisible by $11.$
Recall that the restrictions on $(1)$ and $(2)$ are $0\leq p<2k+1$ and $0<q<2k+2,$ respectively. Substituting $(6)$ into either inequality gives $p+1<q.$ Combining all these results produces \[0<p+1<q<2k+2. \hspace{28mm}(8)\] To minimize $n$ in either $(1)$ or $(3),$ we minimize $k,$ so we minimize $p$ and $q$ in $(8).$ From $(6)$ and $(7),$ we construct the following table: \[\begin{array}{c|c|c|c} & & & \\ [-2.5ex] \boldsymbol{p} & \boldsymbol{q} & \boldsymbol{k} & \textbf{Satisfies }\boldsymbol{(8)?} \\ [0.5ex] \hline & & & \\ [-2ex] 11 & 11 & 4 & \\ 21 & 22 & 10 & \\ 31 & 33 & 16 & \checkmark \\ \geq41 & \geq44 & \geq22 & \checkmark \\ \end{array}\] Finally, we have $(p,q,k)=(31,33,16).$ Substituting this result into either $(1)$ or $(3)$ generates $n=\boxed{258}.$
We can verify that \[\frac{f(258)}{g(258)}=\frac{1\cdot31+f(258+1\cdot31)}{2\cdot33+g(258+2\cdot33)}=\frac{31+\overbrace{f(289)}^{17}}{66+\underbrace{g(324)}_{18}}=\frac{48}{84}=\frac47.\]
~MRENTHUSIASM

## Solution 3
Since $n$ isn't a perfect square, let $n=m^2+k$ with $0<k<2m+1$ . If $k$ is odd, then $f(n)=g(n)$ . If $k$ is even, then \begin{align*} f(n)&=(m+1)^2-(m^2+k)+(m+1)=3m+2-k, \\ g(n)&=(m+2)^2-(m^2+k)+(m+2)=5m+6-k, \end{align*} from which \begin{align*} 7(3m+2-k)&=4(5m+6-k) \\ m&=3k+10. \end{align*} Since $k$ is even, $m$ is even. Since $k\neq 0$ , the smallest $k$ is $2$ which produces the smallest $n$ : \[k=2 \implies m=16 \implies n=16^2+2=\boxed{258}.\] ~Afo

## Solution 4 (Quadratics With Two Variables)
To begin, note that if $n$ is a perfect square, $f(n)=g(n)$ , so $f(n)/g(n)=1$ , so we must look at values of $n$ that are not perfect squares (what a surprise). First, let the distance between $n$ and the first perfect square greater than or equal to it be $k$ , making the values of $f(n+k)$ and $g(n+k)$ integers. Using this notation, we see that $f(n)=k+f(n+k)$ , giving us a formula for the numerator of our ratio. However, since the function of $g(n)$ does not add one to the previous inputs in the function until a perfect square is achieved, but adds values of two, we can not achieve the value of $\sqrt{n+k}$ in $g(n)$ unless $k$ is an even number. However, this is impossible, since if $k$ was an even number, $f(n)=g(n)$ , giving a ratio of one. Thus, $k$ must be an odd number.
Thus, since $k$ must be an odd number, regardless of whether $n$ is even or odd, to get an integral value in $g(n)$ , we must get to the next perfect square after $n+k$ . To make matters easier, let $z^2=n+k$ . Thus, in $g(n)$ , we want to achieve $(z+1)^2$ .
Expanding $(z+1)^2$ and substituting in the fact that $z=\sqrt{n+k}$ yields:
\[(z+1)^2=z^2+2z+1=n+k+2\sqrt{n+k}+1\]
Thus, we must add the quantity $k+2z+1$ to $n$ to achieve a integral value in the function $g(n)$ . Thus.
\[g(n)=(k+2z+1)+\sqrt{n+k+2\sqrt{n+k}+1}\]
However, note that the quantity within the square root is just $(z+1)^2$ , and so:
\[g(n)=k+3z+2\]
Thus, \[\frac{f(n)}{g(n)}=\frac{k+z}{k+3z+2}\]
Since we want this quantity to equal $\frac{4}{7}$ , we can set the above equation equal to this number and collect all the variables to one side to achieve
\[3k-5z=8\]
Substituting back in that $z=\sqrt{n+k}$ , and then separating variables and squaring yields that
\[9k^2-73k+64=25n\]
Now, if we treat $n$ as a constant, we can use the quadratic formula in respect to $k$ to get an equation for $k$ in terms of $n$ (without all the squares). Doing so yields
\[\frac{73\pm\sqrt{3025+900n}}{18}=k\]
Now, since $n$ and $k$ are integers, we want the quantity within the square root to be a perfect square. Note that $55^2=3025$ . Thus, assume that the quantity within the root is equal to the perfect square, $m^2$ . Thus, after using a difference of squares, we have \[(m-55)(m+55)=900n\] Since we want $n$ to be an integer, we know that the $LHS$ should be divisible by five, so, let's assume that we should have $m$ divisible by five. If so, the quantity $18k-73$ must be divisible by five, meaning that $k$ leaves a remainder of one when divided by 5 (if the reader knows LaTeX well enough to write this as a modulo argument, please go ahead and do so!).
Thus, we see that to achieve integers $n$ and $k$ that could potentially satisfy the problem statement, we must try the values of $k$ congruent to one modulo five. However, if we recall a statement made earlier in the solution, we see that we can skip all even values of $k$ produced by this modulo argument.
Also, note that $k=1,6$ won't work, as they are too small, and will give an erroneous value for $n$ . After trying $k=11,21,31$ , we see that $k=31$ will give a value of $m=485$ , which yields $n=\boxed{258}$ , which, if plugged in to for our equations of $f(n)$ and $g(n)$ , will yield the desired ratio, and we're done.
Side Note: If any part of this solution is not rigorous, or too vague, please label it in the margin with "needs proof". If you can prove it, please add a lemma to the solution doing so :)
-Azeem H. (mathislife52)

## Solution 5 (Basic Substitutions)
First of all, if $n$ is a perfect square, $f(n)=g(n)=\sqrt{n}$ and their quotient is $1.$ So, for the rest of this solution, assume $n$ is not a perfect square.
Let $a^2$ be the smallest perfect square greater than $n$ and let $b^2$ be the smallest perfect square greater than $n$ with the same parity as $n,$ and note that either $b=a$ or $b=a+1.$ Notice that $(a-1)^2 < n < a^2.$
With a bit of inspection, it becomes clear that $f(n) = a+(a^2-n)$ and $g(n) = b+(b^2-n).$
If $a$ and $n$ have the same parity, we get $a=b$ so $f(n) = g(n)$ and their quotient is $1.$ So, for the rest of this solution, we let $a$ and $n$ have opposite parity. We have two cases to consider.
Case 1: $n$ is odd and $a$ is even
Here, we get $a=2k$ for some positive integer $k.$ Then, $b = 2k+1.$ We let $n = a^2-(2m+1)$ for some positive integer $m$ so $f(n) = 2k+2m+1$ and $g(n) = 2k+1+2m+1+4k+1 = 6k+2m+3.$
We set $\frac{2k+2m+1}{6k+2m+3}=\frac{4}{7},$ cross multiply, and rearrange to get $6m-10k=5.$ Since $k$ and $m$ are integers, the LHS will always be even and the RHS will always be odd, and thus, this case yields no solutions.
Case 2: $n$ is even and $a$ is odd
Here, we get $a=2k+1$ for some positive ineger $k.$ Then, $b=2k+2.$ We let $n = a^2-(2m+1)$ for some positive integer $m$ so $f(n)=2k+1+2m+1=2k+2m+2$ and $g(n)=2k+2+2m+1+4k+3 = 6k+2m+6.$
We set $\frac{2k+2m+2}{6k+2m+6} = \frac{4}{7},$ cross multiply, and rearrange to get $5k=3m-5,$ or $k=\frac{3}{5}m-1.$ Since $k$ and $m$ are integers, $m$ must be a multiple of $5.$ Some possible solutions for $(k,m)$ with the least $k$ and $m$ are $(2,5), (5,10), (8,15),$ and $(11,20).$
We wish to minimize $k$ since $a=2k+1.$ One thing to keep in mind is the initial assumption $(a-1)^2 < n < a^2.$
The pair $(2,5)$ gives $a=2(2)+1=5$ and $n=5^2-(2(5)+1)=14.$ But $4^2<14<5^2$ is clearly false, so we discard this case.
The pair $(5,10)$ gives $a=2(5)+1=11$ and $n=11^2-(2(10)+1)=100,$ which is a perfect square and therefore can be discarded.
The pair $(8,15)$ gives $a=2(8)+1=17$ and $n=17^2-(2(15)+1)=258,$ which is between $16^2$ and $17^2$ so it is our smallest solution.
So, $\boxed{258}$ is the correct answer.
~mc21s

## Solution 6 (Short)
Say the answer is in the form $n^{2}-x$ , then $x$ must be odd or else $f(x) = g(x)$ . Say $y = n^{2}-x$ . $f(y) = x+n$ , $g(y) = 3n+2+x$ . Because $f(y)/g(y)$ = $4$ *(an integer)/ $7$ *(an integer), $f(y)$ is $4$ *(an integer) so $n$ must be odd or else $f(y)$ would be odd. Solving for $x$ in terms of $n$ gives integer $x = (5/3)n+8/3$ which means $n$ is $2$ mod $3$ , because $n$ is also odd, $n$ is $5$ mod $6$ . $x$ must be less than $2n-1$ or else the minimum square above $y$ would be $(n-1)^{2}$ . We set an inequality $(5/3)n+8/3<2n-1 => 5n+8<6n-3 => n>11$ . Since $n$ is $5$ mod $6$ , $n = 17$ and $x = 31$ giving $17^{2}-31$ = $\boxed{258}$ .
~mathophobia
~ $\LaTeX$ added by Bread10

## Solution 7
Define a nonnegative integer $k$ such that $g(n)-f(n)$ = $k$ . Since $\frac{f(n)}{g(n)} = \frac{4}{7},$ $k$ is a positive integer. Now, suppose 3 consecutive integers $a-1$ , $a$ , and $a+1$ , and $(a-1)^2 < n < a^2$ . When $g(n) > f(n)$ , $g(n)$ must have a different parity than $a$ , so that $f(n)$ 's recursive sequence ends on $a^2$ , while $g(n)$ continues to $(a+1)^2$ . If this condition is satisfied, we can figure out the value of $k$ based on $a$ . According to the definitions of $f(n)$ and $g(n)$ , $f(n) = a+a^2-n,$ and $g(n) = (a+1)+(a+1)^2-n,$ which gives $k = 2a+2$ . And because of $f(n) + k = g(n)$ , $\frac{k}{g(n)} = \frac{3}{7},$ so cross multiplying gives $3g(n) = 14a+14$ . This means that $14a+14$ is divisible by 3, and thus $a \equiv 2 \pmod{3}$ . The final thing left is to find the smallest $a$ such that the corresponding value of $g(n)$ exist. Simple guess and check should give that the smallest value of $a$ is $a = 17$ , which yields an answer of $n = \boxed{258}$ .
~ Marchk26

## Solution 8 (Fast)
Let $n=k^2-x$ , where $0 \leq x \leq 2k-2$ . This means that $f(n)=k+x$ . For $g(x)$ , note that $x$ must be odd, otherwise $f(n)=g(n)$ . This means that $g(n)$ must 'skip' one perfect square (being $k^2$ ), and go to $(k+1)^2$ . This will take $(k+1)^2-k^2+x+k+1=3k+x+2$ . We have $\frac{k+x}{3k+x+2}=\frac{4}{7}$ . Cross multiplying and simplifying we get $3x-5k=8$ . Taking $mod 5$ we have $3x=3 \mod 5$ or $x = 1 \mod 5$ . Note that the inequality $0 \leq x \leq 2k-2$ when $x=5t+1$ and $t \geq 5$ . Trying out $t=5$ , we get $x=26$ which doesn't work as x is even. Trying out $t=6$ , we get $x=31$ and $k=17$ , which satisfies all conditions, meaning the answer is $17^2-31=\boxed{258}.$
~E___

## Video Solution
https://youtu.be/tRVe2bKwIY8
~Mathematical Dexterity

## Video Solution by Interstigation
https://youtu.be/WmEmwt3xwoo
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .