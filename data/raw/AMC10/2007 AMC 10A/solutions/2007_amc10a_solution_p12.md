# 2007 AMC 10A Problem 12

## Problem

Two tour guides are leading six tourists. The guides decide to split up. Each tourist must choose one of the guides, but with the stipulation that each guide must take at least one tourist. How many different groupings of guides and tourists are possible?

$\text{(A)}\ 56 \qquad \text{(B)}\ 58 \qquad \text{(C)}\ 60 \qquad \text{(D)}\ 62 \qquad \text{(E)}\ 64$

## Video Solution by OmegaLearn
https://youtu.be/0W3VmFp55cM?t=3352
~ pi_is_3.14

## Solution
Each tourist has to pick in between the $2$ guides, so for $6$ tourists there are $2^6$ possible groupings. However, since each guide must take at least one tourist, we subtract the $2$ cases where a guide has no tourist. Thus the answer is $2^6 - 2 = \boxed{62}\ \mathrm{(D)}$ .

## Solution 2
Without loss of generality, let's call one of the tour guides tour guide A, and the other tour guide B. To count the number of total groupings of guides and tourists possible, we can count the number of ways some number of tourists go to tour guide A. Thus, we can see that the total number of groupings is: \[\binom{6}{1} + \binom{6}{2} + \binom{6}{3} + \binom{6}{4} + \binom{6}{5} = \boxed{62} \text{ (D)}\]

## Solution 3 (More detailed)
Very similar to the solution above, we begin by naming the tour guides / WLOG , tour guide $A$ and tour guide $B$ . The possible groupings of tourists and tour guides are: Tour guide $A$ takes 1, Tour guide $B$ takes 5, where there are $\binom{6}{1}$ = $6$ ways to arrange the tourists. Tour guide $A$ takes 2, Tour guide $B$ takes 4, where there are $\binom{6}{2}$ = $15$ ways to arrange the tourists. Tour guide $A$ takes 3, Tour guide $B$ takes 3, where there are $\binom{6}{3}$ = $20$ ways to arrange the tourists. Tour guide $A$ takes 4, Tour guide $B$ takes 2, where there are $\binom{6}{2}$ = $15$ ways to arrange the tourists. Tour guide $A$ takes 5, Tour guide $B$ takes 1, where there are $\binom{6}{1}$ = $6$ ways to arrange the tourists.
Thus, the total number of different groupings of guides and tourists is equal to $6 + 15 + 20 + 15 + 6$ , which equals $\boxed{\text{ (D)} 62}$
~Darth_Cadet
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .