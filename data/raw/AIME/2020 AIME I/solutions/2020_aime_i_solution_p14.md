# 2020 AIME I Problem 14

## Problem

Let $P(x)$ be a quadratic polynomial with complex coefficients whose $x^2$ coefficient is $1.$ Suppose the equation $P(P(x))=0$ has four distinct solutions, $x=3,4,a,b.$ Find the sum of all possible values of $(a+b)^2.$

## Solution 1
Either $P(3) = P(4)$ or not. We first see that if $P(3) = P(4)$ it's easy to obtain by Vieta's that $(a+b)^2 = 49$ . Now, take $P(3) \neq P(4)$ and WLOG $P(3) = P(a), P(4) = P(b)$ . Now, consider the parabola formed by the graph of $P$ . It has vertex $\frac{3+a}{2}$ . Now, say that $P(x) = x^2 - (3+a)x + c$ . We note $P(3)P(4) = c = P(3)\left(4 - 4a + \frac{8a - 1}{2}\right) \implies a = \frac{7P(3) + 1}{8}$ . Now, we note $P(4) = \frac{7}{2}$ by plugging in again. Now, it's easy to find that $a = -2.5, b = -3.5$ , yielding a value of $36$ . Finally, we add $49 + 36 = \boxed{085}$ . ~awang11, charmander3333
Remark : We know that $c=\frac{8a-1}{2}$ from $P(3)+P(4)=3+a$ .

## Solution 2
Let the roots of $P(x)$ be $m$ and $n$ , then we can write \[P(x)=x^2-(m+n)x+mn\] The fact that $P(P(x))=0$ has solutions $x=3,4,a,b$ implies that some combination of $2$ of these are the solution to $P(x)=m$ , and the other $2$ are the solution to $P(x)=n$ . It's fairly easy to see there are only $2$ possible such groupings: $P(3)=P(4)=m$ and $P(a)=P(b)=n$ , or $P(3)=P(a)=m$ and $P(4)=P(b)=n$ (Note that $a,b$ are interchangeable, and so are $m$ and $n$ ). We now casework: If $P(3)=P(4)=m$ , then \[9-3(m+n)+mn=16-4(m+n)+mn=m \implies m+n=7\] \[a^2-a(m+n)+mn=b^2-b(m+n)+mn=n \implies a+b=m+n=7\] so this gives $(a+b)^2=7^2=49$ . Next, if $P(3)=P(a)=m$ , then \[9-3(m+n)+mn=a^2-a(m+n)+mn=m \implies a+3=m+n\] \[16-4(m+n)+mn=b^2-b(m+n)+mn=n \implies b+4=m+n\] Subtracting the first part of the first equation from the first part of the second equation gives \[7-(m+n)=n-m \implies 2n=7 \implies n=\frac{7}{2} \implies m=-3\] Hence, $a+b=2(m+n)-7=2\cdot \frac{1}{2}-7=-6$ , and so $(a+b)^2=(-6)^2=36$ . Therefore, the solution is $49+36=\boxed{085}$ ~ktong

## Solution 3
Write $P(x) = x^2+wx+z$ . Split the problem into two cases: $P(3)\ne P(4)$ and $P(3) = P(4)$ .
Case 1: We have $P(3) \ne P(4)$ . We must have \[w=-P(3)-P(4) = -(9+3w+z)-(16+4w+z) = -25-7w-2z.\] Rearrange and divide through by $8$ to obtain \[w = \frac{-25-2z}{8}.\] Now, note that \[z = P(3)P(4) = (9+3w+z)(16+4w+z) = \left(9 + 3\cdot \frac{-25-2z}{8} + z\right)\left(16 + 4 \cdot \frac{-25-2z}{8} + z\right) =\] \[\left(-\frac{3}{8} + \frac{z}{4}\right)\left(\frac{7}{2}\right) = -\frac{21}{16} + \frac{7z}{8}.\] Now, rearrange to get \[\frac{z}{8} = -\frac{21}{16}\] and thus \[z = -\frac{21}{2}.\] Substituting this into our equation for $w$ yields $w = -\frac{1}{2}$ . Then, it is clear that $P$ does not have a double root at $P(3)$ , so we must have $P(a) = P(3)$ and $P(b) = P(4)$ or vice versa. This gives $3+a = \frac{1}{2}$ and $4+b = \frac{1}{2}$ or vice versa, implying that $a+b = 1-3-4 = -6$ and $(a+b)^2 = 36$ .
Case 2: We have $P(3) = P(4)$ . Then, we must have $w = -7$ . It is clear that $P(a) = P(b)$ (we would otherwise get $P(a)=P(3)=P(4)$ implying $a \in \{3,4\}$ or vice versa), so $a+b=-w=7$ and $(a+b)^2 = 49$ .
Thus, our final answer is $49+36=\boxed{085}$ . ~GeronimoStilton

## Solution 4
Let $P(x) = (x - r)(x - s)$ where $r$ and $s$ are its roots.
Note that \[P(r) = P(s) = P(P(3)) = P(P(4)) = P(P(a)) = P(P(b)) = 0.\] Since $P(x)$ is a quadratic, it can have at most two distinct roots, so there must be two pairs of $P(n)$ out of the four $P(3), P(4), P(a),$ and $P(b)$ which are equal to each other. (They have to be pairs because $P(x)$ can only have 2 roots, if we had something like $P(a) = P(3) = P(4) = r$ and $P(b) = s$ then $P(x)$ would have $3$ roots when counting multiplicity which is not possible.)
Case 1: $P(3) = P(4).$
Then $P(a) = P(b).$ WLOG, let $(3 - r)(3 - s)=(4 - r)(4 - s) = r$ and $(a - r)(a - s)=(b - r)(b - s)=s.$ Solving for $a + b$ gives us $a + b = r + s = 3 + 4 = 7 \implies (a + b)^2 = 49.$
Case 2: $P(3) \neq P(4).$
WLOG, let $P(3) = P(a) = r$ and $P(4) = P(b) = s.$ So $(3 - r)(3 - s) = r = (a - r)(a - s)$ and $(4 - r)(4 - s) = s = (b - r)(b - s).$ Subtracting $(4 - r)(4 - s) = s$ from $(3 - r)(3 - s) = r$ gives $-7 + r + s = r -s$ , so $s = \frac{7}{2}.$ Plugging this back into $(4-r)(4-s) = s$ gives $r = -3.$ The coefficient of the $x^3$ term in $P(P(x))$ is $-2(r+s)$ , so by Vieta's Formulas the sum of the roots of $P(P(x))$ is $2$ times that of $P(x).$ We know $r + s = \frac{1}{2}$ , so $3 + 4 + a + b = \frac{1}{2} \cdot 2 = 1.$ Then $a + b = -6 \implies (a + b)^2 = 36.$
The requested sum is $36 + 49 =\boxed{85}.$
~ grogg007 , TheUltimate123

## Solution 5 (Official MAA)
Note that because $P\big(P(3)\big)=P\big(P(4)\big)= 0$ , $P(3)$ and $P(4)$ are roots of $P(x)$ . There are two cases. CASE 1: $P(3) = P(4)$ . Then $P(x)$ is symmetric about $x=\tfrac72$ ; that is to say, $P(r) = P(7-r)$ for all $r$ . Thus the remaining two roots must sum to $7$ . Indeed, the polynomials $P(x) = \left(x-\frac72\right)^2 + \frac{11}4 \pm i\sqrt3$ satisfy the conditions. CASE 2: $P(3)\neq P(4)$ . Then $P(3)$ and $P(4)$ are the two distinct roots of $P(x)$ , so \[P(x) = \big(x-P(3)\big)\big(x-P(4)\big)\] for all $x$ . Note that any solution to $P\big(P(x)\big) = 0$ must satisfy either $P(x) = P(3)$ or $P(x) = P(4)$ . Because $P(x)$ is quadratic, the polynomials $P(x) - P(3)$ and $P(x) - P(4)$ each have the same sum of roots as the polynomial $P(x)$ , which is $P(3) + P(4)$ . Thus the answer in this case is $2\big(P(3) + P(4)\big)-7$ , and so it suffices to compute the value of $P(3)+P(4)$ .
Let $P(3)=u$ and $P(4) = v$ . Substituting $x=3$ and $x=4$ into the above quadratic polynomial yields the system of equations \begin{align*} u &= (3-u)(3-v) = 9 - 3u - 3v + uv\\ v &= (4-u)(4-v) = 16 - 4u - 4v + uv. \end{align*} Subtracting the first equation from the second gives $v - u = 7 - u - v$ , yielding $v = \frac72.$ Substituting this value into the second equation gives \[\dfrac72 = \left(4 - u\right)\left(4 - \dfrac72\right),\] yielding $u = -3.$ The sum of the two solutions is $2\left(\tfrac72-3\right)-7 = -6$ . In this case, $P(x)= (x+3)\left(x-\frac72\right)$ .
The requested sum of squares is $7^2+(-6)^2 = \boxed{085}$ .

## Solution 6
Let $P(x) = (x-c)^2 - d$ for some $c$ , $d$ .
Then, we can write $P(P(x)) = ((x-c)^2 - d - c)^2 - d$ . Setting the expression equal to $0$ and solving for $x$ gives:
$x = \pm \sqrt{ \pm \sqrt{d} + d + c} + c$
Therefore, we have that $x$ takes on the four values $\sqrt{\sqrt{d} + d + c} + c$ , $-\sqrt{\sqrt{d} + d + c} + c$ , $\sqrt{-\sqrt{d} + d + c} + c$ , and $-\sqrt{-\sqrt{d} + d + c} + c$ . Two of these values are $3$ and $4$ , and the other two are $a$ and $b$ .
We can split these four values into two "groups" based on the radicand in the expression - for example, the first group consists of the first two values listed above, and the second group consists of the other two values.
$\textbf{Case 1}$ : Both the 3 and 4 values are from the same group.
In this case, the $a$ and $b$ values are both from the other group. The sum of this is just $2c$ because the radical cancels out. Because of this, we can see that $c$ is just the average of $3$ and $4$ , so we have $2c = 3 + 4 = 7$ , so $(a+b)^2 = 7^2 = 49$ .
$\textbf{Case 2}$ : The 3 and 4 values come from different groups.
It is easy to see that all possibilities in this case are basically symmetric and yield the same value for $(a+b)^2$ . Without loss of generality, assume that $\sqrt{\sqrt{d} + d + c} + c = 4$ and $\sqrt{-\sqrt{d} + d + c} + c = 3$ . Note that we can't switch the values of these two expressions since the first one is guaranteed to be larger.
We can write $\sqrt{\sqrt{d} + d + c} + c = 1 + \sqrt{-\sqrt{d} + d + c} + c$ .
Moving most terms to the left side and simplifying gives $\sqrt{\sqrt{d} + d + c} - \sqrt{-\sqrt{d} + d + c} = 1$ .
We can square both sides and simplify:
$\sqrt{d} + d + c - \sqrt{d} + d + c - 2\sqrt{(d + c + \sqrt{d})(d + c - \sqrt{d})} = 1$
$2d + 2c - 2\sqrt{(d + c + \sqrt{d})(d + c - \sqrt{d})} = 1$
$\sqrt{(d + c + \sqrt{d})(d + c - \sqrt{d})} = (d+c) - \frac{1}{2}$
$\sqrt{(d+c)^2 - (\sqrt{d})^2} = (d+c) - \frac{1}{2}$
$\sqrt{d^2 + 2dc + c^2 - d} = (d+c) - \frac{1}{2}$
Squaring both sides again gives the following:
$d^2 + 2dc + c^2 - d = d^2 + 2dc + c^2 - d - c + \frac{1}{4}$
Nearly all terms cancel out, yielding $c = \frac{1}{4}$ .
By substituting this back in, we obtain $\sqrt{\sqrt{d} + d + c} = \frac{15}{4}$ and $\sqrt{-\sqrt{d} + d + c} = \frac{11}{4}$ .
The sum of $a$ and $b$ is equal to $-\sqrt{\sqrt{d} + d + c} - \sqrt{-\sqrt{d} + d + c} + 2c = -\frac{15}{4} - \frac{11}{4} + \frac{1}{2} = -6$ , so $(a+b)^2 = 36$ .
Adding up both values gives $49 + 36 = \boxed{085}$ as our final answer.

## Video Solution
https://youtu.be/_Iji1DW7QaY?si=t6Qbn2XYAfknnIxr
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .