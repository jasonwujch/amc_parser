# 2011 AMC 10A Problem 16

## Problem

Which of the following is equal to $\sqrt{9-6\sqrt{2}}+\sqrt{9+6\sqrt{2}}$ ?

$\text{(A)}\,3\sqrt2 \qquad\text{(B)}\,2\sqrt6 \qquad\text{(C)}\,\frac{7\sqrt2}{2} \qquad\text{(D)}\,3\sqrt3 \qquad\text{(E)}\,6$

## Solution 1 (Fast)
We find the answer by squaring, then square rooting the expression.
\begin{align*} &\sqrt{9-6\sqrt{2}}+\sqrt{9+6\sqrt{2}}\\\\ = \ &\sqrt{\left(\sqrt{9-6\sqrt{2}}+\sqrt{9+6\sqrt{2}}\right)^2}\\\\ = \ &\sqrt{9-6\sqrt{2}+2\sqrt{(9-6\sqrt{2})(9+6\sqrt{2})}+9+6\sqrt{2}}\\\\ = \ &\sqrt{18+2\sqrt{(9-6\sqrt{2})(9+6\sqrt{2})}}\\\\ = \ &\sqrt{18+2\sqrt{9^2-(6\sqrt{2})^2}}\\\\ = \ &\sqrt{18+2\sqrt{81-72}}\\\\ = \ &\sqrt{18+2\sqrt{9}}\\\\ = \ &\sqrt{18+6}\\\\= \ &\sqrt{24}\\\\ = \ &\boxed{2\sqrt{6} \ \mathbf{(B)}}. \end{align*}

## Solution 2 (FASTER!)
We can change the insides of the square root into a perfect square and then simplify.
\[\sqrt{9-6\sqrt{2}}+\sqrt{9+6\sqrt{2}}\] \[= \sqrt{6-6\sqrt{2}+3}+\sqrt{6+6\sqrt{2}+3}\] \[= \sqrt{\left(\sqrt{6}-\sqrt{3}\right)^2}+\sqrt{\left(\sqrt{6}+\sqrt{3}\right)^2}\] \[= \sqrt{6}-\sqrt{3}+\sqrt{6}+\sqrt{3}\] \[= \boxed{B) 2\sqrt{6}}\]

## Solution 3 (FASTEST!!)
Square roots remind us of squares. So lets try to make $9 - 6\sqrt{2} = (a-b)^2$ . Doing a little experimentation we find that \[9 - 6\sqrt{2} = (\sqrt{6} - \sqrt{3})^2.\] Similarly since $9 + 6\sqrt{2} = (a+b)^2$ we know that \[9 + 6\sqrt{2} = (\sqrt{6} + \sqrt{3})^2.\]
We want to find $\sqrt{9-6\sqrt{2}}+\sqrt{9+6\sqrt{2}}$ . Using what we found above we know \[\sqrt{9 -6\sqrt{2}}+\sqrt{9+6\sqrt{2}} = (\sqrt{6} - \sqrt{3}) + (\sqrt{6} + \sqrt{3}) = 2\sqrt{6}.\] This is nothing but $\boxed{B) 2\sqrt{6}}$ .
~coolmath_2018
Note: This is basically just Solution 2 except you "do a little experimentation"

## Solution 4 (No Words)
\[x=\sqrt{9-6\sqrt{2}}+\sqrt{9+6\sqrt{2}}\] \[x^{2}=9-6\sqrt{2}+9+6\sqrt{2}+2\sqrt{\left(9-6\sqrt{2}\right)\left(9+6\sqrt{2}\right)}\] \[x^{2}=18+2\sqrt{81-72}\] \[x^{2}=18+2\sqrt{9}\] \[x^{2}=18+6\] \[x^{2}=24\] \[x=\pm\sqrt{24}\] \[x=\pm2\sqrt{6}\] \[\boxed{\textbf{(B) } 2\sqrt{6}}\]
~JH. L

## Solution 5 (Bash / Int. Alg.)
First, factor $\sqrt3$ out of the whole expression: $\sqrt3\left(\sqrt{3-2\sqrt2}+\sqrt{3+2\sqrt2}\right)$ Let $\sqrt{3-2\sqrt{2}}=a+b\sqrt2.$ We square both sides, leaving us with $3-2\sqrt{2}=a^2+2ab\sqrt2+2b^2.$ We equate coefficients, and we see that $3=a^2+2b^2$ and $-2=2ab\implies ab=-1.$ We can see a pair of values that works easily, $(a,b)=(1,-1)$ or $(a,b)=(-1,1).$ A quick sign check tells us that the valid solution is $(-1,1).$ Similarly, for $\sqrt{3+2\sqrt{2}},$ we get $1+\sqrt2.$ When we add these two, we get $2\sqrt2,$ and multiplying by $\sqrt3,$ we get $\boxed{\text{(B)}~2\sqrt6}.$
We can quickly check our answer by estimating $\sqrt2=1.41$ and $\sqrt3=1.73$ : $\sqrt3\left(\sqrt{3-2\sqrt2}+\sqrt{3+2\sqrt2}\right)$ becomes $\sqrt3\left(\sqrt{3-2\cdot1.41}+\sqrt{3+2\cdot1.41}\right)=\sqrt3\left(\sqrt{3-2.82}+\sqrt{3+2.82}\right)=\sqrt3\left(\sqrt{0.18}+\sqrt{5.82}\right)\approx\sqrt3\left(\dfrac{3\sqrt2}{10}+2.4\right)\approx1.73\left(\dfrac{3\cdot1.41}{10}+2.4\right)=1.73\left(0.423+2.4\right)=1.73\left(2.823\right)\approx1.7\cdot2.8\approx4.76.$ This should be our approximate answer. We got $2\sqrt6=2\sqrt2\cdot\sqrt3\approx2\cdot1.41\cdot1.73=2.82\cdot1.73\approx2.8\cdot1.7=4.76$ - the same thing. ~Technodoggo

## Video Solution
https://youtu.be/ow2axpUP53c
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .