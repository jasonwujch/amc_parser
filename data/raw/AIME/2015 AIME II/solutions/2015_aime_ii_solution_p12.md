# 2015 AIME II Problem 12

## Problem

There are $2^{10} = 1024$ possible 10-letter strings in which each letter is either an A or a B. Find the number of such strings that do not have more than 3 adjacent letters that are identical.

## Solution 1
Let $f(n)$ be the number of valid arrangements in a string of length $n$ .
A string can end in 8 ways:
- ...AAA
- ...BBB
- ...AAB
- ...BBA
- ...BAB
- ...ABA
- ...ABB
- ...BAA
If it ends in ...AAA or ...BBB, the only condition is that the string of length $n-3$ preceding the 3 letters can't end with the same letters. If the string ends with ...AAA, the $n-3$ string must end with B in $f(n-3)/2$ ways, and if the string ends with ...BBB, the $n-3$ string must end with A in $f(n-3)/2$ ways, giving us a total of $f(n-3)$ ways.
If it ends in ...AAB or ...BBA, the $n-2$ string can't end with the 2 repeating letters coming after it. If it ends with ...AAB, the $n-2$ string can end in BB or AB or BA, and if it ends with ...BBA, the $n-2$ string can end in AA, AB, or BA. This happens in $4(f(n-2)/4) = f(n-2)$ ways.
Finally, if it ends in ...BAB, ...ABA, ...ABB, or ...BAA, the $n-1$ string must end in the last two letters (for example, if the string of length n ended in BAB, the n-1 string must end with BA). So this gives us $4(f(n-1)/4) = f(n-1)$ ways.
So $f(n) = f(n-1) + f(n-2) + f(n-3)$ . We can calculate the base cases pretty easily: $f(1)$ is 2, $f(2)$ is 4, $f(3)$ is 8, so $f(4)$ is 14. Now we continue working upwards: $f(5) = 14 + 8 + 4 = 26$ . $f(6) = 26 + 14 + 8 = 48$ . $f(7) = 48 + 26 + 14 = 88$ . $f(8) = 88 + 48 + 26 = 162$ . $f(9) = 162 + 88 + 48 = 298$ . Ans = $f(10) = 298 + 162 + 88 = \boxed{548}$ .
~ grogg007

## Solution 2
This is a recursion problem. Let $a_n$ be the number of valid strings of $n$ letters, where the last letter is $A$ . Similarly, let $b_n$ be the number of valid strings of $n$ letters, where the last letter is $B$ .
Note that $a_n=b_{n-1}+b_{n-2}+b_{n-3}$ for all $n\ge4$ .
Similarly, we have $b_n=a_{n-1}+a_{n-2}+a_{n-3}$ for all $n\ge4$ .
Here is why: every valid strings of $n$ letters $(n\ge4)$ where the first letter is $A$ must begin with one of the following:
$AAAB$ - and the number of valid ways is $b_{n-3}$ .
$AAB$ - and the number of valid ways is $b_{n-2}$ .
$AB$ - and there are $b_{n-1}$ ways.
We know that $a_1=1$ , $a_2=2$ , and $a_3=4$ . Similarly, we have $b_1=1$ , $b_2=2$ , and $b_3=4$ . We can quickly check our recursion to see if our recursive formula works. By the formula, $a_4=b_3+b_2+b_1=7$ , and listing out all $a_4$ , we can quickly verify our formula.
Therefore, we have the following:
$\begin{tabular}{c|c|c|c|c|c|c|c|c|c|c}Value of n & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10\\\hline a & 1 & 2 & 4 & 7 & 13 & 24 & 44 & 81 & 149 & 274\\b & 1 & 2 & 4 & 7 & 13 & 24 & 44 & 81 & 149 & 274\end{tabular}$
The total number of valid $10$ letter strings is equal to $a_{10}+b_{10}=274+274=\boxed{548}$ .
Notice that $a_n = b_n$ , since $a_1=b_1$ , $a_2=b_2$ , and $a_3=b_3$ . Therefore, we didn't really need to list out both recursion formulas, which could save us some time.

## Solution 3 (Without Recursion)
Playing around with strings gives this approach: We have a certain number of As, then Bs, and so on. Therefore, what if we denoted each solution with numbers like $(3,3,3,1)$ to denote AAABBBAAAB or vice versa (starting with Bs)? Every string can be represented like this!
We can have from 4 to 10 numbers in our parentheses. For each case, we will start with the largest number possible, usually a bunch of 3s, then go down systematically. Realize also that if we are left with just 2s and 1s, there is only one number of 2s and 1s that adds up to the leftover amount. Our final answer is the sum of all of these parenthetical sets [each set multiplied by its permutations, as order matters] multiplied by two [starting with either A or B, and alternating as we go along].
$4 \rightarrow (3,3,3,1) = 4, (3,3,2,2) = 6$
$5 \rightarrow (3, 3, 2, 1, 1) = 30, (3, 2, 2, 2, 1) = 20, (2,2,2,2,2)=1$
$6 \rightarrow (3,3,1,1,1,1) = 15, (3,2,2,1,1,1) = 60, (2,2,2,2,1,1) = 15$
$7 \rightarrow (3,2,1,1,1,1,1) = 42, (2,2,2,1,1,1,1) = 35$
$8 \rightarrow (3,1...1) = 8, (2,2,1...1) = 28$
$9 \rightarrow (2,1...1) = 9$
$10 \rightarrow (1,1....1) =1$
Adding them all up gives you 274; multiplying by 2 gives $\boxed{548}$ .

## Solution 4
We are going to build the string, 1 character at a time. And, we are going to only care about the streak of letters at the end of the string.
Let $a_n$ be the number of strings of length n that satisfy the problem statement and also has a "streak" of length 1 at the end. ABABBA has a streak of length 1.
Let $b_n$ be the number of strings of length n that satisfy the problem statement and also has of length 2 at the end. ABABBAA has a streak of length 2. There are 2 "A" s at the end of the string.
Let $c_n$ be the number of string of length n that that satisfy the problem statement and also has a "streak" of length 3 at the end. ABABBAAA has a streak of length 3. There are 3 "A" s at the end of the string.
Let's establish a recursive relationship. $a_{n+1} = a_n+b_n+c_n$ , since you can simply break the streak. $b_{n+1} = a_n$ , and $c_{n+1} = b_n$ Since you can just add to the streak.
We can log everything using a table.
$\begin{tabular}{c|c|c|c|c|c|c|c|c|c|c}Value of n & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10\\\hline a & 2 & 2 & 4 & 8 & 14 & 26 & 48 & 88 & 162 & 298\\b & 0 & 2 & 2 & 4 & 8 & 14 & 26 & 48 & 88 & 162 \\c & 0 & 0 & 2 & 2 &4 & 8 & 14 & 26 & 48 & 88\end{tabular}$
Adding $a_{10}$ , $b_{10}$ , $c_{10}$ gets the total number of numbers that doesn't have more than 3 concecutive letters.
That gets a total of $298+162+88 = \boxed{548}$
-AlexLikeMath

## Solution 5
Let $S_n$ be the number of n-letter strings satisfying the problem criteria. Then we can easily see $S_1 = 2, S_2 = 4, S_3 = 8, S_4 = 16-2 =14$ . For $n \ge 4$ consider the last three elements of the list. For example to get $S_5$ we could try to take $S_4$ and multiply by 2 since for each $S_4$ string we have two choices for the fifth character. However we have to be careful if the last three characters of $S_4$ are all the same, as in that case we would be overcounting, (i.e if we have a string $\dots aaa$ , we can only add $b$ to the end so that the problem criteria is satisfied. Additionally strings such as $\dots aaa$ or $\dots bbb$ should only be counted once as we only have one choice for the $n$ th character to add ( $b$ and $a$ respectively).
Thus to compute $S_n$ we start with $S_{n-1}$ then take out the strings ending in $\dots bbb$ or $\dots aaa$ . There are $S_{n-4}$ remaining valid strings (i.e if we pick any of the $S_{n-4}$ valid strings, examine the last character, if it is a $b$ then we append $aaa$ to it, and if if it an $a$ we append $bbb$ to it, hence the number of $S_{n-1}$ strings are in one-to-one correspondence with the number of strings in $S_{n-4}$ . Thus we have the recursion $S_n = 2(S_{n-1} - S_{n-4}) + S_{n-4}$ (where we are first taking away $S_{n-4}$ , doubling the result, then adding $S_{n-4}$ back in signifying that we only count it once, as described above).
The recursion simplifies to $S_n = 2S_{n-1} - S_{n-4}$ and we can now quickly compute the remaining values: \[S_5 = 2S_4 - S_1 = 26, S_6 = 2(26)-4 = 48, S_7 = 2(48) - 8 = 88, S_8 = 2(88) - 14 = 162, S_9 = 2(162) - 26 = 298, S_{10} = 2S_9 - 48 = \boxed{548}\]
~afroromanian

## Solution 6 (Generating Functions)
Let us define a "run" as a set of consecutive letters that are all the same and let a "maximal run" be a run that is not the proper subset of any other run, in other words, it cannot be expanded.
From now on, we consider all runs to be maximal.
Note that the minimum number of runs in the $10$ -letter string is $4$ (or else the Pigeonhole Principle tells us that at least $1$ run has $4$ or more letters in it, contradiction), and the maximum number of runs is clearly $10.$
Since an arbitrary run can have anywhere from $1$ to $3$ letters in it, it follows that the number of $10$ -letter strings with $n$ runs (where $4 \leq n \leq 10$ ) is \[2[x^{10}] (x+x^2+x^3)^n,\] i.e. twice the coefficient of $x^{10}$ in the expansion of $(x+x^2+x^3)^n.$ (Note that we multiplied by $2$ because there are two choices for which letter the first run has and then the rest are fixed).
Hence, we wish to find \[2\sum_{n=4}^{10} [x^{10}] (x+x^2+x^3)^n.\] First, we can rewrite this as \begin{align*} \sum_{n=4}^{10} [x^{10}] (x+x^2+x^3)^n &= \sum_{n=4}^{10} [x^{10}] \ x^n \cdot (1+x+x^2)^n \\ &= \sum_{n=4}^{10} [x^{10-n}] \left(\frac{1-x^3}{1-x}\right)^n \\ &= \sum_{n=4}^{10} [x^{10-n}] \frac{(1-x^3)^n}{(1-x)^n}. \\ \end{align*} Now, we proceed case by case, utilizing the Binomial Theorem for the numerator in all of the cases:
For $n=4,$ we have \begin{align*} [x^6] \frac{(1-x^3)^4}{(1-x)^4} &= \binom{4}{0} [x^6] (1-x)^{-4} - \binom{4}{1} [x^3] (1-x)^{-4} + \binom{4}{2} [x^0] (1-x)^{-4} \\ &= 1\cdot\binom{9}{3} - 4\cdot\binom{6}{3} + 6\cdot\binom{3}{3} \\ &= 1\cdot84-4\cdot20+6\cdot1 \\ &= 84-80+6 \\ &= \underline{10}. \end{align*} For $n=5,$ we have \begin{align*} [x^5] \frac{(1-x^3)^5}{(1-x)^5} &= \binom{5}{0} [x^5] (1-x)^{-5} - \binom{5}{1}[x^2] (1-x)^{-5} \\ &= 1\cdot\binom{9}{4}-5\cdot\binom{6}{4} \\ &= 1\cdot126-5\cdot15 \\ &= 126-75 \\ &= \underline{51}. \end{align*}For $n=6,$ we have \begin{align*} [x^4] \frac{(1-x^3)^6}{(1-x)^6} &= \binom{6}{0} [x^4](1-x)^{-6} - \binom{6}{1}[x^1](1-x)^{-6} \\ &= 1 \cdot \binom{9}{5} - 6 \cdot \binom{6}{5} \\ &= 1 \cdot 126 - 6 \cdot 6 \\ &= 126-36 \\ &= \underline{90}. \end{align*}For $n=7,$ we have \begin{align*} [x^3] \frac{(1-x^3)^7}{(1-x)^7} &= \binom{7}{0}[x^3](1-x)^{-7} - \binom{7}{1}[x^0](1-x)^{-7} \\ &= 1\cdot \binom{9}{6} - 7\cdot\binom{6}{6} \\ &= 1\cdot84-7\cdot1\\ &= 84-7 \\ &= \underline{77}. \end{align*}For $n=8,$ we have \begin{align*} [x^2] \frac{(1-x^3)^8}{(1-x)^8} &=\binom{8}{0} [x^2](1-x)^{-8} \\ &= 1\cdot\binom{9}{7} \\ &= 1\cdot36 \\ &= \underline{36}. \end{align*}For $n=9,$ we have \begin{align*} [x^1] \frac{(1-x^3)^9}{(1-x)^9} &= \binom{9}{0} [x^1] (1-x)^{-9}\\ &= 1\cdot\binom{9}{8} \\ &= 1\cdot9 \\ &= \underline{9}. \end{align*}For $n=10,$ we have \begin{align*} [x^0] \frac{(1-x^3)^{10}}{(1-x)^{10}} &= [x^0] (1-x)^{-10} \\ &= 1\cdot\binom{9}{9} \\ &= 1\cdot1 \\ &= \underline{1}. \end{align*}Hence, the answer is \begin{align*} 2\sum_{n=4}^{10} [x^{10-n}] \frac{(1-x^3)^n}{(1-x)^n} &= 2(10+51+90+77+36+9+1) \\ &= 2\cdot274 \\ &= \boxed{548}. \end{align*}
-lpieleanu
### Remark
2015 AMC 12A #22 is a harder version of this problem.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .