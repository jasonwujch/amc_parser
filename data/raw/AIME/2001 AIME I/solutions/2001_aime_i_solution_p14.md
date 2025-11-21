# 2001 AIME I Problem 14

## Problem

A mail carrier delivers mail to the nineteen houses on the east side of Elm Street. The carrier notices that no two adjacent houses ever get mail on the same day, but that there are never more than two houses in a row that get no mail on the same day. How many different patterns of mail delivery are possible?

## Solutions

## Solution 1
Let $0$ represent a house that does not receive mail and $1$ represent a house that does receive mail. This problem is now asking for the number of $19$ -digit strings of $0$ 's and $1$ 's such that there are no two consecutive $1$ 's and no three consecutive $0$ 's.
The last two digits of any $n$ -digit string can't be $11$ , so the only possibilities are $00$ , $01$ , and $10$ .
Let $a_n$ be the number of $n$ -digit strings ending in $00$ , $b_n$ be the number of $n$ -digit strings ending in $01$ , and $c_n$ be the number of $n$ -digit strings ending in $10$ .
If an $n$ -digit string ends in $00$ , then the previous digit must be a $1$ , and the last two digits of the $n-1$ digits substring will be $10$ . So \[a_{n} = c_{n-1}.\]
If an $n$ -digit string ends in $01$ , then the previous digit can be either a $0$ or a $1$ , and the last two digits of the $n-1$ digits substring can be either $00$ or $10$ . So \[b_{n} = a_{n-1} + c_{n-1}.\]
If an $n$ -digit string ends in $10$ , then the previous digit must be a $0$ , and the last two digits of the $n-1$ digits substring will be $01$ . So \[c_{n} = b_{n-1}.\]
Clearly, $a_2=b_2=c_2=1$ . Using the recursive equations and initial values: \[\begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|} \multicolumn{19}{c}{}\\\hline n&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16&17&18&19\\\hline a_n&1&1&1&2&2&3&4&5&7&9&12&16&21&28&37&49&65&86\\\hline b_n&1&2&2&3&4&5&7&9&12&16&21&28&37&49&65&86&114&151\\\hline c_n&1&1&2&2&3&4&5&7&9&12&16&21&28&37&49&65&86&114\\\hline \end{array}\]
As a result $a_{19}+b_{19}+c_{19}=\boxed{351}$ .

## Solution 2 ( Less recursion than solution 1)
Let $M_n$ represent the number of mail delivery patterns that end with the last house receiving mail. This is $b_n$ in Solution 1. Similarly define $A_n$ to be the number of mail delivery patterns that end with last house not receiving mail. This is just $a_n$ and $c_n$ in solution 1. Let $T_n$ be the total number of mail delivery patterns.
Here are the possible ending cases: the string ends in $1, 10,$ or $100$ . The first case is just $M_n$ . The second case is $M_{n-1}$ . The third case is $M_{n-2}$ . So we have $T_n = M_n + M_{n-1} + M_{n-2}$ . Since we want $T_{19}$ , it is just $M_{18} + M_{17} + M_{16}$ . Now using the same logic as above we can find $M_n = M_{n-2} + M_{n-3}$ ( the cases are 01 and 001). We can refer back to solution 1's table and only keep track of $b_n$ , ignoring both $a_n$ and $c_n$ .
- MathLegend27

## Solution 3 (Tedious Casework)
We split the problem into cases using the number of houses that get mail. Let "|" represent a house that gets mail, and "o" represent a house that doesn't. With a fixed number of |, an o can be inserted between 2 |'s or on the very left or right. There cannot be more than one o that is free to arrange to be placed between two |'s because no three o's can be adjacent, but there can be a maximum of two o's placed on the very left or right. Note that according to the Pigeonhole Principle , no more than 10 houses can get mail on the same day.
Case 1: 10 houses get mail. No 2 adjacent houses can get mail on the same day, so there must be an o between every two |. $10-1=9$ o's are fixed so we count the number of ways to insert $19 - 10 - 9 = 0$ o's to $10+1 = 11$ spots, or $\binom{11}{0} = 1$ .
Case 2: 9 houses get mail. In this case, $9-1 = 8$ o's are fixed so we count the number of ways to insert $19 - 9 - 8 = 2$ o's to $9+1=10$ spots. However, there is also the case where two o's are both on the very left / right. When both o's that are free to arrange are put on a side, there are $10-1=9$ spots left to insert $2-2=0$ o's. Hence the total number of ways in this case is $\binom{10}{2} + 2\binom{9}{0} = 47$ .
Case 3: 8 houses get mail. In this case, $8-1=7$ o's are fixed so we count the number of ways to insert $19-8-7=4$ o's to $8+1=9$ spots. When two o's are put to the very left / right, there are $9-1=8$ spots left to insert $4-2=2$ o's. We also need to take care of the case where two o's are on the very left and two o's are on the very right: we have $9-1-1=7$ spots to insert $4-2-2=0$ o's. Hence the total number of ways in this case is $\binom{9}{4} + 2\binom{8}{2} + \binom{7}{0} = 183$ .
Case 4: 7 houses get mail. In this case, $7-1=6$ o's are fixed so we count the number of ways to insert $19-7-6=6$ o's to $7+1=8$ spots. When two o's are put to the very left / right, there are $8-1=7$ spots left to insert $6-2=4$ o's. When two o's are on the very left and two o's are on the very right, we have $8-1-1=6$ spots to insert $6-2-2=2$ o's. Hence the total number of ways in this case is $\binom{8}{6} + 2\binom{7}{4} + \binom{6}{2} = 113$ .
Case 5: 6 houses get mail. We have to be careful in this case: $6-1=5$ o's are fixed so we are inserting $19-6-5=8$ o's to $6+1=7$ spots, which means that at least 1 of the 2 sides must have two o's. When 1 of the 2 sides have two o's, there are $7-1=6$ spots to insert $8-2=6$ o's. When both sides have two o's, there are $7-1-1=5$ spots to insert $8-2-2=4$ o's. Hence the total number of ways in this case is $2\binom{6}{6} + \binom{5}{4} = 7$ .
When less than 6 houses get(s) mail, it's again not possible since at least three o's must be together (again, according to the Pigeonhole Principle). Therefore, the desired answer is $1+47+183+113+7=\boxed{351}$ .
- MP8148

## Solution 4 (Clean Recursion without Bash)
There doesn't seem to be anything especially noticeable about the number nineteen in this problem, meaning that we can replace the number nineteen with any number without a big effect on the logic that we use to solve the problem. This pits the problem as a likely candidate for recursion.
At first, it's not immediately clear how to relate the state of $n$ houses in general to that of $n - 1, n - 2,$ or $n - 3.$ We thus break it up into cases, based on whether the first house gets mail or not.
Let $p_n$ be the number of ways to distribute the mail to $n$ houses. Assume that the first house gets mail. Therefore, since no two adjacent houses get mail on the same day, the second house must not get mail. Starting from the third house, however, things start to look messy, and it looks like we have to break our recurrence down into even smaller cases, which is something that we don't like -- we want to keep our relations as simple as possible. Therefore, seeing that we can't work forwards anymore, we try to work backwards.
Once the mail carrier delivers the mail to the first and (lack of mail) to the second houses, have him deliver mail to the remaining $n - 3$ houses at the end of the row, skipping the third house. There are $p_{n - 3}$ ways to do this. Now, we see that the availability of mail at the third house is fixed -- if the fourth house doesn't receive mail, the third one must, and if the fourth house receives mail, the third one can't. Therefore, there are simply $p_{n-3}$ ways to deliver the mail if the first house gets mail.
If the first house doesn't get mail, then we use the same logic -- have the mail carrier skip the second house and deliver the remaining mail to the $n - 2$ houses in $p_{n-2}$ ways. Then, the availability of mail for the second house is fixed, so there are $p_{n - 2}$ ways to deliver the mail in this case.
We thus have established a recurrence relation -- since the first house either gets mail or it doesn't, and cannot achieve both at the same time, we are confident about the validity of our relation: \[p_n = p_{n-2} + p_{n-3}.\] Now, we simply calculate $p_1, p_2,$ and $p_3.$ Then, it's off to the races for computation!
$p_1 = 2,$ because the first house can either gets mail or it doesn't -- there are no restrictions.
$p_2 = 3,$ because all of the possible deliveries are valid (of which there are $2 \cdot 2 = 4$ ) except the one where both houses receive mail.
$p_3 = 4,$ as there are $4$ possible ways (here, M represents that that house gets mail and N represents no mail): MNM, MNN, NNM, NMN.
Using our recurrence relation, we eventually get that $p_{19} = \boxed{351},$ and we're done.
Solution by Ilikeapos

## Solution 5
We use similar wording as in solution 1. In this problem, we divide into 3 cases:
Case 1: The first house gets mail. In other words, the sequence starts with a $1.$
We first introduce two variables. Let $x$ be the number of 01's, and let $y$ be the number of 001's in the sequence. For each case, we will divide further into three sub-cases, based on the pattern of mail delivery for the last three houses.
Sub-case 1: The last house that gets mail is the 17th house. Thus, we have the equation $2x+3y=16,$ which has solutions $(2,4),(5,2),$ and $(8,0).$ There are $\binom{2+4}{2}+\binom{5+2}{2}+\binom{8+0}{8}=37$ total sequences.
Sub-case 2: The last house that gets mail is the 18th house. We have $2x+3y=17,$ and finding all solutions yields 49 total sequences.
Sub-case 3: The last house that gets mail is the 19th house. We have $2x+3y=18,$ which gives us 65 total sequences.
There are 151 sequences for this case.
Case 2: The first house that gets mail is the 2nd house. The sequence begins with $01.$
Our sub-cases are still the same. However, our equations become $2x+3y=15,16,17.$ Computing yields $28+37+49=114$ sequences.
Case 3: The first house that gets mail is the 3rd house. The sequence starts with $001.$
We have the equations $2x+3y=14,15,16$ so we get $21+28+37=86$ sequences.
Totaling up gives us $151+114+86=351$ different sequences.
-math129

## Solution 6 (Different recursion with two rules)
Let $w_n$ be the number of possible ways if the last house has mail, and $b_n$ be the number of possible ways if the last house does not have mail.
If the last house has mail, then, the next house can't have mail, meaning that $b_n = w_{n - 1}$ .
If the last house doesn't have mail, then the next house can either have mail or not have mail. If the next house has mail, then we simply count the number of ways that the row ends in a house with mail, so that means so far, our recursive rule is $w_n = b_{n - 1} + \text{something}$ . If the next house does not have mail, then the next house after that must have mail, meaning that $w_n = b_{n - 1} + b_{n - 2}$ .
Recursing all the way up to $b_{19}$ and $w_{19}$ , we get $100 + 251 = \boxed{351}$

## Solution 7 (Simple Recursion)
Let $a_n$ be the number of ways if the first house has mail, and let $b_n$ be the number of ways if the first house does not get mail.
$a_n=a_{n-2}+a_{n-3}$ because if the first house gets mail, the next house that gets mail must either be the third or fourth house.
$b_n=a_{n-1}+a_{n-2}$ because if the first house does not get mail, the next house that gets mail must either be the second or third house.
Note that we only need list out values of $a_n$ as $b$ depends on $a$ . $a_1=1, a_2=1, a_3=2, a_4=2, \ldots$ .
$a_{19}+b_{19}=a_{17}+a_{16}+a_{18}+a_{17}=a_{16}+2\cdot a_{17}+a_{18}=65+2\cdot 86+114=\boxed{351}$ .

## Solution 8 (- Correspondence & Constructive Counting)
Like the previous solutions we use $1$ s and $0$ s to indicate whether a house get mails or not. Call a sequence of $1$ s and $0$ s valid if it has no two consecutive $1$ s or three consecutive $0$ s.
We claim there is a $1$ -to- $1$ correspondence between (A) a valid sequence of length $19$ ; and (B) a valid sequence of length $25$ that starts and ends with $1$ .
For each valid sequence in (B), we can remove the first three numbers as well as the last three numbers to get a valid sequence in (A).
On the other hand, for each valid sequence in (A), we can append three numbers to each end by the following rules to get a valid sequence in (B):
1) If the sequence starts/ends with $1$ , we append $100$ / $001$ to the start/end;
2) If the sequence starts/ends with $0$ , we append $101$ to the start/end.
Now, since all valid sequences in (B) start with either $1010$ or $1001$ , and end with either $0101$ or $1001$ , it's easy to see this is a $1$ - $1$ correspondence.
To compute the number of valid sequences in (B), we start with $n$ of $1$ s with $n-1$ of $0$ s in between, then distribute the rest $25-(2n-1)=26-2n$ of $0$ s to the $n-1$ slots. The total number of valid sequences is then
\[\sum_n \binom{n-1}{26-2n} = \binom{12}{0} + \binom{11}{2} + \binom{10}{4} + \binom{9}{6} + \binom{8}{8} = 1 + 55 + 210 + 84 + 1 = 351.\]
~asops

## Solution 9
When we see this problem, we immediately think of recursion. Let $a_k$ be the point such that the rightmost house of k houses receives mail. Then $a_1=1$ , $a_2=1$ , $a_3=2$ . Now, we find the recurrence relation \[a_n=a_{n-3}+a_{n-2}\] because we can either have 1 space in between the mailed rightmost house of $a_n$ , or two spaces, as in our previous a’s we already have the a_n mailed rightmost. Solving, we get $a_{17}=86, a_{18}=114, a_{19}=151$ . Now, we realize that the number of ways for the 19 houses to get mail is the sum of $a_{17},a_{18},a_{19}$ because we can either have 2 empty no mail houses, 1 house, or the rightmost house is lit. Summing, we get $\boxed{351}$ .
~MathCosine
These problems are copyrighted © by the Mathematical Association of America.