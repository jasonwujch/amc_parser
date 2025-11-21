# 2020 AIME I Problem 5

## Problem

Six cards numbered $1$ through $6$ are to be lined up in a row. Find the number of arrangements of these six cards where one of the cards can be removed leaving the remaining five cards in either ascending or descending order.

## Solution 1
Realize that any sequence that works (ascending) can be reversed for descending, so we can just take the amount of sequences that satisfy the ascending condition and multiply by two.
If we choose any of the numbers $1$ through $6$ , there are five other spots to put them, so we get $6 \cdot 5 = 30$ . However, we overcount some cases. Take the example of $132456$ . We overcount this case because we can remove the $3$ or the $2$ . Therefore, any cases with two adjacent numbers swapped is overcounted, so we subtract $5$ cases (namely, $213456, 132456, 124356, 123546, 123465$ ,) to get $30-5=25$ , but we have to add back one more for the original case, $123456$ . Therefore, there are $26$ cases. Multiplying by $2$ gives the desired answer, $\boxed{052}$ .
~molocyxu

## Solution 2 (Inspired by 2018 CMIMC Combo Round)
Similar to above, a $1-1$ correspondence between ascending and descending is established by subtracting each number from $7$ .
We note that the given condition is equivalent to "cycling" $123456$ for a contiguous subset of it. For example,
$12(345)6 \rightarrow 125346, 124536$
It's not hard to see that no overcount is possible, and that the cycle is either $1$ "right" or $1$ "left." Therefore, we consider how many elements we flip by. If we flip $1$ or $2$ such elements, then there is one way to cycle them. Otherwise, we have $2$ ways. Therefore, the total number of ascending is $1 + 5 + 2(4 + 3 + 2 + 1) = 26$ , and multiplying by two gives $\boxed{052}.$
~awang11

## Solution 3 (Table)
We create a table with each digit in a corresponding slot. A sample one is shown below.
The values highlighted in red are repeated values of an element that is highlighted green in the table. We count the values highlighted green. There are \( 26\) of these values.
Notice (like said in Solution 1) that there is symmetry between the ascending and descending placements of the cards. This means we must multiply \( 26\) by \( 2\), giving us \( 26 \times 2 =\) $\boxed{052}.$
~Pinotation
~Table by Pinotation

## Solution 4
Similarly to Solution 2, we find the number of ascending arrangements and multiply by 2.
We can choose $5$ cards to be the ascending cards, therefore leaving $6$ places to place the remaining card. There are $\binom{6}{5}\cdot 6=36$ to do this. However, since the problem is asking for the number of arrangements, we overcount cases such as $123456$ . Notice that the only arrangements that overcount are $123456$ (case 1) or if two adjacent numbers of $123456$ are switched (case 2).
$\text{Case 1: }$ This arrangement is counted $6$ times. Each time it is counted for any of the $5$ numbers selected. Therefore we need to subtract $5$ cases of overcounting.
$\text{Case 2: }$ Each time $2$ adjacent numbers of switched, there is one overcount. For example, if we have $213456$ , both $1$ or $2$ could be removed. Since there are $5$ possible switches, we need to subtract $5$ cases of overcounting.
Therefore, we have $36-5-5=26$ total arrangements of ascending numbers. We multiply by two (for descending) to get the answer of $\boxed{052}.$
~PCChess

## Solution 5 (No Overcounting)
Like in previous solutions, we will count the number of ascending arrangements and multiply by 2.
First, consider the arrangement 1-2-3-4-5-6. That gives us 1 arrangement which works.
Next, we can switch two adjacent cards. There are 5 ways to pick two adjacent cards, so this gives us 5 arrangements.
Now, we can "cycle" 3 adjacent cards. For example, 1-2-3 becomes 2-3-1 which becomes 3-1-2. There are 4 ways to pick a set of 3 adjacent cards, so this gives us 4x2=8 arrangements.
Cycling 4 adjacent cards, we get the new arrangements 2-3-4-1 (which works), 3-4-1-2 (which doesn't work), and 4-1-2-3 (which does work). We get 6 arrangements.
Similarly, when cycling 5 cards, we find 2x2=4 arrangements, and when cycling 6 cards, we find 2x1=2 arrangements.
Adding, we figure out that there are 1+5+8+6+4+2=26 ascending arrangements. Multiplying by 2, we get the answer $\boxed{052}.$
~i8Pie

## Solution 6 (Official MAA 1)
First count the number of permutations of the cards such that if one card is removed, the remaining cards will be in ascending order. There is $1$ such permutation where all the cards appear in order: $123456.$ There are $5$ such permutations where two adjacent cards are interchanged, as in $124356.$ The other such permutations arise from removing one card from $123456$ and placing it in a position at least two away from its starting location. There are $4$ such positions to place each of the cards numbered $1$ and $6,$ and $3$ such positions for each of the cards numbered $2, 3, 4,$ and $5.$ This accounts for $2\cdot4 + 4\cdot3 =20$ permutations. Thus there are $1 + 5 + 20 = 26$ permutations where one card can be removed so that the remaining cards are in ascending order. There is an equal number of permutations that result in the cards' being in descending order. This gives the total $26 + 26 = \boxed{52}$ .

## Solution 7 (Official MAA 2)
More generally, suppose there are $n \geq 4$ cards numbered $1, 2, 3, \dots, n$ arranged in ascending order. If any one of the $n$ cards is removed and placed in one of the $n$ positions in the arrangement, the resulting permutation will have the property that one card can be removed so that the remaining cards are in ascending order. This accounts for $n\cdot n = n^2$ permutations. However, the original ascending order has been counted $n$ times, and each order that arises by switching two neighboring cards has been counted twice. Hence the number of arrangements where one card can be removed resulting in the remaining cards' being in ascending order is $n^2-(n-1)-(n-1)=(n-1)^2+1.$ When $n = 6$ , this is $(6-1)^2+1 = 26$ , and the final answer is $2\cdot26 = \boxed{52}$ .

## Solution 8 (Casework)
For ascending, if the $1$ goes in anything but the first two slots, the rest of the numbers have to go in ascending from $2$ , which are $4$ cases if there are $6$ cards. If $1$ goes in the second spot, then you can put any of the rest in the first slot but then the rest are determined, so in the case of $6$ cards, that gives $5$ more. If $1$ goes in the first slot, that means that you are doing the same problem with $n-1$ cards. So the recursion is $a_n=(n-2)+(n-1)+a_{n-1}$ . There's $a_1=1$ and $a_2=2$ , so you get $a_3=2+3=5$ , $a_4=5+5=10$ , $a_5=7+10=17$ , and $a_6=9+17=26$ . Or you can see that $a_n=(n-1)^2+1$ . We double to account for descending and get $\boxed{052}$ .
~ahclark11

## Solution 9 (Symmetry and Case Study)
First, we know that ascending order and descending order are symmetrical to each other (namely, if we get 132456 where after we take out 3, it will be one scenario; and if we flip it and write 654231, it will be another scenario)
Thus, we only need to consider either descending or ascending and then times 2. WLOG let us consider ascending order
Case 1: after we take out 1, the rest will be in ascending order:
Notice that 1 can be tucked in any one of the 6 spaces, thus there are 6 scenarios.
Case 2: after we take out 2, the rest will be in ascending order:
Notice that if we put 2 next to 1 (to the right or to the left of 1), it will be an overcount, so there are only 4 cases for 2.
It is easy to see that this is the same for 3, 4, 5, and 6.
Thus, in total, we have \[(6+4\times5)\times2=\boxed{052}\] ~Adali

## Solution 10 (Illustration)
We start with five cards in ascending order, then insert the sixth card to obtain a valid arrangement.
Based on the card to be inserted, we have six cases. As shown below, the red squares indicate the possible positions to insert the sixth card. [asy] /* Made by MRENTHUSIASM */ unitsize(7mm); void drawSquare(real x, real y) { draw((x+0.5,y+0.5)--(x-0.5,y+0.5)--(x-0.5,y-0.5)--(x+0.5,y-0.5)--cycle,red); } label("$2$",(0.5,8)); label("$3$",(2.5,8)); label("$4$",(4.5,8)); label("$5$",(6.5,8)); label("$6$",(8.5,8)); label("Insert $1.$",(13.5,8),red); drawSquare(-0.5,8); drawSquare(1.5,8); drawSquare(3.5,8); drawSquare(5.5,8); drawSquare(7.5,8); drawSquare(9.5,8); label("$1$",(0.5,6.5)); label("$3$",(2.5,6.5)); label("$4$",(4.5,6.5)); label("$5$",(6.5,6.5)); label("$6$",(8.5,6.5)); label("Insert $2.$",(13.5,6.5),red); drawSquare(3.5,6.5); drawSquare(5.5,6.5); drawSquare(7.5,6.5); drawSquare(9.5,6.5); label("$1$",(0.5,5)); label("$2$",(2.5,5)); label("$4$",(4.5,5)); label("$5$",(6.5,5)); label("$6$",(8.5,5)); label("Insert $3.$",(13.5,5),red); drawSquare(-0.5,5); drawSquare(5.5,5); drawSquare(7.5,5); drawSquare(9.5,5); label("$1$",(0.5,3.5)); label("$2$",(2.5,3.5)); label("$3$",(4.5,3.5)); label("$5$",(6.5,3.5)); label("$6$",(8.5,3.5)); label("Insert $4.$",(13.5,3.5),red); drawSquare(-0.5,3.5); drawSquare(1.5,3.5); drawSquare(7.5,3.5); drawSquare(9.5,3.5); label("$1$",(0.5,2)); label("$2$",(2.5,2)); label("$3$",(4.5,2)); label("$4$",(6.5,2)); label("$6$",(8.5,2)); label("Insert $5.$",(13.5,2),red); drawSquare(-0.5,2); drawSquare(1.5,2); drawSquare(3.5,2); drawSquare(9.5,2); label("$1$",(0.5,0.5)); label("$2$",(2.5,0.5)); label("$3$",(4.5,0.5)); label("$4$",(6.5,0.5)); label("$5$",(8.5,0.5)); label("Insert $6.$",(13.5,0.5),red); drawSquare(-0.5,0.5); drawSquare(1.5,0.5); drawSquare(3.5,0.5); drawSquare(5.5,0.5); [/asy] Note that all arrangements of the six cards are distinct.
There are $26$ arrangements in which removing one card will leave the remaining five cards in ascending order. By symmetry, there are $26$ arrangements in which removing one card will leave the remaining five cards in descending order. So, the answer is $26\cdot2=\boxed{052}.$
~MRENTHUSIASM

## Solution 11
We first realize that as long as we have an ascending sequence of $5$ numbers, we can just plug in a $6$ th to make a sequence that works. For example, if we have $12345$ , we can plug in a $6$ in any of $6$ spaces, before $1$ , between $1$ and $2$ , and so on to after $5$ . We can also realize that this is completely symmetrical if the sequence is in descending order. For example, we could have $54321$ , and we could plug in a 6 in 6 of the spaces. For the total number of combinations, we have 6 ascending cases multiplied by the $6$ places that can hold whatever number is missing, and multiply by 2 because there is descending and ascending number cases.
But wait, what if we have $12345$ and plug in a $6$ at the end and $12346$ and plug in a $5$ at the $5$ th spot? We have overcounted, so we need to subtract off the identical pairs. Assume that one of them is the "right" combination. That means that there are $1$ "right" combination because all the rest will have $2$ of their combinations taken by the previous one. For example, if I have $12356$ and $12346$ , I would count those $123456$ as $12356$ 's instead of $12346$ 's. Therefore, we have $6+4+4+4+4+4 = 26$ combinations of ascending order, and since we need to count those of descending order as well, we have $26\cdot2=\boxed{052}.$
Side note: We could have just realized that the first part was unnecessary, but it does help you understand the problem better.
~Arcticturn

## Solution 12
Like the previous solutions, we calculate ascending possibilities then multiply by two. Then, the configuration can look like +++++ or +-+++ (the minus can go anywhere), where "+" indicates an increase, and "-" indicates a decrease. Obviously, for the first case, the only possibility is 123456. For the second case, we can start with 123456, and then take either a card after the "-" and put it before the "-", or we could take a card before the "-" and put it after the "-". This means that every card other than the one at the position of the "-" can be used in one way. There are five ways to have 4 plus's, and one minus, and for each way, there are 5 ways to rearrange 123456 to achieve that. So, our answer is $2(5\cdot5+1)=\boxed{052}$

## Solution 13 (Undercount+add cases)
First, we select $5$ of the $6$ cards to put in ascending or descending order. Then, we must add the other card to the group to arrange the six cards such that one can be removed so that the remaining cards are in ascending or descending order. Then, it would seem that the answer is $(6C5)*2$ (ascending or descending)* $6$ (the number of ways to place the last card). However, this overcounts some cases. For example, 123456 and 654321 can be made with 12345 and 6, 12346 and 5, etc. Furthermore, 654312 can be made with 65432 and 1 or 65431 and 2. Therefore, we first find that $(6C5)*2*4$ = $48$ . Then, we add the special cases ( $123456$ , $654321$ , $654312$ , $123465$ ) to obtain $\boxed{052}$ .
~mathMagicOPS

## Video Solution
https://www.youtube.com/watch?v=5iwdFd2OLKM&list=PLLCzevlMcsWN9y8YI4KNPZlhdsjPTlRrb&index=5 ~ MathEx

## Video Solution
https://www.youtube.com/watch?v=E6YJh7vsLPU

## Video Solution
https://youtu.be/ctVf7X6fTLI
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .