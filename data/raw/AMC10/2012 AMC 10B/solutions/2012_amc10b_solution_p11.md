# 2012 AMC 10B Problem 11

## Problem

A dessert chef prepares the dessert for every day of a week starting with Sunday. The dessert each day is either cake, pie, ice cream, or pudding. The same dessert may not be served two days in a row. There must be cake on Friday because of a birthday. How many different dessert menus for the week are possible?

$\textbf{(A)}\ 729\qquad\textbf{(B)}\ 972\qquad\textbf{(C)}\ 1024\qquad\textbf{(D)}\ 2187\qquad\textbf{(E)}\ 2304$

## Solution
Desserts must be chosen for $7$ days: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday.
There are $3$ choices for dessert on Saturday: pie, ice cream, or pudding, as there must be cake on Friday and the same dessert may not be served two days in a row. Likewise, there are $3$ choices for dessert on Thursday. Once dessert for Thursday is selected, there are $3$ choices for dessert on Wednesday, once Wednesday's dessert is selected there are $3$ choices for dessert on Tuesday, etc. Thus, there are $3$ choices for dessert for each of $6$ days, so the total number of possible dessert menus is $3^6$ , or $\boxed{\textbf{(A)}\ 729}$ .

## Solution 2
There are $4 \cdot 3^6$ ways for the desserts to be chosen. By symmetry, any of the desserts that are chosen on Friday share $\frac{1}{4}$ of the total arrangements. Therefore our answer is $\frac{4\cdot3^6}{4} = 3^6 = \boxed{729}.$
- Sliced_Bread
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .