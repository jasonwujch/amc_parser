# 2018 AIME I Problem 9

## Problem

Find the number of four-element subsets of $\{1,2,3,4,\dots, 20\}$ with the property that two distinct elements of a subset have a sum of $16$ , and two distinct elements of a subset have a sum of $24$ . For example, $\{3,5,13,19\}$ and $\{6,10,20,18\}$ are two such subsets.

## Solution 1
This problem is tricky because it is the capital of a few "bashy" calculations. Nevertheless, the process is straightforward. Call the set $\{a, b, c, d\}$ .
Note that there are only two cases: 1 where $a + b = 16$ and $c + d = 24$ or 2 where $a + b = 16$ and $a + c = 24$ . Also note that there is no overlap between the two situations! This is because if they overlapped, adding the two equations of both cases and canceling out gives you $a=d$ , which cannot be true.
Case 1. This is probably the simplest: just make a list of possible combinations for $\{a, b\}$ and $\{c, d\}$ . We get $\{1, 15\}\dots\{7, 9\}$ for the first and $\{4, 20\}\dots\{11, 13\}$ for the second. That appears to give us $7*8=56$ solutions, right? NO. Because elements can't repeat, take out the supposed sets \[\{1, 15, 9, 15\}, \{2, 14, 10, 14\}, \{3, 13, 11, 13\}, \{4, 12, 4, 20\}, \{5, 11, 5, 19\},\] \[\{5, 11, 11, 13\}, \{6, 10, 6, 18\}, \{6, 10, 10, 14\}, \{7, 9, 9, 15\}, \{7, 9, 7, 17\}\] That's ten cases gone. So $46$ for Case 1.
Case 2. We can look for solutions by listing possible $a$ values and filling in the blanks. Start with $a=4$ , as that is the minimum. We find $\{4, 12, 20, ?\}$ , and likewise up to $a=15$ . But we can't have $a=8$ or $a=12$ because $a=b$ or $a=c$ , respectively! Now, it would seem like there are $10$ values for $a$ and $17$ unique values for each $?$ , giving a total of $170$ , but that is once again not true because there are some repeated values! There are two cases of overcounting:
case 1) (5,11,13,19) & (5.11.19.13)
The same is for (6,10,14,18) and (7,9,15,17)
case 2) those that have the same b and c values
this case includes:
(1,15,9,7) and (7,9,15,1)
(2,14,10,6) and (6,10,14,2)
(3,13,11,5) and (5,11,13,3)
So we need to subtract 6 overcounts. So, that's $164$ for Case 2.
Total gives $\boxed{210}$ .
-expiLnCalc

## Solution 2
Let's say our four elements in our subset are $a,b,c,d$ . We have two cases. Note that the order of the elements / the element letters themselves don't matter since they are all on equal grounds at the start.
$\textrm{Case } 1 \textrm{:}$ $a+b = 16$ and $c+d = 24$ .
List out possibilities for $a+b$ $(\text{i.e. } 1+15, 2+14, 3+13 \text{ etc.})$ but don't list $8+8$ because those are the same elements and that is restricted.
Then list out the possibilities for $c+d \text{ }(\text{i.e. } 4+20, 5+19, 6+18, \text{ etc.})$ but don't list $12+12$ because they are the same elements.
This will give you $7 \cdot 8$ elements, which is $56$ . However, as stated above, we have overlap. Just count starting from $a+b$ . $15,14,13,11,10,9,7,6,5,4$ all overlap once, which is $10$ , thus $56 - 10 = 46$ cases in this case. Note that $12$ wasn't included because again, if $c+d = 24$ , $c$ and $d$ cannot be $12$ .
$\textrm{Case } 2 \textrm{:}$ $a+b = 16$ and $b+c = 24$ .
Here, $b$ is included in both equations. We can easily see that $a, b, c$ will never equal each other.
Furthermore, there are 17 choices for $d$ ( $20 - 3$ included elements) for each $b$ . Listing out the possible $b$ s, we go from $15,14,13,11,10,9,7,6,5,4$ . Do not include $8$ or $12$ because if they are included, then $a/c$ will be the same as $b$ , which is restricted.
There are $10$ options there, and thus $10 \cdot 17 = 170$ . But, note that if $d = b+8$ , $a+d = a+b+8 = 24$ , and so we have a double-counted set. Starting with $b=15$ , we have $15, 14, 13, 11, 10, 9$ (where $d$ is $7, 6, 5, 3, 2, 1)$ . That means there are $6$ double-counted cases. Thus $170 - 6 = 164$ cases in this case.
Adding these up, we get $46+164 = \boxed{210}.$
~IronicNinja ~ $\LaTeX$ by AlcBoy1729 ~Formatted by ojaswupadhyay and phoenixfire

## Solution 3 (Official MAA)
There are two types of $\{a,b,c,d\} \subseteq \{1,2,3,4\dots,20\}$ that have the needed property. There is either an assignment of distinct values for $a,\,b,\,c,$ and $d$ such that $a+b=16$ and $c+d=24$ or an assignment such that $a+b=16$ and $a+c=24.$ These two types are mutually exclusive because $c+d=24$ and $a+c=24$ imply that $a=d.$ For the first type, there are $7$ choices for $\{a,b\},$ namely $\{1,15\},\,\{2,14\},\,\{3,13\},\,\{4,12\},\,\{5,11\},\,\{6,10\},$ and $\{7,9\},$ and there are $8$ choices for $\{c,d\},$ namely $\{4,20\},\,\{5,19\},\,\{6,18\},\,\{7,17\},\,\{8,16\},\,\{9,15\},\{10,14\},$ and $\{11,13\}.$ Thus a four-element subset of the first type can be formed by taking the union of one of $7$ two-element subsets with one of $8$ two-element subsets as long as these two subsets are disjoint. There are $10$ such pairings that are not disjoint out of the $7\cdot 8=56$ pairings, so there are $56-10=46$ subsets of the first type.
For subsets of the second type, there are $10$ choices for the value of $a$ $(4,\,5,\,6,\,7,\,9,\,10,\,11,\,13,\,14,\,15)$ such that $b=16-a$ and $c=24-a$ can be two other elements of the subset. Note that in each of these cases, $c-b=(24-a)-(16-a)=8.$ For each of these, there are $20-3=17$ other values that can be chosen for the element $d$ in the subset. But $10\cdot 17=170$ counts some subsets more than once. In particular, a subset is counted twice if $b+d=24$ or $c+d=16$ . In such cases either $d=a+8$ or $d=a-8$ . There are exactly $6$ subsets where the role of $a$ can be played by two different elements of the set. They are $\{1,7,9,15\},\,\{2,6,10,14\},\,\{3,5,11,13\},\,\{5,11,13,19\},\,\{6,10,14,18\},$ and $\{7,9,15,17\}$ . Thus there are $170-6=164$ subsets of the second type.
In all, there are $46+164=210$ subsets with the required property.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .