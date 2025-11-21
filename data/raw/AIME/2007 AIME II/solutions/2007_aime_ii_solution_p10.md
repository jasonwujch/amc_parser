# 2007 AIME II Problem 10

## Problem

Let $S$ be a set with six elements . Let $\mathcal{P}$ be the set of all subsets of $S.$ Subsets $A$ and $B$ of $S$ , not necessarily distinct, are chosen independently and at random from $\mathcal{P}$ . The probability that $B$ is contained in one of $A$ or $S-A$ is $\frac{m}{n^{r}},$ where $m$ , $n$ , and $r$ are positive integers , $n$ is prime , and $m$ and $n$ are relatively prime . Find $m+n+r.$ (The set $S-A$ is the set of all elements of $S$ which are not in $A.$ )

## Solution 1
Use casework :
- $B$ has 6 elements: Probability: must have either 0 or 6 elements, probability: .
- $B$ has 5 elements: Probability: must have either 0, 6, or 1, 5 elements. The total probability is .
- $B$ has 4 elements: Probability: must have either 0, 6; 1, 5; or 2,4 elements. If there are 1 or 5 elements, the set which contains 5 elements must have four emcompassing and a fifth element out of the remaining numbers. The total probability is .
- Probability: $\frac{1}{2^6} = \frac{1}{64}$
- $A$ must have either 0 or 6 elements, probability: $\frac{2}{2^6} = \frac{2}{64}$ .
- Probability: ${6\choose5}/64 = \frac{6}{64}$
- $A$ must have either 0, 6, or 1, 5 elements. The total probability is $\frac{2}{64} + \frac{2}{64} = \frac{4}{64}$ .
- Probability: ${6\choose4}/64 = \frac{15}{64}$
- $A$ must have either 0, 6; 1, 5; or 2,4 elements. If there are 1 or 5 elements, the set which contains 5 elements must have four emcompassing $B$ and a fifth element out of the remaining $2$ numbers. The total probability is $\frac{2}{64}\left({2\choose0} + {2\choose1} + {2\choose2}\right) = \frac{2}{64} + \frac{4}{64} + \frac{2}{64} = \frac{8}{64}$ .
We could just continue our casework. In general, the probability of picking B with $n$ elements is $\frac{{6\choose n}}{64}$ . Since the sum of the elements in the $k$ th row of Pascal's Triangle is $2^k$ , the probability of obtaining $A$ or $S-A$ which encompasses $B$ is $\frac{2^{7-n}}{64}$ . In addition, we must count for when $B$ is the empty set (probability: $\frac{1}{64}$ ), of which all sets of $A$ will work (probability: $1$ ).
Thus, the solution we are looking for is $\left(\sum_{i=1}^6 \frac{{6\choose i}}{64} \cdot \frac{2^{7-i}}{64}\right) + \frac{1}{64} \cdot \frac{64}{64}$ $=\frac{(1)(64)+(6)(64)+(15)(32)+(20)(16)+(15)(8)+(6)(4)+(1)(2)}{(64)(64)}$ $=\frac{1394}{2^{12}}$ $=\frac{697}{2^{11}}$ .
The answer is $697 + 2 + 11 = 710$ .

## Solution 2
we need $B$ to be a subset of $A$ or $S-A$ we can divide each element of $S$ into 4 categories:
- it is in $A$ and $B$
- it is in $A$ but not in $B$
- it is not in $A$ but is in $B$
- or it is not in $A$ and not in $B$
these can be denoted as $+A+B$ , $+A-B$ , $-A+B$ , and $-A-B$
we note that if all of the elements are in $+A+B$ , $+A-B$ or $-A-B$ we have that $B$ is a subset of $A$ which can happen in $\dfrac{3^6}{4^6}$ ways
similarly if the elements are in $+A-B$ , $-A+B$ , or $-A-B$ we have that $B$ is a subset of $S-A$ which can happen in $\dfrac{3^6}{4^6}$ ways as well
but we need to make sure we don't over-count ways that are in both sets these are when $+A-B$ or $-A-B$ which can happen in $\dfrac{2^6}{4^6}$ ways so our probability is $\dfrac{2\cdot 3^6-2^6}{4^6}= \dfrac{3^6-2^5}{2^{11}}=\dfrac{697}{2^{11}}$ .
so the final answer is $697 + 2 + 11 = 710$ .

## Solution 3
$B$ must be in $A$ or $B$ must be in $S-A$ . This is equivalent to saying that $B$ must be in $A$ or $B$ is disjoint from $A$ . The probability of this is the sum of the probabilities of each event individually minus the probability of each event occurring simultaneously. There are $\binom{6}{x}$ ways to choose $A$ , where $x$ is the number of elements in $A$ . From those $x$ elements, there are ${2^x}$ ways to choose $B$ . Thus, the probability that $B$ is in $A$ is the sum of all the values $\binom{6}{x}({2^x})$ for values of $x$ ranging from $0$ to $6$ . For the second probability, the ways to choose $A$ stays the same but the ways to choose $B$ is now ${2^{6-x}}$ . We see that these two summations are simply from the Binomial Theorem and that each of them is ${(2+1)^6}$ . We subtract the case where both of them are true. This only happens when $B$ is the null set. $A$ can be any subset of $S$ , so there are ${2^6}$ possibilities. Our final sum of possibilities is $2\cdot 3^6-2^6$ . We have ${2^6}$ total possibilities for both $A$ and $B$ , so there are ${2^{12}}$ total possibilities. This reduces down to $\dfrac{2\cdot 3^6-2^6}{4^6}= \dfrac{3^6-2^5}{2^{11}}=\dfrac{697}{2^{11}}$ . The answer is thus $697 + 2 + 11 = 710$ .

## Solution 4
Let $|S|$ denote the number of elements in a general set $S$ . We use complementary counting.
There is a total of $2^6$ elements in $P$ , so the total number of ways to choose $A$ and $B$ is $(2^6)^2 = 2^{12}$ .
Note that the number of $x$ -element subset of $S$ is $\binom{6}{x}$ . In general, for $0 \le |A| \le 6$ , in order for $B$ to be in neither $A$ nor $S-A$ , $B$ must have at least one element from both $A$ and $S-A$ . In other words, $B$ must contain any subset of $A$ and $S-A$ except for the empty set $\{\}$ . This can be done in $\binom{6}{|A|} (2^{|A|} - 1)(2^{6-|A|} - 1)$ ways. As $|A|$ ranges from $0$ to $6$ , we can calculate the total number of unsuccessful outcomes to be \[\sum_{|A| = 0}^{6} \binom{6}{|A|} (2^{|A|} - 1)(2^{6-|A|} - 1) = 2702.\] So our desired answer is \[1 - \dfrac{2702}{2^{12}} = \dfrac{697}{2^{11}} \Rightarrow \boxed{710}.\]
-MP8148

## Solution 5
To begin with, we note that there are $2^6$ subsets of $S$ (which we can assume is $\{1,2,3,4,5,6\}$ ), including the null set. This gives a total of $(2^6)^2 = 2^{12}$ total possibilities for A and B.
Case 1: B is contained in A. If B has $0$ elements, which occurs in $\binom{6}{0}$ ways, A can be anything, giving us $\binom{6}{0} \cdot 2^6$ . If B has $1$ element, A must contain that element, and then the remaining 5 are free to be in A or not in A. This gives us $\binom{6}{1} \cdot 2^5$ . Summing, we end up with the binomial expansion of $(2 + 1)^6 = 3^6$ .
Case 2: B is contained in S-A. By symmetry, this case is the same as Case 1, once again giving us $3^6$ possibilities.
Case 3: B is contained in both. We claim here that B can only be the null set. For contradiction, assume that there exists some element $x$ in B which satisfies this restriction. Then, A must contain $x$ as well, but we also know that $S-A$ contains $x$ , contradiction. Hence, B is the null set, whereas A can be anything. This gives us $2^6$ possibilities.
Since we have overcounted Case 3 in both of the other two cases, our final count is $2 \cdot 3^6 - 2^6$ . This gives us the probability $\frac{2 \cdot 3^6 - 2^6}{2^{12}}$ . Upon simplifying, we end up with $\frac{697}{2^{11}}$ , giving the desired answer of $\boxed{710}$ . - Spacesam
~clarifications by LeonidasTheConquerer

## Video Solution
2007 AIME II #10
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.