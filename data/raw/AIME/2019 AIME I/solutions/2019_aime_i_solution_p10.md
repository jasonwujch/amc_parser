# 2019 AIME I Problem 10

## Problem

For distinct complex numbers $z_1,z_2,\dots,z_{673}$ , the polynomial \[(x-z_1)^3(x-z_2)^3 \cdots (x-z_{673})^3\] can be expressed as $x^{2019} + 20x^{2018} + 19x^{2017}+g(x)$ , where $g(x)$ is a polynomial with complex coefficients and with degree at most $2016$ . The sum \[\left| \sum_{1 \le j <k \le 673} z_jz_k \right|\] can be expressed in the form $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
In order to begin this problem, we must first understand what it is asking for. The notation \[\left| \sum_{1 \le j <k \le 673} z_jz_k \right|\] simply asks for the absolute value of the sum of the product of the distinct unique roots of the polynomial taken two at a time or \[(z_1z_2+z_1z_3+ \dots + z_1z_{672}+z_1z_{673})+(z_2z_3+z_2z_4+ \dots +z_2z_{673}) + (z_3z_4+z_3z_5+ \dots +z_3z_{673}) + \dots +z_{672}z_{673}.\] Call this sum $S$ .
Now we can begin the problem. Rewrite the polynomial as $P=(x-z_1)(x-z_1)(x-z_1)(x-z_2)(x-z_2)(x-z_2) \dots (x-z_{673})(x-z_{673})(x-z_{673})$ . Then we have that the roots of $P$ are $z_1,z_1,z_1,z_2,z_2,z_2, \dots , z_{673},z_{673},z_{673}$ .
By Vieta's formulas, we have that the sum of the roots of $P$ is $(-1)^1 \cdot \dfrac{20}{1}=-20=z_1+z_1+z_1+z_2+z_2+z_2+ \dots + z_{673}+z_{673}+z_{673}=3(z_1+z_2+z_3+ \dots +z_{673})$ . Thus, $z_1+z_2+z_3+ \dots +z_{673}=- \dfrac{20}{3}.$
Similarly, we also have that the the sum of the roots of $P$ taken two at a time is $(-1)^2 \cdot \dfrac{19}{1} = 19.$ This is equal to $z_1^2+z_1^2+z_1^2+z_1z_2+z_1z_2+z_1z_2+ \dots = \\ 3(z_1^2+z_2^2+ \dots + z_{673}^2) + 9(z_1z_2+z_1z_3+z_1z_4+ \dots + z_{672}z_{673}) = 3(z_1^2+z_2^2+ \dots + z_{673}^2) + 9S.$
Now we need to find and expression for $z_1^2+z_2^2+ \dots + z_{673}^2$ in terms of $S$ . We note that $(z_1+z_2+z_3+ \dots +z_{673})^2= (-20/3)^2=\dfrac{400}{9} \\ =(z_1^2+z_2^2+ \dots + z_{673}^2)+2(z_1z_2+z_1z_3+z_1z_4+ \dots + z_{672}z_{673})=(z_1^2+z_2^2+ \dots + z_{673}^2)+2S.$ Thus, $z_1^2+z_2^2+ \dots + z_{673}^2= \dfrac{400}{9} -2S$ .
Plugging this into our other Vieta equation, we have $3 \left( \dfrac{400}{9} -2S \right) +9S = 19$ . This gives $S = - \dfrac{343}{9} \Rightarrow \left| S \right| = \dfrac{343}{9}$ . Since 343 is relatively prime to 9, $m+n = 343+9 = \fbox{352}$ .

## Solution 2 (Fake Solve)
This is a quick fake solve using $z_i = 0$ where $3 \le i \le 673$ and only $z_1,z_2 \neq 0$ .
By Vieta's, \[3z_1+3z_2=-20\] and \[3z_1^2+3z_2^2+9z_1z_2 = 19.\] Rearranging gives $z_1 + z_2 = \dfrac{-20}{3}$ and $3(z_1^2 + 2z_1z_2 + z_2^2) + 3z_1z_2 = 19$ giving $3(z_1 + z_2)^2 + 3z_1z_2 = 19$ .
Substituting gives $3\left(\dfrac{400}{9}\right) + 3z_1z_2 = 19$ which simplifies to $\dfrac{400}{3} + 3z_1z_2 = \dfrac{57}{3}$ .
So, $3z_1z_2 = \dfrac{-343}{3}$ , $z_1z_2 = \dfrac{-343}{9}$ , $|\dfrac{-343}{9}|=\dfrac{343}{9}$ , \[m+n = 343+9 = \boxed{352}.\]

## Solution 3
Let $x=\sum_{1\le j<k\le 673} z_jz_k$ . By Vieta's, \[3\sum_{i=1}^{673}z_i=-20\implies \sum_{i=1}^{673}z_i=-\frac{20}3.\] Then, consider the $19x^{2017}$ term. To produce the product of two roots, the two roots can either be either $(z_i,z_i)$ for some $i$ , or $(z_j,z_k)$ for some $j<k$ . In the former case, this can happen in $\tbinom 32=3$ ways, and in the latter case, this can happen in $3^2=9$ ways. Hence, \begin{align*} 19=3\sum_{i=1}^{673} z_i^2+9\sum_{1\le j<k\le 673} z_jz_k=3\left(\left(-\frac{20}3\right)^2-2x\right)+9x&=\frac{400}3+3x\\ \implies x&=-\frac{343}9, \end{align*} and the requested sum is $343+9=\boxed{352}$ .

## Solution 4
Let \[(f(x))^3=x^{2019}+20x^{2018}+19x^{2017}+g(x).\] Therefore, $f(x)=(x-z_{1})(x-z_{1})\cdots (x-z_{673})$ . This is also equivalent to \[f(x)=x^{673}+ax^{672}+bx^{671}+h(x)\] for some real coefficients $a$ and $b$ and some polynomial $h(x)$ with degree $670$ . We can see that the big summation expression is simply summing the product of the roots of $f(x)$ taken two at a time. By Vieta's, this is just the coefficient $b$ . The first three terms of $(f(x))^3$ can be bashed in terms of $a$ and $b$ to get \[20 = 3a\] \[19 = 3a^2+3b\] Thus, $a=\frac{20}{3}$ and $b=\frac{1}{3}\left(19-3\left(\frac{20}{3} \right)^2 \right)$ . That is $|b|=\frac{343}{9}=\frac{m}{n}$ . $m+n=343+9=\boxed{352}$

## Solution 5 (Newton's Sums)
In the problem statement, we're given that the polynomial is $(x-z_1)^3(x-z_2)^3(x-z_3)^2\cdots (x-z_{673})^3$ which can be expressed as $x^{2019}+20x^{2018}+19x^{2017}+g(x)$ . So it has 673 roots of multiplicity 3 each, for a total of 2019 roots.
We start by calling $\left| \sum_{1 \le j <k \le 673} z_jz_k \right| = S$ . Next, let the sum of the roots of the polynomial be $P_1$ , which equals $3(x_1+x_2+\cdots+x_{673})$ , and the sum of the square of the roots be $P_2$ , which equals $3(z_1^2+z_2^2+z_3^2+\dots+z_{673}^2)$ .
By Vieta's, \[-20 = 3(z_1+z_2+z_3+z_4 \dots+z_{673})\] \[19 = 3(z_1^2+z_2^2+z_3^2+\dots+z_{673}^2) + 9S\]
The latter can be easily verified by using a combinatorics approach. $19$ is the sum of all the possible pairs of two roots of the polynomial. Which has $\binom{2019}{2}$ without simplification. Now looking at the latter above, there are $3\cdot673$ terms in the first part and $9\cdot\binom{673}{2}$ .
With some computation, we see $\binom{2019}{2}$ $= 3\cdot673+$ $9\cdot\binom{673}{2}$ . This step was simply done to check that we missed no steps.
Now using Newton Sums , where $P_2 = z_1^2+z_2^2+z_3^2+\dots+z_{673}^2$ . We first have that $P_1\cdot a_n + 1\cdot a_{n-1}=0$ and plugging in values, we get that $P_1\cdot 1 + 1\cdot 20 = 0 \implies P_1=-20.$ Then, $P_2\cdot a_n + P_1 \cdot a_{n-1} + 2\cdot a_{n-2}$ and plugging in the values we know, we get that
\[P_2 + -20\cdot20 + 19\cdot2 = 0 \implies P_2 = 362\]
\[19 = 362 + 9S \implies S = \frac{343}{9}\] Thus, $\frac{343}{9}$ leads to the answer $\boxed{352}$ .
~YBSuburbanTea
~minor edits by BakedPotato66

## Solution 6 (Official MAA 1)
Because each root of the polynomial appears with multiplicity $3,$ Viète's Formulas show that \[z_1+z_2+\cdots+z_{673}=-\frac{20}3\] and \[z_1^2+z_2^2+\cdots+z_{673}^2 =\frac13\left((-20)^2-2\cdot19\right)=\frac{362}3.\] Then the identity \[\left(\sum_{i=1}^{673}z_i\right)^2=\sum_{i=1}^{673}z_i^2+2\left(\sum_{1\le j<k\le 673}z_jz_k\right)\] shows that \[\sum_{1\le j<k\le 673}z_jz_k=\frac{\left(-\frac{20}3\right)^2-\frac{362}3}{2}=-\frac{343}9.\] The requested sum is $343+9=352.$
Note that such a polynomial does exist. For example, let $z_{673}=-\tfrac{20}3,$ and for $i=1,2,3,\dots,336,$ let \[z_i=\sqrt{\frac{343i}{9\sum_{j=1}^{336}j}}\qquad \text{and}\qquad z_{i+336}=-z_i.\] Then \[\sum_{i=1}^{673}z_i=-\frac{20}3\qquad\text{and}\qquad\sum_{i=1}^{673}z_i^2=2\sum_{i=1}^{336}\frac{343i}{9\sum_{i=1}^{336}j}+\left(\frac{20}3\right)^2=\frac{362}3,\] as required.

## Solution 7 (Official MAA 2)
There are constants $a$ and $b$ such that \[(x-z_1)(x-z_2)(x-z_3)\cdots(x-z_{673})=x^{673}+ax^{672}+bx^{671}+\cdots.\] Then \[(x^{673}+ax^{672}+bx^{671}+\cdots)^3=x^{2019}+20x^{2018}+19x^{2017}+\cdots.\] Comparing the $x^{2018}$ and $x^{2017}$ coefficients shows that $3a=20$ and $3a^2+3b=19.$ Solving this system yields $a=\tfrac{20}3$ and $b=-\tfrac{343}9.$ Viète's Formulas then give $\left|\sum_{1\le j<k\le 673}z_jz_k\right|=|b|=\tfrac{343}9,$ as above.

## Solution 8
Note that we are trying to find the sum of the products of the pairwise distinct $z_k$ . First, disregard the repeated roots and call the roots of the polynomial $x_1, x_2\ldots x_{2019}$ for simplicity's sake.
Then, $(z_1+z_2\ldots z_{2019})^2=2\sum_{1\leq j<k\leq2019}{z_jz_k}+\sum_{1\leq k\leq 2019}{z_k^2}$ . Notice that $\sum_{1\leq j<k\leq2019} {z_jz_k}=19$ and $(x_1+ x_2\ldots +x_{2019})^2=20^2=400$ by Vietas so $\sum_{1\leq k\leq 2019}{z_k^2}=362$ . Also, since every root is repeated 3 times, $\sum_{1\leq k\leq 2019}{z_k^2}=3\sum_{1\leq k\leq673}{z_k^2} \Longrightarrow \sum_{1\leq k\leq673}{z_k^2}=\frac{362}{3}$ where the $z_k$ in the second sum are all distinct.
Call $|\sum_{1 \le j <k \le 673} z_jz_k|=|s|$ . Taking into account repeated roots, if we pair any two roots together, there will be $\binom{3}{1}=3$ copies for each $z_k^2, 1\leq z\leq 673$ and $3\cdot 3=9$ copies for each $z_jz_k$ where $z_j$ and $z_k$ are distinct.
Since the sum of any two pairs of roots is 19, $9s+3\sum_{1\leq k\leq673}{z_k^2}=19$ or $9s+362=19 \Longrightarrow s=\frac{-343}{9}, |s|=\frac{343}{9}$ . $m+n=343+9=352$ .
~ Magnetoninja

## Video Solution by OmegaLearn
https://youtu.be/Dp-pw6NNKRo?t=776
~ pi_is_3.14

## Video Solution by The Power of Logic
https://www.youtube.com/watch?v=7SFKuEdgwMA
~The Power of Logic

## Video Solution & More by MegaMath
Video #2 (Vieta's Formulas): https://www.youtube.com/watch?v=6-kcdBsmCmc
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .