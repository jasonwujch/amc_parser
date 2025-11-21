# 2000 AIME I Problem 11

## Problem

Let $S$ be the sum of all numbers of the form $a/b,$ where $a$ and $b$ are relatively prime positive divisors of $1000.$ What is the greatest integer that does not exceed $S/10$ ?

## Solution 1
Since all divisors of $1000 = 2^35^3$ can be written in the form of $2^{m}5^{n}$ , it follows that $\frac{a}{b}$ can also be expressed in the form of $2^{x}5^{y}$ , where $-3 \le x,y \le 3$ . Thus every number in the form of $a/b$ will be expressed one time in the product
\[(2^{-3} + 2^{-2} + 2^{-1} + 2^{0} + 2^{1} + 2^2 + 2^3)(5^{-3} + 5^{-2} +5^{-1} + 5^{0} + 5^{1} + 5^2 + 5^3)\]
Using the formula for a geometric series , this reduces to $S = \frac{2^{-3}(2^7 - 1)}{2-1} \cdot \frac{5^{-3}(5^{7} - 1)}{5-1} = \frac{127 \cdot 78124}{4000} = 2480 + \frac{437}{1000}$ , and $\left\lfloor \frac{S}{10} \right\rfloor = \boxed{248}$ .

## Solution 2
Essentially, the problem asks us to compute \[\sum_{a=-3}^3 \sum_{b=-3}^3 \frac{2^a}{5^b}\] which is pretty easy: \[\sum_{a=-3}^3 \sum_{b=-3}^3 \frac{2^a}{5^b} = \sum_{a=-3}^3 2^a \sum_{b=-3}^3 \frac{1}{5^b} = \sum_{a=-3}^3 2^a 5^{3}\bigg( \frac{1-5^{-7}}{1-\frac{1}{5}} \bigg) = 5^{3}\bigg( \frac{1-5^{-7}}{1-\frac{1}{5}} \bigg) \sum_{a=-3}^3 2^a = 5^{3}\bigg( \frac{1-5^{-7}}{1-\frac{1}{5}} \bigg)2^{-3} \bigg( \frac{1-2^7}{1-2} \bigg) = 2480 + \frac{437}{1000}\] so our answer is $\left\lfloor \frac{2480 + \frac{437}{1000}}{10} \right\rfloor = \boxed{248}$ .

## Solution 3
The sum is equivalent to $\sum_{i | 10^6}^{} \frac{i}{1000}$ Therefore, it's the sum of the factors of $10^6$ divided by $1000$ . The sum is $\frac{127 \times 19531}{1000}$ by the sum of factors formula. The answer is therefore $\boxed{248}$ after some computation. - whatRthose

## Solution 4 (head on)
We can organize the fractions and reduce them in quantities to reach our answer. First, separate the fractions with coprime parts into those that are combinations of powers of 2 and 5, and those that are a combination of a 1 and another divisor.
To begin with the first list, list powers of 2 and 5 from 0 to 3. In this specific case I find it easier to augment every denominator to 1000 and then divide by 1000. To do this, write the corresponding divisor under each power. e.g. 2 - 500, 4 - 250, 5 - 200, etc. Call this the "partner" of any divisor.
Now we now the amount to multiply the numerator if given number is in the denominator. Now we simply combine and reduce these groups. If the powers of 2 are on the denominator, then every power of five will be multiplied by the partner of the power of 2. Essentially, all we have to do is a large scale distributive property application. There is nothing complicated about this except to be careful.
Add all powers of 2: 15
Add their partners: 1875
Add all powers of 5: 156
Add their partners: 1248
Then, follow this formula: (sum of powers * sum opposite power's partners)+(sum of powers * sum opposite power's partners)
Or, $156*1875+15*1248$ $=311220$
Now, divide by 1000 to compensate for the denominator. $311.22$
Finally, we have to calculate the other list of fractions with 1 and another divisor. e.g. 1 - 250, 1 - 20 etc. (these all count) This time we need to list all divisors of 1000, including 1. Remove all powers of 2 or 5, because we already included those in the other list. Now, notice there are two cases. 1: 1 is in the denominator, making the fraction an integer. 2: 1 is in the numerator.
Adding all the integers in the first case gives us 2169. The second case can actually be discarded, but still can be found. Realize that if we include the powers of 2 and 5, then the second case is (sum of all divisors)/1000. Remove all partners of powers of 2 and 5, and we'll get exactly 217/1000, or 0.22.
Finally, add all the numbers together: $311.22 + 2169 + 0.22 = 2480.44$
And divide by 10: $248.044$
After an odyssey of bashing: $\boxed{248}$
-jackshi2006

## Solution 5 (less brain)
Since $1$ is relatively prime to everything, including itself, we start with $b=1$ . The numerators will be all factors of 1000, and the sum of the factors of 1000 is $(1+2+4+8)(1+5+25+125) = 15*156=2340$ .
If the denominator is in the form $2^k$ , then the numerator must be in the form $5^j$ . The sum of the possible numerators is $1+5+25+125 = 156$ , so the sum of all such fractions with denominator $2^k$ is $\frac{156}{2}+\frac{156}{4}+\frac{156}{8} = 136.5$
If the denominator is in the form $5^k$ , then the numerator must be in the form $2^j$ . The sum of the possible numerators is $1+2+4+8 =15$ , so the sum of all such fractions with denominator $5^k$ is $\frac{15}{5}+\frac{15}{25}+\frac{15}{125}$ , which is around $3.6$ .
If the denominator is in the form $2^k5^j$ , where $k\ge 1$ and $j\ge 1$ , the numerator must be $1$ . We can get the sum of all such fractions from $(\frac{1}{2}+\frac{1}{4}+\frac{1}{8})(\frac{1}{5}+\frac{1}{25}+\frac{1}{125}) = \frac{217}{1000}$ .
Adding, we get $2480$ , with a bit extra, so our answer is $\boxed{248}$ .
~skibbysiggy
These problems are copyrighted © by the Mathematical Association of America.