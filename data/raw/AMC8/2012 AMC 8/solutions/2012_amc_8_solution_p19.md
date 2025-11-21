# 2012 AMC 8 Problem 19

## Problem

In a jar of red, green, and blue marbles, all but 6 are red marbles, all but 8 are green, and all but 4 are blue. How many marbles are in the jar?

$\textbf{(A)}\hspace{.05in}6\qquad\textbf{(B)}\hspace{.05in}8\qquad\textbf{(C)}\hspace{.05in}9\qquad\textbf{(D)}\hspace{.05in}10\qquad\textbf{(E)}\hspace{.05in}12$

## Solution 1 (Trial and Error)
$6$ are blue and green - $b+g=6$
$8$ are red and blue - $r+b=8$
$4$ are red and green - $r+g=4$
We can do trial and error. Let's make blue $5$ . That makes green $1$ and red $3$ because $6-5=1$ and $8-5=3$ . To check this, let's plug $1$ and $3$ into $r+g=4$ , which works. Now count the number of marbles - $5+3+1=9$ . So the answer is $\boxed{\textbf{(C)}\ 9}.$

## Solution 2
We already knew the facts: $6$ are blue and green, meaning $b+g=6$ ; $8$ are red and blue, meaning $r+b=8$ ; $4$ are red and green, meaning $r+g=4$ . Then we need to add these three equations: $b+g+r+b+r+g=2(r+g+b)=6+8+4=18$ . It gives us all of the marbles are $r+g+b = 18/2 = 9$ . So the answer is $\boxed{\textbf{(C)}\ 9}$ . ~LarryFlora

## Solution 3 (Venn Diagrams)
We may draw three Venn diagrams to represent these three cases, respectively.
![](https://wiki-images.artofproblemsolving.com//c/c7/Screen_Shot_2021-08-29_at_9.14.51_AM.png)
Let the amount of all the marbles be $x$ , meaning $R+G+B = x$ .
The Venn diagrams give us the equation: $x = (x-6)+(x-8)+(x-4)$ . So $x = 3x-18$ , $x = 18/2 =9$ . Thus, the answer is $\boxed{\textbf{(C)}\ 9}$ . ~LarryFlora

## Solution 4 (Answer Choices)
Since we know all but $8$ marbles in the jar are green, the jar must have at least $9$ marbles. Then we can just start from $C$ and keep going. If there are $9$ marbles total, there are $3$ red marbles $(9-6)$ , $1$ green marble $(9-8)$ , and $5$ blue marbles $(9-4)$ . Since we assumed there were $9$ marbles and $3+1+5=9$ , the answer is $\boxed{\textbf{(C)}\ 9}$ .

## Solution 5 (Algebra)
Let $x$ be the number of total marbles. There are $x – 6$ red marbles, $x – 8$ green marbles, and $x – 4$ blue marbles. We can create an equation: $(x – 6)+(x – 8)+(x – 4)=x$ Solving, we get $x=9$ , which means the total number of marbles is $\boxed{\textbf{(C)}\ 9}$ . -J.L.L (Feel free to edit)

## Solution 6
Let $x$ be the number of total marbles, $r$ be the number of red marbles, $g$ be the number of green marbles, and $b$ be the number of blue marbles. Then we have $x - r = 6$ , $x - g = 8$ , $x - b = 4$ , and $r + g + b = x$ . Adding the first three equations together, we get $3x - r - g - b = 18$ or $3x - (r + g + b) = 18$ . Substituting in the fourth equation, we have $3x - x = 18$ $\implies$ $\boxed{\textbf{(C)}\ 9}$ .
~ cxsmi

## Video Solution
https://youtu.be/mMph7QH1kX0 Soo, DRMS, NM
https://youtu.be/-p5qv7DftrU ~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/TkZvMa30Juo?t=1316
~pi_is_3.14
### See Also