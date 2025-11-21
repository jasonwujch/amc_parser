# 2021 AMC 10A Problem 20

## Problem

In how many ways can the sequence $1,2,3,4,5$ be rearranged so that no three consecutive terms are increasing and no three consecutive terms are decreasing?

$\textbf{(A)} ~10\qquad\textbf{(B)} ~18\qquad\textbf{(C)} ~24 \qquad\textbf{(D)} ~32 \qquad\textbf{(E)} ~44$

## Solution 1 (Enumeration by Symmetry)
By symmetry with respect to $3,$ note that $(x_1,x_2,x_3,x_4,x_5)$ is a valid sequence if and only if $(6-x_1,6-x_2,6-x_3,6-x_4,6-x_5)$ is a valid sequence. We enumerate the valid sequences that start with $1,2,31,$ or $32,$ as shown below:
[asy] /* Made by MRENTHUSIASM */ size(16cm); draw((0.25,0)--(1.75,3),red,EndArrow); draw((0.25,0)--(1.75,0),red,EndArrow); draw((0.25,0)--(1.75,-3),red,EndArrow); draw((2.25,3)--(3.75,3),red,EndArrow); draw((2.25,0)--(3.75,0.75),red,EndArrow); draw((2.25,0)--(3.75,-0.75),red,EndArrow); draw((2.25,-3)--(3.75,-2.25),red,EndArrow); draw((2.25,-3)--(3.75,-3.75),red,EndArrow); draw((4.25,3)--(5.75,3),red,EndArrow); draw((4.25,0.75)--(5.75,0.75),red,EndArrow); draw((4.25,-0.75)--(5.75,-0.75),red,EndArrow); draw((4.25,-2.25)--(5.75,-2.25),red,EndArrow); draw((4.25,-3.75)--(5.75,-3.75),red,EndArrow); draw((6.25,3)--(7.75,3),red,EndArrow); draw((6.25,0.75)--(7.75,0.75),red,EndArrow); draw((6.25,-0.75)--(7.75,-0.75),red,EndArrow); draw((6.25,-2.25)--(7.75,-2.25),red,EndArrow); draw((6.25,-3.75)--(7.75,-3.75),red,EndArrow); label("$1$",(0,0)); label("$3$",(2,3)); label("$2$",(4,3)); label("$5$",(6,3)); label("$4$",(8,3)); label("$4$",(2,0)); label("$2$",(4,0.75)); label("$5$",(6,0.75)); label("$3$",(8,0.75)); label("$3$",(4,-0.75)); label("$5$",(6,-0.75)); label("$2$",(8,-0.75)); label("$5$",(2,-3)); label("$2$",(4,-2.25)); label("$4$",(6,-2.25)); label("$3$",(8,-2.25)); label("$3$",(4,-3.75)); label("$4$",(6,-3.75)); label("$2$",(8,-3.75)); draw((12.75,0)--(14.25,4.5),red,EndArrow); draw((12.75,0)--(14.25,1.5),red,EndArrow); draw((12.75,0)--(14.25,-1.5),red,EndArrow); draw((12.75,0)--(14.25,-4.5),red,EndArrow); draw((14.75,4.5)--(16.25,5.25),red,EndArrow); draw((14.75,4.5)--(16.25,3.75),red,EndArrow); draw((14.75,1.5)--(16.25,1.5),red,EndArrow); draw((14.75,-1.5)--(16.25,-0.75),red,EndArrow); draw((14.75,-1.5)--(16.25,-2.25),red,EndArrow); draw((14.75,-4.5)--(16.25,-3.75),red,EndArrow); draw((14.75,-4.5)--(16.25,-5.25),red,EndArrow); draw((16.75,5.25)--(18.25,5.25),red,EndArrow); draw((16.75,3.75)--(18.25,3.75),red,EndArrow); draw((16.75,1.5)--(18.25,1.5),red,EndArrow); draw((16.75,-0.75)--(18.25,-0.75),red,EndArrow); draw((16.75,-2.25)--(18.25,-2.25),red,EndArrow); draw((16.75,-3.75)--(18.25,-3.75),red,EndArrow); draw((16.75,-5.25)--(18.25,-5.25),red,EndArrow); draw((18.75,5.25)--(20.25,5.25),red,EndArrow); draw((18.75,3.75)--(20.25,3.75),red,EndArrow); draw((18.75,1.5)--(20.25,1.5),red,EndArrow); draw((18.75,-0.75)--(20.25,-0.75),red,EndArrow); draw((18.75,-2.25)--(20.25,-2.25),red,EndArrow); draw((18.75,-3.75)--(20.25,-3.75),red,EndArrow); draw((18.75,-5.25)--(20.25,-5.25),red,EndArrow); label("$2$",(12.5,0)); label("$1$",(14.5,4.5)); label("$3$",(14.5,1.5)); label("$4$",(14.5,-1.5)); label("$5$",(14.5,-4.5)); label("$4$",(16.5,5.25)); label("$5$",(16.5,3.75)); label("$1$",(16.5,1.5)); label("$1$",(16.5,-0.75)); label("$3$",(16.5,-2.25)); label("$1$",(16.5,-3.75)); label("$3$",(16.5,-5.25)); label("$3$",(18.5,5.25)); label("$3$",(18.5,3.75)); label("$5$",(18.5,1.5)); label("$5$",(18.5,-0.75)); label("$5$",(18.5,-2.25)); label("$4$",(18.5,-3.75)); label("$4$",(18.5,-5.25)); label("$5$",(20.5,5.25)); label("$4$",(20.5,3.75)); label("$4$",(20.5,1.5)); label("$3$",(20.5,-0.75)); label("$1$",(20.5,-2.25)); label("$3$",(20.5,-3.75)); label("$1$",(20.5,-5.25)); draw((25.25,0)--(26.75,1.5),red,EndArrow); draw((25.25,0)--(26.75,-1.5),red,EndArrow); draw((27.25,1.5)--(28.75,2.25),red,EndArrow); draw((27.25,1.5)--(28.75,0.75),red,EndArrow); draw((27.25,-1.5)--(28.75,-0.75),red,EndArrow); draw((27.25,-1.5)--(28.75,-2.25),red,EndArrow); draw((29.25,2.25)--(30.75,2.25),red,EndArrow); draw((29.25,0.75)--(30.75,0.75),red,EndArrow); draw((29.25,-0.75)--(30.75,-0.75),red,EndArrow); draw((29.25,-2.25)--(30.75,-2.25),red,EndArrow); draw((31.25,2.25)--(32.75,2.25),red,EndArrow); draw((31.25,0.75)--(32.75,0.75),red,EndArrow); draw((31.25,-0.75)--(32.75,-0.75),red,EndArrow); draw((31.25,-2.25)--(32.75,-2.25),red,EndArrow); label("$3$",(25,0)); label("$1$",(27,1.5)); label("$2$",(27,-1.5)); label("$4$",(29,2.25)); label("$5$",(29,0.75)); label("$4$",(29,-0.75)); label("$5$",(29,-2.25)); label("$2$",(31,2.25)); label("$2$",(31,0.75)); label("$1$",(31,-0.75)); label("$1$",(31,-2.25)); label("$5$",(33,2.25)); label("$4$",(33,0.75)); label("$5$",(33,-0.75)); label("$4$",(33,-2.25)); [/asy]
There are $16$ valid sequences that start with $1,2,31,$ or $32.$ By symmetry, there are $16$ valid sequences that start with $5,4,35,$ or $34.$ So, the answer is $16+16=\boxed{\textbf{(D)} ~32}.$
~MRENTHUSIASM (inspired by Snowfan)

## Solution 2 (Casework on the Consecutive Digits)
Reading the terms from left to right, we have two cases for the consecutive digits, where $+$ means increase and $-$ means decrease:
$\textbf{Case \#1: }\boldsymbol{+,-,+,-}$
$\textbf{Case \#2: }\boldsymbol{-,+,-,+}$
For $\text{Case \#1},$ note that for the second and fourth terms, one term must be $5,$ and the other term must be either $3$ or $4.$ We have four subcases:
$(1) \ \underline{\hspace{3mm}}3\underline{\hspace{3mm}}5\underline{\hspace{3mm}}$
$(2) \ \underline{\hspace{3mm}}5\underline{\hspace{3mm}}3\underline{\hspace{3mm}}$
$(3) \ \underline{\hspace{3mm}}4\underline{\hspace{3mm}}5\underline{\hspace{3mm}}$
$(4) \ \underline{\hspace{3mm}}5\underline{\hspace{3mm}}4\underline{\hspace{3mm}}$
For $(1),$ the first two blanks must be $1$ and $2$ in some order, and the last blank must be $4.$ So, we get $2$ possibilities. Similarly, $(2)$ also has $2$ possibilities.
For $(3),$ there are no restrictions for the numbers $1, 2,$ and $3.$ So, we get $3!=6$ possibilities. Similarly, $(4)$ also has $6$ possibilities.
Together, $\text{Case \#1}$ has $2+2+6+6=16$ possibilities. By symmetry, $\text{Case \#2}$ also has $16$ possibilities.
Finally, the answer is $16+16=\boxed{\textbf{(D)} ~32}.$
Remark
This problem is somewhat similar to 2004 AIME I Problem 6 .
~MRENTHUSIASM

## Solution 3 (Casework Similar to Solution 2)
Like Solution 2, we have two cases. Due to symmetry, we just need to count one of the cases. For the purpose of this solution, we will be doing $-,+,-,+$ . Instead of starting with 5, we start with 1.
There are two ways to place it:
_1_ _ _
_ _ _1_
Now we place 2, it can either be next to 1 and on the outside, or is place in where 1 would go in the other case. So now we have another two "sub case":
_1_2_(case 1)
21_ _ _(case 2)
There are 3! ways to arrange the rest for case 1, since there is no restriction.
For case 2, we need to consider how many ways to arrange 3,4,5 in a a>b<c fashion. It should seem pretty obvious that b has to be 3, so there will be 2! way to put 4 and 5.
Now we find our result, times 2 for symmetry, times 2 for placement of 1 and times (3!+2!) for the two different cases for placement of 2. This give us $2*2*(3!+2!)=4*(6+2)=\boxed{\textbf{(D)} ~32}$ .
~~Xhte

## Solution 4 (Casework on the Position of 5)
We only need to find the # of rearrangements when 5 is the 4th digit and 5th digit. Find the total, and multiply by 2. Then we can get the answer by adding the case when 5 is the third digit.
Case : 5 is the 5th digit. __ __ __ __ 5
Then $4$ can only be either 1st digit or the 3rd digit.
4 __ __ __ 5, then the only way is that $3$ is the 3rd digit, so it can be either $231$ or $132$ , give us $2$ results.
__ __ 4 __ 5, then the 1st digit must be $2$ or $3$ , $2$ gives us $1$ way, and $3$ gives us $2$ ways. (Can't be $1$ because the first digit would increasing). Therefore, $4$ in the middle and $5$ in the last would result in $3$ ways.
Case : $5$ is the fourth digit. __ __ __ 5 __
Then the last digit can be all of the 4 numbers $1$ , $2$ , $3$ , and $4$ . Let's say if the last digit is $4$ , then the 2nd digit would be the largest for the remaining digits to prevent increasing order or decreasing order. Then the remaining two are interchangeable, give us $2!$ ways. All of the $4$ can work, so case $2$ would result in $2!+2!+2!+2!=8$ ways.
Case : $5$ is in the middle. __ __ 5 __ __
Then there are only two cases: 1. $42513$ , then 4 and 3 are interchangeable, which results in $2!*2!$ . Or it can be $43512$ , then 4 and 2 are interchangeable, but it can not be $23514$ , so there can only be 2 possible ways: $43512$ , $21534$ .
Therefore, case 3 would result in $4+2=6$ ways.
$8+3+2=13$ , so the total ways for case 1 and case 2 with both increasing and decreasing would be $13*2=26.$
Finally, we have $26+6=\boxed{\textbf{(D)} ~32}.$
~Michael595

## Solution 5 (Overcounting)
First, we list the triples that are invalid:
543, 542, 541, 532, 531, 521, 432, 431, 321
By symmetry, there are the same amount of increasing triplets as there are decreasing ones. This yields 18 invalid 3 digit permutations in total.
Suppose the triplet is ABC and the other 2 digits are X and Y. We then have 3 ways to arrange a triplet with 2 other digits.
ABCXY, XABCY, XYABC
X and Y can be arranged 2 ways.
XY, YX
This produces 18*3*2=108 permutations of invalid results. We have 5! ways to arrange 5 numbers so 120-108=12.
Now, we must account for overcounting. For example, when 543 is counted, it only registers as one invalid permutation but in fact, it is 3 whole invalid permutations. We then complete this for the rest of the list:
54321 has 543, 432, and 321
54213 has 542 and 421
54123 has 541 and 123
53214 has 532 and 321
53124 has 531 and 124
52134 has 521 and 134
43215 has 432 and 321
43125 has 431 and 125
32145 has 321 and 145
This produces 19 values that we have overcounted but this value itself is also overcounted. We already counted 9 of the terms. This brings the final value of overcounted terms down to 10 for the decreasing triplets. By symmetry, 10 increasing triplets were overcounted.
This gives us $120-108+20=\boxed{\textbf{(D)} ~32}.$
~ Lukiebear

## Solution 6 (Using a Table)
It is easier to consider the complement of the desired cases, so try to find the cases that DO have three integers in increasing order. First, write down the sets of three numbers that feature the numbers in increasing order. They are $123, 124, 125, 134, 135, 145, 234, 245, 345$ . Each of these can be in three positions: the three are in the front with two more numbers in the back, the three are in the middle with two on each side, and two in the front and the set of three in the back. Now, count the number of combinations of $5$ numbers that each of the set of three can form that have not been previously accounted for. Also, if the set features both $3$ increasing and $3$ decreasing, then do not count it because we will separately count them.
\[\begin{tabular}[t]{|l|c|c|c|} \hline Three Increasing Numbers&Front&Middle&Back\\\hline 123&2&2&2\\\hline 124&2&2&2\\\hline 125&1&2&2\\\hline 134&2&2&2\\\hline 135&1&2&2\\\hline 145&1&2&2\\\hline 234&2&1&1\\\hline 245&1&1&1\\\hline 345&1&0&1\\\hline \end{tabular}\]
This gives us a total of $41$ possibilities. These account for the possibilities with ONLY increasing numbers. Mirror over to the other side to get the set of combinations with either at least $1$ set of $3$ increasing numbers in a row or only at least $1$ set of $3$ decreasing numbers, but not both. We can count the ones with both separately. $14532, 12543, 13542, 54123, 53124, 52134$ . Total of $6$ .
$41\cdot 2+6=82+6=88$ . This is the compliment. There are a total of $5!=120$ . $120-88=32$ .
Thus, the answer is $\boxed{\textbf{(D)} ~32}$ .
~Evan Liu ~Marshall_Huang (changes to LaTex and one spelling error)

## Solution 7 (Symmetry)
First, note that there is a symmetry from $+,-,+,-$ to $-,+,-,+$ as follows: $a, b, c, d, e \leftrightarrow 6-a, 6-b, 6-c, 6-d, 6-e$ . Now, consider the placement of 5 in the $+,-,+,-$ case. Clearly, 5 is the maximum value, so it must be placed in the 2nd position or the 4th position, but we also have symmetry $a, b, c, d, e \leftrightarrow e, d, c, b, a$ . We will find the number of sequences with 5 in the second position by using casework on the position of the 4.
Case 1:
4 5 __ __ __: 3 is the maximum value, so it must go into the 4th position, leaving us 2 ways to fill in 1 and 2.
Case 2:
__ 5 __ 4 __: 1, 2, and 3 are all less than 4 or 5, so they can be filled in any manner: 3! = 6.
Overall, we have 8 ways to fill in the sequences. By our two types of symmetry, there are $8 \cdot 2 \cdot 2 = \boxed{\textbf{(D)} ~32}$ .
~alligator112

## Solution 8 (PIE: No Casework)
We use complementary counting.
Let $A$ be the set of all permutations $(a_1, a_2, a_3, a_4, a_5)$ of $(1,2,3,4,5)$ in which there exists at least one set of three consecutive increasing terms, and let $B$ be the set of all permutations of $(1,2,3,4,5)$ in which there exists at least one set of three consecutive decreasing terms. The complement is $|A \cup B|=|A|+|B|-|A \cap B|$ .
First, we calculate $|A|$ . Let $S_i$ be the set of permutations in which $(a_i, a_{i+1}, a_{i+2})$ is increasing for $i=1,2,3$ . We have \[|A|=|S_1 \cup S_2 \cup S_3|=|S_1|+|S_2|+|S_3|-|S_1 \cap S_2|-|S_2 \cap S_3|-|S_3 \cap S_1|+|S_1 \cap S_2 \cap S_3|.\]
Since there are $\binom{5}{3}$ ways to pick $(a_1, a_2, a_3)$ (there's only one way to arrange them in increasing order) and $2!$ ways to order $a_4, a_5$ , \[|S_1|=\binom{5}{3} \cdot 2!=20.\] By symmetry, we find $|S_2|=|S_3|=20$ .
Since we require $a_1<a_2<a_3<a_4$ and there are $\binom{5}{4}$ ways to pick the numbers (again, only one way to arrange them in increasing order), \[|S_1 \cap S_2|=\binom{5}{4} \cdot 1!=5.\] By symmetry, $|S_2 \cap S_3|=5$ .
Notice that $S_3 \cap S_1=S_1 \cap S_2 \cap S_3$ since both translate to $a_1<a_2<a_3<a_4<a_5$ , so we get \[|A|=20+20+20-5-5-|S_3 \cap S_1|+|S_1\cap S_3|=60-10=50.\] By symmetry, $|B|=50$ , and it remains to compute $|A\cap B|$ .
We have two cases, either $a_1<a_2<a_3>a_4>a_5$ or $a_1>a_2>a_3<a_4<a_5$ (it is easy to verify that these are the only ones that work). WLOG consider the first. We must have $a_3=5$ since it's the largest, and for every choice of $a_1, a_2$ , there is exactly one way to arrange them in order and to choose/arrange $a_3,a_4$ . So, there are $\binom{4}{2}$ ways to pick $a_1, a_2$ . Multiplying by 2 gives \[|A\cap B|=2\cdot 6=12 \implies |A \cup B|=50+50-12=88.\]
Since there are $5!=120$ permutations in total, the answer is $120-88=\boxed{\textbf{(D)}~32}$ .
~bomberdoodles

## Solution 9 (Quick)
Notice that the ways to arrange the numbers is $n$ , $n+2$ , $n+3$ , $n+2$ , and $n$ , for when it starts with $1$ , $2$ , $3$ , $4$ , and $5$ , respectively. Now that we have found a pattern, we can just solve for $n$ , so we can choose to find the ways if it starts with $1$ or $5$ . Solving, we get $n$ = 5. So, the answer is $5+7+8+7+5=\boxed{\textbf{(D)}~32}$ .
~hashbrown2009

## Solution 10 (Brute Force)
We write out the $5!=120$ cases, then filter out the valid ones:
$13254,14253,14352,15243,15342,21435,21534,23154,24153,24351,25143,25341,\linebreak 31425,31524,32415,32514,34152,34251,35142,35241,41325,41523,42315,42513,\linebreak 43512,45132,45231,51324,51423,52314,52413,53412.$
We count these out and get $\boxed{\textbf{(D)} ~32}$ permutations that work.
~contactbibliophile
Note: We are NOT going to write our $120$ cases and factor them out. I don't know why this is the first solution to pop up.
~Shreyansh
Note: Moved to number ten due to the sheer unnecessary nature of this solution :)
~ABIRGH

## Video Solution by OmegaLearn (Using PIE - Principle of Inclusion Exclusion)
https://youtu.be/Fqak5BArpdc
~ pi_is_3.14

## Video Solution by Power of Logic (Using Idea of Symmetrically Counting)
https://youtu.be/ZLQ8KYtai_M

## Video Solution by TheBeautyofMath
https://youtu.be/UZZoSYHBJlI
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .