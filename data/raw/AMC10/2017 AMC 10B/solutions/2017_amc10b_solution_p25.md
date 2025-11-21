# 2017 AMC 10B Problem 25

## Problem

Last year Isabella took $7$ math tests and received $7$ different scores, each an integer between $91$ and $100$ , inclusive. After each test she noticed that the average of her test scores was an integer. Her score on the seventh test was $95$ . What was her score on the sixth test?

$\textbf{(A)}\ 92\qquad\textbf{(B)}\ 94\qquad\textbf{(C)}\ 96\qquad\textbf{(D)}\ 98\qquad\textbf{(E)}\ 100$

## Solution 1
Let the sum of the scores of Isabella's first $6$ tests be $S$ . Because the mean of her first $7$ scores is an integer, then $S + 95 \equiv 0 \text{ (mod 7)} \Rightarrow S \equiv3 \text{ (mod 7)}$ . Also, $S \equiv 0 \text{ (mod 6)}$ , so by the CRT , $S \equiv 24 \text{ (mod 42)}$ . We also know that $91 \cdot 6 \leq S \leq 100 \cdot 6$ , so by inspection, $S = 570$ . However, we also have that the mean of the first $5$ test scores must be an integer, so the sum of the first $5$ test scores must be an multiple of $5$ , which implies that the $6$ th test score must also be a multiple of 5; observing the answer choices the only answer that is a multiple of 5 is $\boxed{\textbf{(E) } 100}$ .

## Solution 2
First, we find the largest sum of scores which is $100+99+98+97+96+95+94$ which equals $7(97)$ . Then we find the smallest sum of scores which is $91+92+93+94+95+96+97$ which is $7(94)$ . So the possible sums for the 7 test scores so that they provide an integer average are $7(97), 7(96), 7(95)$ and $7(94)$ which are $679, 672, 665,$ and $658$ respectively. Now in order to get the sum of the first 6 tests, we subtract $95$ from each sum producing $584, 577, 570,$ and $563$ . Notice only $570$ is divisible by $6$ so, therefore, the sum of the first $6$ tests is $570$ . We need to find her score on the $6th$ test so we have to find which number will give us a number divisible by $5$ when subtracted from $570.$ Since $95$ is the $7th$ test score and all test scores are distinct that only leaves $\boxed{\textbf{(E) } 100}$ .

## Solution 3
Since all of the scores are from $91 - 100$ , we can subtract 90 from all of the scores. Since the last score was a 95, the sum of the scores from the first six tests must be $2 \pmod 7$ and $0 \pmod 6$ . Trying out a few cases, the only solution possible is 30 (this is from adding numbers 1-10). The sixth test score must be $0 \pmod 5$ because $30\equiv 0\pmod5$ . The only possible test scores are $95$ and $100$ , and $95$ is already used, so the answer is $\boxed{\textbf{(E)}100}$ .

## Solution 4 (Working Backwards)
We work backwards to solve this problem. In the $n^{th}$ test, $\sum_{i=1}^{n} i$ (mod n) = 0. In the following table, the tests already taken are in bold, the latest test is underlined. We work from the row of (mod 7), (mod 6), and (mod 5) to determine the test order by trial and error.
\[\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|} \hline & 91 & 92 & 93 & 94 & 95 & 96 & 97 & 98 & 99 & 100 \\ \hline mod 7 & \textbf{0} & \textbf{1} & 2 & \textbf{3} & \underline{\textbf{4}} & \textbf{5} & \textbf{6} & 0 & 1 & \textbf{2} \\ \hline mod 6 & \textbf{1} & \textbf{2} & 3 & \textbf{4} & 5 & \textbf{0} & \textbf{1} & 2 & 3 & \underline{\textbf{4}} \\ \hline mod 5 & \textbf{1} & \textbf{2} & 3 & \underline{\textbf{4}} & 0 & \textbf{1} & \textbf{2} & 3 & 4 & 0 \\ \hline mod 4 & \underline{\textbf{3}} & \textbf{0} & 1 & 2 & 3 & \textbf{0} & \textbf{1} & 2 & 3 & 0 \\ \hline mod 3 & 1 & \textbf{2} & 0 & 1 & 2 & \textbf{0} & \underline{\textbf{1}} & 2 & 0 & 1 \\ \hline mod 2 & 1 & \underline{\textbf{0}} & 1 & 0 & 1 & \textbf{0} & 1 & 0 & 1 & 0 \\ \hline \end{tabular}\]
In the $4^{th}$ test, the test score could be 91 or 97.
As you can see, the test score of the $6^{th}$ test is $\boxed{\textbf{(E)}100}$
~ isabelchen

## Solution 5
Let's denote $x$ as $a_1+a_2+a_3+a_4+a_5+a_6$ , where $a_n$ is her $n$ th test score. We start by saying $\frac{x+95}{7} = [91,92,...100]$ . This results from the fact that her test averages are integers and her test scores are in the range of $91$ to $100$ . So $x+95=[637,644,...700] \implies x=[542,549,...605]$ . Next, we also see that $\frac{x}{6}=[91,92,...100]$ which becomes $x=[546,552,...600]$ . The only point of intersection of $[542,549,...605]$ and $[546,552,...600]$ is $570$ so $x=570$ . Now we can also see that $\frac{x-a_6}{5}=[91,92,...100]$ , so $x-a_6=[455,460,...500]$ , and since $x=570$ , $570-a_6=[455,460,...500] \implies a_6=570-[455,460,...500]$ . $a_6$ has to be in the range of $91$ and $100$ , so the only values in the set $[455,460,...500]$ that work are $470$ and $475$ which result in $a_6 = 100 \text{ or } 95$ respectively. But since her test scores are all distinct, and $95$ is already used for $a_7$ , our answer is $\boxed{\text{(E) }100}$ .
~Kempu33334

## Video Solution
https://youtu.be/YFz4bctJYVE ~Happytwin
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .