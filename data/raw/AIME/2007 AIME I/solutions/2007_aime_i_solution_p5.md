# 2007 AIME I Problem 5

## Problem

The formula for converting a Fahrenheit temperature $F$ to the corresponding Celsius temperature $C$ is $C = \frac{5}{9}(F-32).$ An integer Fahrenheit temperature is converted to Celsius, rounded to the nearest integer, converted back to Fahrenheit, and again rounded to the nearest integer .

For how many integer Fahrenheit temperatures between 32 and 1000 inclusive does the original temperature equal the final temperature?

## Solution

## Solution 1
Examine $F - 32$ modulo 9.
- If $F - 32 \equiv 0 \pmod{9}$ , then we can define $9x = F - 32$ . This shows that $F = \left[\frac{9}{5}\left[\frac{5}{9}(F-32)\right] + 32\right] \Longrightarrow F = \left[\frac{9}{5}(5x) + 32\right] \Longrightarrow F = 9x + 32$ . This case works.
- If $F - 32 \equiv 1 \pmod{9}$ , then we can define $9x + 1 = F - 32$ . This shows that $F = \left[\frac{9}{5}\left[\frac{5}{9}(F-32)\right] + 32\right] \Longrightarrow F = \left[\frac{9}{5}(5x + 1) + 32\right] \Longrightarrow$ $F = \left[9x + \frac{9}{5}+ 32 \right] \Longrightarrow F = 9x + 34$ . So this case doesn't work.
Generalizing this, we define that $9x + k = F - 32$ . Thus, $F = \left[\frac{9}{5}\left[\frac{5}{9}(9x + k)\right] + 32\right] \Longrightarrow F = \left[\frac{9}{5}(5x + \left[\frac{5}{9}k\right]) + 32\right] \Longrightarrow F = \left[\frac{9}{5} \left[\frac{5}{9}k \right] \right] + 9x + 32$ . We need to find all values $0 \le k \le 8$ that $\left[ \frac{9}{5} \left[ \frac{5}{9} k \right] \right] = k$ . Testing every value of $k$ shows that $k = 0, 2, 4, 5, 7$ , so $5$ of every $9$ values of $k$ work.
There are $\lfloor \frac{1000 - 32}{9} \rfloor = 107$ cycles of $9$ , giving $5 \cdot 107 = 535$ numbers that work. Of the remaining $6$ numbers from $995$ onwards, $995,\ 997,\ 999,\ 1000$ work, giving us $535 + 4 = \boxed{539}$ as the solution.

## Solution 2
Notice that $\left[ \frac{9}{5} \left[ \frac{5}{9} k \right] \right] = k$ holds if $k=\left[ \frac{9}{5}x\right]$ for some integer $x$ . Thus, after translating from $F\to F-32$ we want count how many values of $x$ there are such that $k=\left[ \frac{9}{5}x\right]$ is an integer from $0$ to $968$ . This value is computed as $\left[968*\frac{5}{9}\right]+1 = \boxed{539}$ , adding in the extra solution corresponding to $0$ .
### Note
Proof that $\left[ \frac{9}{5} \left[ \frac{5}{9} k \right] \right] = k$ if $k=\left[ \frac{9}{5}x\right]$ for some integer $x$ :
First assume that $k$ cannot be written in the form $k=\left[ \frac{9}{5}x\right]$ for any integer $x$ . Let $z = \left[ \frac{5}{9}k\right]$ . Our equation simplifies to $k = \left[ \frac{9}{5}z\right]$ . However, this equation is not possible, as we defined $k$ such that it could not be written in this form. Therefore, if $k \neq \left[ \frac{9}{5}x\right]$ , then $\left[ \frac{9}{5} \left[ \frac{5}{9} k \right] \right] \neq k$ .
Now we will prove that if $k = \left[ \frac{9}{5}x\right]$ , $\left[ \frac{9}{5} \left[ \frac{5}{9} k \right] \right] = k$ . We realize that because of the 5 in the denominator of $\left[ \frac{9}{5}x \right]$ , $\left[ \frac{9}{5}x \right]$ will be at most $\frac{2}{5}$ away from $\frac{9}{5}x$ . Let $z = \left[ \frac{9}{5}x \right]- \frac{9}{5}x$ , meaning that $-\frac{2}{5} \leq z \leq \frac{2}{5}$ . Now we substitute this into our equation:
\[\left[ \frac{9}{5} \left[ \frac{5}{9} k \right] \right] = \left[ \frac{9}{5} \left[ \frac{5}{9} \left[ \frac{9}{5}x\right] \right] \right] = \left[ \frac{9}{5} \left[ \frac{5}{9} (\frac{9}{5}x + z) \right] \right] = \left[ \frac{9}{5} \left[ \frac{5}{9} (\frac{9}{5}x + z) \right] \right] = \left[ \frac{9}{5} \left[ x+ \frac{5}{9}z \right] \right]\] .
Now we use the fact that $-\frac{2}{5} \leq z \leq \frac{2}{5}$
\[\left[ \frac{9}{5} \left[ x - \frac{5}{9}(\frac{2}{5}) \right] \right] \leq \left[ \frac{9}{5} \left[ x + \frac{5}{9}(z) \right] \right] \leq \left[ \frac{9}{5} \left[ x + \frac{5}{9}(\frac{2}{5}) \right] \right]\]
\[\left[ \frac{9}{5} x \right] \leq \left[ \frac{9}{5} \left[ x + \frac{5}{9}(z) \right] \right] = \left[ \frac{9}{5} \left[ \frac{5}{9}k \right] \right] \leq \left[ \frac{9}{5}x \right]\]
Hence $\left[ \frac{9}{5} \left[ \frac{5}{9}k \right] \right] = \left[ \frac{9}{5}x \right] = k$ and we are done.
- mako17

## Solution 3
Let $c$ be a degree Celsius, and $f=\frac 95c+32$ rounded to the nearest integer. Since $f$ was rounded to the nearest integer we have $|f-((\frac 95)c+32)|\leq 1/2$ , which is equivalent to $|(\frac 59)(f-32)-c|\leq \frac 5{18}$ if we multiply by $5/9$ . Therefore, it must round to $c$ because $\frac 5{18}<\frac 12$ so $c$ is the closest integer. Therefore there is one solution per degree Celsius in the range from $0$ to $(\frac 59)(1000-32) + 1=(\frac 59)(968) + 1=538.8$ , meaning there are $539$ solutions.

## Solution 4
Start listing out values for $F$ and their corresponding values of $C$ . You will soon find that every 9 values starting from $F$ = 32, there is a pattern:
$F=32$ : Works
$F=33$ : Doesn't work
$F=34$ : work
$F=35$ : Doesn’t work
$F=36$ : Works
$F=37$ : Works
$F=38$ : Doesn’t work
$F=39$ : Works
$F=40$ : Doesn’t work
$F=41$ : Works
There are $969$ numbers between $32$ and $1000$ , inclusive. This is $107$ sets of $9$ , plus $6$ extra numbers at the end. In each set of $9$ , there are $5$ “Works,” so we have $107\cdot5 = 535$ values of $F$ that work.
Now we must add the $6$ extra numbers. The number of “Works” in the first $6$ terms of the pattern is $4$ , so our final answer is $535 + 4 = 539$ solutions that work.
Submitted by warriorcats

## Solution 5(similar to solution 3 but faster solution if you have no time)
Notice that every $C$ value corresponds to exactly one $F$ value but multiple $F$ values can correspond to a $C$ value. Thus, the smallest $C$ value is $0$ and the largest $C$ value is $538$ yielding $\boxed{539}$ solutions.
-alanisawesome2018

## Video Solution
2007 AIME I #5
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.