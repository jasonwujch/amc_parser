# 2024 AMC 10B Problem 25

## Problem

Each of $27$ bricks (right rectangular prisms) has dimensions $a \times b \times c$ , where $a$ , $b$ , and $c$ are pairwise relatively prime positive integers. These bricks are arranged to form a $3 \times 3 \times 3$ block, as shown on the left below. A $28$ th brick with the same dimensions is introduced, and these bricks are reconfigured into a $2 \times 2 \times 7$ block, shown on the right. The new block is $1$ unit taller, $1$ unit wider, and $1$ unit deeper than the old one. What is $a + b + c$ ?

$\textbf{(A) }88 \qquad \textbf{(B) }89 \qquad \textbf{(C) }90 \qquad \textbf{(D) }91 \qquad \textbf{(E) }92 \qquad$

## Solution 1 (Less than 60 seconds)
The $3$ x $3$ x $3$ block has side lengths of $3a, 3b, 3c$ . The $2$ x $2$ x $7$ block has side lengths of $2b, 2c, 7a$ .
We can create the following system of equations, knowing that the new block has $1$ unit taller, deeper, and wider than the original: \[3a+1 = 2b\] \[3b+1=2c\] \[3c+1=7a\]
Adding all the equations together, we get $b+c+3 = 4a$ . Adding $a-3$ to both sides, we get $a+b+c = 5a-3$ . The question states that $a,b,c$ are all relatively prime positive integers. Therefore, our answer must be congruent to $2 \pmod{5}$ . The only answer choice satisfying this is $\boxed{E(92)}$ . ~lprado

## Solution 2 (Solution 1 but longer)
We will define the equations the same as solution 1. \[3a+1 = 2b\] \[3b+1=2c\] \[3c+1=7a\] Solve equation 2 for c and substitute that value in for equation 3, giving us \[3a+1 = 2b\] \[\frac{3b+1}{2}=c\] \[\frac{3*(3b+1)}{2}+1=7a\]
Multiply 14 to the first equation and rearrange to get \[42a = 28b-14\] and multiply the third by 2 and rearrange to get \[27b+15 = 42a\] Solve for b to get $b = 29$ , substitute into equation 1 from the original to get $a = 19$ , and lastly, substitute a into original equation 2 to get $c = 44$ . Thus, $a+b+c = 19+29+44 = \boxed{E(92)}$ . ~Failure.net

## Solution 3
We will define the equations the same as solution 1 and 2. \[3a+1 = 2b\] \[3b+1=2c\] \[3c+1=7a\] Multiply 1st equation by 1.5 to get \[4.5a+1.5=3b\] Add 1 to get \[4.5a+2.5=3b+1\] Substitute to get \[4.5a+2.5=2c\] Multiply this one by 1.5 as well, getting \[6.75a+3.75=3c\] Adding 1 again to get \[6.75a+4.75=3c+1\] Replace \[3c+1\] with \[7a\] getting \[6.75a+4.75=7a\] Solve for \[a\] getting \[0.25a=4.75\] \[a=19\]
Solve for b: \[3(19)+1=2b\] \[57+1=2b\] \[b=29\]
Solve for c: \[3(29)+1=2c\] \[87+1=2c\] \[c=44\] Thus, $a+b+c = 19+29+44 = \boxed{E(92)}$
~newly2056

## Solution 4 (No Fractions)
As stated in solutions 1, 2, 3, the equations are as follows: (1) \[3a+1=2b\] (2) \[3b+1=2c\] (3) \[3c+1=7a\] Multiply equation (2) by 2 to get equation (4): (4) \[6b+2=4c\] and substitute (1) into (4): (5) \[9a+5=4c\] (3) \[7a-1=3c\] Multiplying (5) by 3 and (3) by 4 gives: \[3(9a+5)=4(7a-1)\] from which we get $a=19$ . Substituting $a$ into (1) and (3) yields $b=29$ and $c=44$ . Therefore, $a+b+c = \boxed{E(92)}$
~mathwizard123123

## Video Solution 1 by Pi Academy (In Less Than 5 Mins ⚡🚀)
https://www.youtube.com/watch?v=XI7jmtVchZ0
~ jj_empire10

## Video Solution 2 by SpreadTheMathLove
https://youtu.be/b-BBUKAVgeI?si=GAN4hho24927eJKX
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .