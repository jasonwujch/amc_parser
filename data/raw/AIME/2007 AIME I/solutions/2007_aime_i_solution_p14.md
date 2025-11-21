# 2007 AIME I Problem 14

## Problem

A sequence is defined over non-negative integral indexes in the following way: $a_{0}=a_{1}=3$ , $a_{n+1}a_{n-1}=a_{n}^{2}+2007$ .

Find the greatest integer that does not exceed $\frac{a_{2006}^{2}+a_{2007}^{2}}{a_{2006}a_{2007}}.$

## Solutions

## Solution 1
Define a function $f(n)$ on the non-negative integers, as \[f(n) = \frac{a_n^2 + a_{n+1}^2}{a_na_{n+1}} = \frac{a_n}{a_{n+1}}+\frac{a_{n+1}}{a_{n}}\] We want $\left\lfloor f(2006) \right\rfloor$ .
Consider the relation $a_{n+1}a_{n-1}=a_{n}^{2}+2007$ . Dividing through by $a_{n}a_{n-1}$ , we get \[.\phantom{------------} \frac{a_{n+1}}{a_{n}} = \frac{a_{n}}{a_{n-1}} + \frac{2007}{a_{n}a_{n-1}} \phantom{------------} (1)\] and dividing through by $a_{n}a_{n+1}$ , we get \[.\phantom{------------} \frac{a_{n-1}}{a_{n}} = \frac{a_{n}}{a_{n+1}} + \frac{2007}{a_{n}a_{n+1}} \phantom{------------} (2)\] Adding LHS of $(1)$ with RHS of $(2)$ (and vice-versa), we get \[\frac{a_{n+1}}{a_{n}} + \frac{a_{n}}{a_{n+1}} + \frac{2007}{a_{n}a_{n+1}} = \frac{a_{n}}{a_{n-1}} + \frac{a_{n-1}}{a_{n}} + \frac{2007}{a_{n}a_{n-1}}\] i.e. \[f(n)+ \frac{2007}{a_{n}a_{n+1}} = f(n-1) + \frac{2007}{a_{n}a_{n-1}}\] Rearranging this to the form $f(n)-f(n-1)$ and summing over $n=1$ to $n=2006$ , we notice that most of the terms on each side telescope. Without rearranging, you can see that most terms cancel against the corresponding term on the other side. We are left with \[f(2006) + \frac{2007}{a_{2006}a_{2007}} = f(0) + \frac{2007}{a_{1}a_{0}}\] We have $f(0) = 2$ , and $2007/a_0a_1 = 2007/9 = 223$ . So \[f(2006) = 2 + 223 - \frac{2007}{a_{2006}a_{2007}} = 224 + \left( 1 - \frac{2007}{a_{2006}a_{2007}}\right)\] Since all the $a_i$ are positive, $(1)$ tells us that the ratio $a_{n+1}/a_n$ of successive terms is increasing. Since this ratio starts with $a_1/a_0 = 1$ , this means that the sequence $(a_n)$ is increasing. Since $a_2=672$ already, we must have $a_{2006}a_{2007} > 672^2 > 2007$ . It follows that $0<1-\frac{2007}{a_{2006}a_{2007}}<1$ and so $\left\lfloor f(2006) \right\rfloor = \boxed{224}$ .

## Solution 2
We are given that
$a_{n+1}a_{n-1}= a_{n}^{2}+2007$ , $a_{n-1}^{2}+2007 = a_{n}a_{n-2}$ .
Add these two equations to get
This is an invariant . Defining $b_{i}= \frac{a_{i}}{a_{i-1}}$ for each $i \ge 2$ , the above equation means
$b_{n+1}+\frac{1}{b_{n}}= b_{n}+\frac{1}{b_{n-1}}$ .
We can thus calculate that $b_{2007}+\frac{1}{b_{2006}}= b_{3}+\frac{1}{b_{2}}= 225$ . Using the equation $a_{2007}a_{2005}=a_{2006}^{2}+2007$ and dividing both sides by $a_{2006}a_{2005}$ , notice that $b_{2007}= \frac{a_{2007}}{a_{2006}}= \frac{a_{2006}^{2}+2007}{a_{2006}a_{2005}}> \frac{a_{2006}}{a_{2005}}= b_{2006}$ . This means that
$b_{2007}+\frac{1}{b_{2007}}< b_{2007}+\frac{1}{b_{2006}}= 225$ . It is only a tiny bit less because all the $b_i$ are greater than $1$ , so we conclude that the floor of $\frac{a_{2007}^{2}+a_{2006}^{2}}{a_{2007}a_{2006}}= b_{2007}+\frac{1}{b_{2007}}$ is $\boxed{224}$ .

## Solution 3
The equation $a_{n+1}a_{n-1}-a_n^2=2007$ looks like the determinant \[\left|\begin{array}{cc}a_{n+1}&a_n\\a_n&a_{n-1}\end{array}\right|=2007.\] Therefore, the determinant of this matrix is invariant. Guessing that this sequence might be a linear recursion because of the matrix form given below, we define the sequence $b_n$ defined by $b_1=b_2=3$ and $b_{n+1}=\alpha b_n+\beta b_{n-1}$ for $n\ge 2$ . We wish to find $\alpha$ and $\beta$ such that $a_n=b_n$ for all $n\ge 1$ . To do this, we use the following matrix form of a linear recurrence relation
\[\left(\begin{array}{cc}b_{n+1}&b_n\\b_n&b_{n-1}\end{array}\right)=\left(\begin{array}{cc}\alpha&\beta\\1&0\end{array}\right)\left(\begin{array}{cc}b_{n}&b_{n-1}\\b_{n-1}&b_{n-2}\end{array}\right).\]
When we take determinants, this equation becomes
\[\text{det}\left(\begin{array}{cc}b_{n+1}&b_n\\b_n&b_{n-1}\end{array}\right)=\text{det}\left(\begin{array}{cc}\alpha&\beta\\1&0\end{array}\right)\text{det}\left(\begin{array}{cc}b_{n}&b_{n-1}\\b_{n-1}&b_{n-2}\end{array}\right).\]
We want \[\text{det}\left(\begin{array}{cc}b_{n+1}&b_n\\b_n&b_{n-1}\end{array}\right)=2007\] for all $n$ . Therefore, we replace the two matrices by $2007$ to find that
\[2007=\text{det}\left(\begin{array}{cc}\alpha&\beta\\1&0\end{array}\right)\cdot 2007\] \[1=\text{det}\left(\begin{array}{cc}\alpha&\beta\\1&0\end{array}\right)=-\beta.\] Therefore, $\beta=-1$ . Computing that $a_3=672$ , and using the fact that $b_3=\alpha b_2-b_1$ , we conclude that $\alpha=225$ . Clearly, $a_1=b_1$ , $a_2=b_2$ , and $a_3=b_3$ . We claim that $a_n=b_n$ for all $n\ge 1$ . We proceed by induction . If $a_k=b_k$ for all $k\le n$ , then clearly, \[b_nb_{n-2}-b_{n-1}^2=a_na_{n-2}-a_{n-1}^2=2007.\] We also know by the definition of $b_{n+1}$ that
\[\text{det}\left(\begin{array}{cc}b_{n+1}&b_n\\b_n&b_{n-1}\end{array}\right)=\text{det}\left(\begin{array}{cc}\alpha&\beta\\1&0\end{array}\right)\text{det}\left(\begin{array}{cc}b_{n}&b_{n-1}\\b_{n-1}&b_{n-2}\end{array}\right).\]
We know that the RHS is $2007$ by previous work. Therefore, $b_{n+1}b_{n-1}-b_n^2=2007$ . After substuting in the values we know, this becomes $b_{n+1}a_{n-1}-a_n^2=2007$ . Thinking of this as a linear equation in the variable $b_{n+1}$ , we already know that this has the solution $b_{n+1}=a_{n+1}$ . Therefore, by induction, $a_n=b_n$ for all $n\ge 1$ . We conclude that $a_n$ satisfies the linear recurrence $a_{n+1}=225a_n-a_{n-1}$ .
It's easy to prove that $a_n$ is a strictly increasing sequence of integers for $n\ge 3$ . Now
\[\frac{a_{2007}^2+a_{2006}^2}{a_{2007}a_{2006}}=\frac{a_{2007}}{a_{2006}}+\frac{a_{2006}}{a_{2007}}=\frac{225a_{2006}-a_{2005}}{a_{2006}}+\frac{a_{2006}}{a_{2007}}.\]
\[=225+\frac{a_{2006}}{a_{2007}}-\frac{a_{2005}}{a_{2006}}=225+\frac{a_{2006}^2-a_{2005}a_{2007}}{a_{2005}a_{2006}}.\]
\[=225-\frac{2007}{a_{2005}a_{2006}}.\]
The sequence certainly grows fast enough such that $\frac{2007}{a_{2005}a_{2006}}<1$ . Therefore, the largest integer less than or equal to this value is $\boxed{224}$ .

## Solution 4 ( generalized )
This is a more elementary and rigorous solution to a slightly generalized version. The defining recursive sequence is generalized to
\[a_{n+1}a_{n-1} = a_n^2 + 9k, ---------(1)\] where $k$ is a positive integer and $a_0 = a_1 = 3.$
Lemma 1 : For $n \geq 1$ , \[a_{n+1} = ( k + 2)a_n - a_{n-1}. ---------(2)\] We shall prove by induction. From (1), $a_2 = 3k + 3$ . From the lemma, $a_2 = (k + 2) 3 - 3 = 3k + 3.$ Base case proven. Assume that the lemma is true for some $t \geq 1$ . Then, eliminating the $a_{t-1}$ using (1) and (2) gives
\[(k+2)a_ta_{t+1} = a_t^2 + a_{t+1}^2 + 9k. ---------(3)\]
It follows from (2) that
\[(k+2)a_{t+1} - a_t =\frac{(k+2)a_{t+1}a_t - a_t^2}{a_t} =\frac{a_{t+1}^2 + 9k}{a_t} =a_{t+2},\]
where the last line followed from (1) for case $n = t+1$ .
Lemma 2 : For $n \geq 0,$ \[a_{n+1} \geq a_{n}.\] Base case is obvious. Assume that $a_{t+1} \geq a_{t}$ for some $t \geq 0$ . Then it follows that \[a_{t+2} =\frac{a_{t+1}^2 + 9k}{a_t} = a_{t+1}(\frac{a_{t+1}}{a_t} ) + 9k \geq a_{t+1} + 9k > a_{t+1}.\]
This completes the induction.
Lemma 3 : For $n \geq 1,$ \[a_n a_{n+1} > 9k\]
Using (1) and Lemma 2, for $n \geq 1,$ \[a_{n+1}a_n \geq a_{n+1}a_{n-1} = a_n^2 + 9k > 9k\]
Finally, using (3), for $n \geq 1,$ \[\frac{a_n^2 + a_{n+1}^2}{a_n a_{n+1}} =\frac{(k+2)a_n a_{n+1} - 9k}{a_n a_{n+1}} = k+2 -\frac{9k}{a_n a_{n+1}}.\] Using lemma 3, the largest integer less than or equal to this value would be $k + 1$ .

## Solution 5 (pure algebra)
We will try to manipulate $\frac{a_0^2+a_1^2}{a_0a_1}$ to get $\frac{a_1^2+a_2^2}{a_1a_2}$ .
$\frac{a_0^2+a_1^2}{a_0a_1} = \frac{a_0+\frac{a_1^2}{a_0}}{a_1} = \frac{a_0+\frac{a_1^2+2007}{a_0}-\frac{2007}{a_0}}{a_1}$ Using the recurrence relation, $= \frac{a_0+a_2-\frac{2007}{a_0}}{a_1} = \frac{a_0a_2+a_2^2-\frac{2007a_2}{a_0}}{a_1a_2}$ Applying the relation to $a_0a_2$ , $= \frac{a_1^2+2007+a_2^2-\frac{2007a_2}{a_0}}{a_1a_2} = \frac{a_1^2+a_2^2}{a_1a_2}+\frac{2007}{a_1a_2}-\frac{2007}{a_0a_1}$
We can keep on using this method to get that $\frac{a_0^2+a_1^2}{a_0a_1} = \frac{a_{2006}^2+a_{2007}^2}{a_{2006}a_{2007}}+\frac{2007}{a_{2006}a_{2007}}-\frac{2007}{a_{2005}a_{2006}}+\frac{2007}{a_{2005}a_{2006}}-\ldots-\frac{2007}{a_{0}a_{1}}$
This telescopes to $\frac{a_0^2+a_1^2}{a_0a_1} = \frac{a_{2006}^2+a_{2007}^2}{a_{2006}a_{2007}}+\frac{2007}{a_{2006}a_{2007}}-\frac{2007}{a_{0}a_{1}}$
or $\frac{a_{2006}^2+a_{2007}^2}{a_{2006}a_{2007}} = \frac{a_0^2+a_1^2}{a_0a_1}+\frac{2007}{a_{0}a_{1}}-\frac{2007}{a_{2006}a_{2007}}$
Finding the first few values, we notice that they increase rapidly, so $\frac{2007}{a_{2006}a_{2007}} < 1$ . Calculating the other values, $\frac{a_{2006}^2+a_{2007}^2}{a_{2006}a_{2007}} = 2+223-\frac{2007}{a_{2006}a_{2007}}$ .
The greatest number that does not exceed this is $\boxed{224}$

## Solution 6 (using limits)
Let's start by computing the first couple terms of the given sequence so we know what we're working with. It's given that $a_0 = a_1 = 0$ , and solving for $a_2$ and $a_3$ using the given relation we get $a_2 = 672 = 3(224)$ and $a_3 = 3(224^{2} + 223)$ , respectively. It will be clear why I decided to factor these expressions as I did momentarily.
Next, let's see what the expression $\frac{a_{n}^{2}+a_{n + 1}^{2}}{a_{n}a_{n + 1}}$ looks like for small values of $n$ . For $n = 1$ , we get $\frac{1 + 224^2}{224}$ , the floor of which is clearly $224$ because the $1$ in the numerator is insignificant. Repeating the procedure for $n + 1$ is somewhat messier, but we end up getting $\frac{224^4 + 224^2\cdot223\cdot2 + 224^2 + 223^2}{224^3 + 224\cdot223}$ . It's not too hard to see that $224^4$ is much larger than the sum of the remaining terms in the numerator, and that $224^3$ is similarly a lot greater than the other term in the denominator. In fact, the second-largest term in the numerator is only barely larger than $224^3$ , while the second-largest term in the denominator is smaller than $224^2$ . Thus, the floor of this expression will come out to be $224$ as well.
Now we must consider whether this finding holds true for the rest of the sequence we're examining. First of all, notice that each time $n$ increases by $1$ , the degrees of both the numerator and denominator increase by $2$ , because we are squaring the $n+1th$ term in the numerator while the same term, appearing in the denominator, is being generated in part by squaring the term before it (seen in the relation $a_{n+1}^2 = (\frac{a_{n}^2 + 2007}{a_{n-1}})^2$ ). Thus, the degree of the numerator will always be one greater than the degree of the denominator; we have only to show that the other terms in the expression remain sufficiently small enough so as not to disturb the $\approx224:1$ ratio between the two.
For the non-greatest terms in the expression to offset this ratio for values of $n$ in the ballpark of $2006$ , they would have to have massive coefficients, because or else they are dwarfed by the additional $224$ attached to the leading term. Thankfully, this is not the case. Since we are simply squaring previous terms repeatedly to get new terms, we end up getting a sequence that is approximately equal to $\frac{224^k+224^{k-1}+224^{k-2} . . . }{224^{k-1}+224^{k-2} . . . }$ for all $k\geq2$ , whose $\lim_{k\to\infty}=$ $\boxed{224}$ .
~anellipticcurveoverq

## Video Solution
2007 AIME I #14
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.