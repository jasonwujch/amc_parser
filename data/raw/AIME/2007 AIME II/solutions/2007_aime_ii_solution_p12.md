# 2007 AIME II Problem 12

## Problem

The increasing geometric sequence $x_{0},x_{1},x_{2},\ldots$ consists entirely of integral powers of $3.$ Given that

$\sum_{n=0}^{7}\log_{3}(x_{n}) = 308$ and $56 \leq \log_{3}\left ( \sum_{n=0}^{7}x_{n}\right ) \leq 57,$

find $\log_{3}(x_{14}).$

## Solution
Suppose that $x_0 = a$ , and that the common ratio between the terms is $r$ .
The first conditions tells us that $\log_3 a + \log_3 ar + \ldots + \log_3 ar^7 = 308$ . Using the rules of logarithms , we can simplify that to $\log_3 a^8r^{1 + 2 + \ldots + 7} = 308$ . Thus, $a^8r^{28} = 3^{308}$ . Since all of the terms of the geometric sequence are integral powers of $3$ , we know that both $a$ and $r$ must be powers of 3. Denote $3^x = a$ and $3^y = r$ . We find that $8x + 28y = 308$ . The possible positive integral pairs of $(x,y)$ are $(35,1),\ (28,3),\ (21,5),\ (14,7),\ (7,9),\ (0,11)$ .
The second condition tells us that $56 \le \log_3 (a + ar + \ldots ar^7) \le 57$ . Using the sum formula for a geometric series and substituting $x$ and $y$ , this simplifies to $3^{56} \le 3^x \frac{3^{8y} - 1}{3^y-1} \le 3^{57}$ . The fractional part $\approx \frac{3^{8y}}{3^y} = 3^{7y}$ . Thus, we need $\approx 56 \le x + 7y \le 57$ . Checking the pairs above, only $(21,5)$ is close.
Our solution is therefore $\log_3 (ar^{14}) = \log_3 3^x + \log_3 3^{14y} = x + 14y = \boxed{091}$ .

## Solution 2
All these integral powers of $3$ are all different, thus in base $3$ the sum of these powers would consist of $1$ s and $0$ s. Thus the largest value $x_7$ must be $3^{56}$ in order to preserve the givens. Then we find by the given that $x_7x_6x_5\dots x_0 = 3^{308}$ , and we know that the exponents of $x_i$ are in an arithmetic sequence. Thus $56+(56-r)+(56-2r)+\dots +(56-7r) = 308$ , and $r = 5$ . Thus $\log_3 (x_{14}) = \boxed{091}$ .

## Solution 3
Like above, we use logarithmic identities to convert the problem into workable equations. We begin by labelling the powers of 3. Call $x_0$ , $x_1$ , $x_2$ ..., as $3^n$ , $3^{n+m}$ , and $3^{n+2m}$ ... respectively. With this format we can rewrite the first given equation as $n + n + m + n+2m + n+3m+...+n+7m = 308$ . Simplify to get $2n+7m=77$ . (1)
Now, rewrite the second given equation as $3^{56} \leq \left( \sum_{n=0}^{7}x_{n} \right) \leq 3^{57}$ . Obviously, $x_7$ , aka $3^{n+7m}$ $<3^{57}$ because there are some small fractional change that is left over. This means $n+7m$ is $\leq56$ . Thinking about the geometric sequence, it's clear each consecutive value of $x_i$ will be either a power of three times smaller or larger. In other words, the earliest values of $x_i$ will be negligible compared to the last values of $x_i$ . Even in the best case scenario, where the common ratio is 3, the values left of $x_7$ are not enough to sum to a value greater than 2 times $x_7$ (amount needed to raise the power of 3 by 1). This confirms that $3^{n+7m} = 3^{56}$ . (2)
Use equations 1 and 2 to get $m=5$ and $n=21$ . $\log_{3}{x_{14}} = \log_{3}{3^{21+14*5}} = 21+14*5 = \boxed{091}$
-jackshi2006

## Solution 4 (dum)
Proceed as in Solution 3 for the first few steps. We have the sequence $3^{a},3^{a+n},3^{a+2n}...$ . As stated above, we then get that $a+a+n+...+a+7n=308$ , from which we simplify to $2a+7n=77$ . From here, we just go brute force using the second statement (that $3^{56}\leq 3^{a}+...+3^{a+7n}\leq 3^{57}$ ). Rearranging the equation from earlier, we get \[n=11-\frac{2a}{7}\] from which it is clear that $a$ is a multiple of $7$ . Testing the first few values of $a$ , we get: Case 1 ( $a=7,n=9$ ) The sequence is then $3^{7}+...+3^{70}$ , which breaks the upper bound. Case 2 ( $a=14,n=7$ ) The sequence is then $3^{14}+...+3^{63}$ , which also breaks the upper bound. Case 3 ( $a=21,n=5$ ) This is the first reasonable one, giving $3^{21}+...+3^{56}$ . It seems like this would break the upper bound, but from some testing we get: \[3^{21}+...+3^{56}<3^{57}\] \[1+...+3^{35}<3^{36}\] \[1+...+3^{30}<2*3^{35}\] \[3^{5}+...+3^{30}<2*3^{35}-1\] \[1+...+3^{25}<2*3^{30}-3^{-5}\] Repeating this process over and over, we eventually get (while ignoring the extremely small fractions left over) \[1<2*3^{5}\] which confirms that this satisfies our upper bound. Thus $a=21,n=5$ , so $x_14=3^{a+14n}\rightarrow3^{91}$ . We then get the requested answer, $\log_3(3^{91})=\boxed{091}$ ~ amcrunner
These problems are copyrighted © by the Mathematical Association of America.