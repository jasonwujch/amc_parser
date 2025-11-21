# 2019 AMC 8 Problem 19

## Problem

In a tournament there are six teams that play each other twice. A team earns $3$ points for a win, $1$ point for a draw, and $0$ points for a loss. After all the games have been played it turns out that the top three teams earned the same number of total points. What is the greatest possible number of total points for each of the top three teams?

$\textbf{(A) }22\qquad\textbf{(B) }23\qquad\textbf{(C) }24\qquad\textbf{(D) }26\qquad\textbf{(E) }30$

## Solution 1
This isn't finished to another. This gives equality, as each team wins once and loses once as well. For a win, we have $3$ points, so a team gets $3\times2=6$ points if they each win a game and lose a game. This case brings a total of $18+6=24$ points.
Therefore, we use Case 2 since it brings the greater amount of points, or $\boxed {\textbf {(C) }24}$ .
Note that case 2 can be easily seen to be better as follows. Let $x_A$ be the number of points $A$ gets, $x_B$ be the number of points $B$ gets, and $x_C$ be the number of points $C$ gets. Since $x_A = x_B = x_C$ , to maximize $x_A$ , we can just maximize $x_A + x_B + x_C$ . But in each match, if one team wins then the total sum increases by $3$ points, whereas if they tie, the total sum increases by $2$ points. So, it is best if there are the fewest ties possible.

## Solution 2
We can name the top three teams as $A$ , $B$ , and $C$ . We can see that (respective scores of) $A=B=C$ because these teams have the same points. If we look at the matches that involve the top three teams, we see that there are some duplicates: $AB$ , $BC$ , and $AC$ come twice. In order to even out the scores and get the maximum score, we can say that in match $AB$ , $A$ and $B$ each win once out of the two games that they play. We can say the same thing for $AC$ and $BC$ . This tells us that each team $A$ , $B$ , and $C$ win and lose twice. This gives each team a total of $3 + 3 + 0 + 0 = 6$ points. Now, we need to include the other three teams. We can label these teams as $D$ , $E$ , and $F$ . We can write down every match that $A, B,$ or $C$ plays in that we haven't counted yet: $AD$ , $AD$ , $AE$ , $AE$ , $AF$ , $AF$ , $BD$ , $BD$ , $BE$ , $BE$ , $BF$ , $BF$ , $CD$ , $CD$ , $CE$ , $CE$ , $CF$ , and $CF$ . We can say $A$ , $B$ , and $C$ win each of these in order to obtain the maximum score that $A$ , $B$ , and $C$ can have. If $A$ , $B$ , and $C$ win all six of their matches, $A$ , $B$ , and $C$ will have a score of $18$ . $18 + 6$ results in a maximum score of $\boxed{\textbf{(C) }24}$

## Solution 3
To start, we calculate how many games each team plays. Each team can play against $5$ other teams twice, so there are $10$ games that each team plays. So the answer is $10\cdot 3$ which is $30$ But wait... if we want $3$ teams to have the same amount of points, there can't possibly be a team who wins all their games. Let the top three teams be $A,B$ , and $C.$ $A$ plays $B$ and $C$ twice, so in order to maximize the games being played, we can split it $50-50$ between the $4$ games $A$ plays against $B$ or $C$ . We find that we just subtract $2$ games or $6$ points. Therefore the answer is $30-6$ , $24$ or $\boxed{\textbf{(C) }24}$

## Solution 4
Let the top $3$ teams be $A, B, C$ and the bottom teams to be $D, E, F$ . There are $2$ types of games the winners ( $A, B, C$ ) can play: Winners vs losers and Winner vs Winner.
Case 1: Winner vs Loser
For A, it would be $AD, AE, AF$ . We want to maximize this or make $A$ win in all $6$ ( $3\times2$ ) games. Therefore, A would get $6\times3$ points or $18$ .
Case 2: Winner vs Winner
There are $_{3}P_{2}=\frac{3!}{1!}=6$ games they can play against each other. Since we want each $3$ to have an equal amount. Each team should win $2$ games and get $6$ points. In total, $18+6=\boxed{\textbf{(C) }24}$ ~RandomMathGuy500

## Video Solution by Math-X
https://youtu.be/IgpayYB48C4?si=ZFTK7CQBPH6nrE9h&t=5702
~Math-X

## Video Solution
https://youtu.be/sPdg92Alud4
~Education, the Study of Everything

## Video Solutions
Associated Video - https://youtu.be/s0O3_uXZrOI
https://youtu.be/hM4sHJSMNDs
-Happpytwin

## Video Solution by OmegaLearn
https://youtu.be/HISL2-N5NVg?t=4616
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=k_AuB_bzidc&list=PLbhMrFqoXXwmwbk2CWeYOYPRbGtmdPUhL&index=20

## Video Solution
https://youtu.be/d-JoEwIOlKQ
~savannahsolver

## Video Solution by The Power of Logic(1 to 25 Full Solution)
https://youtu.be/Xm4ZGND9WoY
~Hayabusa1
### See Also