# 2021 AIME II Problem 6

## Problem

For any finite set $S$ , let $|S|$ denote the number of elements in $S$ . Find the number of ordered pairs $(A,B)$ such that $A$ and $B$ are (not necessarily distinct) subsets of $\{1,2,3,4,5\}$ that satisfy \[|A| \cdot |B| = |A \cap B| \cdot |A \cup B|\]

## Solution 1
By PIE, $|A|+|B|-|A \cap B| = |A \cup B|$ . Substituting into the equation and factoring, we get that $(|A| - |A \cap B|)(|B| - |A \cap B|) = 0$ , so therefore $A \subseteq B$ or $B \subseteq A$ . WLOG $A\subseteq B$ , then for each element there are $3$ possibilities, either it is in both $A$ and $B$ , it is in $B$ but not $A$ , or it is in neither $A$ nor $B$ . This gives us $3^{5}$ possibilities, and we multiply by $2$ since it could have also been the other way around. Now we need to subtract the overlaps where $A=B$ , and this case has $2^{5}=32$ ways that could happen. It is $32$ because each number could be in the subset or it could not be in the subset. So the final answer is $2\cdot 3^5 - 2^5 = \boxed{454}$ .
~math31415926535

## Solution 2
We denote $\Omega = \left\{ 1 , 2 , 3 , 4 , 5 \right\}$ . We denote $X = A \cap B$ , $Y = A \backslash \left( A \cap B \right)$ , $Z = B \backslash \left( A \cap B \right)$ , $W = \Omega \backslash \left( A \cup B \right)$ .
Therefore, $X \cup Y \cup Z \cup W = \Omega$ and the intersection of any two out of sets $X$ , $Y$ , $Z$ , $W$ is an empty set. Therefore, $\left( X , Y , Z , W \right)$ is a partition of $\Omega$ .
Following from our definition of $X$ , $Y$ , $Z$ , we have $A \cup B = X \cup Y \cup Z$ .
Therefore, the equation
\[|A| \cdot |B| = |A \cap B| \cdot |A \cup B|\]
can be equivalently written as
\[\left( | X | + | Y | \right) \left( | X | + | Z | \right) = | X | \left( | X | + | Y | + | Z | \right) .\]
This equality can be simplified as
\[| Y | \cdot | Z | = 0 .\]
Therefore, we have the following three cases: (1) $|Y| = 0$ and $|Z| \neq 0$ , (2) $|Z| = 0$ and $|Y| \neq 0$ , (3) $|Y| = |Z| = 0$ . Next, we analyze each of these cases, separately.
Case 1: $|Y| = 0$ and $|Z| \neq 0$ .
In this case, to count the number of solutions, we do the complementary counting.
First, we count the number of solutions that satisfy $|Y| = 0$ .
Hence, each number in $\Omega$ falls into exactly one out of these three sets: $X$ , $Z$ , $W$ . Following from the rule of product, the number of solutions is $3^5$ .
Second, we count the number of solutions that satisfy $|Y| = 0$ and $|Z| = 0$ .
Hence, each number in $\Omega$ falls into exactly one out of these two sets: $X$ , $W$ . Following from the rule of product, the number of solutions is $2^5$ .
Therefore, following from the complementary counting, the number of solutions in this case is equal to the number of solutions that satisfy $|Y| = 0$ minus the number of solutions that satisfy $|Y| = 0$ and $|Z| = 0$ , i.e., $3^5 - 2^5$ .
Case 2: $|Z| = 0$ and $|Y| \neq 0$ .
This case is symmetric to Case 1. Therefore, the number of solutions in this case is the same as the number of solutions in Case 1, i.e., $3^5 - 2^5$ .
Case 3: $|Y| = 0$ and $|Z| = 0$ .
Recall that this is one part of our analysis in Case 1. Hence, the number solutions in this case is $2^5$ .
By putting all cases together, following from the rule of sum, the total number of solutions is equal to
\begin{align*} \left( 3^5 - 2^5 \right) + \left( 3^5 - 2^5 \right) + 2^5 & = 2 \cdot 3^5 - 2^5 \\ & = \boxed{454} . \end{align*}
~ Steven Chen (www.professorchenedu.com)

## Solution 3 (Principle of Inclusion-Exclusion)
By the Principle of Inclusion-Exclusion (abbreviated as PIE) , we have $|A \cup B|=|A|+|B|-|A \cap B|,$ from which we rewrite the given equation as \[|A| \cdot |B| = |A \cap B| \cdot \left(|A|+|B|-|A \cap B|\right).\] Rearranging and applying Simon's Favorite Factoring Trick give \begin{align*} |A| \cdot |B| &= |A \cap B|\cdot|A| + |A \cap B|\cdot|B| - |A \cap B|^2 \\ |A| \cdot |B| - |A \cap B|\cdot|A| - |A \cap B|\cdot|B| &= - |A \cap B|^2 \\ \left(|A| - |A \cap B|\right)\cdot\left(|B| - |A \cap B|\right) &=0, \end{align*} from which at least one of the following is true:
- $|A|=|A \cap B|$
- $|B|=|A \cap B|$
Let $|A \cap B|=k.$ For each value of $k\in\{0,1,2,3,4,5\},$ we will use PIE to count the ordered pairs $(A,B):$
Suppose $|A|=k.$ There are $\binom{5}{k}$ ways to choose the elements for $A.$ These $k$ elements must also appear in $B.$ Next, there are $2^{5-k}$ ways to add any number of the remaining $5-k$ elements to $B$ (Each element has $2$ options: in $B$ or not in $B.$ ). There are $\binom{5}{k}2^{5-k}$ ordered pairs for $|A|=k.$ Similarly, there are $\binom{5}{k}2^{5-k}$ ordered pairs for $|B|=k.$
To fix the overcount, we subtract the number of ordered pairs that are counted twice, in which $|A|=|B|=k.$ There are $\binom{5}{k}$ such ordered pairs.
Therefore, there are \[2\binom{5}{k}2^{5-k}-\binom{5}{k}\] ordered pairs for $|A \cap B|=k.$
Two solutions follow from here:

## Solution 3.1 (Binomial Theorem)
The answer is \begin{align*} \sum_{k=0}^{5}\left[2\binom{5}{k}2^{5-k}-\binom{5}{k}\right] &= 2\sum_{k=0}^{5}\binom{5}{k}2^{5-k}-\sum_{k=0}^{5}\binom{5}{k} \\ &=2(2+1)^5-(1+1)^5 \\ &=2(243)-32 \\ &=\boxed{454}. \end{align*} ~MRENTHUSIASM

## Solution 3.2 (Bash)
The answer is \begin{align*} &\hspace{5.125mm}\sum_{k=0}^{5}\left[2\binom{5}{k}2^{5-k}-\binom{5}{k}\right] \\ &=\left[2\binom{5}{0}2^{5-0}-\binom{5}{0}\right] + \left[2\binom{5}{1}2^{5-1}-\binom{5}{1}\right] + \left[2\binom{5}{2}2^{5-2}-\binom{5}{2}\right] + \left[2\binom{5}{3}2^{5-3}-\binom{5}{3}\right] + \left[2\binom{5}{4}2^{5-4}-\binom{5}{4}\right] + \left[2\binom{5}{5}2^{5-5}-\binom{5}{5}\right] \\ &=\left[2\left(1\right)2^5-1\right] + \left[2\left(5\right)2^4-5\right] + \left[2\left(10\right)2^3-10\right] + \left[2\left(10\right)2^2-10\right] + \left[2\left(5\right)2^1-5\right] + \left[2\left(1\right)2^0-1\right] \\ &=63+155+150+70+15+1 \\ &=\boxed{454}. \end{align*} ~MRENTHUSIASM

## Solution 4 (Simple Bash)
Proceed with Solution 1 to get $(|A| - |A \cap B|)(|B| - |A \cap B|) = 0$ . WLOG, assume $|A| = |A \cap B|$ . Thus, $A \subseteq B$ .
Since $A \subseteq B$ , if $|B| = n$ , there are $2^n$ possible sets $A$ , and there are also ${5 \choose n}$ ways of choosing such $B$ .
Therefore, the number of possible pairs of sets $(A, B)$ is
\[\sum_{k=0}^{5} 2^n {5 \choose n}\]
We can compute this manually since it's only from $k=0$ to $5$ , and computing gives us $243$ . We can double this result for $B \subseteq A$ , and we get $2(243) = 486$ .
However, we have double counted the cases where $A$ and $B$ are the same sets. There are $32$ possible such cases, so we subtract $32$ from $486$ to get $\boxed{454}$ .
~ adam_zheng

## Video Solution by Interstigation
https://youtu.be/jEghPVjyHoc
~Interstigation

## Video Solution & Set Theory Review
https://youtu.be/3vcLujj74RM
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .