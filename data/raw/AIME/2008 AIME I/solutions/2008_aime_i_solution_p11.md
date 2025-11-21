# 2008 AIME I Problem 11

## Problem

Consider sequences that consist entirely of $A$ 's and $B$ 's and that have the property that every run of consecutive $A$ 's has even length, and every run of consecutive $B$ 's has odd length. Examples of such sequences are $AA$ , $B$ , and $AABAA$ , while $BBAB$ is not such a sequence. How many such sequences have length 14?

## Solution 1a
Let $a_n$ and $b_n$ denote, respectively, the number of sequences of length $n$ ending in $A$ and $B$ . If a sequence ends in an $A$ , then it must have been formed by appending two $A$ s to the end of a string of length $n-2$ . If a sequence ends in a $B,$ it must have either been formed by appending one $B$ to a string of length $n-1$ ending in an $A$ , or by appending two $B$ s to a string of length $n-2$ ending in a $B$ . Thus, we have the recursions \begin{align*} a_n &= a_{n-2} + b_{n-2}\\ b_n &= a_{n-1} + b_{n-2} \end{align*} By counting, we find that $a_1 = 0, b_1 = 1, a_2 = 1, b_2 = 0$ . \[\begin{array}{|r||r|r|||r||r|r|} \hline n & a_n & b_n & n & a_n & b_n\\ \hline 1&0&1& 8&6&10\\ 2&1&0& 9&11&11\\ 3&1&2& 10&16&21\\ 4&1&1& 11&22&27\\ 5&3&3& 12&37&43\\ 6&2&4& 13&49&64\\ 7&6&5& 14&80&92\\ \hline \end{array}\] Therefore, the number of such strings of length $14$ is $a_{14} + b_{14} = \boxed{172}$ .

## Solution 1b
Let $a_n$ and $b_n$ denote, respectively, the number of sequences of length $n$ ending in $A$ and $B$ .
Additionally, let $t_n$ denote the total number of sequences of length $n$ . Then, $t_n=a_n+b_n$ , as the total amount of sequences of length $n$ consists of the sequences of length $n$ ending in $A$ and the sequences of length $n$ ending in $B$ . \begin{align*} a_n &= a_{n-2} + b_{n-2}\\ b_n &= a_{n-1} + b_{n-2} \end{align*} The recursion for $a_n$ tells us that $a_n=a_{n-2}+b_{n-2}$ . However, this is also the definition for $t_{n-2}$ . Therefore, $a_n=t_{n-2}$ .
We also know from our recursion for $b_n$ that $b_n=a_{n-1}+b_{n-2}$ . Substituting for $a_n$ and $b_n$ into our recursion for $t_n$ gives us $t_n=t_{n-2}+a_{n-1}+b_{n-2}$ .
Furthermore, note that since $a_n=t_{n-2}$ , $a_{n-1}=t_{n-3}$ . Furthermore, using our definition for $t_{n-2}$ , we can rewrite $b_{n-2}$ as $t_{n-2}-a_{n-2}$ . Substituting for $a_{n-1}$ and $b_{n-2}$ into our recursion for $t_n$ gives us $t_n=t_{n-2}+t_{n-3}+t_{n-2}-a_{n-2}$ .
Finally, note that since $a_n=t_{n-2}$ , $a_{n-2}=t_{n-4}$ . Substituting for $a_{n-2}$ into our recursion for $t_n$ gives us $t_n=2t_{n-2}+t_{n-3}-t_{n-4}$ . We now have a recursion only in terms of $t$ .
By counting, we find that $t_1=1$ , $t_2=1$ , $t_3=3$ , and $t_4=2$ . \[\begin{array}{|r|r||r|r|} \hline n & t_n & n & t_n\\ \hline 1&1&8&16\\ 2&1&9&22\\ 3&3&10&37\\ 4&2&11&49\\ 5&6&12&80\\ 6&6&13&113\\ 7&11&14&172\\ \hline \end{array}\]
Therefore, the number of such sequences of length 14 is $\boxed{172}$ .

## Solution 1c
Define $A_{n}$ being sequences with the first letter being A, $B_{n}$ being sequences with the first letter being B.
$A_{14}$ = $B_{12}$ + $B_{10}$ + $B_{8}$ + $B_{6}$ + $B_{4}$ + $B_{2}$ (1) $B_{14}$ = $A_{13}$ + $A_{11}$ + $A_{9}$ + $A_{7}$ + $A_{5}$ + $A_{3}$ + $A_{1}$ (2)
We also know that
$A_{12}$ = $B_{10}$ + $B_{8}$ + $B_{6}$ + $B_{4}$ + $B_{2}$ $B_{12}$ = $A_{11}$ + $A_{9}$ + $A_{7}$ + $A_{5}$ + $A_{3}$ + $A_{1}$
We can Plug in $A_{12}$ and $B_{12}$ into (1) and (2) to get
$A_{14}$ = $B_{12}$ + $A_{12}$ $B_{14}$ = $A_{13}$ + $B_{12}$
We have the equation and the rest of the solutions are in Solution 1a.
Note: Only solution 1c is written by me. 1a and 1b are not written by me.
~toub3490

## Solution 2
We replace "14" with " $2n$ ". We first note that we must have an even number of chunks of $B$ 's, because of parity issues. We then note that every chunk of $B$ 's except the last one must end in the sequence $BAA$ , since we need at least two $A$ 's to separate it from the next chunk of $B$ 's. The last chunk of $B$ 's must, of course, end with a $B$ . Thus our sequence must look like this : \[\boxed{\quad A\text{'s} \quad} \boxed{\quad B\text{'s} \quad} BAA \boxed{\quad A\text{'s} \quad} \cdots \boxed{\quad B\text{'s} \quad}BAA \boxed{\quad A\text{'s} \quad} \boxed{\quad B\text{'s} \quad} B \boxed{\quad A\text{'s} \quad} ,\] where each box holds an even number of letters (possibly zero).
If we want a sequence with $2k$ chunks of $B$ 's, then we have $(2n - 6k + 2)$ letters with which to fill the boxes. Since each box must have an even number of letters, we may put the letters in the boxes in pairs. Then we have $(n - 3k + 1)$ pairs of letters to put into $4k + 1$ boxes. By a classic balls-and-bins argument, the number of ways to do this is \[\binom{n + k + 1}{4k} .\] It follows that the total number of desirable sequences is \[\sum_k \binom{n + k + 1}{4k} .\] For $n = 7$ , this evaluates as $\binom{8}{0} + \binom{9}{4} + \binom{10}{8} = 1 + 126 + 45 = \boxed{172}$ .

## Solution 3
There must be an even amount of runs of consecutive $B$ s due to parity. Thus, we can split this sequence into the following cases: $A$ , $BAAB$ , $AABAAB$ , $BAABAA$ , $AABAABAA$ , $BAABAABAAB$ , $AABAABAABAAB$ , $BAABAABAABAA$ , and $AABAABAABAABAA$ , in which the amount of letters in one run does not necessarily represent the amount of letters there can be.
For the first case and the last case, there is only one possible sequence of letters.
For all other cases, we can insert two of the same letter at a time into a run that has the exact same letter. For example, for the second case, we can insert two $A$ s and make the sequence $BAAAAB$ . There are three "slots" in which we can insert two additional letters in, and we must insert five groups of new letters. By stars and bars , the number of ways for the second case is $\binom{7}{2}=21$ .
Applying this logic to all of the other cases gives us $\binom{7}{3}$ , $\binom{7}{3}$ , $\binom{7}{4}$ , $\binom{8}{6}$ , $\binom{8}{1}$ , and $\binom{8}{1}$ . Adding 1+ $\binom{7}{2}$ + $\binom{7}{3}$ + $\binom{7}{3}$ + $\binom{7}{4}$ + $\binom{8}{6}$ + $\binom{8}{1}$ + $\binom{8}{1}$ gives us the answer $\boxed{172}$ .
These problems are copyrighted © by the Mathematical Association of America.