# 2021 AIME I Problem 10

## Problem

Consider the sequence $(a_k)_{k\ge 1}$ of positive rational numbers defined by $a_1 = \frac{2020}{2021}$ and for $k\ge 1$ , if $a_k = \frac{m}{n}$ for relatively prime positive integers $m$ and $n$ , then

\[a_{k+1} = \frac{m + 18}{n+19}.\] Determine the sum of all positive integers $j$ such that the rational number $a_j$ can be written in the form $\frac{t}{t+1}$ for some positive integer $t$ .

## Solution 1
We know that $a_{1}=\tfrac{t}{t+1}$ when $t=2020$ so $1$ is a possible value of $j$ . Note also that $a_{2}=\tfrac{2038}{2040}=\tfrac{1019}{1020}=\tfrac{t}{t+1}$ for $t=1019$ . Then $a_{2+q}=\tfrac{1019+18q}{1020+19q}$ unless $1019+18q$ and $1020+19q$ are not relatively prime which happens when $q+1$ divides $18q+1019$ (by the Euclidean Algorithm), or $q+1$ divides $1001$ . Thus, the least value of $q$ is $6$ and $j=2+6=8$ . We know $a_{8}=\tfrac{1019+108}{1020+114}=\tfrac{1127}{1134}=\tfrac{161}{162}$ . Now $a_{8+q}=\tfrac{161+18q}{162+19q}$ unless $18q+161$ and $19q+162$ are not relatively prime which happens the first time $q+1$ divides $18q+161$ or $q+1$ divides $143$ or $q=10$ , and $j=8+10=18$ . We have $a_{18}=\tfrac{161+180}{162+190}=\tfrac{341}{352}=\tfrac{31}{32}$ . Now $a_{18+q}=\tfrac{31+18q}{32+19q}$ unless $18q+31$ and $19q+32$ are not relatively prime. This happens the first time $q+1$ divides $18q+31$ implying $q+1$ divides $13$ , which is prime so $q=12$ and $j=18+12=30$ . We have $a_{30}=\tfrac{31+216}{32+228}=\tfrac{247}{260}=\tfrac{19}{20}$ . We have $a_{30+q}=\tfrac{18q+19}{19q+20}$ , which is always reduced by EA, so the sum of all $j$ is $1+2+8+18+30=\boxed{059}$ .
~sugar_rush
Remark 1
Whenever a fraction is in the form $\frac{t}{t+1}$ in lowest terms, the difference between the numerator and the denominator in the original fraction will always divide the numerator. We can model $a_j$ as $\frac{m+18k}{m+19k+1}$ (not necessarily simplified) if $a_{j-k}=\frac{m}{m+1}$ for integers $j$ and $k$ . We want the least $k$ such that $\gcd(k+1,{m+18k})\neq1$ . Let $d$ be a divisor of both $k+1$ and $m+18k$ , then $d\mid18k+18$ , so $d\mid{m-18}$ . This follows from the Euclidean Algorithm.
~ Magnetoninja
Remark 2
The reason we look for the least $q$ in each case is because after that $q$ or $j$ value, the fraction will simplify to $m/n$ again and it won't follow the condition we defined. For example, in the $a_{2+q}=\tfrac{1019+18q}{1020+19q}$ case, after $j = 8$ , the equation becomes useless because the fraction has simplified to something different, so we "switch over" to $a_{8+q}=\tfrac{161+18q}{162+19q}.$
~ grogg007

## Solution 2 (Euclidean Algorithm and Generalization)
Let $a_{j_1}, a_{j_2}, a_{j_3}, \ldots, a_{j_u}$ be all terms in the form $\frac{t}{t+1},$ where $j_1<j_2<j_3<\cdots<j_u,$ and $t$ is some positive integer.
We wish to find $\sum_{i=1}^{u}{j_i}.$ Suppose $a_{j_i}=\frac{m}{m+1}$ for some positive integer $m.$
To find we look for the smallest positive integer for which is reducible:
If $\frac{m+18k'}{m+1+19k'}$ is reducible, then there exists a common factor $d>1$ for $m+18k'$ and $m+1+19k'.$ By the Euclidean Algorithm , we have \begin{align*} d\mid m+18k' \text{ and } d\mid m+1+19k' &\implies d\mid m+18k' \text{ and } d\mid k'+1 \\ &\implies d\mid m-18 \text{ and } d\mid k'+1. \end{align*} Since $m-18$ and $k'+1$ are not relatively prime, and $m$ is fixed, the smallest value of $k'$ such that $\frac{m+18k'}{m+1+19k'}$ is reducible occurs when $k'+1$ is the smallest prime factor of $m-18.$
We will prove that for such value of the number can be written in the form \[a_{j_{i+1}}=a_{j_i+k'}=\frac{m+18k'}{m+1+19k'}=\frac{(m-18)+18(k'+1)}{(m-18)+19(k'+1)}=\frac{\frac{m-18}{k'+1}+18}{\frac{m-18}{k'+1}+19}, \hspace{10mm} (*)\] where $t=\frac{m-18}{k'+1}+18$ must be a positive integer.
We start with $m=2020$ and $a_{j_1}=a_1=\frac{2020}{2021},$ then find $a_{j_2}, a_{j_3}, \ldots, a_{j_u}$ by filling out the table below recursively: \[\begin{array}{c|c|c|c|c|c} & & & & & \\ [-2ex] \boldsymbol{i} & \boldsymbol{m} & \boldsymbol{m-18} & \boldsymbol{k'+1} & \boldsymbol{k'} & \boldsymbol{a_{j_{i+1}} \left(\textbf{by } (*)\right)} \\ [0.5ex] \hline & & & & & \\ [-1.5ex] 1 & 2020 & 2002 & 2 & 1 & \hspace{4.25mm} a_2 = \frac{1019}{1020} \\ [1ex] 2 & 1019 & 1001 & 7 & 6 & \hspace{2.75mm} a_8 = \frac{161}{162} \\ [1ex] 3 & 161 & 143 & 11 & 10 & a_{18} = \frac{31}{32} \\ [1ex] 4 & 31 & 13 & 13 & 12 & a_{30} = \frac{19}{20} \\ [1ex] 5 & 19 & 1 & \text{N/A} & \text{N/A} & \text{N/A} \\ [1ex] \end{array}\] As $\left(j_1,j_2,j_3,j_4,j_5\right)=(1,2,8,18,30),$ the answer is $\sum_{i=1}^{5}{j_i}=\boxed{059}.$
Remark
Alternatively, from $(*)$ we can set \[\frac{m+18k'}{m+1+19k'}=\frac{t}{t+1}.\] We cross-multiply, rearrange, and apply Simon's Favorite Factoring Trick to get \[\left(k'+1\right)(t-18)=m-18.\] Since $k'+1\geq2,$ to find the smallest $k',$ we need $k'+1$ to be the smallest prime factor of $m-18.$ Now we continue with the last two paragraphs of the solution above.
~MRENTHUSIASM

## Video Solution
https://youtu.be/oiUcYn1uYMM
~Math Problem Solving Skills

## Video Solution by Punxsutawney Phil
https://youtube.com/watch?v=LIjTty3rVso

## Video Solution by grogg007
https://m.youtube.com/watch?v=wvaveSgvKyc
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .