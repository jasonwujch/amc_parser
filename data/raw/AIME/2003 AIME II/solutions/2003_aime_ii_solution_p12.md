# 2003 AIME II Problem 12

## Problem

The members of a distinguished committee were choosing a president, and each member gave one vote to one of the 27 candidates. For each candidate, the exact percentage of votes the candidate got was smaller by at least 1 than the number of votes for that candidate. What was the smallest possible number of members of the committee?

## Solution
Let $v_i$ be the number of votes candidate $i$ received, and let $s=v_1+\cdots+v_{27}$ be the total number of votes cast. Our goal is to determine the smallest possible $s$ .
Candidate $i$ got $\frac{v_i}s$ of the votes, hence the percentage of votes they received is $\frac{100v_i}s$ . The condition in the problem statement says that $\forall i: \frac{100v_i}s + 1 \leq v_i$ . ( $\forall$ means "for all", so this means "For all $i$ , $\frac{100v_i}s + 1 \leq v_i$ is true")
Obviously, if some $v_i$ would be $0$ or $1$ , the condition would be false. Thus $\forall i: v_i\geq 2$ . We can then rewrite the above inequality as $\forall i: s\geq\frac{100v_i}{v_i-1}$ .
If for some $i$ we have $v_i=2$ , then from the inequality we just derived we would have $s\geq 200$ .
If for some $i$ we have $v_i=3$ , then $s\geq 150$ .
And if for some $i$ we have $v_i=4$ , then $s\geq \frac{400}3 = 133\frac13$ , and hence $s\geq 134$ .
Is it possible to have $s<134$ ? We just proved that to have such $s$ , all $v_i$ have to be at least $5$ . But then $s=v_1+\cdots+v_{27}\geq 27\cdot 5 = 135$ , which is a contradiction. Hence the smallest possible $s$ is at least $134$ .
Now consider a situation where $26$ candidates got $5$ votes each, and one candidate got $4$ votes. In this situation, the total number of votes is exactly $134$ , and for each candidate the above inequality is satisfied. Hence the minimum number of committee members is $s=\boxed{134}$ .
Note: Each of the $26$ candidates received $\simeq 3.63\%$ votes, and the last candidate received $\simeq 2.985\%$ votes.

## Solution 2
Let there be $N$ members of the committee. Suppose candidate $n$ gets $a_n$ votes. Then $a_n$ as a percentage out of $N$ is $100\frac{a_n}{N}$ . Setting up the inequality $a_n \geq 1 + 100\frac{a_n}{N}$ and simplifying, $a_n \geq \lceil(\frac{N}{N - 100})\rceil$ (the ceiling function is there because $a_n$ is an integer. Note that if we set all $a_i$ equal to $\lceil(\frac{N}{100 - N})\rceil$ we have $N \geq 27\lceil(\frac{N}{100 - N})\rceil$ . Clearly $N = 134$ is the least such number that satisfies this inequality. Now we must show that we can find suitable $a_i$ . We can let 26 of them equal to $5$ and one of them equal to $4$ . Therefore, $N = \boxed{134}$ is the answer. - whatRthose

## Solution 3
Let $n$ be the total number of people in the committee, and $a_i$ be the number of votes candidate $i$ gets where $1 \leq i \leq 27$ . The problem tells us that \[\frac{100a_i}{n} \leq a_i - 1 \implies 100a_i \leq na_i - n \implies a_i \geq \frac{n}{n-100}.\] Therefore, \[\sum^{27}_{i=1} a_i = n \geq \sum^{27}_{i=1} \frac{n}{n-100} = \frac{27n}{n-100},\] and so $n(n-127) \geq 0 \implies n \geq 127$ . Trying $n = 127$ , we get that \[a_i \geq \frac{127}{27} \approx 4.7 \implies a_i \geq 5 \implies \sum^{27}_{a_i} a_i \geq 5 \cdot 27 = 135 \geq 127,\] a contradiction. Bashing out a few more, we find that $\boxed{n = 134}$ works perfectly fine.

## Video Solution by Sal Khan
https://www.youtube.com/watch?v=KD46pC_KFWk&list=PLSQl0a2vh4HCtW1EiNlfW_YoNAA38D0l4&index=10 - AMBRIGGS
These problems are copyrighted © by the Mathematical Association of America.