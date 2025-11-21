# 2022 AIME II Problem 1

## Problem

Adults made up $\frac5{12}$ of the crowd of people at a concert. After a bus carrying $50$ more people arrived, adults made up $\frac{11}{25}$ of the people at the concert. Find the minimum number of adults who could have been at the concert after the bus arrived.

## Solution 1
Let $x$ be the number of people at the party before the bus arrives. We know that $x\equiv 0\pmod {12}$ , as $\frac{5}{12}$ of people at the party before the bus arrives are adults. Similarly, we know that $x + 50 \equiv 0 \pmod{25}$ , as $\frac{11}{25}$ of the people at the party are adults after the bus arrives. $x + 50 \equiv 0 \pmod{25}$ can be reduced to $x \equiv 0 \pmod{25}$ , and since we are looking for the minimum amount of people, $x$ is $300$ . That means there are $350$ people at the party after the bus arrives, and thus there are $350 \cdot \frac{11}{25} = \boxed{154}$ adults at the party.
~eamo

## Solution 2 (Kind of lame)
Since at the beginning, adults make up $\frac{5}{12}$ of the concert, the amount of people must be a multiple of 12.
Call the amount of people in the beginning $x$ .Then $x$ must be divisible by 12, in other words: $x$ must be a multiple of 12. Since after 50 more people arrived, adults make up $\frac{11}{25}$ of the concert, $x+50$ is a multiple of 25. This means $x+50$ must be a multiple of 5.
Notice that if a number is divisible by 5, it must end with a 0 or 5. Since 5 is impossible (obviously, since multiples of 12 end in 2, 4, 6, 8, 0,...), $x$ must end in 0.
Notice that the multiples of 12 that end in 0 are: 60, 120, 180, etc.. By trying out, you can clearly see that $x=300$ is the minimum number of people at the concert.
So therefore, after 50 more people arrive, there are $300+50=350$ people at the concert, and the number of adults is $350*\frac{11}{25}=154$ . Therefore the answer is $\boxed{154}$ .
I know this solution is kind of lame, but this is still pretty straightforward. This solution is very similar to the first one, though.
~hastapasta

## Solution 3
Let $a$ be the number of adults before the bus arrived and $x$ be the total number of people at the concert. So, $\frac{a}{x}=\frac{5}{12}$ . Solving for $x$ in terms of $a$ , $x = \frac{12}{5}a$ . After the bus arrives, let's say there are an additional $y$ adults out of the 50 more people who enter the concert. From that, we get $\frac{a+y}{x+50}=\frac{11}{25}$ . Replacing $x$ with the value of $a$ , the second equation becomes $\frac{a+y}{\frac{12}{5}a+50}=\frac{11}{25}$ .
By cross-multiplying and simplifying, we get that $25(y-22)=\frac{7a}{5}$ .
Observe that we must make sure $y-22$ is positive and divisible by $7$ to have an integer value of $a$ . The smallest possible value of $y$ that satisfies this conditions is $29$ . Plugging this into the equation, $a = 125$ . The question asks for the minimum number of adults that are there after the bus arrives, which is $a+y$ . Thus, the answer is simply $125+29=\boxed{154}$ .
~mathical8

## Video Solution (Mathematical Dexterity)
https://www.youtube.com/watch?v=gBIxZ6SUr_w

## Video Solution by Power of Logic
https://youtu.be/ZRnMlqgAJVM

## Video Solution by WhyMath
https://youtu.be/2TfPEFpopTs
~savannahsolver

## Video Solution by Dr. Xue's Math School – The Art of Choosing Variables (less than 2min)
https://youtu.be/q9t8gcH2uo4
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .