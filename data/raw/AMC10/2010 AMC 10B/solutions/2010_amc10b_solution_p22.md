# 2010 AMC 10B Problem 22

## Problem

Seven distinct pieces of candy are to be distributed among three bags. The red bag and the blue bag must each receive at least one piece of candy; the white bag may remain empty. How many arrangements are possible?

$\textbf{(A)}\ 1930 \qquad \textbf{(B)}\ 1931 \qquad \textbf{(C)}\ 1932 \qquad \textbf{(D)}\ 1933 \qquad \textbf{(E)}\ 1934$

## Solution 1
We can count the total number of ways to distribute the candies (ignoring the restrictions), and then subtract the overcount to get the answer.
Each candy has three choices; it can go in any of the three bags.
Since there are seven candies, that makes the total distribution $3^7=2187$
To find the overcount, we calculate the number of invalid distributions: the red or blue bag is empty.
The number of distributions such that the red bag is empty is equal to $2^7$ , since it's equivalent to distributing the $7$ candies into $2$ bags.
We know that the number of distributions with the blue bag is empty will be the same number because of the symmetry, so it's also $2^7$ .
The case where both the red and the blue bags are empty (all $7$ candies are in the white bag) are included in both of the above calculations, and this case has only $1$ distribution.
The total overcount is
The final answer will be $\text{total}-\text{overcount}=2187-(2^8-1) = 2187-256+1=1931+1=\boxed{\textbf{(C)}\ 1932}$
You can do the last step slightly faster by noticing $3^7 \equiv 7 \pmod{10}$ and $2^8 \equiv 6 \pmod{10}$ , so the end total will be $3^7 - 2^8 +1 \equiv 7 - 6 + 1 \equiv 2 \pmod{10}$ . The only answer given that satisfies this is $\boxed{\textbf{(C)}\ 1932}$ .

## Solution 2
We can use to our advantage the answer choices $\text{AMC}$ has given us, and eliminate the obvious wrong answer choices.
We can first figure out how many ways there are to take two candies from seven distinct candies to place them into the red/blue bags: $7\cdot 6=42$ .
Now we can look at the answer choices to find out which ones are divisible by $42$ , since the total number of combinations must be $42$ multiplied by some other number.
Since answers A, B, D, and E are not divisible by 3 (divisor of 42), the answer must be $\boxed{\textbf{(C)}\ 1932}$ .

## Solution 3
Let $r$ be the number of red bag candies. For ${1 \leq r \leq 6}$ .
So the number of candies left for the blue bag and the red bag is $7-r$ . Based on the problem, 1 candy must be fixed for the blue bag, which can be done $7-r$ ways. Now, before we continue, we need to realize that fixing a candy can lead to some over counting in cases where none in the white bag overlap. So we should try and find an alternative because we'll be over counting more than twice, and that will become extremely difficult to account for each case's over counting.
So, without fixing candies, we can put everything into options and work on the white bag, because once we figure out two bags, the remaining one is decided.
The options for the candies in the white bag are two: In the white bag or out of the white bag(by default, in the blue bag).
Now, for choosing the red bag, we have ${7 \choose r}$ .
Then, we have for the white bag: $2^{7-r}$ . Because we aren't fixing one for blue, the power is $7-r$ instead of $7-r-1$
We have: $({7 \choose r}) \cdot (2^{7-r})$ Adding them up for ${1 \leq r \leq 6}$ , we get 2058.
Now, for the invalid cases. Because we didn't fix candy for the blue bag, we need to subtract the cases where the blue bag remains empty. We can accomplish this pretty easily.
When $r = 6$ , how many ways can the remaining 1 candy $not$ be placed in the blue bag. This can be done ${7 \choose 1} = 7$ ways.
When $r = 5$ , how many ways can the remaining 2 candies $not$ be placed in the blue bag. This can be done ${7 \choose 2} = 21$ ways.
When $r = 4$ , how many ways can the remaining 3 candies $not$ be placed in the blue bag. This can be done ${7 \choose 3} = 35$ ways.
And because ${7 \choose 4} = {7 \choose 3}, {7 \choose 5} = {7 \choose 2}, and {7 \choose 6} = {7 \choose 1}$ , we just multiply by two.
Finally, we have: $2058 - 2 \cdot (7+21+35) = 2058 - 126 = \boxed{\textbf{(C)}\ 1932}$
~Raghu9372

## Video Solutions
https://youtu.be/ZfnxbpdFKjU?t=195
~IceMatrix
https://youtu.be/8WrdYLw9_ns?t=739
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .