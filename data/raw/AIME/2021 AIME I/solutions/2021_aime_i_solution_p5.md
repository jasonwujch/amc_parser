# 2021 AIME I Problem 5

## Problem

Call a three-term strictly increasing arithmetic sequence of integers special if the sum of the squares of the three terms equals the product of the middle term and the square of the common difference. Find the sum of the third terms of all special sequences.

## Solution 1
Let the terms be $a-b$ , $a$ , and $a+b$ . Then we want $(a-b)^2+a^2+(a+b)^2=ab^2$ , or $3a^2+2b^2=ab^2$ . Rearranging, we get $b^2=\frac{3a^2}{a-2}$ . Simplifying further, $b^2=3a+6+\frac{12}{a-2}$ . Looking at this second equation, since the right side must be an integer, $a-2$ must equal $\pm1, 2, 3, 4, 6, 12$ . Looking at the first equation, we see $a>2$ since $b^2$ is positive. This means we must test $a=3, 4, 5, 6, 8, 14$ . After testing these, we see that only $a=5$ and $a=14$ work which give $b=5$ and $b=7$ respectively. Thus the answer is $10+21=\boxed{031}$ . ~JHawk0224
Note: You could also use synthetic division to get $b^2=\frac{3a^2}{a-2}$ .

## Solution 2
Let the common difference be $d$ and let the middle term be $x$ . Then, we have that the sequence is \[x-d,~x,~x+d.\] This means that the sum of the squares of the 3 terms of the sequence is \[(x-d)^2+x^2+(x+d)^2=x^2-2xd+d^2+x^2+x^2+2xd+d^2=3x^2+2d^2.\] We know that this must be equal to $xd^2,$ so we can write that \[3x^2+2d^2=xd^2,\] and it follows that \[3x^2-xd^2+2d^2=3x^2-\left(d^2\right)x+2d^2=0.\]
Now, we can treat $d$ as a constant and use the quadratic formula to get \[x=\frac{d^2\pm \sqrt{d^4-4(3)(2d^2)}}{6}.\] We can factor pull $d^2$ out of the square root to get \[x=\frac{d^2\pm d\sqrt{d^2-24}}{6}.\] Here, it is easy to figure out the values of $d$ . Let $\sqrt{d^2-24} = k$ , then $d^2-k^2=24$ which is $(d+k)(d-k)=24,$ note that $d$ , $k$ are integers. Examining the parity, we find that $d+k$ and $d-k$ are of the same parity. Now, we solve by factoring. We can find that $d=5$ and $d=7$ are the only positive integer values of $d$ that make $\sqrt{d^2-24}$ a positive integer. $^{*}$ $d=5$ gives $x=5$ and $x=\frac{10}{3}$ , but we can ignore the latter. $d=7$ gives $x=14$ , as well as a fraction which we can ignore.
Since $d=5,~x=5$ and $d=7, x=14$ are the only two solutions and we want the sum of the third terms, our answer is $(5+5)+(7+14)=10+21=\boxed{031}$ . -BorealBear, minor edit by Kinglogic
$^*$ To prove this, let $\sqrt{d^2-24} = k$ , then $d^2-k^2=24$ which is $(d+k)(d-k)=24,$ then remembering that $d$ and $k$ are integers see if you can figure it out. - PureSwag

## Solution 3
Proceed as in solution 2, until we reach \[3x^2+2d^2=xd^2,\] Write
$d^2=\frac{3x^2}{x-2}$ , it follows that $x-2=3k^2$ for some (positive) integer k and $k \mid x$ .
Taking both sides modulo $k$ , $-2 \equiv 0 \pmod{k}$ , so $k \mid 2 \rightarrow k=1,2$ .
When $k=1$ , we have $x=5$ and $d=5$ . When $k=2$ , we have $x=14$ and $d=7$ . Summing the two cases, we have $10+21=\boxed{031}$ .
-Ross Gao

## Solution 4 (Combining Solution 1 and Solution 3)
As in Solution 1, write the three integers in the sequence as $a-d$ , $a$ , and $a+d$ .
Then the sum of the squares of the three integers is $(a-d)^2+a^2+(a+d)^2 = 3a^2+2d^2$ .
Setting this equal to the middle term times the common difference squared, which is $ad^2$ ,
and solving for $d^2$ we get:
$3a^2+2d^2 = ad^2 \implies ad^2-2d^2 = 3a^2 \implies d^2(a-2) = 3a^2 \implies d^2 = \frac{3a^2}{a-2}$
The numerator has to be positive, so the denominator has to be positive too for the sequence
to be strictly increasing; that is, $a>2$ .
For $\frac{3a^2}{a-2}$ to be a perfect square, $\frac{3}{a-2}$ must be a perfect square as well.
This means that $a-2$ is divisible by 3, and whatever left over is a perfect square.
We can express this as an equation: let the perfect square left over be $n^2$ . Then:
$3n^2 = a-2$ . Now when you divide the numerator and denominator by 3, you are left with
$d^2 = \frac{a^2}{n^2} \implies d = \frac{a}{n}$ . Because the sequence is of integers, d must also be an
integer, which means that $n$ must divide $a$ .
Taking the above equation we can solve for $a$ : $3n^2 = a-2 \implies a = 3n^2+2$ .
This means that $3n^2+2$ is divisible by $n$ . $3n^2$ is automatically divisible by $n$ , so
$2$ must be divisible by $n$ . Then $n$ must be either of $\{1,2\}$ . Plugging back into the equation,
$n = 1 \implies a = 5 \implies d = 5$ , so $a+d = 5+5 = 10$ .
$n = 2 \implies a = 14 \implies d = 7$ , so $a+d = 14+7 = 21$ .
Finally, $10+21 = \boxed{031}$
-KingRavi

## Solution 5
Following from previous solutions, we derive $3x^2+2a^2=xa^2.$ We divide both sides to get $3\left(\frac{x}{a}\right)^2+2=x.$ Since $x$ is an integer, $\frac{x}{a}$ must also be an integer, so we have $x=pa$ , for some factor $p$ . We then get $3p^2+2=pa.$ We then take this to modulo $p$ , getting $2\equiv 0 \pmod p.$ The only possibilities for $p$ are therefore 1 and 2. We plug these into $3p^2+2=pa$ , for $a=5$ and $x=5$ , giving us the sequence $0,5,10$ , or $2a=14$ and $x=14$ , for the sequence $7,14,21.$ $10+21 = \boxed{031}.$
-RYang2

## Video Solution 1
https://youtu.be/92dvTKV1nPc
~MathProblemSolvingSkills.com

## Video Solution 2
https://www.youtube.com/watch?v=I43RH5DUa1I

## Video Solution 3
https://youtu.be/M3DsERqhiDk?t=1465
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .