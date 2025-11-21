# 2000 AMC 8 Problem 20

## Problem

You have nine coins: a collection of pennies, nickels, dimes, and quarters having a total value of $ $1.02$ , with at least one coin of each type. How many dimes must you have?

$\text{(A)}\ 1\qquad\text{(B)}\ 2\qquad\text{(C)}\ 3\qquad\text{(D)}\ 4\qquad\text{(E)}\ 5$

## Solution 1
Since you have one coin of each type, $1 + 5 + 10 + 25 = 41$ cents are already determined, leaving you with a total of $102 - 41 = 61$ cents remaining for $5$ coins.
You must have $1$ more penny. If you had more than $1$ penny, you must have at least $6$ pennies to leave a multiple of $5$ for the nickels, dimes, and quarters. But you only have $5$ more coins to assign.
Now you have $61 - 1 = 60$ cents remaining for $4$ coins, which may be nickels, quarters, or dimes. If you have only one more dime, that leaves $50$ cents in $3$ nickels or quarters, which is impossible. If you have two dimes, that leaves $40$ cents for $2$ nickels or quarters, which is again impossible. If you have three dimes, that leaves $30$ cents for $1$ nickel or quarter, which is still impossible. And all four remaining coins being dimes will not be enough.
Therefore, you must have no more dimes to assign, and the $60$ cents in $4$ coins must be divided between the quarters and nickels. We quickly see that $2$ nickels and $2$ quarters work. Thus, the total count is $2$ quarters, $2$ nickels, $1$ penny, plus one more coin of each type that we originally subtracted. Double-checking, that gives a total $2 + 2 + 1 + 4 = 9$ coins, and a total of $2\cdot 25 + 2\cdot 5 + 1 + (1 + 5 + 10 + 25) = 102$ cents.
There is only $1$ dime in that combo, so the answer is $\boxed{A}$ .

## Solution 2 (Faster)
We see that there must be 102 cents, so therefore there's at least 2 pennies. That leaves 7 coins. We assume that there are 3 quarters, leaving 25 cents with 4 coins left. If all 4 are nickels, that would only be 20 cents, missing 5. Therefore, one nickel must be changed into 1 dime, so the answer is $\boxed{A}$
Solution by ILoveMath31415926535

## Solution 3
It is clear that there should only be $2$ pennies; any more would take up too many coins, and the limit is $9$ . Now we have $ $1$ left, and $7$ coins to use. Looking at the quarters, we can make methodical guesses. If there is $1$ quarter, then we would have to make $ $0.75$ with $6$ coins. We take a few educated guesses for the nickel and dime combos, and see that $1$ quarter will not work. Trying values for $2$ quarters, we see that this will not work either. When we reach $3$ quarters, the remaining is $ $0.25$ made from $4$ coins. We try with $2$ dimes, which does not work (it only takes $3$ coins) and we try with $1$ dime. After trying $2$ pennies, $3$ quarters, $1$ dime, and $3$ nickels, it is evident that this combo works. Therefore, the answer is $\boxed{A}$
~mk

## Video Solution by OmegaLearn
https://youtu.be/HISL2-N5NVg?t=1409
~ pi_is_3.14

## Video Solution 2
https://youtu.be/Vm-proRV5wI . Soo, DRMS, NM
https://www.youtube.com/watch?v=un-zQJRS49k ~David
### See Also