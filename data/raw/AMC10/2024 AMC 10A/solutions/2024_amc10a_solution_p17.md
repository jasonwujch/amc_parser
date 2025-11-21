# 2024 AMC 10A Problem 17

## Problem

Two teams are in a best-two-out-of-three playoff: the teams will play at most $3$ games, and the winner of the playoff is the first team to win $2$ games. The first game is played on Team A's home field, and the remaining games are played on Team B's home field. Team A has a $\frac{2}{3}$ chance of winning at home, and its probability of winning when playing away from home is $p$ . Outcomes of the games are independent. The probability that Team A wins the playoff is $\frac{1}{2}$ . Then $p$ can be written in the form $\frac{1}{2}(m - \sqrt{n})$ , where $m$ and $n$ are positive integers. What is $m + n$ ?

$\textbf{(A) } 10 \qquad \textbf{(B) } 11 \qquad \textbf{(C) } 12 \qquad \textbf{(D) } 13 \qquad \textbf{(E) } 14$

## Solution
We only have three cases where A wins: AA, ABA, and BAA (A denotes a team A win and B denotes a team B win). Knowing this, we can sum up the probability of each case. Thus the total probability is $\frac{2}{3}p+\frac{2}{3}(1-p)p+\frac{1}{3}p^2=\frac{1}{2}$ . Multiplying both sides by 6 yields $4p+4p(1-p)+2p^2=3$ , so $2p^2-8p+3=0$ and we find that $p=\frac{4\pm\sqrt{10}}{2}$ . Luckily, we know that the answer should contain $\frac{1}{2}(m - \sqrt{n})$ , so the solution is $p=\frac{4-\sqrt{10}}{2}=\frac{1}{2}(4-\sqrt{10})$ and the answer is $4+10=\boxed{\textbf{(E) } 14}$ .
~eevee9406
Another way to see the answer is subtraction and not addition is to realize that $p$ is between $0$ and $1$ since it is a probability. ~andliu766

## Video Solution 1 by Pi Academy
https://youtube/fW7OGWee31c?si=oq7toGPh2QaksLHE

## Video Solution 2 by SpreadTheMathLove
https://youtu.be/Db5nW_t-iP8?si=Ywz_NKciPRGZqInr

## Video Solution 3 by TheNeuralMathAcademy
https://www.youtube.com/watch?v=4b_YLnyegtw&t=3361s
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .