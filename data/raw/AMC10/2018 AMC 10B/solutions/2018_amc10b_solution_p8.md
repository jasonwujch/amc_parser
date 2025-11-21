# 2018 AMC 10B Problem 8

## Problem

Sara makes a staircase out of toothpicks as shown:

[asy] size(150); defaultpen(linewidth(0.8)); path h = ellipse((0.5,0),0.45,0.015), v = ellipse((0,0.5),0.015,0.45); for(int i=0;i<=2;i=i+1) { for(int j=0;j<=3-i;j=j+1) { filldraw(shift((i,j))*h,black); filldraw(shift((j,i))*v,black); } } [/asy]

This is a 3-step staircase and uses 18 toothpicks. How many steps would be in a staircase that used 180 toothpicks?

$\textbf{(A)}\ 10\qquad\textbf{(B)}\ 11\qquad\textbf{(C)}\ 12\qquad\textbf{(D)}\ 24\qquad\textbf{(E)}\ 30$

## Solutions

## Solution 1
Notice that the sequence of numbers of toothpicks from the 1st step to the 3rd step is $4, 10, 18$
We find that the first difference between 4 and 10 is 6 and 10 and 18 is 8.
So, the second difference is constant, 2 (the difference between 6 and 8)
Because the second differences are constant, the sequence comes from a quadratic polynomial in the form $ax^2+bx+c$
Creating a system of equations, we find that (by plugging in values to $ax^2+bx+c$ ):
$a + b + c = 4$ $4a + 2b + c = 10$ $9a + 3b + c = 18$
So, (a,b,c) is (1,3,0) and we get the quadratic $x^2 + 3x$
Set $x^2 + 3x = 180$ and factor
$(x-12)(x+15)$
So x = 12, and from this we see that the solution is $\boxed {(C) 12}$

## Solution 2
A staircase with $n$ steps contains $4 + 6 + 8 + ... + 2n + 2$ toothpicks. This can be rewritten as $(n+1)(n+2) -2$ .
So, $(n+1)(n+2) - 2 = 180$
So, $(n+1)(n+2) = 182.$
Inspection could tell us that $13 \cdot 14 = 182$ , so the answer is $13 - 1 = \boxed {(C) 12}$

## Solution 3
Layer $1$ : $4$ steps
Layer $1,2$ : $10$ steps
Layer $1,2,3$ : $18$ steps
Layer $1,2,3,4$ : $28$ steps
From inspection, we can see that with each increase in layer the difference in toothpicks between the current layer and the previous increases by $2$ . Using this pattern:
$4, 10, 18, 28, 40, 54, 70, 88, 108, 130, 154, 180$
From this we see that the solution is $\boxed {(C) 12}$
By: Soccer_JAMS

## Solution 4 (10th Grade Math)
Notice that we have the points \( (1,4) \), \( (2,10) \), \( (3,18) \). Then, we calculate the first difference to get 6 and 8 respectively, and calculate the second difference to get 2. This is a quadratic expression in the form \( ax^2 + bx + c \).
Because we have a table of elements, \( 2a = \) the second difference, so \( 2a = 2 \Rightarrow a = 1 \). The quadratic is now \( y = x^2 + bx + c \). We plug in two points to get \( 4 = b + c \) and \( 10 = 4 + 2b + c \Rightarrow 6 = 2b + c \). Solving through elimination gives us \( b = 2 \), and \( c = 2 \).
We now have \( y = x^2 + 2x + 2 \). We put \( y = 180 \), and see that \( 180 = x^2 + 2x + 2 \), and \( 0 = x^2 + 2x - 178 \). We use the quadratic formula to get \( -2 \pm \sqrt{716}/2 \). \( \sqrt{716} \) is greater than \( 26^2 \) but less that \( 27^2 \), so we say \( \sqrt{716} = 26 \). We then get 12 or -14.
We cannot have a negative number of steps, so our answer is $\boxed {(C) 12}$ .
~Pinotation

## Solution 5
We can find a function that gives us the number of toothpicks for every layer. Using finite difference, we know that the degree must be $2$ and the leading coefficient is $1$ . The function is $f(n)=n^2+3n$ where $n$ is the layer and $f(n)$ is the number of toothpicks.
We have to solve for $n$ when $n^2+3n=180\Rightarrow n^2+3n-180=0$ . Factor to get $(n-12)(n+15)$ . The roots are $12$ and $-15$ . Clearly $-15$ is impossible so the answer is $\boxed {(C) 12}$ .
~Zeric Hang

## Solution 6
Notice that the number of toothpicks can be found by adding all the horizontal and all the vertical toothpicks. We can see that for the case of 3 steps, there are $2(3+3+2+1)=18$ toothpicks. Thus, the equation is $2S + 2(1+2+3...+S)=180$ with $S$ being the number of steps. Solving, we get $S = 12$ , or $\boxed {(C) 12}$ . -liu4505

## Solution 6 General Formula
There are $\frac{n(n+1)}{2}$ squares. Each has $4$ toothpick sides. To remove overlap, note that there are $4n$ perimeter toothpicks. $\frac{\frac{n(n+1)}{2}\cdot 4-4n}{2}$ is the number of overlapped toothpicks Add $4n$ to get the perimeter (non-overlapping). Formula is $\text{number of toothpicks} = n^2+3n$ Then you can "guess" or factor (also guessing) to get the answer $\boxed{\text{(C) }12}$ . ~bjc

## Not a solution! Just an observation.
If you are trying to look for a pattern, you can see that the first column is made of 4 toothpicks. The second one is made from 2 squares: 3 toothpicks for the first square and 4 for the second. The third one is made up of 3 squares: 3 toothpicks for the first and second one, and 4 for the third one. The pattern continues like that. So for the first one, you have 0 "3 toothpick squares" and 1 "4 toothpick squares". The second is 1 to 1. The third is 2:1. And the amount of three toothpick squares increase by one every column.
The list is as follow for the number of toothpicks used... $4$ , $4+3$ , $4+6$ , $4+9$ , and so on. 4, 7, 10, 13, 16, 19, ...
- Flutterfly

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/8j0RvjRsjCc
~Education, the Study of Everything

## Video Solution
https://youtu.be/FbUEFq85jGE
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .