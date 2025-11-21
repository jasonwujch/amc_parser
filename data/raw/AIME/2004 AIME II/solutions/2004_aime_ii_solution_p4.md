# 2004 AIME II Problem 4

## Problem

How many positive integers less than 10,000 have at most two different digits ?

## Solution
First, let's count numbers with only a single digit. We have nine of these for each length, and four lengths, so 36 total numbers.
Now, let's count those with two distinct digits. We handle the cases "0 included" and "0 not included" separately.
There are ${9 \choose 2}$ ways to choose two digits, $A$ and $B$ . Given two digits, there are $2^n - 2$ ways to arrange them in an $n$ -digit number, for a total of $(2^1 - 2) + (2^2 - 2) + (2^3 -2) + (2^4 - 2) = 22$ such numbers (or we can list them: $AB, BA, AAB, ABA, BAA, ABB, BAB, BBA, AAAB, AABA, ABAA,$ $BAAA, AABB, ABAB, BAAB, ABBA, BABA, BBAA, ABBB, BABB, BBAB, BBBA$ ). Thus, we have ${9 \choose 2} \cdot 22 = 36\cdot22 = 792$ numbers of this form.
Now, suppose 0 is one of our digits. We have nine choices for the other digit. For each choice, we have $2^{n - 1} - 1$ $n$ -digit numbers we can form, for a total of $(2^0 - 1) + (2^1 - 1) + (2^2 - 1) + (2^3 - 1) = 11$ such numbers (or we can list them: $A0, A00, A0A, AA0, A000, AA00, A0A0, A00A, AAA0, AA0A, A0AA$ ). This gives us $9\cdot 11 = 99$ numbers of this form.
Thus, in total, we have $36 + 792 + 99 = \boxed{927}$ such numbers.

## Solution 2
We use casework on the number of digits for this problem.
If the number has a single digit, namely the number $n \in [1,9],$ we can clearly all such $n$ work.
If the number has two digits, or the number $n \in [10,99]$ we can clearly see all such $n$ work.
If the number $n$ has three digits, there are a total of $900$ three digit numbers, and there are $9 \cdot 9 \cdot 8$ numbers that have all distinct digits so there are $900 - 9 \cdot 9 \cdot 8$ total three digit numbers that work.
If the number $n$ has four digits, then we have a total of $9 +\binom{9}{2}\left(\binom{4}{1}+\binom{4}{2} +\binom{4}{3}\right) + 9 \cdot \left(\binom{3}{1}+\binom{3}{2} +\binom{3}{3}\right)$ so in total we get $\boxed{927}$ numbers that work.
Alternatively, $n$ has four digits can be calculated as follows: When $n$ has one unique digit, there are $9$ possibilities. When $n$ has two unique digits there are two cases. Case 1: two digits are the same with each other and different with the other pair of similar digits. In that case there are $\frac{\binom{4}{2}(9^2)}{2}$ numbers that work. The case had to be divided by $2$ because it counts the cases of distinct digits $(x,y)$ again when $(y,x)$ is picked. Case 2: three digits are the same and one is different. There are $4(9^2)$ numbers that work.

## Solution 3
We go with complementary counting. 3 different digits. First, we need atleast a three digit number. There are $9 \cdot 9 \cdot 8$ = 648 ways to do this with a three digit number. Note that I can simply add any one of the digits from $1-9$ to the left of any of these digits to get a 4 digit number, that has atleast 3 distinct digits (It can be either of some form like ABCA or ABCD). Thus there will be $9 \cdot 648 = 5832$ such numbers. But wait, we have missed all the cases where the third digit is $0$ . There are $9 \cdot 9 \cdot 8 = 648$ such ways (There are two $9's$ there because I can repeat atleast one digit). This count came to me while typing. Originally, I just did it regularly. Take the case of all 4 distinct, then the case of two repeating where one of them is the left-most digit. Now, we are missing the cases where two digits from the last three places repeat in a 4 digit number. All the cases where the first digit repeats with any of the last 3, and the cases where all 4 are distinct have been covered. For this, we split it into two cases. First case is such that the repeating digit is not $0$ . We have $\binom{3}{2} \cdot \binom{9}{1} \cdot 8 \cdot 8 = 1728$ such cases. Now, we will let $0$ be the repeating digits to get $\binom{3}{2} \cdot 9 \cdot 8 = 216$ cases. \[648 + 5832 + 648 + 1728 + 216 = 9072 \implies \boxed{9999 - 9072 =927}\] The question says $less$ than $10,000$ , so we subtract from $9999$ , not $10,000$ .
These problems are copyrighted © by the Mathematical Association of America.