# 2005 AIME I Problem 5

## Problem

Robert has 4 indistinguishable gold coins and 4 indistinguishable silver coins. Each coin has an engraving of one face on one side, but not on the other. He wants to stack the eight coins on a table into a single stack so that no two adjacent coins are face to face. Find the number of possible distinguishable arrangements of the 8 coins.

## Solution 1
There are two separate parts to this problem: one is the color (gold vs silver), and the other is the orientation.
There are ${8\choose4} = 70$ ways to position the gold coins in the stack of 8 coins, which determines the positions of the silver coins.
Create a string of letters H and T to denote the orientation of the top of the coin. To avoid making two faces touch, we cannot have the arrangement HT. Thus, all possible configurations must be a string of tails followed by a string of heads, since after the first H no more tails can appear. The first H can occur in a maximum of eight times different positions, and then there is also the possibility that it doesn’t occur at all, for $9$ total configurations. Thus, the answer is $70 \cdot 9 = \boxed{630}$ .

## Solution 2
We can imagine the $8$ coins as a string of $0\text{'s}$ and $1\text{'s}$ . Because no $2$ adjacent coins can have $2$ faces touching, subsequent to changing from $0$ to $1$ , the numbers following $1$ must be $1\text{'s}$ ; therefore, the number of possible permutations if all the coins are indistinguishable is $9$ (there are $8$ possible places to change from $0$ to $1$ and there is the possibility that there no change occurs). There are $\binom 8 4$ possibilities of what coins are gold and what coins are silver, so the solution is $\boxed{9\cdot \binom 8 4=630}$ .

## Solution 3
First, we can break this problem up into two parts: the amount of ways to order the coins based on color, and which side is facing up for each coin (assuming they are indistinguishable). In the end, we multiply these values together.
First, there are obviously $\binom{8}{4}$ ways to order the coins based on color.
Next, we set up a recurrence. Let $a_n$ be the number of ways $n$ indistinguishable coins to be stacked such that no heads are facing each other.
Consider the top coin. If it is facing up, then there are $a_{n-1}$ ways for the rest of the coins below it to be arranged. If it is facing down however, there will only be one way to arrange the coins. We can the recurrence: \[a_n=a_{n-1}+1.\] Note $a_1=2$ , so $a_8 = 9$ .
Finally, to get the result, we do $70\times 9$ to get $\boxed{630}$ .
~superagh
### Intuition
Really try not to overthink especially in combinatorics. In this case, we just have to notice that after we place a coin facing up ANYWHERE, the rest of the coins to the right of the row of coins MUST be facing up. (Or else we have a coin facing up followed by a coin facing down, and that is not cool). So for example, suppose we started with a coin facing up. Then the next coin must also be facing up. Then so must the next coin. And so on. Now we know what happens if it starts with a coin facing up. Hmmmmmmm. What if it starts with a coin facing down?
Well, start with a coin facing down. Now, does the next coin HAVE to have a coin facing down, or can it have a coin facing up? It could have both! But wait! What happens if the next coin is heads? Well we saw already that now the next coin must be heads, or else we have a up coin followed by a down coin, which once again, sucks. So now everything to the right of the up coin must be facing up.
So we can have the following configurations: $9U, 1D+8U, 2D+7U, 3D+6U, ..., 9D+0U$ . These are the total number of configurations, which is $9$ . (As a sidenote, we really count the number of solutions to $a+b=8$ , which is $8+1=9$ ). So we must now put the 4 gold coins as a part of this sequence of ups and downs. This can be done in $8\choose 4$ ways, and the rest of the silver coins can be put in $8-4$ choose $4$ ways. (We subtract the $4$ from the $8$ for the silver coin placement, because we already used up $4$ coins, namely the gold ones). So we have the answer as $9 \binom {8}{4}=630$ .
~th1nq3r
These problems are copyrighted © by the Mathematical Association of America.