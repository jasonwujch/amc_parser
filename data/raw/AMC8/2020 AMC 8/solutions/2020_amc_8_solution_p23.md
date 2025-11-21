# 2020 AMC 8 Problem 23

## Problem

Five different awards are to be given to three students. Each student will receive at least one award. In how many different ways can the awards be distributed?

$\textbf{(A) }120 \qquad \textbf{(B) }150 \qquad \textbf{(C) }180 \qquad \textbf{(D) }210 \qquad \textbf{(E) }240$

## Solution 1 (Constructive Counting)
Firstly, observe that a single student can't receive $4$ or $5$ awards because this would mean that one of the other students receives no awards. Thus, each student must receive either $1$ , $2$ , or $3$ awards. If a student receives $3$ awards, then the other two students must each receive $1$ award; if a student receives $2$ awards, then another student must also receive $2$ awards and the remaining student must receive $1$ award. We consider each of these two cases in turn.
If a student receives three awards, there are $3$ ways to choose which student this is, and $\binom{5}{3}$ ways to give that student $3$ out of the $5$ awards. Next, there are $2$ students left and $2$ awards to give out, with each student getting one award. There are clearly just $2$ ways to distribute these two awards out, giving $3\cdot\binom{5}{3}\cdot 2=60$ ways to distribute the awards in this case.
In the other case, two students receive $2$ awards and one student receives $1$ award. We know there are $3$ choices for which student gets $1$ award. There are $\binom{3}{1}$ ways to do this. Then, there are $\binom{5}{2}$ ways to give the first student his two awards, leaving $3$ awards yet to be distributed. There are then $\binom{3}{2}$ ways to give the second student his $2$ awards. Finally, there is only $1$ student and $1$ award left, so there is only $1$ way to distribute this award. This results in $\binom{5}{2}\cdot\binom{3}{2}\cdot 1\cdot 3 =90$ ways to distribute the awards in this case. Adding the results of these two cases, we get $60+90=\boxed{\textbf{(B) }150}$ .

## Version of Solution 1
Upon inspection (specified in the above solution), there are two cases of the distribution of awards to the students: one student gets 3 awards and the other each get 1 award or one student gets 1 award and the other two get 2 awards.
In the first case, there are $\binom{3}{1} = 3$ ways to choose the person who gets 3 awards. From here, there are $\binom{5}{3} = 10$ ways to choose the 3 awards from the 5 total awards. Now, one person has $2$ choices for awards and the other has $1$ choice for the award. Thus, the total number of ways to choose awards in this case is $3 \cdot 10 \cdot 2 \cdot 1 = 60$ .
In the other case, there are $\binom{3}{1} = 3$ ways to choose the person who gets 1 award, and $5$ choices for his/her award. Then, one person has $\binom{4}{2} = 6$ ways to have his/her awards and the other person has $\dbinom{2}{2} = 1$ ways to have his/her awards. This gives $3 \cdot 5 \cdot 6 \cdot 1 = 90$ ways for this case.
Adding these numbers together, we get $60 + 90 = 150$ ways to distribute the awards, or choice $\boxed{\textbf{(B) }150}$ .

## Solution 3 (Complementary Counting)
Without the restriction that each student receives at least one award, we could take each of the awards and choose one of the $3$ students to give it to. This would be $3^5$ ways to distribute the awards in total. Now we need to subtract the cases where at least one student doesn't receive an award. If a student doesn't receive an award, there are $3$ choices for which student that is, so $2^5$ ways of choosing a student to receive each of the awards; in total, $3\cdot32=96$ .
However, if $2$ students both don't receive an award, then this case would be counted twice among the $96$ , so we need to add back in these cases. Said in other words, $2$ students not receiving an award is equivalent to $1$ student receiving $5$ awards, and there are $3$ choices for whom that student would be. To finish, the total number of ways to distribute the awards is $243 - 96+3$ , or $\boxed{\textbf{(B) }150}$ .

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/UnVo6jZ3Wnk?si=aB0A9Rb1KMIxOcpQ&t=5070
~Math-X

## Video Solution (🚀Under 3 min🚀)
https://youtu.be/0CWA2KWvAXY

## Video Solution by Robin "The Smartest Dude" Shang
https://youtu.be/3mMfy_evxl4

## Video Solution by OmegaLearn
https://youtu.be/dFFjlxm43b0?t=899
~ pi_is_3.14

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=Dg_2wXNY3tE

## Video Solution by WhyMath
https://youtu.be/HkFQe7ZxBb4
~WhyMath

## Video Solutions by The Learning Royal
https://youtu.be/tDChKU0pVN4
https://youtu.be/RUg6QfV5yg4

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=1443
~Interstigation

## Video Solution by STEMbreezy
https://youtu.be/wq8EUCe5oQU?t=243
~STEMbreezy