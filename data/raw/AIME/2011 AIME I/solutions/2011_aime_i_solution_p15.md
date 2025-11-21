# 2011 AIME I Problem 15

## Problem

For some integer $m$ , the polynomial $x^3 - 2011x + m$ has the three integer roots $a$ , $b$ , and $c$ . Find $|a| + |b| + |c|$ .

## Solution 1
From Vieta's formulas, we know that $a+b+c = 0$ , and $ab+bc+ac = -2011$ . Thus $a = -(b+c)$ . All three of $a$ , $b$ , and $c$ are non-zero: say, if $a=0$ , then $b=-c=\pm\sqrt{2011}$ (which is not an integer). $\textsc{wlog}$ , let $|a| \ge |b| \ge |c|$ . If $a > 0$ , then $b,c < 0$ and if $a < 0$ , then $b,c > 0,$ from the fact that $a+b+c=0$ . We have \[-2011=ab+bc+ac = a(b+c)+bc = -a^2+bc\] Thus $a^2 = 2011 + bc$ . We know that $b$ , $c$ have the same sign, so product $bc$ is always positive. So $|a| \ge 45 = \lceil \sqrt{2011} \rceil$ .
Also, if we fix $a$ , $b+c$ is fixed, so $bc$ is maximized when $b = c$ . Hence, \[2011 = a^2 - bc > \tfrac{3}{4}a^2 \qquad \Longrightarrow \qquad a ^2 < \tfrac{4}{3}\cdot 2011 = 2681+\tfrac{1}{3}\] So $|a| \le 51$ . Thus we have bounded $a$ as $45\le |a| \le 51$ , i.e. $45\le |b+c| \le 51$ since $a=-(b+c)$ . Let's analyze $bc=(b+c)^2-2011$ . Here is a table:
We can tell we don't need to bother with $45$ ,
$105 = (3)(5)(7)$ , So $46$ won't work. $198/47 > 4$ ,
$198$ is not divisible by $5$ , $198/6 = 33$ , which is too small to get $47$ .
$293/48 > 6$ , $293$ is not divisible by $7$ or $8$ or $9$ , we can clearly tell that $10$ is too much.
Hence, $|a| = 49$ , $a^2 -2011 = 390$ . $b = 39$ , $c = 10$ .
Answer: $\boxed{098}$

## Solution 2
Starting off like the previous solution, we know that $a + b + c = 0$ , and $ab + bc + ac = -2011$ .
Therefore, $c = -b-a$ .
Substituting, $ab + b(-b-a) + a(-b-a) = ab-b^2-ab-ab-a^2 = -2011$ .
Factoring the perfect square, we get: $ab-(b+a)^2=-2011$ or $(b+a)^2-ab=2011$ .
Therefore, a sum ( $a+b$ ) squared minus a product ( $ab$ ) gives $2011$ ..
We can guess and check different $a+b$ ’s starting with $45$ since $44^2 < 2011$ .
$45^2 = 2025$ therefore $ab = 2025-2011 = 14$ .
Since no factors of $14$ can sum to $45$ ( $1+14$ being the largest sum), a + b cannot equal $45$ .
$46^2 = 2116$ making $ab = 105 = 3 * 5 * 7$ .
$5 * 7 + 3 < 46$ and $3 * 5 * 7 > 46$ so $46$ cannot work either.
We can continue to do this until we reach $49$ .
$49^2 = 2401$ making $ab = 390 = 2 * 3 * 5* 13$ .
$3 * 13 + 2* 5 = 49$ , so one root is $10$ and another is $39$ . The roots sum to zero, so the last root must be $-49$ .
$|-49|+10+39 = \boxed{098}$ .

## Solution 3
Let us first note the obvious that is derived from Vieta's formulas: $a+b+c=0, ab+bc+ac=-2011$ . Now, due to the first equation, let us say that $a+b=-c$ , meaning that $a,b>0$ and $c<0$ . Now, since both $a$ and $b$ are greater than 0, their absolute values are both equal to $a$ and $b$ , respectively. Since $c$ is less than 0, it equals $-a-b$ . Therefore, $|c|=|-a-b|=a+b$ , meaning $|a|+|b|+|c|=2(a+b)$ . We now apply Newton's sums to get that $a^2+b^2+ab=2011$ ,or $(a+b)^2-ab=2011$ . Solving, we find that $49^2-390$ satisfies this, meaning $a+b=49$ , so $2(a+b)=\boxed{098}$ .

## Solution 4 (Quadratic)
From Vieta's Formulas we have $a + b + c = 0$ and $a(b + c) + bc = -2011.$ $b + c = -a \implies -a^2 + bc = -2011.$ $a^2 = (b + c)^2 \implies bc + 2011 = (b + c)^2.$ So now we have a simple looking two-variable quadratic equation. From here, we can solve for $c$ in terms of $b$ using the quadratic formula and see if we can do something with the discriminant. $bc + 2011 = b^2 + 2bc + c^2.$ $c^2 + (b)c + (b^2 - 2011) = 0.$ So $c = \frac{-b \pm \sqrt{8044 - 3b^2}}{2}.$ So $8044 - 3b^2$ must be a perfect square. $8044$ is around $89^2$ , so we can start from here and work downwards. Immediately, we see that if $8044 - 3b^2 = 88^2, b = 10.$ Will this work? If $b = 10,$ then $c$ can be $-49$ or $39$ . So we have two cases:
Case 1: $c = -49$
$b + c = -39$ and $bc = -490$
$a(-39) - 490 = -2011 \implies a = -39.$ But this doesn't satisfy the equation $a + b + c = 0,$ so this case won't work.
Case 2: $c = 39$
$b + c = 49$ and $bc = 390$
$a(49) + 390 = -2011 \implies a = -49.$ Since $a + b + c = 10 + 39 - 49 = 0$ this works.
So our answer is $10 + 39 + 49 = \boxed{98}.$
~ grogg007

## Solution 5 (mod to help bash)
First, derive the equations $a=-b-c$ and $ab+bc+ca=-2011\implies b^2+bc+c^2=2011$ . Since the product is negative, $a$ is negative, and $b$ and $c$ positive. Now, a simple mod 3 testing of all cases shows that $b\equiv \{1,2\} \pmod{3}$ , and $c$ has the repective value. We can choose $b$ not congruent to 0, make sure you see why. Now, we bash on values of $b$ , testing the quadratic function to see if $c$ is positive. You can also use a delta argument like solution 4, but this is simpler. We get that for $b=10$ , $c=39, -49$ . Choosing $c$ positive we get $a=-49$ , so $|a|+|b|+|c|=10+49+39=\boxed{098}$ ~firebolt360

## Solution 6
Note that $-c=b+a$ , so $c^2=a^2+2ab+b^2$ , or $-c^2+ab=-a^2-ab-b^2$ . Also, $ab+bc+ca=-2011$ , so $(a+b)c+ab=-c^2+ab=-2011$ . Substituting $-c^2+ab=-a^2-ab-b^2$ , we can obtain $a^2+ab+b^2=2011$ , or $\frac{a^3-b^3}{a-b}=2011$ . If it is not known that $2011$ is prime, it may be proved in $5$ minutes or so by checking all primes up to $43$ . If $2011$ divided either of $a, b$ , then in order for $a^3-b^3$ to contain an extra copy of $2011$ , both $a, b$ would need to be divisible by $2021$ . But then $c$ would also be divisible by $2011$ , and the sum $ab+bc+ca$ would clearly be divisible by $2011^2$ .
By LTE, $v_{2011}(a^3-b^3)=v_{2011}(a-b)$ if $a-b$ is divisible by $2011$ and neither $a,b$ are divisible by $2011$ . Thus, the only possibility remaining is if $a-b$ did not divide $2011$ . Let $a=k+b$ . Then, we have $(b+k)^3-b^3=2011k$ . Rearranging gives $3b(b+k)=2011-k^2$ . As in the above solutions, we may eliminate certain values of $k$ by using mods. Then, we may test values until we obtain $k=29$ , and $a=10$ . Thus, $b=39$ , $c=-49$ , and our answer is $49+39+10=098$ .

## Video Solution
https://www.youtube.com/watch?v=QNbfAu5rdJI&t=26s ~ MathEx
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .