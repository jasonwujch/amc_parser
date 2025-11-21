# 2013 AIME I Problem 6

## Problem

Melinda has three empty boxes and $12$ textbooks, three of which are mathematics textbooks. One box will hold any three of her textbooks, one will hold any four of her textbooks, and one will hold any five of her textbooks. If Melinda packs her textbooks into these boxes in random order, the probability that all three mathematics textbooks end up in the same box can be written as $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
The total ways the textbooks can be arranged in the 3 boxes is $12\textbf{C}3\cdot 9\textbf{C}4$ , which is equivalent to $\frac{12\cdot 11\cdot 10\cdot 9\cdot 8\cdot 7\cdot 6}{144}=12\cdot11\cdot10\cdot7\cdot3$ . If all of the math textbooks are put into the box that can hold $3$ textbooks, there are $9!/(4!\cdot 5!)=9\textbf{C}4$ ways for the other textbooks to be arranged. If all of the math textbooks are put into the box that can hold $4$ textbooks, there are $9$ ways to choose the other book in that box, times $8\textbf{C}3$ ways for the other books to be arranged. If all of the math textbooks are put into the box with the capability of holding $5$ textbooks, there are $9\textbf{C}2$ ways to choose the other 2 textbooks in that box, times $7\textbf{C}3$ ways to arrange the other 7 textbooks. $9\textbf{C}4=9\cdot7\cdot2=126$ , $9\cdot 8\textbf{C}3=9\cdot8\cdot7=504$ , and $9\textbf{C}2\cdot 7\textbf{C}3=9\cdot7\cdot5\cdot4=1260$ , so the total number of ways the math textbooks can all be placed into the same box is $126+504+1260=1890$ . So, the probability of this occurring is $\frac{(9\cdot7)(2+8+(4\cdot5))}{12\cdot11\cdot10\cdot7\cdot3}=\frac{1890}{27720}$ . If the numerator and denominator are both divided by $9\cdot7$ , we have $\frac{(2+8+(4\cdot5))}{4\cdot11\cdot10}=\frac{30}{440}$ . Simplifying the numerator yields $\frac{30}{10\cdot4\cdot11}$ , and dividing both numerator and denominator by $10$ results in $\frac{3}{44}$ . This fraction cannot be simplified any further, so $m=3$ and $n=44$ . Therefore, $m+n=3+44=\boxed{047}$ .

## Solution 2
Consider the books as either math or not-math where books in each category are indistiguishable from one another. Then, there are $\,_{12}C_{3}$ total distinguishable ways to pack the books. Now, in order to determine the desired propability, we must find the total number of ways the condition that all math books are in the same box can be satisfied. We proceed with casework for each box:
Case 1: The math books are placed into the smallest box. This can be done in $\binom{3}{3}$ ways.
Case 2: The math books are placed into the middle box. This can be done in $\binom{4}{3}$ ways.
Case 3: The math books are placed into the largest box. This can be done in $\binom{5}{3}$ ways.
So, the total ways the condition can be satisfied is $\binom{3}{3} + \binom{4}{3} + \binom{5}{3}$ . This can be simplified to $\binom{6}{4} = \binom{6}{2}$ by the Hockey Stick Identity . Therefore, the desired probability is $\dfrac{\dbinom{6}{2} }{\dbinom{12}{3}}$ = $\dfrac{3}{44}$ , and $m+n=3+44=\boxed{047}$ .

## Solution 3 (Permutation)
There are three cases as follows. Note these are PERMUTATIONS, as the books are distinct!
1. Math books in the 3-size box. Probability is $\frac{3\cdot2\cdot1}{12\cdot11\cdot10}$ , because we choose one of the $3$ places for math book 1, then one of the $2$ for math book 2, and the last one. Total number of orders: $12\cdot11\cdot10=1320$ .
2. In the 4-size: same logic gets you $\frac{1}{55}$ , since we have $4$ places for math book 1, and so on.
3. In the 5-size: you get $\frac{1}{22}$ , for a sum of $\frac{3}{44}$ so your answer is $\boxed{047}$ .

## Solution 4
Assume that the $9$ other books are all distinct. The number of ways to place the other $9$ books and the $3$ is $\frac {12!}{3!}$ . The number of ways to put all the $3$ math books into the box that holds $3$ books is $9!$ . The number of ways to put all the $3$ math books into the box that holds $4$ books is $\binom {4}{3} \cdot 9!$ , and the number of ways to put all the $3$ math books into the box that holds $5$ books is $\binom {5}{3} \cdot 9!$ . The number of desired outcomes is $15 \cdot 9!$ , and the total number of outcomes is $\frac {12!}{6}$ . Simplifying, we get the answer is $\frac {3}{44}$ , so our answer is $\boxed {047}$ .
~Arcticturn

## Video Solution
https://www.youtube.com/watch?v=9way8JrtD04&t=555s ~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .