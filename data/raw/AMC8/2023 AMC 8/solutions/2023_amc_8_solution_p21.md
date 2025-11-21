# 2023 AMC 8 Problem 21

## Problem

Alina writes the numbers $1, 2, \dots , 9$ on separate cards, one number per card. She wishes to divide the cards into $3$ groups of $3$ cards so that the sum of the numbers in each group will be the same. In how many ways can this be done?

$\textbf{(A) } 0 \qquad \textbf{(B) } 1 \qquad \textbf{(C) } 2 \qquad \textbf{(D) } 3 \qquad \textbf{(E) } 4$

## Solution 1
First, we need to find the sum of each group when split. This is the total sum of all the elements divided by the # of groups. $1 + 2 \cdots + 9 = \frac{9(10)}{2} = 45$ . Then, dividing by $3$ , we have $\frac{45}{3} = 15$ , so each group of $3$ must have a sum of 15. To make the counting easier, we will just see the possible groups 9 can be with. The possible groups 9 can be with 2 distinct numbers are $(9, 2, 4)$ and $(9, 1, 5)$ . Going down both of these avenues, we will repeat the same process for $8$ using the remaining elements in the list. Where there is only 1 set of elements getting the sum of $7$ , $8$ needs in both cases. After $8$ is decided, the remaining 3 elements are forced in a group, yielding us an answer of $\boxed{\textbf{(C)}\ 2}$ as our sets are $(9, 1, 5) (8, 3, 4) (7, 2, 6)$ and $(9, 2, 4) (8, 1, 6) (7, 3 ,5)$ .
~CHECKMATE2021, apex304, SohumUttamchandani, wuwang2002, TaeKim, Cxrupptedpat

## Solution 2
The group with $5$ must have the two other numbers adding up to $10$ , since the sum of all the numbers is $(1 + 2 \cdots + 9) = \frac{9(10)}{2} = 45$ . The sum of the numbers in each group must therefore be $\frac{45}{3}=15$ . We can have $(1, 5, 9)$ , $(2, 5, 8)$ , $(3, 5, 7)$ , or $(4, 5, 6)$ . With the first group, we have $(2, 3, 4, 6, 7, 8)$ left over. The only way to form a group of $3$ numbers that add up to $15$ is with $(3, 4, 8)$ or $(2, 6, 7)$ . One of the possible arrangements is therefore $(1, 5, 9) (3, 4, 8) (2, 6, 7)$ . Then, with the second group, we have $(1, 3, 4, 6, 7, 9)$ left over. With these numbers, there is no way to form a group of $3$ numbers adding to $15$ . Similarly, with the third group there is $(1, 2, 4, 6, 8, 9)$ left over and we can make a group of $3$ numbers adding to $15$ with $(1, 6, 8)$ or $(2, 4, 9)$ . Another arrangement is $(3, 5, 7) (1, 6, 8) (2, 4, 9)$ . Finally, the last group has $(1, 2, 3, 7, 8, 9)$ left over. There is no way to make a group of $3$ numbers adding to $15$ with this, so the arrangements are $(1, 5, 9) (3, 4, 8) (2, 6, 7)$ and $(3, 5, 7) (1, 6, 8) (2, 4, 9)$ . So，there are $\boxed{\textbf{(C)}\ 2}$ sets that can be formed.
~Turtwig113

## Solution 3
The sum of the numbers across all equally valued sets is $(1 + 2 \cdots + 9) = \frac{9(10)}{2} = 45$ . The value of the numbers in each set would be $\frac{45}{3} = \textbf{15}$ . We know that the numbers $9$ , $8$ , and $7$ must belong in different sets, as putting any $2$ numbers in $1$ set will either pass or match the limit of $15$ per set, and we would then still need to add $1$ more number after that. Note that these numbers must be distinct, as Alina only has $1$ of each number, and order does not matter in the sets. Starting with the set that includes the number $9$ , the next two numbers must add up to $6$ , and there are $\textbf{2}$ ways of doing this $(2,4) (1,5)$ . Note we cannot use any number past $6$ , as those numbers must be used in the other sets. The next set, which includes the number $8$ , must have two numbers that add up to $7$ , and there are $\textbf{3}$ ways to do this $(2,5) (1,6) (3,4)$ . The final set, which includes the number $7$ , must have $2$ numbers that sum up to $8$ , and there are $\textbf{2}$ ways to do this $(2,6) (3,5)$ . Now we have found the number of ways in which each set sums up to $15$ . To find the number of ways in which all three sets sum up to $15$ concurrently, we must take the minimum of $2$ , $3$ , and $2$ , which gives us an answer of $\boxed{\textbf{(C)}\ 2}$ triplets of sets with 3 values, in which each set sum to the same amount.
~Fernat123

## Solution 4
Note that each group of numbers should sum to $\frac{1+2+3+4+5+6+7+8+9}{3} = 15.$ Thus, this is equivalent to asking, “How many ways can you fill in a three by three magic square with the integers $1$ through $9$ ?” since we can take the three rows of the magic square as our three groups. If you have closely studied magic squares, you might know that in a three by three magic square that is to be filled in with the integers $1$ through $9$ , the center of the square would be $5$ (the average of the numbers), and the numbers in the corners should be even(*). The such pairs (disregarding order) are $(2,8)$ and $(4,6).$ Let’s fix the position of $2$ to be the top left corner. This would make $8$ in the bottom right corner. We can have either $4$ or $6$ to be in the top right corner, for a total of $\boxed{\textbf{(C)}\ 2}$ such groups of three. (The groups are $(8,3,4) (1,5,7) (6,9,2)$ and $(8,1,6) (3,5,7) (4,9,2).$ ) Note that if we had instead fixed the position of $4$ , $6$ , or $8$ , they would correspond to one of the two cases, just in a different configuration.
(*)We can prove this using proof by contradiction. Label the nine small squares within the magic square from $a$ to $i$ from left to right, top to bottom. Firstly, we know that $a+i$ and $c+g$ sum to $10$ since the center square is $5$ . Thus, $a$ and $i$ must have the same parity, and so must $c$ and $g$ . Suppose that $a$ and $c$ have different parity. Since $a+b+c=15$ , $b$ must be even. By a similar argument, $h$ must also be even, and so must $d$ and $f$ . Our initial assumption is that one of $a$ and $c$ is odd and the other is even; however, we end up with six even numbers needed to fill in the square, but there are only four even integers from $1$ to $9$ . Now suppose that all of $a, c, g,$ and $i$ are odd. This would make each of $b, d, f,$ and $h$ odd, but clearly we do not have enough odd numbers to make all nine numbers odd. Thus, each corner square must be even.
~ Brian__Liu

## Solution 5(Trial and Error)
To start, we must find the value that all three groups must add to, which is $\frac{1+2+3+4+5+6+7+8+9}{3} = 15.$ . Then, we can notice that the numbers $1, 2,$ and $3$ must be in different groups because two of them and any other digit 1-9 added together cannot produce 15 (For example, $2+3=5$ which means that we need a $10$ to sum to 15. In the same way, $7, 8,$ and $9$ cannot be placed in the same group because putting them in the same group would make the numbers greater than 15 (For example, $7+8=15$ , meaning that it would be impossible to add another number with making the sum greater than 15. Now, we can just use trial and error to solve the problem (this is feasible because there are only $3*2=6$ ways to pair a number $1-3$ and $7-9$ and then add another number $4-6$ in order to sum to 15. By trial and error, we see that 1 and 7 must not be paired together because to have a sum of 15, there must be another 7 in the group (The problem only lets us use 1 of each number). This eliminates two of the options we are considering. Now, we only have to check the 4 options where 7 is not in a group with 1.
By trial and error, we can see that only two cases work:
1. $(1,8,6); (2,9,4); (3,7,5)$ and 2. $(1,9,5); (2,7,6); (3,8,4)$
Because we only have two options, the answer is $B$

## Solution 6(Potentially)
I don't know for sure, but this problem could be the same as picking 3 pairs of lines in a magic square. The only 3 sets that work are either all columns or all rows, as diagonals have only 2 pairs, and they overlap. Giving us 2, or $C$ (If their are any errors with this, please let me know)
~CubiksRube

## Video Solution by CoolMathProblems
https://youtu.be/_TMRSjRWPis?feature=shared

## Video Solution by Math-X
https://youtu.be/Ku_c1YHnLt0?si=S79t9BmOmSb-ACds&t=4641
~Math-X

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=2418 ~hsnacademy

## Video Solution
https://youtu.be/Ex54LNNPAwY
Please like and subscribe

## Video Solution (THINKING CREATIVELY!!!)
https://youtu.be/egXB9xayUF8
~Education, the Study of Everything

## Video Solution 1 (Using Casework)
https://youtu.be/l1MfKj5MkWg

## Animated Video Solution
https://youtu.be/_gpWj2lYers
~Star League ( https://starleague.us )

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=2853

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=2747

## Video Solution by WhyMath
https://youtu.be/l9zexK9hiBo
~savannahsolver

## Video Solution by harungurcan
https://www.youtube.com/watch?v=Ki4tPSGAapU&t=872s
~harungurcan

## Video Solution by MathyWorks
https://www.youtube.com/watch?v=hB7CDrVnNCs
~SlimeKnight

## Video Solution by Dr. David
https://youtu.be/rEgmKDZp9LE
### See Also