# 2018 AMC 8 Problem 19

## Problem

In a sign pyramid a cell gets a "+" if the two cells below it have the same sign, and it gets a "-" if the two cells below it have different signs. The diagram below illustrates a sign pyramid with four levels. How many possible ways are there to fill the four cells in the bottom row to produce a "+" at the top of the pyramid?

[asy] unitsize(2cm); path box = (-0.5,-0.2)--(-0.5,0.2)--(0.5,0.2)--(0.5,-0.2)--cycle; draw(box); label("$+$",(0,0)); draw(shift(1,0)*box); label("$-$",(1,0)); draw(shift(2,0)*box); label("$+$",(2,0)); draw(shift(3,0)*box); label("$-$",(3,0)); draw(shift(0.5,0.4)*box); label("$-$",(0.5,0.4)); draw(shift(1.5,0.4)*box); label("$-$",(1.5,0.4)); draw(shift(2.5,0.4)*box); label("$-$",(2.5,0.4)); draw(shift(1,0.8)*box); label("$+$",(1,0.8)); draw(shift(2,0.8)*box); label("$+$",(2,0.8)); draw(shift(1.5,1.2)*box); label("$+$",(1.5,1.2)); [/asy]

$\textbf{(A) } 2 \qquad \textbf{(B) } 4 \qquad \textbf{(C) } 8 \qquad \textbf{(D) } 12 \qquad \textbf{(E) } 16$

## Solution 1
You could just make out all of the patterns that make the top positive. In this case, you would have the following patterns:
+−−+, −++−, −−−−, ++++, −+−+, +−+−, ++−−, −−++. There are 8 patterns and so the answer is $\boxed{\textbf{(C) } 8}$ .
-NinjaBoi2000

## Solution 2
The top box is fixed by the problem.
Choose the left 3 bottom-row boxes freely. There are $2^3=8$ ways.
Then the left 2 boxes on the row above are determined.
Then the left 1 box on the row above that is determined
Then the right 1 box on that row is determined.
Then the right 1 box on the row below is determined.
Then the right 1 box on the bottom row is determined, completing the diagram.
So the answer is $\boxed{\textbf{(C) } 8}$ .
~BraveCobra22aops

## Solution 3
Let the plus sign represent 1 and the negative sign represent -1.
The four numbers on the bottom are $a$ , $b$ , $c$ , and $d$ , which are either 1 or -1.
[asy] unitsize(2cm); path box = (-0.5,-0.2)--(-0.5,0.2)--(0.5,0.2)--(0.5,-0.2)--cycle; draw(box); label("$a$",(0,0)); draw(shift(1,0)*box); label("$b$",(1,0)); draw(shift(2,0)*box); label("$c$",(2,0)); draw(shift(3,0)*box); label("$d$",(3,0)); draw(shift(0.5,0.4)*box); label("$ab$",(0.5,0.4)); draw(shift(1.5,0.4)*box); label("$bc$",(1.5,0.4)); draw(shift(2.5,0.4)*box); label("$cd$",(2.5,0.4)); draw(shift(1,0.8)*box); label("$ab^2c$",(1,0.8)); draw(shift(2,0.8)*box); label("$bc^2d$",(2,0.8)); draw(shift(1.5,1.2)*box); label("$ab^3c^3d$",(1.5,1.2)); [/asy]
Which means $ab^3c^3d$ = 1. Since $b$ and $c$ are either 1 or -1, $b^3 = b$ and $c^3 = c$ . This shows that $abcd$ = 1.
Therefore either $a$ , $b$ , $c$ , and $d$ are all positive or negative, or 2 are positive and 2 are negative.
There are 2 ways where $a$ , $b$ , $c$ , and $d$ are 1 (1, 1, 1, 1) and (-1, -1, -1, -1)
There are 6 ways where 2 variables are positive and 2 are negative: (1, 1, -1, -1), (1, -1, 1, -1), (-1, 1, 1, -1), (-1, -1, 1, 1), (-1, 1, -1, 1), and (-1, -1, 1, 1).
So the answer is $\boxed{\textbf{(C) } 8}$ .
Note: This result can also be achieved by realizing that there are $4! / 2! 2! = 6$ ways to arrange $2$ negatives and $2$ positives and $1$ way each to arrange four of one sign.
~atharvd
~cxsmi (Note)

## Solution 4
The pyramid is built on the basic 3 blocks pattern: one above and two below. The basic pattern have four possible symbols and half of them have a $+$ on the above, half of them have a $-$ above. So, For the lowest layer with $4$ blocks, there are $2^4=16$ possible combination and half of them will lead a $+$ (or $-$ ) on the top. The answer is $16/2=\boxed{\textbf{(C) } 8}$ .
If you notice this rule, you can give the answer whatever how many layers you have. The answer will be $2^{n-1}$ for the layer with $n$ blocks.

## Solution 5
We can use casework to solve this problem. The only way for the top cell to have a $+$ in it is if the third row of the pyramid (the one with $2$ cells) is either $--$ or $++$ . First, let's pretend that the third row of the pyramid is $++$ . The only way for that to happen is if the second row (the one with $3$ cells) is --- or $+++$ . Now, let's pretend that the second is $+++$ . That would have $2$ possibilities for the first row (the one with $4$ cells), $++++$ and $----$ . Next, let's pretend that the second row is ---. That makes two more possibilities for the first row, $-+-+$ and $+-+-$ . Now, let's pretend that the 3rd row is $--$ , which means that the second row is either $-+-$ or $+-+$ . You will soon find that $-+-$ find $2$ possibilities for the first row, $-++-$ or $-++-$ , and $2$ possibilities for $+-+$ , $--++$ and $++--$ . Together, we find that the answer is $2+2+2+2=\boxed{\textbf{(C) } 8}$ .

## Solution 6 (Non-rigorous)
There are two choices for the uppermost: $+$ or $-$ . There are 16 cases in total ( $2^4$ ). Half of 16 is 8. The answer is $\boxed{\textbf{(C) } 8}$ .
(Note: this is not recommended for solving, just an idea after solving.)
~nolypoly11

## Solution 7 (Using probability)
If you pick the signs for two boxes at random, there is equal probability that the one above them will be either a $+$ or a $-$ . There are 16( $2^4$ ) cases possible for the bottom four, so half of that, $\boxed{\textbf{(C) } 8}$ , is the answer.

## Video Solution
https://youtu.be/29RtYSU89vA
~Education, the Study of Everything

## Video Solution
https://youtu.be/j8wm3gfOYvU
~savannahsolver

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=TpsuRedYOiM&t=250s
### See Also