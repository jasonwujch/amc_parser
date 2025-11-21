# 2002 AMC 12P Problem 22

## Problem

Under the new AMC $10, 12$ scoring method, $6$ points are given for each correct answer, $2.5$ points are given for each unanswered question, and no points are given for an incorrect answer. Some of the possible scores between $0$ and $150$ can be obtained in only one way, for example, the only way to obtain a score of $146.5$ is to have $24$ correct answers and one unanswered question. Some scores can be obtained in exactly two ways, for example, a score of $104.5$ can be obtained with $17$ correct answers, $1$ unanswered question, and $7$ incorrect, and also with $12$ correct answers and $13$ unanswered questions. There are (three) scores that can be obtained in exactly three ways. What is their sum?

$\text{(A) }175 \qquad \text{(B) }179.5 \qquad \text{(C) }182 \qquad \text{(D) }188.5 \qquad \text{(E) }201$

## Solution 1
Let $c$ denote the amount of correct answers, $u$ denote the amount of unanswered questions, and $w$ denote the amount of wrong answers. The conversion rate is what differentiates between two ways to get the same score.
There are two ways to realize the conversion rate of wrong answers to unanswered questions and correct answers to unanswered questions.

## Sub Solution 1.1
Notice how the way to get $104.5$ points directly tells us the conversion rate. $17$ correct questions, $1$ unanswered question, and $7$ wrong answers is equivalent to $12$ correct answers, $13$ unanswered questions, and $0$ wrong answers. Since $17-12=5, 1-13=-12,$ and $7-0=7$ , the conversion rate is $c, u, w \implies c-5, u+12, w-7.$

## Sub Solution 1.2
The second way to find out the conversion rate is to actually do the math. If a wrong answer is converted to an unanswered question, the total value will be $2.5$ more than the total value. If a correct answer is converted to an unanswered question, the total value will be $6-2.5=3.5$ less than the total value. Thus, we want the "more than" to be equal to the "less than".
Let $x$ denote the amount of correct answers converted to unanswered questions and $y$ denote the amount of wrong answers converted to unanswered questions. Since we want "more than" to be equal to the "less than", $3.5x=2.5y$ , where $x$ and $y$ are integers. Multiply by $2$ on both sides, $7x=5y$ implies $x=5$ and $y=7.$ Again, the conversion rate is $c, u, w \implies c-5, u+12, w-7.$

## Sub Solutions Combine
Either way, we find $c, u, w \implies c-5, u+12, w-7.$ If there are three ways, this implies the first way $c, u, w$ the second way is $c, u, w \implies c-5, u+12, w-7,$ and the third way is $c, u, w \implies c-10, u+24, w-14.$ Since $c, u, w \geq0,$ it follows that our three cases' first ways are as follows:
$11$ correct answers, $0$ unanswered questions, $14$ wrong answers
$10$ correct answers, $0$ unanswered questions, $15$ wrong answers
$10$ correct answers, $1$ unanswered questions, $14$ wrong answers.
Thus, our answer is $6(11+10+10)+2.5(0+0+1)+0(14+15+14)=\boxed {\text{(D) }188.5}.$

## Solution 2
This solution is formulated in formal language rather than cheesy methods, though the idea is the same. Additionally, we do not need to take into account the amount of wrong answers, which is easier to deal with.
Let $c$ denote the amount of correct answers, $u$ denote the amount of unanswered questions. Then $c+u \leq 25.$ We want to find the LCM of $2.5$ and $6$ so we can convert between different ways, similar to solution $1.$ The LCM is equal to $30$ , since $6 \cdot \textbf{5}=30$ and $2.5 \cdot \textbf{12}=30.$
The first way will take the form $(c,u).$ The second way will take the form $(c+5, u-12).$ The third way will take the form $(c+10, u-24).$ In particular, since we cannot have a negative amount of unanswered questions, $u \geq 24.$ Combined with $c+u \leq 25$ , our three cases are $(0,24), (1,24),$ and $(0,25).$
Thus, our answer is $6(0+1+0) + 2.5(24+24+25)=\boxed {\text{(D) }188.5}.$
### Note
The conversion rate can either be $(c+5, u-12).$ or $(c-5, u+12).$ Both solutions use a different conversion rate to illustrate this point. The first solution defines the "first way" as the one with the most correct, while the second solution defines the "first way" as the one with the most unanswered.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .