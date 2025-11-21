# 2007 AIME II Problem 14

## Problem

Let $f(x)$ be a polynomial with real coefficients such that $f(0) = 1,$ $f(2)+f(3)=125,$ and for all $x$ , $f(x)f(2x^{2})=f(2x^{3}+x).$ Find $f(5).$

## Official Solution (MAA)
If the leading term of $f(x)$ is $ax^m$ , then the leading term of $f(x)f(2x^2) = ax^m \cdot a(2x^2)^m = 2^ma^2x^{3m}$ , and the leading term of $f(2x^3 + x) = 2^max^{3m}$ . Hence $2^ma^2 = 2^ma$ , and $a = 1$ . Because $f(0) = 1$ , the product of all the roots of $f(x)$ is $\pm 1$ . If $f(\lambda) = 0$ , then $f(2\lambda^3 + \lambda) = 0$ . Assume that there exists a root $\lambda$ with $|\lambda| \neq 1$ . Then there must be such a root $\lambda_1$ with $|\lambda_1| > 1$ . Then \[|2\lambda^3 + \lambda| \ge 2|\lambda|^3 - |\lambda| > 2|\lambda| - |\lambda| = |\lambda|.\] But then $f(x)$ would have infinitely many roots, given by $\lambda_{k+1} = 2\lambda_k^3 + \lambda_k$ , for $k \ge 1$ . Therefore $|\lambda| = 1$ for all of the roots of the polynomial. Thus $\lambda\overline{\lambda}=1$ , and $(2\lambda^3 + \lambda)\overline{(2\lambda^3 + \lambda)} = 1$ . Solving these equations simultaneously for $\lambda = a + bi$ yields $a = 0$ , $b^2 = 1$ , and so $\lambda^2 = -1$ . Because the polynomial has real coefficients, the polynomial must have the form $f(x) = (1 + x^2)^n$ for some integer $n \ge 1$ . The condition $f(2) + f(3) = 125$ implies $n = 2$ , giving $f(5) = \boxed{676}$ .

## Solution 1
Let $r$ be a root of $f(x)$ . Then we have $f(r)f(2r^2)=f(2r^3+r)$ ; since $r$ is a root, we have $f(r)=0$ ; therefore $2r^3+r$ is also a root. Thus, if $r$ is real and non-zero, $|2r^3+r|>r$ , so $f(x)$ has infinitely many roots. Since $f(x)$ is a polynomial (thus of finite degree) and $f(0)$ is nonzero, $f(x)$ has no real roots.
Note that $f(x)$ is not constant. We then find two complex roots: $r = \pm i$ . We find that $f(i)f(-2) = f(-i)$ , and that $f(-i)f(-2) = f(i)$ . This means that $f(i)f(-i)f(-2)^2 = f(i)f(-i) \Longrightarrow f(i)f(-i)(f(-2)^2 - 1) = 0$ . Thus, $\pm i$ are roots of the polynomial, and so $(x - i)(x + i) = x^2 + 1$ will be a factor of the polynomial. (Note: This requires the assumption that $f(-2)\neq1$ . Clearly, $f(-2)\neq-1$ , because that would imply the existence of a real root.)
The polynomial is thus in the form of $f(x) = (x^2 + 1)g(x)$ . Substituting into the given expression, we have
\[(x^2+1)g(x)(4x^4+1)g(2x^2)=((2x^3+x)^2+1)g(2x^3+x)\] \[(4x^6+4x^4+x^2+1)g(x)g(2x^2)=(4x^6+4x^4+x^2+1)g(2x^3+x)\]
Thus either $4x^6+4x^4+x^2+1=(4x^4+1)(x^2+1)$ is 0 for any $x$ , or $g(x)$ satisfies the same constraints as $f(x)$ . Continuing, by infinite descent, $f(x) = (x^2 + 1)^n$ for some $n$ .
Since $f(2)+f(3)=125=5^n+10^n$ for some $n$ , we have $n=2$ ; so $f(5) = \boxed{676}$ .
Comment: The answer is clearly correct, but the proof has a gap, i.e. there is no reason that $f(-2)\neq1$ . Since $f(x)$ has no real roots, the degree must be even. Consider $g(x)= f(x)/f(-x)$ . Then since $f$ is non-zero, $g(x)=g(2x^3+x)$ . Now the function $2x^3+x$ applied repeatedly from some real starting value of x becomes arbitrarily large, and the limit of $g(x)$ as $|x|$ approaches infinity is 1, so $g(x)$ =1 for all x, or $f(x)=f(-x)$ . Then $f(x)=h(x^2+1)$ for some polynomial $h(x)$ , and $h(x^2+1)h(4x^4+1)=h(4x^6+4x^4+x^2+1) = h((x^2+1)(4x^4+1))$ . Now suppose h has degree m. It is clearly monic. Assume that the next highest non-zero coefficient in h is k. Then, subtracting $((x^2+1)(4x^4+1))^m$ from both sides of the equation yields a polynomial equality with degree $4m+2k$ on the left and degree $6k$ on the right, a contradiction. So $h(x)=x^m$ , and $f(x)=(1+x^2)^m$ .

## Solution 2
Let $r$ be a root of $f(x).$ This means that $f(r)f(2r^2)=f(2r^3+r).$ In other words, $2r^3+r$ is a root of $f(x)$ too. Since $f(x)$ can't have infinitely many roots, \[Q(x)=P(P(\dotsb P(P(r)) \dotsb))\] is cyclic, where $P(x)=2x^3+x.$ Now, we will do casework.
Case 1: $\deg f\geq1$
Subcase 1: $|r|>1$
This means that \[|2r^3+r|\geq|2r^3|-|r|=|r|(2|r|^2-1)>|r|(2\cdot1^2-1)=|r|.\] It follows that $|2r^3+r|>|r|$ for all $r.$ This implies that $Q(r)$ can't be cyclic. Thus, it is impossible for $|r|>1$ to be true.
Subcase 2: $|r|<1$
This means that $|2r^3+r|\geq2|r^3|-|r|=|r|(|2r^2|-1)<|r|.$ It follows that $|2r^3+r|<|r|$ for all $r.$ This implies that $Q(r)$ can't be cyclic. Thus, it is impossible for $|r|>1$ to be true.
Subcase 3: $|r|=1.$
Since $|r|$ is not greater than or less than 1, $|r|=1.$ This means that all the roots of the polynomial have a magnitude of $1.$ More specifically, $|2r^3+r|$ has a magnitude of one. Since this would mean an equality condition from the triangle inequality, $2r^3$ and $r$ are collinear with the origin in the complex plane. In other words, $\frac{2r^3}{r}=\pm c\Leftrightarrow cr=2r^3\Leftrightarrow 2r^2=c\Leftrightarrow r=\pm\sqrt{\pm\frac{c}{2}},$ for some real constant $c.$ Now, from $|r|=1,$ we find that $\left|\pm\sqrt{\pm\frac{c}{2}}\right|=1\Leftrightarrow \sqrt{\pm\frac{c}{2}}=1\Leftrightarrow \pm\frac{c}{2}=1\Leftrightarrow c=\pm2.$ Putting this back into the equation, we find that $r=1,-1,i,-i.$ Now, this means that $2r^3+r=3,-3,i,-i.$ $3$ and $-3$ obviously doesn't have a magnitude of $1.$ Thus, $i,-i$ are the only possible roots of the polynomial. Since roots come in conjugate pairs, $f(x)=[(x-i)(x+i)]^n=(x^2+1)^n,$ works for all constants $n\neq0.$
Case 2: $\deg f=0.$
This means that $f(x)=c,$ for some constant $c.$ In other words, $c^2=c.$ We can easily find that this means that $c=0,1.$ Combining all the cases, we conclude that $f(x)=(x^2+1)^n,0,1$ are the only polynomials that satisfy this equation. Now, we can test! $f(x)=0,1$ obviously don't satisfy $f(2)+f(3)=125.$ Thus, $f(x)=(x^2+1)^n.$ Substituting, we find that $5^n+10^n=125\Leftrightarrow n=2.$ We conclude that $f(5)=(5^2+1)^2=26^2=\boxed{676}.$
~ pinkpig

## Video Solution
2007 AIME II #14
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.