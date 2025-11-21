# 2025 AMC 10A Problem 16

## Problem

There are three jars. Each of three coins is placed in one of the three jars, chosen at random and independently of the placement of the other coins. What is the expected number of coins in a jar with the most coins?

$\textbf{(A) } \frac{4}{3}\qquad\textbf{(B) } \frac{13}{9}\qquad\textbf{(C) } \frac{5}{8}\qquad\textbf{(D) } \frac{17}{9}\qquad\textbf{(E) } 2$

## Solution 1 (Case Work)
We have three coins and three jars. Each coin is placed independently and randomly into one of the jars. Let $M$ be the maximum number of coins in any jar. We want to compute the expected value of $M$ .
Step 1: Count total outcomes
Each coin has $3$ choices, so the total number of equally likely placements is $3^3 = 27$ .
Step 2: Casework on the maximum number of coins
Case 1: $M = 1$ . This occurs when each jar has exactly one coin. There are $3! = 6$ assignments of coins to jars. Hence, $\Pr(M=1) = \frac{6}{27} = \frac{2}{9}$ .
Case 2: $M = 3$ . This occurs when all three coins fall into the same jar. There are $3$ jars to choose from, so $\Pr(M=3) = \frac{3}{27} = \frac{1}{9}$ .
Case 3: $M = 2$ . This occurs when one jar has $2$ coins, another jar has $1$ coin, and the last jar has $0$ coins. We can choose which jar gets $2$ coins in $3$ ways, which jar gets $1$ coin in $2$ ways, and which $2$ coins out of the $3$ go into the jar with two coins, so we multiply by $\dbinom{3}{2}$ , which is just $3$ (note we don't have to do this for the earlier cases because for case $2$ , all $3$ coins go into one jar, and for case $1$ , the factorial already accounts for that). Therefore, there are $3^2 \cdot 2 = 18$ outcomes. Thus, $\Pr(M=2) = \frac{18}{27} = \frac{2}{3}$ .
Step 3: Compute the expected value The expected value of $M$ is $\mathbb{E}[M] = 1 \cdot \frac{2}{9} + 2 \cdot \frac{2}{3} + 3 \cdot \frac{1}{9}$ . Converting everything to ninths, we have $\mathbb{E}[M] = \frac{2}{9} + \frac{12}{9} + \frac{3}{9} = \frac{17}{9}$ .
Hence, the expected number of coins in the jar with the most coins is $\boxed{\text{(D) }\frac{17}{9}}$ .
$Pr$ =Probability of
$\mathbb{E}$ =Expected value
~Boywithnuke(Goal to 10 followers)
~aldzandrtc(Fixed mistake, original = "Case 3: $M = 2$ . This occurs when one jar has 2 coins, another jar has 1 coin, and the last jar has 0 coins. We can choose which jar gets 2 coins in 3 ways, which jar gets 1 coin in 2 ways, and which jar is alone in 3 ways. Therefore, there are $3 \cdot 2 \cdot 3 = 18$ outcomes. Thus, $\Pr(M=2) = \frac{18}{27} = \frac{2}{3}$ ." After we choose which jar gets 2 coins, which jar gets one, we don't need to multiply by 3 to see which jar gets 0, because once the first 2 are picked, the last jar is set. However, the number $\frac{2}{3}$ is coincidentally correct, because you need assign which 2 coins go into the jar with 2 coins, so you multiply by 3 choose 2, which is 3. Feel free to fix it up, because I am not experienced with latex)
~ Minor edits by SixthGradeBookWorm927 ~ Minor edit by AlgeBruh16
~ Minor edit by jeffyang2025
### Another way of finding cases of M = 2
As described in the solution, there are $3^3=27$ ways of distributing the coins into the $3$ jars. Because there are $6$ ways for M=1 and $3$ ways for M=3, there are $27 - 6 - 3 = 18$ ways for $M=2$ .

## Solution 2 (Fast)
Assuming all jars and coins are distinct, there are $27$ total outcomes. $3!=6$ of them distribute exactly, and thus a max of, $1$ per cup, $3$ ways to choose a jar to put all $3$ coins in for a max of $3$ . This leaves $27-6-3=18$ for a max of $2$ , so the expected value is $\frac{6 \cdot 1 + 18 \cdot 2 + 3 \cdot 3}{27} = \boxed{\text{(D) }\frac{17}{9}}$
~megaboy6679

## Solution 3 (Circular Counting)
In circular counting, expected value is determined as \[\mathbb{E}_C n(A) = \frac{C n(A)}{\mathbb{T} - C n(A) - n(A)}\] Where \( \mathbb{E}_C n(A) \) is the expected value, \( C n(A) \) is the circular gap theorem, \( \mathbb{T} \) is the total number of cases, and \( n(A) \) is the invalid cases.
Arrange the three jars and three coins into a circle of 6 elements. We want to count all the ways in which no 2 or no 3 coins are next to one another. This can easily be done using the circular gap theorem, which states \[C n(A) = \frac{n}{k} \binom{n-k-1}{k-1}\] Where \( n \) is the number of elements in our circle and \( k \) is the number of non adjacencies, in which we wish to count \( n = 6 \) and \( k \in \{1,2,3\} \) (The reason we have only 1, 2, and 3 is because if we have \( n=6 \) and \( k \ge 4 \), we see that the combinatorial part of \( C n(A) \) becomes invalid).
So we begin counting.
For \( k=1 \), using the formula, we have \( \frac{6}{1} \binom{4}{0} \) which is 6.
For \( k=2 \), using the formula, we have \( \frac{6}{2} \binom{3}{1} \), which is 9.
For \( k=3 \), using the formula, we have \( \frac{6}{3} \binom{2}{2} \) which is 2.
Thus we have \( C_6(k \in \{1,2,3\}) = 6+9+2 = 17 \).
Now we calculate the denominator of \( \mathbb{E}_C n(A) \). We see the total number of cases is \( 3^3 = 27 \). So we can find \( \mathbb{T} - C n(A) \). We check for \( n(A) \), in which through common sense, we can see that if the triplet $(a,b,c)$ represents the number of coins given to each jar, the triplet $(1,1,1)$ doesn't satisfy the condition, as all jars have an equal number of coins. Therefore \( n(A)=1 \).
Our answer is \[\mathbb{E}_C n(A) = \frac{C n(A)}{\mathbb{T} - C n(A) - n(A)}\] \[\mathbb{E}_C n(A) = \frac{17}{27-17-1}\] \[\mathbb{E}_C n(A) = \boxed{\text{(D) }\frac{17}{9}}\]
~Pinotation

## Solution 4 (Weighted Probabilities)
WLOG label the jars as $1,2,3$ and the coins as $a,b,c$ . The probability for a given coin to land in a given jar is \[\frac{1}{3}\] The number of ways for all three coins to land in the same jar is $3$ , either all in jar $1$ , all in jar $2$ , or all in jar $3$ . Next, the number of ways to have two coins in one jar and one in another in another is $3^2 \cdot 2 = 18$ . Finally, since there are $3^3=27$ ways, the last weight is \[27-18-3=6\] Thus \[\frac{1}{27} \cdot 3 \cdot 3 + \frac{1}{27} \cdot 2 \cdot 18 + \frac{1}{27} \cdot 1 \cdot 6\] Thus we get \[\boxed{\text{(D) }\frac{17}{9}}\]
~Aeioujyot
~Minor $\LaTeX$ edit by jeffyang2025

## Solution 5
Denote the expected number of coins in a jar with the most coins as $E$
Hence, $E = 1 + \dfrac{1}{3} \times (1 + \dfrac{1}{3} \times 1) + \dfrac{2}{3} \times (0 + \dfrac{2}{3} \times 1) = \boxed{\text{(D) }\frac{17}{9}}$
~ reda_mandymath

## Solution 6
Create a tree diagram and add up the probabilities.
$P = \frac{3}{9} + \frac{2}{9} + \frac{2}{9} + \frac{2}{9} + \frac{2}{9} + \frac{2}{9} + \frac{2}{9} + \frac{1}{9} + \frac{1}{9} = \boxed{\text{(D)}\frac{17}{9}}$
Note: (It does not matter which jar you pick at the head of the diagram so long a you stay consistent) ~Rames_Jong

## Chinese Video Solution
https://www.bilibili.com/video/BV1nhkUByEzM/
~metrixgo

## Video Solution (In 1 Min)
https://youtu.be/8iDugBBzei8?si=QXHiwxmA5eqXyEZY ~ Pi Academy

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK

## Video Solution by grogg007
https://youtu.be/CCYoHk2Af34?start=1520

## Video Solution by Daily Dose of Math
https://youtu.be/WZmTGRl4O84
~Thesmartgreekmathdude
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .