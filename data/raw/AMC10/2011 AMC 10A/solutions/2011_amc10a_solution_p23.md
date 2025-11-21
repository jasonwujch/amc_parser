# 2011 AMC 10A Problem 23

## Problem

Seven students count from 1 to 1000 as follows:

Alice says all the numbers, except she skips the middle number in each consecutive group of three numbers. That is, Alice says 1, 3, 4, 6, 7, 9, . . ., 997, 999, 1000.

Barbara says all of the numbers that Alice doesn't say, except she also skips the middle number in each consecutive group of three numbers.

Candice says all of the numbers that neither Alice nor Barbara says, except she also skips the middle number in each consecutive group of three numbers.

Debbie, Eliza, and Fatima say all of the numbers that none of the students with the first names beginning before theirs in the alphabet say, except each also skips the middle number in each of her consecutive groups of three numbers.

Finally, George says the only number that no one else says.

What number does George say?

$\textbf{(A)}\ 37\qquad\textbf{(B)}\ 242\qquad\textbf{(C)}\ 365\qquad\textbf{(D)}\ 728\qquad\textbf{(E)}\ 998$

## Solution 1
First look at the numbers Alice says. $1, 3, 4, 6, 7, 9 \cdots$ skipping every number that is congruent to $2 \pmod 3$ . Thus, Barbara says those numbers EXCEPT every second - being $2 + 3^1 \equiv 5 \pmod{3^2=9}$ . So Barbara skips every number congruent to $5 \pmod 9$ . We continue and see:
Alice skips $2 \pmod 3$ , Barbara skips $5 \pmod 9$ , Candice skips $14 \pmod {27}$ , Debbie skips $41 \pmod {81}$ , Eliza skips $122 \pmod {243}$ , and Fatima skips $365 \pmod {729}$ .
Since the only number congruent to $365 \pmod {729}$ and less than $1,000$ is $365$ , the correct answer is $\boxed{365\ \mathbf{(C)}}$ .

## Solution 2
After Alice says all her numbers, the numbers not mentioned yet are \[\text{Alice: } 2,5,8,11,14,17,\cdots,998.\] After Barbara says all her numbers, the numbers that haven't been said yet are \[\text{Barbara: } 5,14,23,32,41,50,\cdots,995.\] After Candice, the list is \[\text{Candice: } 14,41,68,\cdots,986.\] Notice how each list is an arithmetic sequence where the common differene is thrice the common ratio of the previous list and the first term is the second term of the previous list. Now that the pattern is clear, we construct the rest of the lists: \[\text{Debbie: } 41,122,203,\cdots,959\] \[\text{Eliza: } 122,365,608,878\] \[\text{Fatima: } 365\]
Thus, George says $\boxed{\textbf{(C) } 365}$ .

## Solution 3
Notice that Alice has skipped the numbers $3n-1$ for $n=1,2,3,...,333$ . Namely, \[3\cdot1-1,3\cdot2-1,3\cdot3-1,...,3\cdot333-1\] Thus the numbers that Barbara skips are \[3\cdot2-1,3\cdot5-1,3\cdot8-1,...\] or in a more general expression, $3(3n-1)-1$ for $n=1,2,3,...$ . Namely, \[3\cdot(3\cdot1-1)-1,3\cdot(3\cdot2-1)-1,3\cdot(3\cdot3-1)-1,...\] Repeating the pattern until George, we have the first number he says, \[3(3(3(3(3(3\cdot1-1)-1)-1)-1)-1)-1= \boxed{\textbf{(C) } 365}\] In addition, note that the second number George says exceeds $1000$ .

## Solution 4 (Answer Choices)
Similar to Solution 1 we find that the only number that George can say must leave a remainder of $2$ when divided by $3$ , and that it must also leave a remainder of $5$ when divided by $9$ . Since we as human beings are usually lazy, and that MAA provides answer choices, we check all the possible numbers and find that our answer is $\boxed{\textbf{(C) } 365}$ .

## Solution 5
Every integer from 1 to 1000 can be written in the form $t_n+1$ in base 10, where $t_n$ is a trinary integer with no more than 7 significant digits. The important insight is that person $1\le{k}\le6$ will not say $n$ if and only if the $k$ th digit from the right of $t_n$ is 1. Therefore, the last 6 digits of $t_n$ must be 1, as the first 6 people never said the number. The only options for $t_n$ are thus $2111111$ , $1111111$ , and $0111111$ . But, since George only said one number, the first two must have been too big for it to be $\le1000$ . Our answer is therefore $111111_3+1=\frac{3^6-1}{3-1}+1=364+1=\boxed{\textbf{(C) } 365}$

## Solution 6 (similar to 1)
We see that Alice excludes the middle numbers in $1,2,3,4,5,6,7,8,9,\cdots.$ She excludes $2\mod3.$ Barbara excludes the middle numbers in $2,5,8,11,14,17,20,\cdots.$ She excludes $5\mod9.$ Let each mod be $a\mod b.$ We notice that, each time, $b$ triples, and $a=\dfrac{b+1}2.$ We can guess that $729$ is about the right size for $b$ ( $b$ must be an exponent of $3$ ); any larger, and $a$ wouldn't be less than $1000.$ (We could also count: abcdef is $6$ times, so $3^6$ ) Thus, $a=\dfrac{729+1}2=365$ ~Technodoggo

## Solution 7 (backwards solution 3)
We work backwards to find the placement of George's number in every person's set as a function of the place in the next person's set. Let George's number be the item number $x$ in his set (obviously $1$ ). Then Fatima places sets of three around every number in George's set and subtracts one to find the item number of George's number in her set (now $3\cdot 1-1=2$ ). This process repeats five more times for a total of six times.
We apply the function $f(x)=3x-1$ six times to attain the sequence of numbers $1,2,5,14,41,122,\boxed{\textbf{(C)}\;365}$ .
~eevee9406
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .