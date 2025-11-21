# 2018 AIME I Problem 12

## Problem

For every subset $T$ of $U = \{ 1,2,3,\ldots,18 \}$ , let $s(T)$ be the sum of the elements of $T$ , with $s(\emptyset)$ defined to be $0$ . If $T$ is chosen at random among all subsets of $U$ , the probability that $s(T)$ is divisible by $3$ is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m$ .

## Solution 1
The question asks us for the probability that a randomly chosen subset of the set of the first 18 positive integers has the property that the sum of its elements is divisible by 3. Note that the total number of subsets is $2^{18}$ because each element can either be in or not in the subset. To find the probability, we will find the total numbers of ways the problem can occur and divide by $2^{18}$ .
To simplify the problem, let’s convert the set to mod 3:
\[U' = \{1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0\}\]
Note that there are six elements congruent to 0 mod 3, 6 congruent to 1 mod 3, and 6 congruent to 2 mod 3. After conversion to mod three, the problem is the same but we’re dealing with much simpler numbers. Let’s apply casework on this converted set based on $S = s(T')$ , the sum of the elements of a subset $T'$ of $U'$ .
$\textbf{Case 1: }S=0$
In this case, we can restrict the subsets to subsets that only contain 0. There are six 0’s and each one can be in or out of the subset, for a total of $2^{6} = 64$ subsets. In fact, for every case we will have, we can always add a sequence of 0’s and the total sum will not change, so we will have to multiply by 64 for each case. Therefore, let’s just calculate the total number of ways we can have each case and remember to multiply it in after summing up the cases. This is equivalent to finding the number of ways you can choose such subsets without including the 0's. Therefore this case gives us $\boxed{1}$ way.
$\textbf{Case 2: }S= 3$
In this case and each of the subsequent cases, we denote the number of 1’s in the case and the number of two’s in the case as $x, y$ respectively. Then in this case we have two subcases;
$x, y = 3,0:$ This case has $\tbinom{6}{3} \cdot \tbinom{6}{0} = 20$ ways.
$x, y = 1,1:$ This case has $\tbinom{6}{1} \cdot \tbinom{6}{1} = 36$ ways.
In total, this case has $20+36=\boxed{56}$ ways.
$\textbf{Case 3: }S=6$
In this case, there are 4 subcases;
$x, y = 6,0:$ This case has $\tbinom{6}{6} \cdot \tbinom{6}{0} = 1$ way.
$x, y = 4,1:$ This case has $\tbinom{6}{4} \cdot \tbinom{6}{1} = 90$ ways.
$x, y = 2,2:$ This case has $\tbinom{6}{2} \cdot \tbinom{6}{2} = 225$ ways.
$x, y = 0,3:$ This case has $\tbinom{6}{0} \cdot \tbinom{6}{3} = 20$ ways.
In total, this case has $1+90+225+20=\boxed{336}$ ways.
Note that for each case, the # of 1’s goes down by 2 and the # of 2’s goes up by 1. This is because the sum is fixed, so when we change one it must be balanced out by the other. This is similar to the Diophantine equation $x + 2y= S$ and the total number of solutions will be $\tbinom{6}{x} \cdot \tbinom{6}{y}$ . From here we continue our casework, and our subcases will be coming out quickly as we have realized this relation.
$\textbf{Case 4: }S=9$
In this case we have 3 subcases:
$x, y = 5,2:$ This case has $\tbinom{6}{5} \cdot \tbinom{6}{1} = 90$ ways.
$x, y = 3,3:$ This case has $\tbinom{6}{3} \cdot \tbinom{6}{3} = 400$ ways.
$x, y = 1,4:$ This case has $\tbinom{6}{1} \cdot \tbinom{6}{4} = 90$ ways.
In total, this case has $90+400+90=\boxed{580}$ ways.
$\textbf{Case 5: } S=12$
In this case we have 4 subcases:
$x, y = 6,3:$ This case has $\tbinom{6}{6} \cdot \tbinom{6}{3} = 20$ ways.
$x, y = 4,4:$ This case has $\tbinom{6}{4} \cdot \tbinom{6}{4} = 225$ ways.
$x, y = 2,5:$ This case has $\tbinom{6}{2} \cdot \tbinom{6}{5} = 90$ ways.
$x, y = 0,6:$ This case has $\tbinom{6}{0} \cdot \tbinom{6}{6} = 1$ way.
Therefore the total number of ways in this case is $20 + 225 + 90 + 1=\boxed{336}$ . Here we notice something interesting. Not only is the answer the same as Case 3, the subcases deliver the exact same answers, just in reverse order. Why is that?
We discover the pattern that the values of $x, y$ of each subcase of Case 5 can be obtained by subtracting the corresponding values of $x, y$ of each subcase in Case 3 from 6 ( For example, the subcase 0, 6 in Case 5 corresponds to the subcase 6, 0 in Case 3). Then by the combinatorial identity, $\tbinom{6}{k} = \tbinom{6}{6-k}$ , which is why each subcase evaluates to the same number. But can we extend this reasoning to all subcases to save time?
Let’s write this proof formally. Let $W_S$ be the number of subsets of the set $\{1,2,1,2,1,2,1,2,1,2,1,2\}$ (where each 1 and 2 is distinguishable) such that the sum of the elements of the subset is $S$ and $S$ is divisible by 3. We define the empty set as having a sum of 0. We claim that $W_S = W_{18-S}$ .
$W_S = \sum_{i=1}^{|D|} \tbinom{6}{x_i}\tbinom{6}{y_i}$ if and only if there exists $x_i, y_i$ that satisfy $0\leq x_i \leq 6$ , $0\leq y_i \leq 6$ , $x_i + 2y_i = S$ , and $D$ is the set of the pairs $x_i, y_i$ . This is because for each pair $x_i$ , $y_i$ there are six elements of the same residue mod(3) to choose $x_i$ and $y_i$ numbers from, and their value sum must be $S$ .
Let all $x_n$ , $y_n$ satisfy $x_n = 6-x_i$ and $y_n = 6-y_i$ . We can rewrite the equation $x_i+ 2y_i = S \implies -x_i- 2y_i = -S \implies 6-x_i+ 6-2y_i= 12 - S$ $\implies 6-x_i+12-2y_i = 18-S \implies 6-x_i + 2(6-y_i) = 18-S$ \[\implies x_n + 2y_n = 18 - S\]
Therefore, since $0\leq x_i, y_i\leq 6$ and $x_n = 6-x_i$ and $y_n = 6-y_i$ , $0\leq x_n, y_n\leq 6$ . As shown above, $x_n + 2y_n = 18 - S$ and since $S$ and 18 are divisible by 3, 18 - $S$ is divisible by 3. Therefore, by the fact that $W_S = \sum_{i=1}^{|D|} \tbinom{6}{x_i}\tbinom{6}{y_i}$ , we have that;
$W_{18-S} = \sum_{n=1}^{|D|} \tbinom{6}{x_n}\tbinom{6}{y_n} \implies W_{18-S} = \sum_{i=1}^{|D|} \tbinom{6}{6-x_i}\tbinom{6}{6-y_i} \implies W_{18-S} = \sum_{i=1}^{|D|} \tbinom{6}{x_i}\tbinom{6}{y_i} = W_S$ , proving our claim.
We have found our shortcut, so instead of bashing out the remaining cases, we can use this symmetry. The total number of ways over all the cases is $\sum_{k=0}^{6} W_{3k} = 2 \cdot (1+56+336)+580 = 1366$ . The final answer is $\frac{2^{6}\cdot 1366}{2^{18}} = \frac{1366}{2^{12}} = \frac{683}{2^{11}}.$
There are no more 2’s left to factor out of the numerator, so we are done and the answer is $\boxed{\boxed{683}}$ .
~KingRavi

## Solution 2
Consider the elements of $U$ modulo $3.$
Ignore the $0$ 's because we're gonna multiply $\binom{6}{0}+..+\binom{6}{6}=2^6$ at the end. Let $a$ be the $1's$ and $b$ be the $2's$ . The key here is that $2 \equiv -1 \pmod{3}$ so the difference between the number of $a$ and $b$ is a multiple of $3$ .
1. Counted twice because $a$ and $b$ can be switched:
$6a$
$6a,3b$
$5a,2b$
$4a,b$
$3a$
2. Counted once:
$6a,6b$ ... $0a,0b$
By Vandermonde's Identity on the second case, this is $2^6 \left( 2\left(1+20+90+90+20\right) + \binom{12}{6} \right)\implies \boxed{683}$

## Solution 3 (Triple Vandermonde's)
Elements $0 \pmod{3}$ can either be included or excluded, for a total of $2^6$ . Then, like the previous solution, let $a$ be the number of elements $1 \pmod{3}$ and $b$ be the number of elements $2 \pmod{3}$ . Then, $a + 2b \equiv 0 \pmod{3} \implies a - b \equiv 0 \pmod{3}$ . Since $0 \le a, b \le 6$ , there are 3 cases:
$\>\>\>\> 1. \> a - b = 0$
Then, we have, \[\binom{6}{0}\binom{6}{0} + \binom{6}{1}\binom{6}{1} + \cdots + \binom{6}{6} \binom{6}{6}\]
Using the substitution $\binom{6}{k} = \binom{6}{6-k}$ on every second binomial coefficient, it is clear that the bottom numbers sum to $6$ , and the ones above sum to $12$ . Apply Vandermonde's, we obtain $\binom{12}{6}$
$\>\>\>\> 2. \> a - b = \pm 3$
For $a - b = 3$ , using the same substitution and applying Vandermonde's, we get: \[\binom{6}{3} \binom{6}{0} + \binom{6}{4} \binom{6}{1} + \cdots + \binom{6}{6} \binom{6}{3} = \binom{12}{3}\]
Then, for $a - b = -3$ , it is completely symmetric with $a - b = 3$ . We get $\binom{12}{3}$
$\>\>\>\> 3. \> a - b = \pm 6$
We have $\binom{6}{6} \binom{6}{0} + \binom{6}{0} \binom{6}{6} = 2$
We get $\frac{2^6 (\binom{12}{6} + 2 \binom{12}{3} + 2)}{2^{18}} = \frac{683}{2^{11}} \implies m = \boxed{683}$ .
~ CrazyVideoGamez

## Solution 4 (Symmetry)
Note that in general, the answer will be around $1/3$ of $2^{18}$ . We will use this to our advantage. Partition $U$ into disjoint subsets $\{1,2,3\}, \{4,5,6\}, \cdots, \{16,17,18\}$ . Within each of these subsets, there are 3 possible remainders $\mod 3$ depending on what elements we choose to include into $T$ : (Using set $\{1,2,3\}$ for demonstration purposes)
Remainder of zero: Include $\{3\}, \{1,2\}, \{\}, \{1,2,3\}$
Remainder of one: Include $\{1\}, \{1,3\}$
Remainder of two: Include $\{2\}, \{2,3\}$
Suppose all subsets are of the form $\{\}, \{1,2,3\}$ . Then, since both choices are $0 \pmod{3}$ , we can choose either one for all six subsets, giving us $2^6$ combinations.
On the other hand, suppose there exists a subset $V$ that isn't of the form $\{\}, \{1,2,3\}$ . Then, for $V$ , it is equally likely that a remainder of zero, one, or two is chosen, since each remainder has $2$ ways to be achieved, i.e. there is a $1/3$ chance for each. Consider the sum of the other subsets $T \setminus V$ . The sum is either $0, 1, 2 \pmod{3}$ . Whatever that remainder $r$ might be, we can always choose $3-r$ as the remainder for our set $V$ , giving us a total of $r + 3 - r \equiv 0 \pmod{3}$ . The probability we choose remainder $3-r$ is $1/3$ as previously mentioned. So, we get $\frac{1}{3}(2^{18} - 2^6)$ total combinations.
Therefore, we get $\frac{2^6 + \frac{1}{3}(2^{18} - 2^6)}{2^{18}} = \frac{683}{2^{11}} \implies m = \boxed{683}$
~ CrazyVideoGamez

## Solution 5
Rewrite the set after mod 3 as above
1 2 0 1 2 0 1 2 0 1 2 0 1 2 0 1 2 0
All 0s can be omitted
Case 1 No 1 No 2 $1$
Case 2 $222$ $20$
Case 3 $222222$ $1$
Case 4 $12$ $6*6=36$
Case 5 $12222$ $6*15=90$
Case 6 $1122$ $15*15=225$
Case 7 $1122222$ $15*6=90$
Case 8 $111$ $20$
Case 9 $111222$ $20*20=400$
Case 10 $111222222$ $20$
Case 11 $11112$ $15*6=90$
Case 12 $11112222$ $15*15=225$
Case 13 $1111122$ $6*15=90$
Case 14 $1111122222$ $6*6=36$
Case 15 $111111$ $1$
Case 16 $111111222$ $20$
Case 17 $111111222222$ $1$
Total $1+20+1+36+90+225+90+20+400+20+90+225+90+36+1+20+1=484+360+450+72=1366$
$P=\frac{1366}{2^{12}}=\frac{683}{2^{11}}$
ANS= $\boxed{683}$
By SpecialBeing2017

## Solution 6
Consider the numbers $\{1,4,7,10,13,16\}$ . Each of those are congruent to $1 \pmod 3$ . There is ${6 \choose 0}=1$ way to choose zero numbers ${6 \choose 1}=6$ ways to choose $1$ and so on. There ends up being ${6 \choose 0}+{6 \choose 3}+{6 \choose 6} = 22$ possible subsets congruent to $0\pmod 3$ . There are $2^6=64$ possible subsets of these numbers. By symmetry there are $21$ subsets each for $1 \pmod 3$ and $2 \pmod3$ .
We get the same numbers for the subsets of $\{2,5,8,11,14,17\}$ .
For $\{3,6,9,12,15,18\}$ , all $2^6$ subsets are $0 \pmod3$ .
So the probability is: $\frac{(22\cdot22+21\cdot21+21\cdot21)\cdot2^6}{2^{18}}=\frac{683}{2^{11}}$

## Solution 7
Notice that six numbers are $0\pmod3$ , six are $1\pmod3$ , and six are $2\pmod3$ . Having numbers $0\pmod3$ will not change the remainder when $s(T)$ is divided by $3$ , so we can choose any number of these in our subset. We ignore these for now. The number of numbers that are $1\pmod3$ , minus the number of numbers that are $2\pmod3$ , must be a multiple of $3$ , possibly zero or negative. We can now split into cases based on how many numbers that are $1\pmod3$ are in the set.
CASE 1- $0$ , $3$ , or $6$ integers: There can be $0$ , $3$ , or $6$ integers that are $2\pmod3$ . We can choose these in \[\left(\binom60+\binom63+\binom66\right)\cdot\left(\binom60+\binom63+\binom66\right)=(1+20+1)^2=484.\]
CASE 2- $1$ or $4$ integers: There can be $2$ or $5$ integers that are $2\pmod3$ . We can choose these in \[\left(\binom61+\binom64\right)\cdot\left(\binom62+\binom65\right)=(6+15)^2=441.\]
CASE 3- $2$ or $5$ integers: There can be $1$ or $4$ integers that are $2\pmod3$ . We can choose these in \[\left(\binom62+\binom65\right)\cdot\left(\binom61+\binom64\right)=(15+6)^2=441.\]
Adding these up, we get that there are $1366$ ways to choose the numbers such that their sum is a multiple of three. Putting back in the possibility that there can be multiples of $3$ in our set, we have that there are \[1366\cdot\left(\binom60+\binom61+\binom62+\binom63+\binom64+\binom65+\binom66\right)=1366\cdot2^6\] subsets $T$ with a sum that is a multiple of $3$ . Since there are $2^{18}$ total subsets, the probability is \[\frac{1366\cdot2^6}{2^{18}}=\frac{683}{2^{11}},\] so the answer is $\boxed{683}$ .

## Solution 8 (Generating Functions)
We use generating functions. Each element of $U$ has two choices that occur with equal probability--either it is in the set or out of the set. Therefore, given $n\in U$ , the probability generating function is \[\frac{1}{2}+\frac{1}{2}x^n.\] Therefore, in the generating function \[\frac{1}{2^{18}}(1+x)(1+x^2)(1+x^3)\cdots (1+x^{18}),\] the coefficient of $x^k$ represents the probability of obtaining a sum of $k$ . We wish to find the sum of the coefficients of all terms of the form $x^{3k}$ (where $k \in \mathbb{Z}_{\geq0}$ ). If $\omega=e^{2\pi i/3}$ is a cube root of unity, then it is well know that for a polynomial $P(x)$ , \[\frac{P(1)+P(\omega)+P(\omega^2)}{3}\] will yield the sum of the coefficients of the terms of the form $x^{3k}$ . (This is known as the third Roots of Unity Filter.) Then we find \begin{align*} \frac{1}{2^{18}}(1+1)(1+1^2)(1+1^3)\cdots (1+1^{18})&=1\\\frac{1}{2^{18}}(1+\omega)(1+\omega^2)(1+\omega^3)\cdots (1+\omega^{18})&=\frac{1}{2^{12}}\\\frac{1}{2^{18}}(1+\omega^2)(1+\omega^4)(1+\omega^6)\cdots (1+\omega^{36})&=\frac{1}{2^{12}}. \end{align*} To evaluate the last two products, we utilized the facts that $\omega^3=1$ and $1+\omega+\omega^2=0$ . Therefore, the desired probability is \[\frac{1+1/2^{12}+1/2^{12}}{3}=\frac{683}{2^{11}}.\] Thus the answer is $\boxed{683}$ .

## Solution 9
Define a set that "works" to be a set for which the sum of the terms is $0$ mod $3$ . The given set mod $3$ is \[\{1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0\}.\] Let $w(N)$ be the number of subsets of the first $N$ terms of this set that "work." Consider just the first $3$ terms: \[\{1,2,0\}.\] There are $2^3=8$ total subsets, and $w(3)=4$ (the subsets are $\emptyset, \{0\}, \{1,2\},$ and $\{1,2,0\}$ ). Now consider the first $6$ terms: \[\{1,2,0,1,2,0\}.\] To find $w(6)$ , we set aside the last $3$ terms as a "reserve" that we can pair with subsets of the first $3$ terms (which we looked at earlier).
First, all $2^3$ subsets of the first $3$ terms can either be paired with a $1$ or a $2$ (or nothing) from the "reserve" terms so that they "work," creating $2^3$ subsets that "work" already. But for each of these, we have the option to add a $0$ from the reserve, so we now have $2\cdot2^3$ subsets that "work." For each of the $w(3)=4$ subsets of the first $3$ terms that "work", we can also add on a $\{1,2\}$ or a $\{1,2,0\}$ from the reserves, creating $2w(3)$ new subsets that "work." And that covers all of them. With all of this information, we can write $w(6)$ as \[w(6)=2\cdot2^3+2w(3)=2(2^3+w(3)).\] The same process can be used to calculate $w(9)$ then $w(12)$ etc. so we can generalize it to \[w(N)=2(2^{N-3}+w(N-3)).\] Thus, we calculate $w(18)$ with this formula: \[w(18)=2( 2^{15} + 2( 2^{12} + 2( 2^9 + 2( 2^6 + 2( 2^3 + 4 ) ) ) ) )=87424.\] Because there are $2^{18}$ total possible subsets, the desired probability is \[\frac{w(18)}{2^{18}}=\frac{87424}{2^{18}}=\frac{683}{2048},\] so the answer is $\boxed{683}.$

## Solution 10
Try smaller cases and find a pattern. Using similar casework as in Solution 1, we can easily find the desired probability if $U$ is of a small size.
If $U = \{ 1,2,0\} \pmod 3$ , then $4$ out of $8$ subsets work, for a probability of $\tfrac12$ .
If $U = \{ 1,2,0,1,2,0\} \pmod 3$ , then $24$ out of $64$ subsets work, for a probability of $\tfrac38$ .
If $U = \{ 1,2,0,1,2,0,1,2,0\} \pmod 3$ , then $176$ out of $512$ subsets work, for a probability of $\tfrac{11}{32}$ .
Let $a_n$ be the numerator of the desired probability if $U$ is of size $3n$ . Then $a_1 = 1, a_2 = 3,$ and $a_3 = 11$ . Noticing that the denominators are multiplied by $4$ each time, we can conclude that the pattern of the numerators is $a_n = 4a_{n-1} - 1$ , so $a_6 = \boxed{683}$ .

## Solution 11 (Quick guesswork for about 2 minutes remaining)
We conjecture that the difference from the probability will be as small as possible from $\tfrac{1}{3}$ (The value approached as $n \rightarrow \infty$ , where $n$ is the number of terms in the largest subset).
We also see that there are $2^{18}$ subsets and know the denominator will be a power of $2$ (since the numerator is an integer).
We essentially want to guess that the greatest integer $n$ satisfying $\left(\frac{2^n}{3}\right)-1 <1000$ can be plugged in to get the solution of round $\left( \frac{2^n}{3} \right)$ .
We see that this occurs at $n=11$ , and get round $\left( \frac{2^{11}}{3} \right)=$ round( $682.66...$ )= $683$ .

## Solution 12 (Very quick recursion)
The total number of subsets is simply $2^{18}.$ Now we need to find the number of subsets that have a sum divisible by $3.$
Ignore the 6 numbers in the list that are divisible by 3. We look only at the number of subsets of $\{1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17\}$ then multiply by $2^6$ at the end. This is because adding a multiple of $3$ to the sum will not change whether it is divisible by $3$ or not and for each of the $6$ multiples, we have two options of whether to add it to the subset or not.
Now, let $f(3k)$ be the number of subsets of $\{1, 2, 4, 5, \dots, 3k-2, 3k-1\}$ that have a sum divisible by $3$ . There are $2k$ numbers in the set. Let us look at the first $2k - 2$ numbers: all subsets of the first $2k - 2$ numbers will have a residue $0, 1,$ or $2$ mod $3.$ If it is $0,$ add both $3k-2$ and $3k-1$ to the subset. If it is $1$ add just $3k-1$ to the set, and if it is $2$ add just $3k-2.$ We don't have to compute all three cases separately; since there is a 1 to 1 correspondence, we only need the sum of the three cases (which we know is $2^{2k-2}$ ).
Now, this counts all the subsets except for those that include neither $3k-1$ nor $3k-2.$ However, this is just $f(3k - 3).$ Thus, $f(3k) = 2^{2k-2} + f(3k-3)$ and the base case is $f(0) = 1.$ We have,
$f(18) = 2^{10} + f(15) = 2^{10} + 2^{8} + f(12) = \dots = 2^{10} + 2^8 + 2^6 + 2^4 + 2^2 + 2^0 + f(0).$ $=2^{10} + 2^8 + \dots + 2^2 + 2.$
Multiplying this by $2^6$ we have, \[\frac{2^7(1 + 2^1 + 2^3 + 2^5 + 2^7 + 2^9)}{2^{18}} .\] The $2^7$ cancels out with the denominator. However, the second term in the product is obviously odd and so does not cancel further with the denominator, which is just a power of $2.$ Thus, we want to find $1 + 2 + 2^3 + 2^5 + 2^7 + 2^9,$ which equals $\boxed{683}.$
Note: While the explanation may seem a bit complicated, the concept behind it is pretty simple. And once you get the solution, computing the answer doesn't take much time.

## Solution 13
The total number of subsets is $\sum_{i=0}^{18}\tbinom{18}{i}=2^{18}$ . If $s(T)\equiv 0\bmod{3}$ , the sum of the elements divides 3. We can rewrite the set as 6 0s, 6 1s, and 6 2s. We can ignore the zeros for now, since they won't influence the sum so we focus on each configuration of the 6 1s and 6 2s such that the sum is divisible by 3 and then multiply by $\sum_{i=0}^{6}\tbinom{6}{i}=2^6$ at the end. We proceed with casework on the number of values that are equivalent to $2\pmod{3}$ as follows:
Case 1: There are zero elements:
Then, there are only configurations of the values congruent to 1 mod 3. There are $\tbinom{6}{0}+\tbinom{6}{3}+\tbinom{6}{6}$ ways to assign values in the set that are congruent to 1 mod 3 such that the sum of those values divides 3. Therefore there are $22$ configurations for this case.
Case 2: There is one element:
There are $6$ ways to choose which element is included in the subset and $\tbinom{6}{1}+\tbinom{6}{4}$ ways to assign values to the numbers congruent to 1 mod 3 in the set. Therefore there are $6\cdot21=126$ configurations for this case.
Case 3: There are two elements:
There are $\tbinom{6}{2}=12$ ways to choose the 2 elements in the set that are congruent to 2 mod 3 and $\tbinom{6}{2}+\tbinom{6}{5}$ possible ways to assign values to the numbers congruent to 1 mod 3. Therefore there are $15\cdot21=315$ configurations for this case.
Case 4: There are three elements:
There are $\tbinom{6}{3}=20$ ways to choose three elements in the set that are congruent to 2 mod 3. There are $\tbinom{6}{0}+\tbinom{6}{3}+\tbinom{6}{6}$ ways to assign values to the numbers congruent to 1 mod 3. Therefore, there are $20\cdot22=440$ configurations for this case.
Case 5, Case 6, and Case 7 are symmetric to Case 3, Case 2, and Case 1 respectively so we can multiply by 2 for those cases.
Putting all the cases together we obtain $2(22+126+315) + 440=1366$ . Multiplying by $2^6$ gives $2^6\cdot1366=2^7\cdot683$ . Since $n=2^{18}$ , $\frac{m}{n}=\frac{683}{2^{11}}$ . Therefore, $m=\boxed{683}$
~ Magnetoninja

## Video Solution
https://www.youtube.com/watch?v=bOXCLR3Wric
(3b1b video on a very similar problem)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .