# 2012 AMC 8 Problem 9

## Problem

The Fort Worth Zoo has a number of two-legged birds and a number of four-legged mammals. On one visit to the zoo, Margie counted 200 heads and 522 legs. How many of the animals that Margie counted were two-legged birds?

$\textbf{(A)}\hspace{.05in}61\qquad\textbf{(B)}\hspace{.05in}122\qquad\textbf{(C)}\hspace{.05in}139\qquad\textbf{(D)}\hspace{.05in}150\qquad\textbf{(E)}\hspace{.05in}161$

## Solution 1: Algebra
Let the number of two-legged birds be $x$ and the number of four-legged mammals be $y$ . We can now use systems of equations to solve this problem.
Write two equations:
$2x + 4y = 522$
$x + y = 200$
Now multiply the latter equation by $2$ .
$2x + 4y = 522$
$2x + 2y = 400$
By subtracting the second equation from the first equation, we find that $2y = 122 \implies y = 61$ . Since there were $200$ heads, meaning that there were $200$ animals, there were $200 - 61 = \boxed{\textbf{(C)}\ 139}$ two-legged birds.

## Solution 2: Cheating the System
First, we "assume" there are 200 two-legged birds only, and 0 four-legged mammals. Of course, this poses a problem, as then there would only be $200\cdot2=400$ legs.
Now we have to do some swapping--for every two-legged bird we swap for a four-legged mammal, we gain 2 legs. For example, if we swapped one bird for one mammal, giving 199 birds and 1 mammal, there would be $400 + 1(2) = 402$ legs. If we swapped two birds for two mammals, there would be $400 + 2(2) = 404$ legs. If we swapped 50 birds for 50 mammals, there would be $400 + 50(2) = 500$ legs.

## Solution 3: Add two legs for each bird
Let's add 2 legs for each bird and assume each bird has four-legged as each mammal. So the total legs of these birds and mammals would be $4*200=800$ . Actually, there were only $522$ legs. The difference between these two numbers exactly gives us the number of all the legs we added for all birds: $800 - 522 = 278$ . Because each bird was added by 2 legs, so the total number of birds would be $278/2 = \boxed{\textbf{(C)}\ 139}$ two-legged birds. ---LarryFlora

## Video Solution
https://youtu.be/CsmpiJC-FBA ~David
https://youtu.be/fQzxnsnp40c ~savannahsolver
### See Also