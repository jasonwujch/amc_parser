# 2009 AIME II Problem 7

## Problem

Define $n!!$ to be $n(n-2)(n-4)\cdots 3\cdot 1$ for $n$ odd and $n(n-2)(n-4)\cdots 4\cdot 2$ for $n$ even. When $\sum_{i=1}^{2009} \frac{(2i-1)!!}{(2i)!!}$ is expressed as a fraction in lowest terms, its denominator is $2^ab$ with $b$ odd. Find $\dfrac{ab}{10}$ .

## Solution 1
First, note that $(2n)!! = 2^n \cdot n!$ , and that $(2n)!! \cdot (2n-1)!! = (2n)!$ .
We can now take the fraction $\dfrac{(2i-1)!!}{(2i)!!}$ and multiply both the numerator and the denominator by $(2i)!!$ . We get that this fraction is equal to $\dfrac{(2i)!}{(2i)!!^2} = \dfrac{(2i)!}{2^{2i}(i!)^2}$ .
Now we can recognize that $\dfrac{(2i)!}{(i!)^2}$ is simply ${2i \choose i}$ , hence this fraction is $\dfrac{{2i\choose i}}{2^{2i}}$ , and our sum turns into $S=\sum_{i=1}^{2009} \dfrac{{2i\choose i}}{2^{2i}}$ .
Let $c = \sum_{i=1}^{2009} {2i\choose i} \cdot 2^{2\cdot 2009 - 2i}$ . Obviously $c$ is an integer, and $S$ can be written as $\dfrac{c}{2^{2\cdot 2009}}$ . Hence if $S$ is expressed as a fraction in lowest terms, its denominator will be of the form $2^a$ for some $a\leq 2\cdot 2009$ .
In other words, we just showed that $b=1$ . To determine $a$ , we need to determine the largest power of $2$ that divides $c$ .
Let $p(i)$ be the largest $x$ such that $2^x$ that divides $i$ .
We can now return to the observation that $(2i)! = (2i)!! \cdot (2i-1)!! = 2^i \cdot i! \cdot (2i-1)!!$ . Together with the obvious fact that $(2i-1)!!$ is odd, we get that $p((2i)!)=p(i!)+i$ .
It immediately follows that $p\left( {2i\choose i} \right) = p((2i)!) - 2p(i!) = i - p(i!)$ , and hence $p\left( {2i\choose i} \cdot 2^{2\cdot 2009 - 2i} \right) = 2\cdot 2009 - i - p(i!)$ .
Obviously, for $i\in\{1,2,\dots,2009\}$ the function $f(i)=2\cdot 2009 - i - p(i!)$ is is a strictly decreasing function. Therefore $p(c) = p\left( {2\cdot 2009\choose 2009} \right) = 2009 - p(2009!)$ .
We can now compute $p(2009!) = \sum_{k=1}^{\infty} \left\lfloor \dfrac{2009}{2^k} \right\rfloor = 1004 + 502 + \cdots + 3 + 1 = 2001$ . Hence $p(c)=2009-2001=8$ .
And thus we have $a=2\cdot 2009 - p(c) = 4010$ , and the answer is $\dfrac{ab}{10} = \dfrac{4010\cdot 1}{10} = \boxed{401}$ .
Additionally, once you count the number of factors of $2$ in the summation, one can consider the fact that, since $b$ must be odd, it has to take on a value of $1,3,5,7,$ or $9$ (Because the number of $2$ s in the summation is clearly greater than $1000$ , dividing by $10$ will yield a number greater than $100$ , and multiplying this number by any odd number greater than $9$ will yield an answer $>999$ , which cannot happen on the AIME.) Once you calculate the value of $4010$ , and divide by $10$ , $b$ must be equal to $1$ , as any other value of $b$ will result in an answer $>999$ . This gives $\boxed{401}$ as the answer.
Just a small note. It's important to note the properties of the $v_p$ function, which is what Solution 1 is using but denoting it as $p (...)$ . We want to calculate $v_2 \left( \sum ^{2009} _{i=1} \dbinom{2i}{i} \cdot 2^{2 \cdot 2009 - 2i} \right)$ as the final step. We know that one property of $v_p$ is that $v_p (a + b) \geq \min \left( v_p(a), v_p (b) \right)$ . Therefore, we have that $v_2 \left( \sum ^{2009} _{i=1} \dbinom{2i}{i} \cdot 2^{2 \cdot 2009 - 2i} \right) \geq \min \left( 2 \cdot 2009 -1, 2 \cdot 2009 -2 - 1, ... , 2 \cdot 2009 - 2008 - v_2 (2008!), 2 \cdot 2009 - 2009 - v_2 (2009!) \right)$ . Thus, we see by similar calculations as in Solution 1, that $v_2 (c) \geq 8$ . From which the conclusion follows.
- (OmicronGamma)

## Solution 2
Using the steps of the previous solution we get $c = \sum_{i=1}^{2009} {2i\choose i} \cdot 2^{2\cdot 2009 - 2i}$ and if you do the small cases(like $1, 2, 3, 4, 5, 6$ ) you realize that you can "thin-slice" the problem and simply look at the cases where $i=2009, 2008$ (they're nearly identical in nature but one has $4$ with it) since $\dbinom{2i}{I}$ hardly contains any powers of $2$ or in other words it's very inefficient and the inefficient cases hold all the power so you can just look at the highest powers of $2$ in $\dbinom{4018}{2009}$ and $\dbinom{4016}{2008}$ and you get the minimum power of $2$ in either expression is $8$ so the answer is $\frac{4010}{10} \implies \boxed{401}$ since it would violate the rules of the AIME and the small cases if $b>1$ .

## Solution 3 (Divisibility)
We can logically deduce that the $b$ value will be 1. Listing out the first few values of odd and even integers, we have: $1, 3, 5, 7, 9, 11, 13...$ and $2, 4, 6, 8, 10, 12, 14, 16...$ . Obviously, none of the factors of $2$ in the denominator will cancel out, since the numerator is odd. Starting on the second term of the numerator, a factor of $3$ occurs every $3$ terms, and starting out on the third term of the denominator, a factor of $3$ appears also every $3$ terms. Thus, the factors of $3$ on the denominator will always cancel out. We can apply the same logic for every other odd factor, so once terms all cancel out, the denominator of the final expression will be in the form $1 \cdot 2^a$ . Since there will be no odd factors in the denominators, all the denominators will be in the form $2^a$ where $a$ is the number of factors of $2$ in $(2009 \cdot 2)! = 4018!$ . This is simply $\sum_{n=1}^{11} \left \lfloor{\frac{4018}{2^n}}\right \rfloor = 4010$ . Therefore, our answer is $\boxed{401}$ .

## Solution 4
Using the initial steps from Solution 1, $S=\sum_{i=1}^{2009} \dfrac{{2i\choose i}}{2^{2i}}$ . Clearly $b = 1$ as in all the summands there are no non-power of 2 factors in the denominator. So we seek to find $a$ . Note that $2^a$ would be the largest denominator in all the summands, so when they are summed it is the common denominator.
Taking the p-adic valuations of each term, the powers of 2 in the denominator for $i$ is $(2i) - v_2(\binom{2i}{i}).$ We can use Kummers theorem to see that $v_2(\binom{2i}{i})$ is the number of digits carried over when $i$ is added to $i$ in base $2$ . This is simply the number of $1$ 's in the binary representation of $i$ .
Looking at the binary representations of some of the larger $i$ we see $2009 = 11111011001_2$ having eight $1$ 's. So the power of two is $2 \cdot 2009 - 8 = 4010$ . Experimenting with $2008, 2007, 2006$ we see that the power of two are all $< 4010$ , and under $2005$ the power of two $2i - v_2(\binom{2i}{i}) < 2i < 4010$ . Therefore $a = 4010$ and $\frac{ab}{10} = \boxed{401}.$
~Aaryabhatta1

## Video Solution
https://youtu.be/ppJkqLd3VNI?si=GX3UXkQ5s-5L6AzO
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.