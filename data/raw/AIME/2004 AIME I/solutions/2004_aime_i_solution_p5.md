# 2004 AIME I Problem 5

## Problem

Alpha and Beta both took part in a two-day problem-solving competition. At the end of the second day, each had attempted questions worth a total of 500 points. Alpha scored 160 points out of 300 points attempted on the first day, and scored 140 points out of 200 points attempted on the second day. Beta who did not attempt 300 points on the first day, had a positive integer score on each of the two days, and Beta's daily success rate (points scored divided by points attempted) on each day was less than Alpha's on that day. Alpha's two-day success ratio was 300/500 = 3/5. The largest possible two-day success ratio that Beta could achieve is $m/n,$ where $m$ and $n$ are relatively prime positive integers. What is $m+n$ ?

## Solution
Let $q$ be the number of questions Beta takes on day 1 and $a$ be the number he gets right. Let $b$ be the number he gets right on day 2.
These inequalities follow: \[\frac{a}{q} < \frac{160}{300} = \frac{8}{15}\] \[\frac{b}{500-q} < \frac{140}{200} = \frac{7}{10}\] Solving for a and b and adding the two inequalities: \[a + b < \frac{8}{15}q + (350 - \frac{7}{10}q)\] \[a + b < 350 - \frac{1}{6}q\] From here, we see the largest possible value of $a+b$ is $349$ .
Checking our conditions, we know that $a$ must be positive so therefore $q$ must be positive. A quick check shows that for $2\le q \le 5$ , $q$ follows all the conditions and results in $a+b=349$ .
This makes Beta's success ratio $\frac{349}{500}$ . Thus, the answer is $m+n = 349 + 500 = \boxed{849}$ .

## Simple Solution
We see that we want Beta to have more points where there is a higher Alpha success rate (that way, the score is shifted more towards the higher Alpha score). With that in mind, $.7 > 8/15$ . Thus, we might as well put as many points as possible into the second day.
That said, we need Beta to have a positive integer score on either end per requirements. The best way is for Beta to go $\frac{1}{2}$ on the first day. That way, we "waste" the least points- both in the numerator and denominator.
Thereafter, we see that, letting $x$ be the number of points Beta gained on the second day, $\frac{x}{498} < \frac{7}{10}$ ; thus $\max(x) = 348$ .
Aha. $348+1+500= \framebox{849}$ .
~minor $\LaTeX$ edit by Yiyj1
These problems are copyrighted © by the Mathematical Association of America.