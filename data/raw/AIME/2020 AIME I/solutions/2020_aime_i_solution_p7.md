# 2020 AIME I Problem 7

## Problem

A club consisting of $11$ men and $12$ women needs to choose a committee from among its members so that the number of women on the committee is one more than the number of men on the committee. The committee could have as few as $1$ member or as many as $23$ members. Let $N$ be the number of such committees that can be formed. Find the sum of the prime numbers that divide $N.$

## Solution 1
Let $k$ be the number of women selected. Then, the number of men not selected is $11-(k-1)=12-k$ . Note that the sum of the number of women selected and the number of men not selected is constant at $12$ . Each combination of women selected and men not selected corresponds to a committee selection. Since choosing 12 individuals from the total of 23 would give $k$ women and $12-k$ men, the number of committee selections is $\binom{23}{12}$ . The answer is $\boxed{081}$ . ~awang11's sol

## Solution 2 (Bash)
We casework on the amount of men on the committee.
If there are no men in the committee, there are $\dbinom{12}{1}$ ways to pick the women on the committee, for a total of $\dbinom{11}{0} \cdot \dbinom{12}{1}$ . Notice that $\dbinom{11}{0}$ is equal to $\dbinom{11}{11}$ , so the case where no men are picked can be grouped with the case where all men are picked. When all men are picked, all women must also be picked, for a total of $\dbinom{12}{12}$ . Therefore, these cases can be combined to \[\dbinom{11}{0} \cdot \left(\dbinom{12}{1} + \dbinom{12}{12}\right)\] Since $\dbinom{12}{12} = \dbinom{12}{0}$ , and $\dbinom{12}{0} + \dbinom{12}{1} = \dbinom{13}{1}$ , we can further simplify this to \[\dbinom{11}{0} \cdot \dbinom{13}{1}\]
All other cases proceed similarly. For example, the case with one men or ten men is equal to $\dbinom{11}{1} \cdot \dbinom{13}{2}$ . Now, if we factor out a $13$ , then all cases except the first two have a factor of $121$ , so we can factor this out too to make our computation slightly easier. The first two cases (with $13$ factored out) give $1+66=67$ , and the rest gives $121(10+75+270+504) = 103,939$ . Adding the $67$ gives $104,006$ . Now, we can test for prime factors. We know there is a factor of $2$ , and the rest is $52,003$ . We can also factor out a $7$ , for $7,429$ , and the rest is $17 \cdot 19 \cdot 23$ . Adding up all the prime factors gives $2+7+13+17+19+23 = \boxed{081}$ .

## Video Solution:
https://youtu.be/MVxsY8DwHVk ~ avn

## Solution 3 (Vandermonde's identity)
Applying [1] by setting $m=12$ , $n=11$ , and $r=11$ , we obtain $\binom{23}{11}\implies$ $\boxed{081}$ . ~Lcz
### Short Proof
Consider the following setup: [asy] size(1000, 100); for(int i=0; i<23; ++i){ dot((i, 0)); } draw((10.5, -1.5)--(10.5, 1.5), dashed); [/asy] The dots to the left represent the men, and the dots to the right represent the women. Now, suppose we put a mark on $11$ people (the $*$ ). Those to the left of the dashed line get to be "in" on the committee if they have a mark. Those on the right side of the dashed line are already on the committee, but if they're marked they get forcibly evicted from it. If there were $x$ people marked on the left, there ends up being $12-(11-x) = x+1$ people not marked on the right. Circles represent those in the committee. [asy] size(1000, 100); for(int i=0; i<23; ++i){ dot((i, 0)); } for(int i=0; i<23; ++i){ if(i%2==0){ if(i >= 11){ draw(circle((i, 0), 0.25)); } continue; } label("$*$", (i,0.5), N); if(i < 11){ draw(circle((i, 0), 0.25)); } } draw((10.5, -1.5)--(10.5, 1.5), dashed); [/asy]
We have our bijection, so the number of ways will be $\binom{23}{11}$ .
~programjames1

## Solution 4
Notice that the committee can consist of $k$ boys and $k+1$ girls. Summing over all possible $k$ gives \[\sum_{k=0}^{11}\binom{11}{k}\binom{12}{k+1}=\binom{11}{0}\binom{12}{1}+\binom{11}{1}\binom{12}{2}+\cdots + \binom{11}{11}\binom{12}{12}\] Using the identity $\binom{n}{k}=\binom{n}{n-k}$ , and Pascal's Identity $\binom{n}{k}+\binom{n}{k+1}=\binom{n+1}{k+1}$ , we get \[\sum_{k=0}^{11}\binom{11}{k}\binom{12}{k+1}=\binom{12}{12}+\binom{12}{1}\left(\binom{11}{0}+\binom{11}{1}\right)+\cdots\] \[=\binom{12}{0}^2+\binom{12}{1}^2+\binom{12}{2}^2+\binom{12}{3}^2+\binom{12}{4}^2+\binom{12}{5}^2+\frac{\binom{12}{6}^2}{2}\] \[=\frac{1}{2}\sum_{k=0}^{12}\binom{12}{k}^2\] Using the identity $\sum_{k=0}^n\binom{n}{k}^2=\binom{2n}{n}$ , this simplifies to \[\frac{1}{2}\cdot \binom{24}{12}=\frac{24\cdot 23\cdot 22\cdot 21\cdot 20\cdot 19\cdot 18\cdot 17\cdot 16\cdot 15\cdot 14\cdot 13}{2\cdot 12\cdot 11\cdot 10\cdot 9\cdot 8\cdot 7\cdot 6\cdot 5\cdot 4\cdot 3\cdot 2}=2\cdot 7\cdot 13\cdot 17\cdot 19\cdot 23\] so the desired answer is $2+7+13+17+19+23=\boxed{081}$ ~ktong

## Solution 5 (Official MAA)
Select any $11$ club members. That group will have $i$ men and $11-i$ women, so the number of women in the club not selected in that group is $12 - (11-i) = i+1$ . Thus, if the committee includes the men who were selected and the women who were not selected, the committee would have the correct number of men and women. Conversely, for every committee that could be formed with $i$ men and $i+1$ women, the men on this committee together with the women not on the committee comprise a subset of $i + (12 - (i+1)) = 11$ club members. Thus \[N = \binom{23}{11}= \frac{23\cdot22\cdot21\cdot20\cdot19\cdot18\cdot17\cdot16\cdot15\cdot14\cdot13}{11\cdot10\cdot9\cdot8\cdot7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1}=23\cdot19\cdot17\cdot13\cdot7\cdot2.\] The requested sum is $23+19+17+13+7+2=\boxed{081}$ .

## Solution 6
Notice that if $k$ men are picked, then $k+1$ women must be picked. Furthermore, $k$ can range from $0$ to $11$ . Then, \[N=\sum_{k=0}^{11} \binom{11}{k}\binom{12}{k+1}=\binom{11}{0}\binom{12}{1}+\binom{11}{1}\binom{12}{2}+\dots+\binom{11}{11}\binom{12}{12}\] Since $\binom{n}{k}=\binom{n}{n-k}$ , this equals \[N=\binom{11}{0}\binom{12}{11}+\binom{11}{1}\binom{12}{10}+\dots+\binom{11}{11}\binom{12}{0}\] According to Vandermonde's Identity, \[N=\binom{11+12}{11}=\binom{23}{11}\] \[N=\frac{23!}{11!\cdot 12!}=\frac{2^{19}\cdot 3^9\cdot 5^4\cdot 7^3\cdot 11^2\cdot 13\cdot 17\cdot 19\cdot 23}{2^{10}\cdot 3^5\cdot 5^2\cdot 7\cdot 11\times 2^8\cdot 3^4\cdot 5^2\cdot 7\cdot 11}=2\cdot 7\cdot 13\cdot 17\cdot 19\cdot 23\rightarrow \boxed{081}\] ~ sid2012

## Solution 7 ( *Rigorous* Recursion)
Test the cases where there are $0$ men $1$ woman, $1$ man $2$ women, $2$ men $3$ women ... you will get the sequence $1$ , $3$ , $10$ , $35$ . Multiply all these numbers by $2$ to get $2$ , $6$ , $20$ , $70$ , which is also $\binom{2}{1}$ , $\binom{4}{2}$ , $\binom{6}{3}$ , $\binom{8}{4}$ . Thus, continuing this pattern, the case with $11$ men and $12$ women should have $\frac{\binom{24}{12}}{2}$ ways to select the committee. -Kevin2010

## Video Solution by OmegaLearn
https://youtu.be/pGkLAX381_s?t=684
~ pi_is_3.14

## Video Solution
https://youtu.be/MVxsY8DwHVk
(Solves using both methods - Casework and Vandermonde's Identity)

## Video Solution
https://www.youtube.com/watch?v=fxlQMiElGFk&list=PLLCzevlMcsWN9y8YI4KNPZlhdsjPTlRrb&index=6 ~ MathEx
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .