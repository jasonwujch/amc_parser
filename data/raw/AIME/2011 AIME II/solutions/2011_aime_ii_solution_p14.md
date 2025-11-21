# 2011 AIME II Problem 14

## Problem

There are $N$ permutations $(a_{1}, a_{2}, ... , a_{30})$ of $1, 2, \ldots, 30$ such that for $m \in \left\{{2, 3, 5}\right\}$ , $m$ divides $a_{n+m} - a_{n}$ for all integers $n$ with $1 \leq n < n+m \leq 30$ . Find the remainder when $N$ is divided by $1000$ .

## Solutions

## Solution 1
Be wary of "position" versus "number" in the solution!
Each POSITION in the 30-position permutation is uniquely defined by an ordered triple $(i, j, k)$ . The $n$ th position is defined by this ordered triple where $i$ is $n \mod 2$ , $j$ is $n \mod 3$ , and $k$ is $n \mod 5$ . There are 2 choices for $i$ , 3 for $j$ , and 5 for $k$ , yielding $2 \cdot 3 \cdot 5=30$ possible triples. Because the least common multiple of 2, 3, and 5 is 30, none of these triples are repeated and all are used. By the conditions of the problem, if $i$ is the same in two different triples, then the two numbers in these positions must be equivalent mod 2. If $j$ is the same, then the two numbers must be equivalent $\mod 3$ , and if $k$ is the same, the two numbers must be equivalent mod 5. Take care to note that that doesn't mean that the number 1 has to have $1 \mod 2$ ! It's that the POSITION which NUMBER 1 occupies has $1 \mod 2$ !
The ordered triple (or position) in which 1 can be placed has 2 options for i, 3 for j, and 5 for k, resulting in 30 different positions of placement.
The ordered triple where 2 can be placed in is somewhat constrained by the placement of 1. Because 1 is not equivalent to 2 in terms of mod 2, 3, or 5, the i, j, and k in their ordered triples must be different. Thus, for the number 2, there are (2-1) choices for i, (3-1) choices for j, and (5-1) choices for k. Thus, there are 1*2*4=8 possible placements for the number two once the number one is placed.
Because 3 is equivalent to 1 mod 2, it must have the same i as the ordered triple of 1. Because 3 is not equivalent to 1 or 2 in terms of mod 3 or 5, it must have different j and k values. Thus, there is 1 choice for i, (2-1) choices for j, and (4-1) choices for k, for a total of $1\cdot 1 \cdot 3=3$ choices for the placement of 3.
As above, 4 is even, so it must have the same value of i as 2. It is also 1 mod 3, so it must have the same j value of 1. 4 is not equivalent to 1, 2, or 3 mod 5, so it must have a different k value than that of 1, 2, and 3. Thus, there is 1 choice for i, 1 choice for j, and (3-1) choices for k, yielding a total of $1 \cdot 1 \cdot 2=2$ possible placements for 4.
5 is odd and is equivalent to 2 mod 3, so it must have the same i value as 1 and the same j value of 2. 5 is not equivalent to 1, 2, 3, or 4 mod 5, so it must have a different k value from 1, 2, 3, and 4. However, 4 different values of k are held by these four numbers, so 5 must hold the one remaining value. Thus, only one possible triple is found for the placement of 5.
All numbers from 6 to 30 are also fixed in this manner. All values of i, j, and k have been used, so every one of these numbers will have a unique triple for placement, as above with the number five. Thus, after 1, 2, 3, and 4 have been placed, the rest of the permutation is fixed.
Thus, $N = 30 \cdot 8 \cdot 3 \cdot 2=30 \cdot 48=1440$ . Thus, the remainder when $N$ is divided by $1000$ is $\boxed{440}.$

## Solution 2
We observe that the condition on the permutations means that two numbers with indices congruent $\mod m$ are themselves congruent $\mod m$ for $m \in \{ 2,3,5\}.$ Furthermore, suppose that $a_n \equiv k \mod m.$ Then, there are $30/m$ indices congruent to $n \mod m,$ and $30/m$ numbers congruent to $k \mod m,$ because 2, 3, and 5 are all factors of 30. Therefore, since every index congruent to $n$ must contain a number congruent to $k,$ and no number can appear twice in the permutation, only the indices congruent to $n$ contain numbers congruent to $k.$ In other words, $a_i \equiv a_j \mod m \iff i \equiv j \mod m.$ But it is not necessary that $\textcolor{red}{(a_i\equiv i)\cup (a_j\equiv j)\mod m}$ . In fact, if that were the case, there would only be one way to assign the indices, since $2,3,5$ are relatively prime to each other and $30=\text{lcm}(2,3,5)$ : $\{a_1,a_2,\dots a_{30}\}\in\{1,2,\dots 30\}\text{ }respectively$ .
This tells us that in a valid permutation, the congruence classes $\mod m$ are simply swapped around, and if the set $S$ is a congruence class $\mod m$ for $m =$ 2, 3, or 5, the set $\{ a_i \vert i \in S \}$ is still a congruence class $\mod m.$ Clearly, each valid permutation of the numbers 1 through 30 corresponds to exactly one permutation of the congruence classes modulo 2, 3, and 5. Also, if we choose some permutations of the congruence classes modulo 2, 3, and 5, they correspond to exactly one valid permutation of the numbers 1 through 30. This can be shown as follows: First of all, the choice of permutations of the congruence classes gives us every number in the permutation modulo 2, 3, and 5, so by the Chinese Remainder Theorem, it gives us every number $\mod 2\cdot 3\cdot 5 = 30.$ Because the numbers must be between 1 and 30 inclusive, it thus uniquely determines what number goes in each index. Furthermore, two different indices cannot contain the same number. We will prove this by contradiction, calling the indices $a_i$ and $a_j$ for $i \neq j.$ If $a_i=a_j,$ then they must have the same residues modulo 2, 3, and 5, and so $i \equiv j$ modulo 2, 3, and 5. Again using the Chinese Remainder Theorem, we conclude that $i \equiv j \mod 30,$ so because $i$ and $j$ are both between 1 and 30 inclusive, $i = j,$ giving us a contradiction. Therefore, every choice of permutations of the congruence classes modulo 2, 3, and 5 corresponds to exactly one valid permutation of the numbers 1 through 30.
In other words, each set of assignment from $a_j\rightarrow j\mod (2,3,5)$ determines a unique string of $30$ numbers. For example:
$\left[(0,1)\rightarrow (1,0)\right]\cap\left[(0,1,2)\rightarrow (0,2,1)\right]\cap\left[(0,1,2,3,4)\rightarrow (4,2,3,0,1)\right]$ : \[\begin{array}{|c||c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|} \hline 2&1&0&1&0&1&0&1&0&1&0&1&0&1&0&1&0&1&0&1&0&1&0&1&0&1&0&1&0&1&0\\ \hline 3&0&2&1&0&2&1&0&2&1&0&2&1&0&2&1&0&2&1&0&2&1&0&2&1&0&2&1&0&2&1\\ \hline 5&4&2&3&0&1&4&2&3&0&1&4&2&3&0&1&4&2&3&0&1&4&2&3&0&1&4&2&3&0&1\\ \hline\hline 30&9&2&13&0&11&4&27&8&25&6&29&22&3&20&1&24&17&28&15&26&19&12&23&10&21&14&7&18&5&16\\ \hline \end{array}\]
We have now established a bijection between valid permutations of the numbers 1 through 30 and permutations of the congruence classes modulo 2, 3, and 5, so $N$ is equal to the number of permutations of congruence classes. There are always $m$ congruence classes $\mod m,$ so $N = 2! \cdot 3! \cdot 5! = 2 \cdot 6 \cdot 120 = 1440 \equiv \framebox[1.3\width]{440} \mod 1000.$

## Solution 3 (2-sec solve)
Note that $30=2\cdot 3\cdot 5$ . Since $\gcd(2, 3, 5)=1$ , by CRT, for each value $k=0\ldots 29$ modulo $30$ there exists a unique ordered triple of values $(a, b, c)$ such that $k\equiv a\pmod{2}$ , $k\equiv b\pmod{3}$ , and $k\equiv c\pmod{5}$ . Therefore, we can independently assign the residues modulo $2, 3, 5$ , so $N=2!\cdot 3!\cdot 5!=1440$ , and the answer is $\boxed{440}$ .
-vockey

## Solution 4( Better explanation of Solution 3)
First let's look at the situation when $m$ is equal to 2. It isn't too difficult to see the given conditions are satisfied iff the sequences $S_1 = a_1,a_3,a_5,a_7...$ and $S_2 =a_2,a_4,a_6...$ each are assigned either $\equiv 0 \pmod 2$ or $\equiv 1 \pmod 2$ . Another way to say this is each element in the sequence $a_1,a_3,a_5,a_7...$ would be the same mod 2, and similarly for the other sequence. There are 2! = 2 ways to assign the mods to the sequences.
Now when $m$ is equal to 3, the sequences are $T_1 = a_1, a_4,a_7..$ , $T_2 = a_2,a_5,a_8,a_11...$ , and $T_3 = a_3,a_6,a_9...$ . Again, for each sequence, all of its elements are congruent either $0$ , $1$ , or $2$ mod $3$ . There are $3! = 6$ ways to assign the mods to the sequences.
Finally do the same thing for $m = 5$ . There are $5!$ ways. In total there are $2 * 6*120 = 1440$ and the answer is $\boxed{440}$ .
Why does this method work? Its due to CRT.
-MathLegend27
Note: the explanation is not complete without mentioning that 2*3*5 = 30, therefore CRT guarantees there is only 1 permutation for every combination of mod selections. If the problem asked for permutations of ${1,2,...,60}$ , the answer would have been $2!3!5!2!2!2!$ .
-Mathdummy

## Solution 5(slightly more rigor than needed)
Note, for the purposes of this problem, it is easier to have our residue classes mod \( m \) to be \( \{1, 2, \dots, m\} \) instead of \( \{0, 1, 2, \dots, m-1\} \).
We will start by finding a general insight for \( m \) given that \( m \mid 30 \). \[m \mid (a_{i + m} - a_i) \implies a_{i + m} \equiv a_i \pmod{m}\] Notice that for every \( p \) between \( 1 \) and \( m \) inclusive, we have \[a_p \equiv a_{p+m} \equiv a_{p+2m} \equiv a_{p+3m} ... \pmod{m}.\] Notice that \( \{p, p+m, p+2m, \dots, p+km\} \) all fall under the residue class \( p \pmod{m} \). Let this list of numbers with indices that are \( p \pmod{m} \) all be congruent to \( \sigma_m(p) \pmod{m} \). Notice that \( \sigma_m \) maps numbers from \( \{1, 2, \dots, m\} \) to \( \{1, 2, \dots, m\} \).
$\textbf{Claim: \( \sigma_m \) is bijective.}$ Since \( \sigma_m \) is a valid function mapping two sets of the same size, we simply prove injectivity.
Assume for the sake of contradiction, for \( p \neq q \), let \( \sigma_m(p) \equiv \sigma_m(q) \pmod{m} \), and let them be congruent to some constant \( x \pmod{m} \). Since \( 1 \leq p, q \leq m \) and \( p \neq q \), this implies \( p \) and \( q \) are not congruent mod \( m \). \[\{p, p+m, p+2m, \dots \} \cap \{q, q+m, q+2m, \dots\} = \emptyset,\] since these sets are distinct mod \( m \).
Therefore, \( \sigma_m \) maps \( \frac{2 \cdot 30}{m} \) distinct values to some \( x \pmod{30} \). However, this implies that there are \( \frac{2 \cdot 30}{m} \) distinct values between \( 1 \) and \( 30 \) falling under the same residue class, which is obviously false. Thus, we have proven the claim.
Since \( \sigma_m \) is injective and maps between two sets of identical size, it is bijective. Therefore, there are \( m! \) ways to create such a mapping called \( \sigma_m \).
For this problem, there are \( 2! \cdot 3! \cdot 5! \) ways to find \( \sigma_2 \), \( \sigma_3 \), and \( \sigma_5 \). (Notice \( \sigma_k \) lies in the symmetric group \( S_k \).)
$\textbf{Claim: Finding \( \sigma_2 \), \( \sigma_3 \), and \( \sigma_5 \) completely determines \( a_i \).}$ If we know \( \sigma_2(i) \), \( \sigma_3(i) \), and \( \sigma_5(i) \), we know \( i \pmod{2} \), \( i \pmod{3} \), and \( i \pmod{5} \). By the Chinese Remainder Theorem (CRT), we know \( i \pmod{30} \), and since \( 1 \leq i \leq 30 \), this completely determines \( i \).
Therefore, \( 2! \cdot 3! \cdot 5! = 2 \cdot 6 \cdot 120 = 1440 \).
Therefore, the answer is $\boxed{440}$
~~Mathcounts Griiinder

## Video Solution
2011 AIME II #14
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .