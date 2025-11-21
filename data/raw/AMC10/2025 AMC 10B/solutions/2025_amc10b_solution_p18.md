# 2025 AMC 10B Problem 18

## Problem

What is the ones digit of the sum \[\lfloor \sqrt{1} \rfloor + \lfloor \sqrt{2} \rfloor + \lfloor \sqrt{3} \rfloor + \dots + \lfloor \sqrt{2025} \rfloor?\] (Recall that $\lfloor x \rfloor$ represents the greatest integer less than or equal to $x$ .)

$\textbf{(A) } 1\qquad\textbf{(B) } 2 \qquad\textbf{(C) }3\qquad\textbf{(D) } 5 \qquad\textbf{(E) } 8$

1 Solution 1

- 1 Solution 1

- 2 Solution 2

- 3 Solution 3: Units Digits!

- 4 Solution For Magic Square Association Problem

- 5 Solution 5: Induction, Units Digits: No hard algebra involved! (easiest)

- 6 Video Solution (Fast and Easy)

- 7 Video Solution 1 by SpreadTheMathLove

- 8 See also

## Solution 1
All terms from the 1st to the 3rd will equal 1, because the value inside the floor function will be greater than or equal to $\sqrt{1} = 1$ but less than $\sqrt{4} = 2$ . Following this logic, all terms from the 4th to the 8th will equal 2, all terms from the 9th to the 15th will equal 3, and all terms from number $n^2$ to $(n + 1)^2 - 1$ will equal $\sqrt{n}$ . Thus, there will be 3 terms equal to 1, 5 terms equal to 2, and so on. Writing out a few terms of the total sum, we have: \[1 \cdot 3 + 2 \cdot 5 + 3 \cdot 7 + \dots + 44 \cdot 89\] The expression above can be written in summation format as:
\[\sum_{n=1}^{44} n(2n + 1).\] We can expand this to the following: \[\sum_{n=1}^{44} 2n^2 + \sum_{n=1}^{44} n\] Using the sum of integers formulas, this becomes \[\frac{2 \cdot 44 \cdot 45 \cdot 89}{6} + \frac{44 \cdot 45}{2}\] The units digit of that expression evaluates to 0. However, we excluded $\lfloor \sqrt{2025} \rfloor = 45$ from our sum because it appears only once in the sequence, so we have to add it back into our expression. Our final answer is $\boxed{\textbf{(D)}\hspace{3pt}5}$ .
~Milkdrinker

## Solution 2
We quickly realize that from $1^2$ to $2^2 - 1$ , the floor of the square root is always $1$ , from $2^2$ to $3^2 - 1$ , the floor of the square root is always $3$ , and so on. So, we have $1\cdot3 + 2\cdot5 + 3\cdot7 + 4\cdot9 + ... 44\cdot89 + 45$ . Now, we can bash for the first digit of each of these products and find that $1\cdot3$ has unit digit $3$ $2\cdot5$ has unit digit $0$ $3\cdot7$ has unit digit $1$ $4\cdot9$ has unit digit $6$ $5\cdot11$ has unit digit $5$ $6\cdot13$ has unit digit $8$ $7\cdot15$ has unit digit $5$ $8\cdot17$ has unit digit $6$ $9\cdot19$ has unit digit $1$ $10 \cdot 21$ has unit digit $0$ And so, we see that a loop has been established for $1-10, 11-20, 21-30, 31-40$ (In normal sums that would be $1^2 - 10^2, 11^2 - 20^2$ , etc. Sum the first $10$ numbers to find that it is equal to $5$ (mod $10$ ), and multiply by $4$ to account for $1$ to $40$ . Now we have $0$ , and we must add the first $4$ numbers of the loop again to get $0$ , and add $45$ for the last number. Thus, we get $\boxed{(D)5}$ as the ones digit.
-henryli3333
Latex edits and minor edits by Wen_Liang

## Solution 3: Units Digits!
As stated in the first Solution, we can notice that the first to third terms will equal 1, the second to eighth terms will equal $2$ , and so on. This is because the square roots of $5$ , $6,$ and $7$ are in between $2$ and $3,$ so using floor function, they would equal $2$ .This concept applies to all the following numbers.
We can notice that the pattern goes like: $1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4,\dots44, 44, 44, 44, 45$ The square roots of perfect squares will not have to be rounded down through the floor function, so to make it easier, we can pull those numbers out. By doing this we get, $(1+2+3+4+5+6+7+\dots+44+45)$ , since $\sqrt{2025} = 45$ and $\sqrt{1} = 1$ .
Pulling out these numbers leaves us with 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, and so on. By looking at the remaining numbers, we can notice a pattern! There are two 1s, four 2s, six 3s, eight 4s...all the way until eighty-eight 44s! This can be simplified into, $2(1)+4(2)+6(3)+8(4)+10(5)+13(6)+\dots+88(44)$ . Notice that the problem is asking for the units digit, so we can do some simple multiplication to find another pattern.
We will expand our second expression: \begin{align*} 2\cdot1=2 \\ 4\cdot2=8 \\ 6\cdot3=8 \\ 8\cdot4=32 \\ 10\cdot5=50 \\ 12\cdot6=72 \\ 14\cdot7=98 \\ 16\cdot8=128 \\ 18\cdot9=162 \\ 20\cdot10=200 \\ \end{align*}
By looking only at the units digit: \begin{align*} 2\cdot1=2 \\ 4\cdot2=8 \\ 6\cdot3=8 \\ 8\cdot4=2 \\ 10\cdot5=0 \\ 12\cdot6=2 \\ 14\cdot7=8 \\ 16\cdot8=8 \\ 18\cdot9=2 \\ 20\cdot10=0 \\ \end{align*}
Huh..a pattern! It seems that this expression cycles in a pattern of $2,8,8,2,0$ . And notice again, if you add up the digits, $2+8+8+2+0=20$ . Notice that the unit's digit is $0$ .
However, we can't immediately assume that the cycle ends neatly, so we must do a quick check with the last four terms of the sequence: $82(41)+84(42)+86(43)+88(44)$ . The units digits end up being $2+8+8+2$ , so this time we're lucky and the cycle ends neatly. As a result, we know that because the cycle adds up to $20$ and doesn't stop mid-cycle, the units digit will be $0.$
Now, we can't just go ahead and give up because we got $0$ as our answer. We still have our first expression to deal with. $(1+2+3+4+5+\dots+44+45)$ By using the sum of numbers formula, we get: $(45(1+45))/2$ , which simplifies to: $45\cdot23 = 1035.$ Since our second expression will have a unit digit of $0$ , we get $0+5 = \boxed{\textbf{(D)}\hspace{3pt}5}$ , as our answer.
~PinkbIbtoy

## Solution For Magic Square Association Problem
We know that $\lfloor$ n $\rfloor$ is the lowest integer less or equal than $x$ . We also know that $\sqrt{4}=2$ , so that $\lfloor \sqrt{1} \rfloor$ , $\lfloor \sqrt{2} \rfloor$ , and $\lfloor \sqrt{3}\rfloor$ all are $1$ . $1-1+1=1$ , so the first $3$ terms equals one. Then, we look to the next $4$ terms. $\lfloor \sqrt{4} \rfloor$ , $\lfloor \sqrt{5} \rfloor$ , $\lfloor \sqrt{6} \rfloor$ , $\lfloor \sqrt{7} \rfloor$ , and $\lfloor \sqrt{8} \rfloor$ all equals 2, making a total of $2+2-2+2-2=-2$ Then all the values from $\lfloor \sqrt{9} \rfloor$ to $\lfloor \sqrt{15} \rfloor$ all equals 3, so now all the terms that equal $3$ or $-3$ have a grand total of $3-3+3-3+3-3+3=3$ . We quickly see a pattern. All the terms that equals $1$ or $-1$ have a total of $1$ , then $-2$ , then $3$ , and so on. $\sqrt{2025}=45$ , so then we can quickly figure out the value to be $1-2+3-4+5-6+7-\dots+45$ . $1-2=-1$ , $3-4=-1$ , and $5-6$ to be $-1$ , all the way to $43-44$ . We can see that $43$ is the $22$ nd odd number, so that we have $-22+45=\boxed{\textbf{}\hspace{3pt}23}$ .
~Coin1

## Solution 5: Induction, Units Digits: No hard algebra involved! (easiest)
Sure, somehow this is #18, but we can solve this problem with basically no algebra or any hard formulas. Also no confusing summation notation or modular arithmetic because we hate those!
Recall that the perfect squares differ by odd numbers. What does this mean?
Well, it means that from all $\lfloor \sqrt{1} \rfloor$ to $\lfloor \sqrt{3} \rfloor$ , it will equal 1, for 3 values because $3-1+1=3$
Likewise, from $\lfloor \sqrt{4} \rfloor$ to $\lfloor \sqrt{8} \rfloor$ , it will equal 2, for 5 values because $8-4+1=5$
Therefore, we can infer that there will be $2n+1$ copies of each number $n$ .
So, the entire sum will be \[1 \cdot 3 + 2 \cdot 5 + 3 \cdot 7 + \dots + 44 \cdot 89 + 45\]
We could $(mod 10)$ this, but that is too hard, so let's try to just look at the units digit for each term. For example, the first two terms units digit will be
$1*3=3$
$2*5=0$
From here, you could just bash out all of them because there are only 45 (which isn't too bad to do, especially considering this is #18 and a lot of people here have already finished the first 15 problems).
However, that is kinda dumb to do in competition, so let's try to use induction!
Once we get to the 11th, 12th, 13th, such terms it will actually be congruent to the first 10 terms, because we are only looking at the units digits.
So, we can just compute the first 10 terms from 1-10, because that will be much quicker:
$1*3=3$
$2*5=0$
$3*7=1$
$4*9=6$
$5*11=5$
$6*13=8$
$7*15=5$
$8*17=6$
$9*19=1$
$10*21=0$
Adding all these up, we have $3+0+1+6+5+8+5+6+1+0=35=5$
Then, the units digit of the first 40 will be equal to $5*4=20=0$
So, we just have to find the last 5 now
The first 4 is obviously $3+0+1+6=10=0$ , then adding the 45th term:
$1*45=5$
Finally, we add all these together:
$0+0+5=5$
And therefore our answer is $\boxed{\textbf{(D)}\hspace{3pt}5}$ .
~notvalid

## Video Solution (Fast and Easy)
https://www.youtube.com/watch?v=AOqAlhzazOM ~ Pi Academy

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .