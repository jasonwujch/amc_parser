# 2017 AMC 10A Problem 24

## Problem

For certain real numbers $a$ , $b$ , and $c$ , the polynomial \[g(x) = x^3 + ax^2 + x + 10\] has three distinct roots, and each root of $g(x)$ is also a root of the polynomial \[f(x) = x^4 + x^3 + bx^2 + 100x + c.\] What is $f(1)$ ?

$\textbf{(A)}\ -9009 \qquad\textbf{(B)}\ -8008 \qquad\textbf{(C)}\ -7007 \qquad\textbf{(D)}\ -6006 \qquad\textbf{(E)}\ -5005$

## Solution 1
$f(x)$ must have four roots, three of which are roots of $g(x)$ . Using the fact that every polynomial has a unique factorization into its roots, and since the leading coefficient of $f(x)$ and $g(x)$ are the same, we know that
\[f(x)=g(x)(x+p)\]
where $-p\in\mathbb{R}$ is the fourth root of $f(x)$ . (Using $(x+p) = (x-r))$ instead of $(x-r)$ makes the following computations less messy.) Substituting $g(x)$ and expanding, we find that
\begin{align*}f(x)&=(x^3+ax^2+x+10)(x+p)\\ &=x^4+(a+p)x^3+(1+ap)x^2+(10+p)x+10p.\end{align*}
Comparing coefficients with $f(x)$ , we see that
\begin{align*} a+p&=1\\ 1+ap=b\\ 10+p&=100\\ 10p&=c.\\ \end{align*}
Let's solve for $a,b,c,$ and $p$ . Since $10+p=100$ , $p=90$ .
Since $a+p=1$ , $a=-89$ .
(Solution 1.1 branches from here and takes a shortcut.)
$c=(10)(90)=900$ .
Then, since $b=1+ap$ , $b=-8009$ . Thus,
\[f(x)=x^4+x^3-8009x^2+100x+900.\]
(Solution 1.2 branches from here and takes another shortcut)
Taking $f(1)$ , we find that
\begin{align*} f(1)&=1^4+1^3-8009(1)^2+100(1)+900\\ &=1+1-8009+100+900\\ &=\boxed{\bold{(C)}\, -7007}.\\ \end{align*}

## Solution 1.1
A faster ending to Solution 1 is as follows.
\begin{align*} f(1)&=(1+p)(1^3+a\cdot1^2+1+10)\\ &=(91)(-77)\\ &= (7)(13)(11)(-7) = (1001)(-7) \\ &=\boxed{\bold{(C)}\, -7007}.\\ \end{align*}

## Solution 1.2
Also a faster ending to Solution 1 is as follows.
To find $f(1)$ we just need to find the sum of the coefficients which is $1 + 1 - 8009 + 100 + 900= \boxed{\bold{(C)} \ , -7007}.$
~ Yiyj1

## Solution 2
We notice that the constant term of $f(x)=c$ and the constant term in $g(x)=10$ . Because $f(x)$ can be factored as $g(x) \cdot (x- r)$ (where $r$ is the unshared root of $f(x)$ , we see that using the constant term, $-10 \cdot r = c$ and therefore $r = -\frac{c}{10}$ . Now we once again write $f(x)$ out in factored form:
\[f(x) = g(x)\cdot (x-r) = (x^3+ax^2+x+10)(x+\frac{c}{10})\] .
We can expand the expression on the right-hand side to get:
\[f(x) = x^4+(a+\frac{c}{10})x^3+(1+\frac{ac}{10})x^2+(10+\frac{c}{10})x+c\]
Now we have $f(x) = x^4+(a+\frac{c}{10})x^3+(1+\frac{ac}{10})x^2+(10+\frac{c}{10})x+c=x^4+x^3+bx^2+100x+c$ .
Simply looking at the coefficients for each corresponding term (knowing that they must be equal), we have the equations: \[10+\frac{c}{10}=100 \Rightarrow c=900\] \[a+\frac{c}{10} = 1, c=900 \Rightarrow a + 90 =1 \Rightarrow a= -89\]
and finally,
\[1+\frac{ac}{10} = b = 1+\frac{-89 \cdot 900}{10} = b = -8009\] .
We know that $f(1)$ is the sum of its coefficients, hence $1+1+b+100+c$ . We substitute the values we obtained for $b$ and $c$ into this expression to get $f(1) = 1 + 1 + (-8009) + 100 + 900 = \boxed{\textbf{(C)}\,-7007}$ .

## Solution 3
Let $r_1,r_2,$ and $r_3$ be the roots of $g(x)$ . Let $r_4$ be the additional root of $f(x)$ . Then from Vieta's formulas on the quadratic term of $g(x)$ and the cubic term of $f(x)$ , we obtain the following:
\begin{align*} r_1+r_2+r_3&=-a \\ r_1+r_2+r_3+r_4&=-1 \end{align*}
Thus $r_4=a-1$ .
Now applying Vieta's formulas on the constant term of $g(x)$ , the linear term of $g(x)$ , and the linear term of $f(x)$ , we obtain:
\begin{align*} r_1r_2r_3 & = -10\\ r_1r_2+r_2r_3+r_3r_1 &= 1\\ r_1r_2r_3+r_2r_3r_4+r_3r_4r_1+r_4r_1r_2 & = -100\\ \end{align*}
Substituting for $r_1r_2r_3$ in the bottom equation and factoring the remainder of the expression, we obtain:
\[-10+(r_1r_2+r_2r_3+r_3r_1)r_4=-10+r_4=-100\]
It follows that $r_4=-90$ . But $r_4=a-1$ so $a=-89$
Now we can factor $f(x)$ in terms of $g(x)$ as
\[f(x)=(x-r_4)g(x)=(x+90)g(x)\]
Then $f(1)=91g(1)$ and
\[g(1)=1^3-89\cdot 1^2+1+10=-77\]
Hence $f(1)=91\cdot(-77)=\boxed{\textbf{(C)}\,-7007}$ .

## Solution 4 (Risky)
Let the roots of $g(x)$ be $r_1$ , $r_2$ , and $r_3$ . Let the roots of $f(x)$ be $r_1$ , $r_2$ , $r_3$ , and $r_4$ . From Vieta's, we have: \begin{align*} r_1+r_2+r_3=-a \\ r_1+r_2+r_3+r_4=-1 \\ r_4=a-1 \end{align*} The fourth root is $a-1$ . Since $r_1$ , $r_2$ , and $r_3$ are common roots, we have: \begin{align*} f(x)=g(x)(x-(a-1)) \\ f(1)=g(1)(1-(a-1)) \\ f(1)=(a+12)(2-a) \\ f(1)=-(a+12)(a-2) \\ \end{align*} Let $a-2=k$ : \begin{align*} f(1)=-k(k+14) \end{align*} Note that $-7007=-1001\cdot(7)=-(7\cdot(11)\cdot(13))\cdot(7)=-91\cdot(77)$ This gives us a pretty good guess of $\boxed{\textbf{(C)}\, -7007}$ .

## Solution 5
First off, let's get rid of the $x^4$ term by finding $h(x)=f(x)-xg(x)$ . This polynomial consists of the difference of two polynomials with $3$ common factors, so it must also have these factors. The polynomial is $h(x)=(1-a)x^3 + (b-1)x^2 + 90x + c$ , and must be equal to $(1-a)g(x)$ . Equating the coefficients, we get $3$ equations. We will tackle the situation one equation at a time, starting the $x$ terms. Looking at the coefficients, we get $\dfrac{90}{1-a} = 1$ . \[\therefore 90=1-a.\] The solution to the previous is obviously $a=-89$ . We can now find $b$ and $c$ . $\dfrac{b-1}{1-a} = a$ , \[\therefore b-1=a(1-a)=-89*90=-8010\] and $b=-8009$ . Finally $\dfrac{c}{1-a} = 10$ , \[\therefore c=10(1-a)=10*90=900\] Solving the original problem, $f(1)=1 + 1 + b + 100 + c = 102+b+c=102+900-8009=\boxed{\textbf{(C)}\, -7007}$ .

## Solution 6
Simple polynomial division is a feasible method. Even though we have variables, we can equate terms at the end of the division so that we can cancel terms. Doing the division of $\frac{f(x)}{g(x)}$ eventually brings us the final step $(1-a)x^3 + (b-1)x^2 + 90x + c$ minus $(1-a)x^3 - (a-a^2)x^2 + (1-a)x + 10(1-a)$ after we multiply $f(x)$ by $(1-a)$ . Now we equate coefficients of same-degree $x$ terms. This gives us $10(1-a) = c, b-1 = a - a^2, 1-a = 90 \Rightarrow a = -89, c = 900, b = -8009$ . We are interested in finding $f(1)$ , which equals $1^4 + 1^3 -8009\cdot1^2 + 100\cdot1 + 900 = \boxed{\textbf{(C)}\,-7007}$ . ~skyscraper

## Solution 7
We first note that $f(x) = g(x) \cdot q(x) + r(x)$ where $q$ is the quotient function and $r$ is the remainder function.
Clearly, $r(x) = 0$ because every single root in $g$ is also in $f$ , thus implying $g$ divides $f$ . So, we wish to find $f(1) = g(1) \cdot q(1)$ .
Such an expression for $g(1)$ is pretty clean here as we can obtain $g(1) = a + 12$ , so we rewrite $f(1) = (a + 12) \cdot q(1)$ . Well, now we need to know how $q$ is expressed in order to obtain $q(1)$ . This motivates us to long divide to obtain the quotient function. After simple long division $q(x) = x + (1 - a)$ . In addition, what is left over, namely $r(x)$ , has a constant piece of $a + 89$ (you'll see in a few sentences why we only care about particularly the constant piece).
Now we can write: $f(1) = (a + 12) \cdot (2 - a)$ .
Now, as we have already established $r(x) = 0$ for ALL $x$ that means $r(0)$ or the constant piece is $0$ , so $89 + a = 0$ , in which we obtain $a = -89$ . We now plug this back into our equation for $f(1)$ to get $(-89 + 12)(2 - (89)) = -77 \cdot 91 = \boxed{\textbf{(C)}\,-7007}$ . ~triggod

## Solution 8
Since $\text{deg(f(x))}=\text{deg(g(x))}+1$ , we can write \[(f(x)=g(x)\left(x-r \right) \Longrightarrow \left(x^3+ax^2+x+10 \right) \left(x-r \right)=x^4+x^3+bx^2+100x+c.\] Expanding this we get \[x^4+\left(a-r \right)x^3+\left(1-ar \right)x^2+\left(10-r \right)x-10r=x^4+x^3+bx^2+100+c.\] From coefficient matching we get the following equations: \[a-r=1\] \[1-ar=b\] \[10-r=100\] \[c=-10r.\] Obviously, the third equation results in $r$ being $=90$ , and plugging that into the fourth equation we get $c=900$ . Now, we can also plug in $r=-90$ to the first equation to get $a=-89$ . Finally, plugging $a$ and $r$ into the second equation we find that $b=-8009$ . We are asked to find $f(1)$ which is simply $b+c+102 = 7007 \Longrightarrow \boxed{C}$ .
-jb2015007
### General Notes
$f(1)$ for any polynomial is simply the sum of the coefficients of the polynomial.
$f(x)/g(x) = x+r$ must have real $r$ . Both $f$ and $g$ have all real coefficients, and so odd-degree $g$ must have an odd number of real roots, and even-degree $f$ must have an even number of real roots, so $f$ 's single additional root must be real.
$77 * 91 = 7 * 11 * 7 * 13$ , and $7*11*13=1001$ is a good number sense fact to know. It's interesting because $1001= 10^3+1$ and the 3 nearest primes to $10$ are $7,11,13$ .

## Video Solution by Pi Academy
https://youtu.be/xd_01X989Q0?si=Q7LINw1XRjoF1xSq
~ Pi Academy

## Video Solution 2
https://youtu.be/wXvRNC-48Lk
https://www.youtube.com/watch?v=MBIiz0mroqk (By Richard Rusczyk)
https://youtu.be/3dfbWzOfJAI?t=4412
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .