# 2023 AIME I Problem 11

## Problem

Find the number of subsets of $\{1,2,3,\ldots,10\}$ that contain exactly one pair of consecutive integers. Examples of such subsets are $\{\mathbf{1},\mathbf{2},5\}$ and $\{1,3,\mathbf{6},\mathbf{7},10\}.$

## Solution 1 (Minimal Casework)
Define $f(x)$ to be the number of subsets of $\{1, 2, 3, 4, \ldots x\}$ that have $0$ consecutive element pairs, and $f'(x)$ to be the number of subsets that have $1$ consecutive pair.
Using casework on where the consecutive element pair is, there is a unique consecutive element pair that satisfies the conditions. It is easy to see that \[f'(10) = 2f(7) + 2f(6) + 2f(1)f(5) + 2f(2)f(4) + f(3)^2.\]
We see that $f(1) = 2$ , $f(2) = 3$ , and $f(n) = f(n-1) + f(n-2)$ . This is because if the element $n$ is included in our subset, then there are $f(n-2)$ possibilities for the rest of the elements (because $n-1$ cannot be used), and otherwise there are $f(n-1)$ possibilities. Thus, by induction, $f(n)$ is the $n+1$ th Fibonacci number.
This means that $f'(10) = 2(34) + 2(21) + 2(2)(13) + 2(3)(8) + 5^2 = \boxed{235}$ .
~mathboy100

## Solution 2
We can solve this problem using casework, with one case for each possible pair of consecutive numbers.
$\textbf{Case 1: (1,2)}$
If we have (1,2) as our pair, we are left with the numbers from 3-10 as elements that can be added to our subset. So, we must compute how many ways we can pick these numbers so that the set has no consecutive numbers other than (1,2). Our first option is to pick no more numbers, giving us $8 \choose {0}$ . We can also pick one number, giving us $7 \choose {1}$ because 3 cannot be picked. Another choice is to pick two numbers and in order to make sure they are not consecutive we must fix one number in between them, giving us $6 \choose {2}$ . This pattern continues for each amount of numbers, yielding $5 \choose {3}$ for 3 numbers and $4 \choose {4}$ for four numbers. Adding these up, we have $8 \choose {0}$ + $7 \choose {1}$ + $6 \choose {2}$ + $5 \choose {3}$ + $4 \choose {4}$ = $\textbf{34}$ .
$\textbf{Case 2: (2,3)}$
If we have (2,3) as our pair, everything works the same as with (1,2), because 1 is still unusable as it is consecutive with 2. The only difference is we now have only 4-10 to work with. Using the same pattern as before, we have $7 \choose {0}$ + $6 \choose {1}$ + $5 \choose {2}$ + $4 \choose {3}$ = $\textbf{21}$ .
$\textbf{Case 3: (3,4)}$
This case remains pretty much the same except we now have an option of whether or not to include 1. If we want to represent this like we have with our other choices, we would say $2 \choose {0}$ for choosing no numbers and $1 \choose {1}$ for choosing 1, leaving us with $2 \choose {0}$ + $1 \choose {1}$ = 2 choices (either including the number 1 in our subset or not including it). As far as the numbers from 5-10, our pattern from previous cases still holds. We have $6 \choose {0}$ + $5 \choose {1}$ + $4 \choose {2}$ + $3 \choose {3}$ = 13. With 2 choices on one side and 13 choices on the other side, we have $2\cdot13$ = $\textbf{26}$ combinations in all.
$\textbf{Case 4: (4,5)}$
Following the patterns we have already created in our previous cases, for the numbers 1-3 we have $3 \choose {0}$ + $2 \choose {1}$ = 3 choices (1, 2, or neither) and for the numbers 6-10 we have $5 \choose {0}$ + $4 \choose {1}$ + $3 \choose {2}$ = 8 choices. With 3 choices on one side and 8 choices on the other side, we have $3\cdot8$ = $\textbf{24}$ combinations in all.
$\textbf{Case 5: (5,6)}$
Again following the patterns we have already created in our previous cases, for the numbers 1-4 we have $4 \choose {0}$ + $3 \choose {1}$ + $2 \choose {2}$ = 5 choices and for the numbers 5-10 we have the same $4 \choose {0}$ + $3 \choose {1}$ + $2 \choose {2}$ = 5 choices. $5\cdot5$ = $\textbf{25}$ combinations in all.
$\textbf{Rest of the cases}$
By symmetry, the case with (6,7) will act the same as case 4 with (4,5). This goes the same for (7,8) and case 3, (8.9) and case 2, and (9,10) and case 1.
Now, we simply add up all of the possibilities for each case to get our final answer. 34 + 21 + 26 + 24 + 25 + 24 + 26 + 21 + 34 = $\boxed{\textbf{(235)}}$
-Algebraik

## Solution 3 (Double Recursive Equations)
Denote by $N_1 \left( m \right)$ the number of subsets of a set $S$ that consists of $m$ consecutive integers, such that each subset contains exactly one pair of consecutive integers.
Denote by $N_0 \left( m \right)$ the number of subsets of a set $S$ that consists of $m$ consecutive integers, such that each subset does not contain any consecutive integers.
Denote by $a$ the smallest number in set $S$ .
First, we compute $N_1 \left( m \right)$ .
Consider $m \geq 3$ . We do casework analysis.
Case 1: A subset does not contain $a$ .
The number of subsets that has exactly one pair of consecutive integers is $N_1 \left( m - 1 \right)$ .
Case 2: A subset contains $a$ but does not contain $a + 1$ .
The number of subsets that has exactly one pair of consecutive integers is $N_1 \left( m - 2 \right)$ .
Case 3: A subset contains $a$ and $a + 1$ .
To have exactly one pair of consecutive integers, this subset cannot have $a + 2$ , and cannot have consecutive integers in $\left\{ a+3, a+4, \cdots , a + m - 1 \right\}$ .
Thus, the number of subsets that has exactly one pair of consecutive integers is $N_0 \left( m - 3 \right)$ .
Therefore, for $m \geq 3$ , \[N_1 \left( m \right) = N_1 \left( m - 1 \right) + N_1 \left( m - 2 \right) + N_0 \left( m - 3 \right) .\]
For $m = 1$ , we have $N_1 \left( 1 \right) = 0$ . For $m = 2$ , we have $N_1 \left( 2 \right) = 1$ .
Second, we compute $N_0 \left( m \right)$ .
Consider $m \geq 2$ . We do casework analysis.
Case 1: A subset does not contain $a$ .
The number of subsets that has no consecutive integers is $N_0 \left( m - 1 \right)$ .
Case 2: A subset contains $a$ .
To avoid having consecutive integers, the subset cannot have $a + 1$ .
Thus, the number of subsets that has no consecutive integers is $N_0 \left( m - 2 \right)$ .
Therefore, for $m \geq 2$ , \[N_0 \left( m \right) = N_0 \left( m - 1 \right) + N_0 \left( m - 2 \right) .\]
For $m = 0$ , we have $N_0 \left( 0 \right) = 1$ . For $m = 1$ , we have $N_0 \left( 1 \right) = 2$ .
By solving the recursive equations above, we get $N_1 \left( 10 \right) = \boxed{\textbf{(235) }}$ .
~ Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 4 (Recursive)
Let $a_n$ be the number of cases from a subset ranging from $1$ - $n$ . We approach the subset from the start and the back to build up a equation. We figure out cases if $1$ and $10$ is in the subset.
If $1$ and $10$ are both not in the subset, We get $a_n$ .
If $1$ is in the subset, and $10$ is not, We get multiple cases from this. If $2$ is in the subset, $3$ would not be in the subset. Now we have { $4$ , $5$ , $6$ , $7$ , $8$ , $9$ } and we'll have to determine how many subsets which there is no consecutive integers. After we do some testing, We get $a_n$ = $F_n+2$ . From this case we get $F_8$ . But if $2$ is not in the subset, We can just get $a_7$ . The same goes for when $10$ is in the subset and $1$ is not, it is also $F_8$ + $a_7$ .
But when $1$ and $10$ are both in the subset, We'll have to find more cases. If $2$ and $9$ are both not in the subset, We simply get $a_6$ . When $2$ is in the subset and $9$ isn't, We know that $3$ is not in the subset since $1$ and $2$ forms a pair, The sum of this case will be $F_7$ . The same also goes for when $9$ is in the subset and $2$ isnt. There is no cases for if $2$ and $9$ are both in the subset, Since that forms $2$ pairs.
Summarizing we get: $a_{10}$ = $a_8$ + $2$ $a_7$ + $a_6$ + $2$ $F_8$ + $2$ $F_7$ .
$2$ $F_8$ + $2$ $F_7$ = $2$ $F_9$ .
We get a equation of $a_{10}$ = $a_8$ + $2$ $a_7$ + $a_6$ + $2$ $F_9$
We compute the basic cases. $a_1$ = $0$ $a_2$ = $1$ $a_3$ = $2$ $a_4$ = $5$
\[\begin{array}{rcl} a & F_a & Cases\\ \hline 1 & 1 & 0 \\ 2 & 1 & 1 \\ 3 & 2 & 2 \\ 4 & 3 & 5 \\ 5 & 5 & 10 \\ 6 & 8 & 20 \\ 7 & 13 & 38 \\ 8 & 21 & 71 \\ 9 & 34 & 130 \\ 10 & 55 & 235 \\ \end{array}\]
We get our answer, $\boxed{235}$ .
~toub3490

## Solution 5 (Similar to Solution 3)
Let $a_n$ be the number of subsets of the set $\{1,2,3,\ldots,n\}$ such that there exists exactly 1 pair of consecutive elements. Let $b_n$ be the number of subsets of the set $\{1, 2, 3\ldots, n\}$ such that there doesn't exist any pair of consecutive elements. First, lets see how we can construct $a_n.$ For each subset $S$ counted in $a_n,$ either: 1. $\{n-1, n\}\subseteq S,$ 2. $n\not\in S$ , or 3. $n-1 \not\in S$ and $n\in S.$ The first case counts $b_{n-3}$ subsets (as $n-1$ cannot be included and the rest cannot have any consecutive elements), The second counts $a_{n-1},$ and the third counts $a_{n-2}.$ Thus, \[a_n = a_{n-1} + a_{n-2} + b_{n-3}.\] Next, Lets try to construct $b_n.$ For each subset $T$ counted in $b_n,$ either: 1. $n \not\in T,$ or 2. $n \in T.$ The first case counts $b_{n-1}$ subsets and the second counts $b_{n-2}.$ Thus, \[b_n = b_{n-1} + b_{n-2}.\] Since $b_1 = 2$ and $b_2 = 3,$ we have that $b_n = F_{n+1},$ so $a_n = a_{n-1} + a_{n-2} + F_{n-2}.$ (The $F_i$ is the $i$ th Fibonacci number). From here, we can construct a table of the values of $a_n$ until $n = 10.$ By listing out possibilities, we can solve for our first 3 values.
\[\begin{array}{r|l} n & a_n \\ \hline 1 & 0 \\ 2 & 1\\ 3 & 2\\ 4 & 2 + 1 + F_2 = 5\\5 & 5 + 2 + F_3 = 10\\6 & 10 + 5 + F_4 = 20 \\ 7 & 20 + 10 + F_5 = 38\\ 8 & 38 + 20 + F_6 = 71 \\ 9& 71 + 38 + F_7 = 130\\ 10 & 130 + 71 + F_8 = 235 \end{array}\] Our answer is $a_{10} = \boxed{235}.$ ~AtharvNaphade

## Solution 6 (Stars and Bars)
Note: This is a very common stars and bars application.
Casework on number of terms, let the number of terms be $n$ . We can come up with a generalized formula for the number of subsets with n terms.
Let $d_1, d_2, ..., d_{n-1}$ be the differences between the n terms. For example, in the set {2, 3, 6},
Let the range of the set be k for now, $d_1 + ... + d_{n-1} = k$ . We select one pair of terms to be consecutive by selecting one of the (n-1) terms to be 1. WLOG, let $d_1 = 1$ . $1 + d_2 + ... + d_{n-1} = k$ .
To ensure the other $d_2, d_3, ..., d_{n-1}$ are greater than 1 such that no two other terms are consecutive or the same, let $D_2 = d_2 + 1; D_3 = d_3 + 1; ...$ . $(n-2) + 1 + D_2 + ... + D_{n-1} = k$ where $D_2, D_3, ..., D_{n-1}$ are positive integers.
Finally, we add in $D_0$ , the distance between 0 and the first term of the set, and $D_n$ , the distance between the last term and 11. This way, the "distance" from 0 to 11 is "bridged" by $D_0$ , k, and $D_N$ . \[D_0 + k + D_n = D_0 + ((n-1) + D_2 + ... + D_{n-1}) + D_N = 11\] \[D_0 + D_2 + D_3 + ... + D_n = 12 - n\] There are n positive terms , by Balls and Urns , there are ${(12-n)-1 \choose (n)-1} = {11-n \choose n-1}$ ways of doing this. However, recall that there were $(n-1)$ ways, and we had used a WLOG to choose which two digits are consecutive. The final formula for the number of valid n-element subsets is hence $(n-1){11-n \choose n-1}$ for $n > 2$ .
Case 1: Two terms $n = 2$ , so $(2-1){11-2 \choose 2-1} = 1{9 \choose 1} = 9$
Case 2: Three terms $n = 3$ , so $(3-1){11-3 \choose 3-1} = 2{8 \choose 2} = 56$
Case 3: Four terms $n = 4$ , so $(4-1){11-4 \choose 4-1} = 3{7 \choose 3} = 105$
Case 4: Five terms $n = 5$ , so $(5-1){11-5 \choose 5-1} = 4{6 \choose 4} = 60$
Case 5: Six terms $n = 6$ , so $(6-1){11-6 \choose 6-1} = 5{5 \choose 5} = 5$
We can check by the Pigeonhole principle that there cannot be more than six terms, so the answer is $9+56+105+60+5=\boxed{235}$ .
~Mathandski

## Solution 7 (Fibonacci)
Note that there are $F_{n+2}$ subsets of a set of $n$ consecutive integers that contains no two consecutive integers. (This can be proven by induction.)
Now, notice that if we take $i$ and $i+1$ as the consecutive integers in our subset, we need to make a subset of the remaining integers such that it doesn't contain any two consecutive integers. Clearly, $i-1$ and $i+2$ cannot be chosen, and since $i-2$ and $i+3$ are sufficiently far apart, it is obvious we do not need to be concerned that an element of the set $\{1, 2, ... , i-2 \}$ is consecutive with any element of the set $\{ i+3, i+4, ... , 10 \}$
Thus, we can count the number of ways to choose a subset from the first set without any two elements being consecutive and multiply this by the number of ways to choose a subset from the second set without any two elements being consecutive. From above, and noting that the first set has $i-2$ consecutive integer elements and the second set has $8-i$ consecutive integer elements, we know that this is $F_i F_{10-i}.$
Summing this over for all $1 \leq i \leq 9$ yields \[\sum_{i=1}^9 F_i F_{10-i} = F_1F_9 + F_2F_8 + F_3F_7 + F_4F_6 + F_5 F_5 + F_6 F_4 + F_7 F_3 + F_8 F_2 + F_9 F_1 = 2(F_1F_9 + F_2F_8 + F_3F_7+F_4F_6) + F_5^2 = 2(1 \cdot 34 + 1 \cdot 21 + 2 \cdot 13 + 3 \cdot 8) + 5^2 = 2 \cdot 105+25 = \boxed{235}.\]
~lpieleanu

## Solution 8 (Polyominoes)
The problem is the same as laying out a line of polynomoes to cover spots $0,1,...10$ : 1 triomino ( $RGG$ ), $n$ dominoes ( $RG$ ), and $8-2n$ monominoes ( $R$ ). The $G$ spots cover the members of the subset. The total number spots is 11, because one $R$ spot always covers the 0, and the other spots cover 1 through 10.
There are 5 ways to choose polyomino sets, and many ways to order each set:
$R + RG + RGG =$ Polyominoes $\rightarrow$ Orderings
$0 + 4 + 1 = 5 \rightarrow 5! / 0!4!1! = ~~~5$
$2 + 3 + 1 = 6 \rightarrow 6! / 2!3!1! = ~60$
$4 + 2 + 1 = 7 \rightarrow 7! / 4!2!1! = 105$
$6 + 1 + 1 = 8 \rightarrow 8! / 6!1!1! = ~56$
$8 + 0 + 1 = 9 \rightarrow 9! / 8!0!1! = ~~~9$
The sum is $\boxed{235}$ .
~BraveCobra22aops

## Solution 9 (Dynamic Programming)
Let $dp(i)$ be the number of subsets of a set $i$ consecutive integers such that the maximum value in the set is $i$ and there exists exactly one pair of consecutive integers. Define $dp2(i)$ similarly, but without any pair of consecutive integers. The base cases are $dp2(1)=dp2(2)=1$ , $dp(1)=0$ , and $dp(2)=1$ .
The transitions are:
\[dp2(i)=\sum_{j=1}^{i-2}(dp2(j))+1\]
\[dp(i)=dp2(i-1)+\sum_{j=1}^{i-2}dp(j)\]
Note that $dp2$ is the Fibonacci numbers.
\[\begin{array}{rcl} i & dp & dp2\\ \hline 1 & 0 & 1 \\ 2 & 1 & 1 \\ 3 & 1 & 2 \\ 4 & 3 & 3 \\ 5 & 5 & 5 \\ 6 & 10 & 8 \\ 7 & 18 & 13 \\ 8 & 33 & 21 \\ 9 & 59 & 34 \\ 10 & 105 & 55 \\ \end{array}\]
Summing over $dp$ yields $1+1+3+5+10+18+33+59+105=\boxed{235}$
~Mathenthus

## Video Solution
https://youtu.be/7xqeCQiPrew
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution (Mathematical Dexterity)
https://www.youtube.com/watch?v=q1ffZP63q3I
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .