# 2010 AIME I Problem 12

## Problem

Let $m \ge 3$ be an integer and let $S = \{3,4,5,\ldots,m\}$ . Find the smallest value of $m$ such that for every partition of $S$ into two subsets, at least one of the subsets contains integers $a$ , $b$ , and $c$ (not necessarily distinct) such that $ab = c$ .

Note : a partition of $S$ is a pair of sets $A$ , $B$ such that $A \cap B = \emptyset$ , $A \cup B = S$ .

## Solution 1
We claim that $243$ is the minimal value of $m$ . Let the two partitioned sets be $A$ and $B$ ; we will try to partition $3, 9, 27, 81,$ and $243$ such that the $ab=c$ condition is not satisfied. Without loss of generality , we place $3$ in $A$ . Then $9$ must be placed in $B$ , so $81$ must be placed in $A$ , and $27$ must be placed in $B$ . Then $243$ cannot be placed in any set, so we know $m$ is less than or equal to $243$ .
For $m \le 242$ , we can partition $S$ into $S \cap \{3, 4, 5, 6, 7, 8, 81, 82, 83, 84 ... 242\}$ and $S \cap \{9, 10, 11 ... 80\}$ , and in neither set are there values where $ab=c$ (since $8 < (3\text{ to }8)^2 < 81$ and $81^2>242$ and $(9\text{ to }80)^2 > 80$ ). Thus $m = \boxed{243}$ .
FYI, this. is a bad solution

## Solution 2
Consider $\{3,4,12\}$ . We could have any two of the three be together in the same set, and the third in the other set. Thus, we have $\{3,4\}, \{3,12\}, \{4,12\}$ . We will try to 'place' numbers in either set such that we never have $a\cdot b = c$ , until we reach a point where we MUST have $a\cdot b =c$ .
We begin with $\{3,12\}$ . Notice that $a,b,c$ do not have to be distinct, meaning we could have $3\cdot 3=9$ . Thus $9$ must be with $4$ . Notice that no matter in which set $36$ is placed, we will be forced to have $a\cdot b =c$ , since $3*12=36$ and $4*9=36$ .
We could have $\{4,12\}$ . Similarly, $16$ must be with $3$ , and no matter to which set $48$ is placed into, we will be forced to have $a \cdot b =c$ .
Now we have $\{3,4\}$ . $9$ must be with $12$ . Then $81$ must be with $\{3,4\}$ . Since $27$ can't be placed in the same set as $\{3,4,81\}$ , $27$ must go with $\{9,12\}$ . But then no matter where $243$ is placed we will have $a\cdot b =c$ .
Thus, $\boxed{243}$ is the minimum $m$ .
~skibbysiggy

## Video Solution
2010 AIME I #12
MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .