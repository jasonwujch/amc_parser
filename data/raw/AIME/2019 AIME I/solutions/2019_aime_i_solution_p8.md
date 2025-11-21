# 2019 AIME I Problem 8

## Problem

Let $x$ be a real number such that $\sin^{10}x+\cos^{10} x = \tfrac{11}{36}$ . Then $\sin^{12}x+\cos^{12} x = \tfrac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
We can substitute $y = \sin^2{x}$ . Since we know that $\cos^2{x}=1-\sin^2{x}$ , we can do some simplification.
This yields $y^5+(1-y)^5=\frac{11}{36}$ . From this, we can substitute again to get some cancellation through binomials. If we let $z=\frac{1}{2}-y$ , we can simplify the equation to: \[\left(\frac{1}{2}+z\right)^5+\left(\frac{1}{2}-z\right)^5=\frac{11}{36}.\] After using binomial theorem, this simplifies to: \[\frac{1}{16}(80z^4+40z^2+1)=\frac{11}{36}.\] If we use the quadratic formula, we obtain $z^2=\frac{1}{12}$ , so $z=\pm\frac{1}{2\sqrt{3}}$ (observe that either choice of $z$ doesn't matter). Substituting $z,$ we get:
\[\sin^{12}{x}+\cos^{12}{x}=\left(\frac{1}{2}-z\right)^6+\left(\frac{1}{2}+z\right)^6=2z^6 + \frac{15z^4}{2} + \frac{15z^2}{8} + \frac{1}{32}=\frac{13}{54}.\]
Therefore, the answer is $13+54=\boxed{067}$ .
-eric2020, inspired by Tommy2002
### Motivation
The motivation to substitute $z=\frac{1}{2}-y$ comes so that after applying the binomial theorem to $y^5+(1-y)^5=\left(\frac{1}{2}+z\right)^5+\left(\frac{1}{2}-z\right)^5,$ a lot of terms will cancel out. Note that all the terms with odd exponents in $\left(\frac{1}{2}+z\right)^5$ will cancel out, while the terms with even exponents will be doubled. mathboy282

## Solution 2
First, for simplicity, let $a=\sin{x}$ and $b=\cos{x}$ . Note that $a^2+b^2=1$ . We then bash the rest of the problem out. Take the fifth power of this expression and get $a^{10}+b^{10}+5a^2b^2(a^6+b^6)+10a^4b^4(a^2+b^2)=\frac{11}{36}+5a^2b^2(a^6+b^6)+10a^4b^4=1$ . Note that we also have $\frac{11}{36}=a^{10}+b^{10}=(a^{10}+b^{10})(a^2+b^2)=a^{12}+b^{12}+a^2b^2(a^8+b^8)$ . So, it suffices to compute $a^2b^2(a^8+b^8)$ . Let $y=a^2b^2$ . We have from cubing $a^2+b^2=1$ that $a^6+b^6+3a^2b^2(a^2+b^2)=1$ or $a^6+b^6=1-3y$ . Next, using $\frac{11}{36}+5a^2b^2(a^6+b^6)+10a^4b^4=1$ , we get $a^2b^2(a^6+b^6)+2a^4b^4=\frac{5}{36}$ or $y(1-3y)+2y^2=y-y^2=\frac{5}{36}$ . Solving gives $y=\frac{5}{6}$ or $y=\frac{1}{6}$ . Clearly $y=\frac{5}{6}$ is extraneous, so $y=\frac{1}{6}$ . Now note that $a^4+b^4=(a^2+b^2)^2-2a^2b^2=\frac{2}{3}$ , and $a^8+b^8=(a^4+b^4)^2-2a^4b^4=\frac{4}{9}-\frac{1}{18}=\frac{7}{18}$ . Thus we finally get $a^{12}+b^{12}=\frac{11}{36}-\frac{7}{18}\cdot\frac{1}{6}=\frac{13}{54}$ , giving $\boxed{067}$ .
- Emathmaster

## Solution 3 (Newton Sums)
Newton sums is basically constructing the powers of the roots of the polynomials instead of deconstructing them which was done in Solution $2$ . Let $\sin^2x$ and $\cos^2x$ be the roots of some polynomial $F(a)$ . Then, by Vieta, $F(a)=a^2-a+b$ for some $b=\sin^2x\cdot\cos^2x$ .
Let $S_k=\left(\sin^2x\right)^k+\left(\cos^2x\right)^k$ . We want to find $S_6$ . Clearly $S_1=1$ and $S_2=1-2b$ . Newton sums tells us that $S_k-S_{k-1}+bS_{k-2}=0\Rightarrow S_k=S_{k-1}-bS_{k-2}$ where $k\ge 3$ for our polynomial $F(a)$ .
Bashing, we have \[S_3=S_2-bS_1\Rightarrow S_3=(1-2b)-b(1)=1-3b\] \[S_4=S_3-bS_2\Rightarrow S_4=(1-3b)-b(1-2b)=2b^2-4b+1\] \[S_5=S_4-bS_3\Rightarrow S_5=(2b^2-4b+1)-b(1-3b)=5b^2-5b+1=\frac{11}{36}\]
Thus \[5b^2-5b+1=\frac{11}{36}\Rightarrow 5b^2-5b+\frac{25}{36}=0, 36b^2-36b+5=0, (6b-1)(6b-5)=0\] $b=\frac{1}{6} \text{ or } \frac{5}{6}$ . Clearly, $\sin^2x\cdot\cos^2x\not=\frac{5}{6}$ so $\sin^2x\cdot\cos^2x=b=\frac{1}{6}$ .
Note $S_4=\frac{7}{18}$ . Solving for $S_6$ , we get $S_6=S_5-\frac{1}{6}S_4=\frac{13}{54}$ . Finally, $13+54=\boxed{067}$ .

## Solution 4
Factor the first equation. \[\sin^{10}x + \cos^{10}x = (\sin^2x+\cos^2x)(\sin^8x-\sin^6x\cos^2x+\sin^4x\cos^4x-\sin^2x\cos^6x+\cos^8x)\] First of all, $\sin^4x+\cos^4x = 1-2\sin^2x\cos^2x$ because $\sin^4x+\cos^4x=(\sin^2x + \cos^2x)^2 -2\sin^2x\cos^2x = 1 - 2\sin^2x\cos^2x$ We group the first, third, and fifth term and second and fourth term. The first group: \begin{align*} \sin^8+\sin^4x\cos^4x+\cos^8x &= (\sin^4x+\cos^4x)^2-\sin^4x\cos^4x)\\ &= (1 - 2\sin^2x\cos^2x)^2-\sin^4x\cos^4x)\\ &= 1+4\sin^4x\cos^4x-4\sin^2x\cos^2x \end{align*} The second group: \begin{align*} -\sin^6x\cos^2x-\sin^2x\cos^6x &= -\sin^2x\cos^2x(\sin^4x+\cos^4x)\\ &= -\sin^2x\cos^2x(1-2\sin^2x\cos^2x)\\ &= -\sin^2x\cos^2x+2\sin^4x\cos^4x \end{align*} Add the two together to make \[1+4\sin^4x\cos^4x-4\sin^2x\cos^2x-\sin^2x\cos^2x+2\sin^4x\cos^4x = 1 - 5\sin^2x\cos^2x+5\sin^4x\cos^4x\] Because this equals $\frac{11}{36}$ , we have \[5\sin^4x\cos^4x- 5\sin^2x\cos^2x+\frac{25}{36}=0\] Let $\sin^2x\cos^2x = a$ so we get \[5a^2- 5a+\frac{25}{36}=0 \Rightarrow a^2-a+\frac{5}{36}\] Solving the quadratic gives us \[a = \frac{1 \pm \frac{2}{3}}{2}\] Because $\sin^2x\cos^2x \le \frac{1}{4}$ , we finally get $a = \frac{1 - \frac{2}{3}}{2} = \frac{1}{6}$ .
Now from the second equation, \begin{align*} \sin^{12}x + \cos^{12}x &= (\sin^4x+\cos^4x)(\sin^8x-\sin^4x\cos^4x+\cos^8x)\\ &= (1-2\sin^2x\cos^2x)((\sin^4x+\cos^4x)^2-3\sin^4x\cos^4x)\\ &= (1-2\sin^2x\cos^2x)((1-2\sin^2x\cos^2x)^2-3\sin^4x\cos^4x) \end{align*} Plug in $\sin^2x\cos^2x = \frac{1}{6}$ to get \[(1-2(\frac{1}{6}))(1-2(\frac{1}{6})^2-3(\frac{1}{6})^2) = \frac{13}{54}\] which yields the answer $\boxed{067}$
~ZericHang

## Solution 5
Define the recursion $a_n=(\sin^2 x)^n+(\cos^2 x)^n$ We know that the characteristic equation of $a_n$ must have 2 roots, so we can recursively define $a_n$ as $a_n=p*a_{n-1}+q*a_{n-2}$ . $p$ is simply the sum of the roots of the characteristic equation, which is $\sin^2 x+\cos^2 x=1$ . $q$ is the product of the roots, which is $-(\sin^2 x)(\cos^2 x)$ . This value is not trivial and we have to solve for it. We know that $a_0=2$ , $a_1=1$ , $a_5=\frac{11}{36}$ . Solving the rest of the recursion gives
\[a_2=1+2q\] \[a_3=1+3q\] \[a_4=1+4q+2q^2\] \[a_5=1+5q+5q^2=\frac{11}{36}\] \[a_6=1+6q+9q^2+2q^3\]
Solving for $q$ in the expression for $a_5$ gives us $q^2+q+\frac{5}{36}=0$ , so $q=-\frac{5}{6}, -\frac{1}{6}$ . Since $q=-(\sin^2 x)(\cos^2 x)$ , we know that the minimum value it can attain is $-\frac{1}{4}$ by AM-GM, so $q$ cannot be $-\frac{5}{6}$ . Plugging in the value of $q$ into the expression for $a_6$ , we get $a_6=1-1+\frac{1}{4}-\frac{1}{108}=\frac{26}{108}=\frac{13}{54}$ . Our final answer is then $13+54=\boxed{067}$
-Natmath

## Solution 6
Let $m=\sin^2 x$ and $n=\cos^2 x$ , then $m+n=1$ and $m^5+n^5=\frac{11}{36}$
$m^6+n^6=(m^5+n^5)(m+n)-mn(m^4+n^4)=(m^5+n^5)-mn(m^4+n^4)$
Now factoring $m^5+n^5$ as solution 4 yields $m^5+n^5=(m+n)(m^4-m^3n+m^2n^2-mn^3+n^4)$ $=m^4+n^4-mn(m^2-mn+n^2)=m^4+n^4-mn[(m+n)^2-3mn]=m^4+n^4-mn(1-3mn)$ .
Since $(m+n)^4=m^4+4m^3n+6m^2n^2+4mn^3+n^4$ , $m^4+n^4=(m+n)^4-2mn(2m^2+3mn+2n^2)=1-2mn(2m^2+3mn+2n^2)$ .
Notice that $2m^2+3mn+2n^2$ can be rewritten as $[\sqrt{2}(a+b)]^2-mn=2-mn$ . Thus, $m^4+n^4=1-2mn(2-mn)$ and $m^5+n^5=1-2mn(2-mn)-mn(1-3mn)=1-5mn+5(mn)^2=\frac{11}{36}$ . As in solution 4, we get $mn=\frac{1}{6}$ and $m^4+n^4=1-2*\frac{1}{6}(2-\frac{1}{6})=\frac{7}{18}$
Substitute $m^4+n^4=\frac{7}{18}$ and $mn=\frac{1}{6}$ , then $m^6+n^6=\frac{11}{36}-\frac{1}{6}*\frac{7}{18}=\frac{13}{54}$ , and the desired answer is $\boxed{067}$

## Solution 7 (Algebra and Recursion)
This was my solution on the real test. Let $a=\sin^{2}x, b=\cos^{2}x$ . Observe that $a+b=1$ , and $(a^{n-1}+b^{n-1}) \cdot (a+b) = a^{n-1}b+ab^{n-1}+a^n+b^n=a^{n-1}+b^{n-1} \implies a^n+b^n=a^{n-1}+b^{n-1}-ab(a^{n-2}+b^{n-2})$ . Let $ab=x$ , and we want to know $x$ .
Starting from $n=2$ , we have $a^2+b^2=1-2x \implies a^3+b^3=1-2x-x=1-3x \implies a^4+b^4=1-4x-x(1-2x)=1-5x+2x^2 \implies a^5+b^5=2x^2-5x+1-x(1-3x)=5x^2-5x+1=\frac{11}{36}$ . Rearrange this quadratic and divide by $5$ to get $x^2-x+\frac{5}{36}=0 \implies x=\{\frac{1}{6}, \frac{5}{6}\}$ . (You can guess the factorization or use the quadratic formula.)
Given we have two solutions, plug both in and see which results in a positive rational fraction. Plugging in $x=\frac{1}{6}$ , we get $a^2+b^2=\frac{2}{3}, a^3+b^3=\frac{1}{2}, a^4+b^4=\frac{7}{18}, a^5+b^5=\frac{11}{36}, a^6+b^6=\frac{11}{36}-\frac{1}{6} \cdot \frac{7}{18} = \frac{26}{108} = \frac{13}{54} \implies \boxed{67}$ .
~First

## Solution 8 (Official MAA)
Let $c=\sin^2x\cdot\cos^2x,$ and let $S(n)=\sin^{2n}x+\cos^{2n}x.$ Then for $n\ge 1$ \begin{align*} S(n)&=(\sin^{2n}x+\cos^{2n}x)\cdot(\sin^2x+\cos^2x)\\ &=\sin^{2n+2}x+\cos^{2n+2}x+\sin^2x\cdot\cos^2x(\sin^{2n-2}x+\cos^{2n-2}x)\\ &=S(n+1)+cS(n-1). \end{align*} Because $S(0)=2$ and $S(1)=1,$ it follows that $S(2)=1-2c, S(3)=1-3c,S(4)=2c^2-4c+1,$ and $\tfrac{11}{36}=S(5)=5c^2-5c+1.$ Hence $c=\tfrac16$ or $\tfrac56,$ and because $4c=\sin^2{2x},$ the only possible value of $c$ is $\tfrac16.$ Therefore \[S(6)=S(5)-cS(4)=\frac{11}{36}-\frac16\left(2\left(\frac16\right)^2-4\left(\frac16\right)+1\right)=\frac{13}{54}.\] The requested sum is $13+54=67.$

## Solution 9 (Recursion)
Let $a_n=\sin^nx+\cos^nx$ for non-negative integers $n$ . Then $a_0=2$ and $a_2=1$ . In addition, \[a_n=\sin^nx+\cos^nx=\left(\sin^{n-2}x+\cos^{n-2}x\right)\left(\sin^2x+\cos^2x\right)-\sin^2x\cos^2x\left(\sin^{n-4}x+\cos^{n-4}x\right)=a_{n-2}-Xa_{n-4},\] where $X=\sin^2x\cos^2x$ . So we can compute \begin{align*} a_4&=1-2X\\ a_6&=1-3X\\ a_8&=1-4X+2X^2\\ a_{10}&=1-5X+5X^2=\frac{11}{36} \end{align*}so $X=\frac{1}{6},\frac{5}{6}$ . But by the sin double angle formula, $\sin^2x\cos^2x=\frac{1}{4}\sin^22x\leq\frac{1}{4}$ , so $X=\frac{1}{6}$ . Then \[a_{12}=a_{10}-Xa_8=\frac{11}{36}-\frac{1}{6}\cdot\frac{7}{18}=\frac{13}{54}\] so the answer is $\boxed{067}$ as desired.
A quick note: this solution uses recursion and is similar to the solution 7 above. It was from trumpeter, posted in the AoPS Forums, Contest Discussion.

## Video Solution By The Power Of Logic
https://youtu.be/TWQn4DvBATc
~ Hayabusa1
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .