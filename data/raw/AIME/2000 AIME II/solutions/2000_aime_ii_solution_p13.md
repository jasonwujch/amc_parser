# 2000 AIME II Problem 13

## Problem

The equation $2000x^6+100x^5+10x^3+x-2=0$ has exactly two real roots, one of which is $\frac{m+\sqrt{n}}r$ , where $m$ , $n$ and $r$ are integers, $m$ and $r$ are relatively prime, and $r>0$ . Find $m+n+r$ .

## Solution
We may factor the equation as: [1]
\begin{align*} 2000x^6+100x^5+10x^3+x-2&=0\\ 2(1000x^6-1) + x(100x^4+10x^2+1)&=0\\ 2[(10x^2)^3-1]+x[(10x^2)^2+(10x^2)+1]&=0\\ 2(10x^2-1)[(10x^2)^2+(10x^2)+1]+x[(10x^2)^2+(10x^2)+1]&=0\\ (20x^2+x-2)(100x^4+10x^2+1)&=0\\ \end{align*}
Now $100x^4+10x^2+1\ge 1>0$ for real $x$ . Thus the real roots must be the roots of the equation $20x^2+x-2=0$ . By the quadratic formula the roots of this are:
\[x=\frac{-1\pm\sqrt{1^2-4(-2)(20)}}{40} = \frac{-1\pm\sqrt{1+160}}{40} = \frac{-1\pm\sqrt{161}}{40}.\]
Thus the only root of the required form is $x=\frac{-1+\sqrt{161}}{40}$ , and so the final answer is $-1+161+40 = \boxed{200}$ .
^ A well-known technique for dealing with symmetric (or in this case, nearly symmetric) polynomials is to divide through by a power of $x$ with half of the polynomial's degree (in this case, divide through by $x^3$ ), and then to use one of the substitutions $t = x \pm \frac{1}{x}$ . In this case, the substitution $t = x\sqrt{10} - \frac{1}{x\sqrt{10}}$ gives $t^2 + 2 = 10x^2 + \frac 1{10x^2}$ and $2\sqrt{10}(t^3 + 3t) = 200x^3 - \frac{2}{10x^3}$ , which reduces the polynomial to just $(t^2 + 3)\left(2\sqrt{10}t + 1\right) = 0$ . Then one can backwards solve for $x$ . Note: After dividing the equation with $x^3$ , divide again with $10$ before substituting it with $t$ to get it right.
A slightly different approach using symmetry: Let $y = 10x - 1/x$ . Notice that the equation can be rewritten (after dividing across by $x^3$ ) as \[2( (10x)^3 - 1/x^3 ) + (10x)^2 + (1/x)^2 + 10 = 0\] Now it is easy to see that the equation reduces to \begin{align*} 2(y^3+30y)+ (y^2+20) + 10 = 0 \\ 2y^3 + y^2 + 60y + 30 = 0 \\ y^2(2y+1) + 30(2y+1) = 0 \\ (2y+1)(y^2+30)= 0 \\ \end{align*} so for real solutions we have $y = -1/2$ . Solve the quadratic in $x$ to get the final answer as $\boxed{200}$ .

## Solution 2 (Complex Bash)
It would be really nice if the coefficients were symmetrical. What if we make the substitution $x = -\frac{i}{\sqrt{10}}y$ ? Then the equation becomes
$-2y^6 - \left(\frac{i}{\sqrt{10}}\right)y^5 + \left(\frac{i}{\sqrt{10}}\right)y^3 - \left(\frac{i}{\sqrt{10}}\right)y - 2 = 0$ .
It's symmetric! Dividing by $y^3$ and rearranging, we get
$-2\left(y^3 + \frac{1}{y^3}\right) - \left(\frac{i}{\sqrt{10}}\right)\left(y^2 + \frac{1}{y^2}\right) + \left(\frac{i}{\sqrt{10}}\right)$
Now, if we let $z = y + \frac{1}{y}$ , we can get the equations
$z = y + \frac{1}{y}$
$z^2 - 2 = y^2 + \frac{1}{y^2}$
and
$z^3 - 3z = y^3 + \frac{1}{y^3}$
(These come from squaring $z$ and subtracting $2$ then multiplying that result by $z$ and subtracting $z$ .) Plugging this into our polynomial, expanding, and rearranging, we get
$-2z^3 - \left(\frac{i}{\sqrt{10}}\right)z^2 + 6z + \left(\frac{3i}{\sqrt{10}}\right)$
Now, we see that the two $i$ terms must cancel in order to get this polynomial equal to $0$ , so what squared equals 3? Plugging in $z = \sqrt{3}$ into the polynomial, we see that it works! Is there something else that equals 3 when squared? Trying $z = -\sqrt{3}$ , we see that it also works! Great, we use long division on the polynomial by
$\left(z - \sqrt{3}\right)\left(z + \sqrt{3}\right) = z^2 - 3$ and we get
$2z - \left(\frac{i}{\sqrt{10}}\right) = 0$ .
We know that the other two solutions for z wouldn't result in real solutions for $x$ since we have to solve a quadratic with a negative discriminant and then multiply by $-\left(\frac{i}{\sqrt{10}}\right)$ . We get that $z = \left(\frac{i}{-2\sqrt{10}}\right)$ . Solving for $y$ (using $y + \frac{1}{y} = z$ ) we get that $y = \frac{-i \pm \sqrt{161}i}{4\sqrt{10}}$ , and multiplying this by $-\left(\frac{i}{\sqrt{10}}\right)$ (because $x = -\left(\frac{i}{\sqrt{10}}\right)y$ ) we get that $x = \frac{-1 \pm \sqrt{161}}{40}$ for a final answer of $-1 + 161 + 40 = \boxed{200}.$
~Grizzy ~formatting edits by fermat_sLastAMC

## Solution 3 (Geometric Series)
Observe that the given equation may be rearranged as $2000x^6-2+(100x^5+10x^3+x)=0$ . The expression in parentheses is a geometric series with common factor $10x^2$ . Using the geometric sum formula, we rewrite as $2000x^6-2+\frac{1000x^7-x}{10x^2-1}=0, 10x^2-1\neq0$ . Factoring a bit, we get $2(1000x^6-1)+(1000x^6-1)\frac{x}{10x^2-1}=0, 10x^2-1\neq0 \implies$ $(1000x^6-1)(2+\frac{x}{10x^2-1})=0, 10x^2-1\neq0$ . Note that setting $1000x^6-1=0$ gives $10x^2-1=0$ , which is clearly extraneous. Hence, we set $2+\frac{x}{10x^2-1}=0$ and use the quadratic formula to get the desired root $x=\frac{-1+\sqrt{161}}{40} \implies -1+161+40=\boxed{200}$
~keeper1098

## Solution 4
If we look at the polynomial's terms, we can see that the number of zeros in a term more or less correlates to the power of $x^2$ . Thus, we let $y=10x^2$ . The equation then becomes $2y^3+xy^2+xy+x-2=0$ , or $x(y^2+y+1)=2(1-y^3)$ .
By the difference of cubes formula, $2(1-y^3)=2(1-y)(1+y+y^2)$ , so we have two cases: either $y^2+y+1=0$ , or $x=2(1-y)$ . We start with the second formula as it is simpler.
Solving with the quadratic formula after re-substitution, we see that $x=\frac{-1\pm\sqrt{161}}{40}$ , so the answer is $-1+161+40=\boxed{200}$ .
For the sake of completeness, if we check the other equation, we come to the conclusion that $y=\frac{-1\pm i\sqrt{3}}{2}$ , so no real solution exists for $x$ . Thus our solution is correct.
~eevee9406

## Solution 5 (substitutions)
Let $x = \frac{y}{10}.$ We have
\[\frac{2000y^6}{10^6} + \frac{100y^5}{10^5}+\frac{10y^3}{10^3}+\frac{y}{10} - 2=0\] \[= \frac{2y^6}{10^3}+\frac{y^5}{10^3}+\frac{y^3}{10^2}+\frac{y}{10}-2\] \[\Longleftrightarrow 2y^6 + y^5 + 10y^3 + 100y - 2000 = 0.\]
Divide this by $y^3,$ and we get
\[2y^3 + y^2 + 10 + \frac{100}{y^2} - \frac{2000}{y^3}.\]
By inspection, this looks like it could be expressed as a polynomial in $z=y - \frac{10}{y}.$ First, let's express $2\left(y^3 - \frac{1000}{y^3}\right)$ in terms of $z.$ We have
\[z^3 = \left(y-\frac{10}{y}\right)^3 = y^3 - 30y + \frac{300}{y} - \frac{1000}{y^3},\] \[\Longleftrightarrow z^3 + 30z = \left(y-\frac{10}{y}\right)^3 + 30\left(y - \frac{10}{y} \right) = y^3 - \frac{1000}{y^3}.\]
So,
\[2y^3 - \frac{2000}{y^3} = 2z^3 + 60z.\]
Now we want to express $y^2 + 10 + \frac{100}{y^2}$ in terms of $z$ too.
\[z^2 + 30 = y^2 - 20 + \frac{100}{y^2}+30 = y^2 + 10 + \frac{100}{y^2}.\]
Finally,
\[2y^3 + y^2 + 10 + \frac{100}{y^2} - \frac{2000}{y^3} = 2z^3 + z^2 + 60z + 30.\]
It is quite easy to see that $-\frac{1}{2}$ is one of the roots of this polynomial. Since the problem specifies that there are exactly two real roots, we know that the other roots of this cubic are nonreal. Now, we backtrack. \[z = -\frac{1}{2} = y-\frac{10}{y}.\] \[y^2 + \frac{y}{2} - 10 = 0\] \[2y^2 + y - 20 = 0\] \[\frac{-1 \pm \sqrt{1+160 }}{4}\] \[\Longleftrightarrow y = \frac{-1 + \sqrt{161}}{4}.\] Since $x=\frac{y}{10}, x = \frac{-1 + \sqrt{161}}{40},$ which means our answer is \[-1 + 161 + 40 = \boxed{200}.\]
~martianrunner

## Video solution
https://www.youtube.com/watch?v=mAXDdKX52TM
These problems are copyrighted © by the Mathematical Association of America.