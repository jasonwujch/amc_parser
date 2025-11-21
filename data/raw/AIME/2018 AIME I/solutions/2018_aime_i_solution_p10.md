# 2018 AIME I Problem 10

## Problem

The wheel shown below consists of two circles and five spokes, with a label at each point where a spoke meets a circle. A bug walks along the wheel, starting at point $A$ . At every step of the process, the bug walks from one labeled point to an adjacent labeled point. Along the inner circle the bug only walks in a counterclockwise direction, and along the outer circle the bug only walks in a clockwise direction. For example, the bug could travel along the path $AJABCHCHIJA$ , which has $10$ steps. Let $n$ be the number of paths with $15$ steps that begin and end at point $A$ . Find the remainder when $n$ is divided by $1000.$

## Solution 1
We divide this up into casework. The "directions" the bug can go are $\text{Clockwise}$ , $\text{Counter-Clockwise}$ , and $\text{Switching}$ . Let an $I$ signal going clockwise (because it has to be in the inner circle), an $O$ signal going counter-clockwise, and an $S$ switching between inner and outer circles. An example string of length fifteen that gets the bug back to $A$ would be $ISSIIISOOSISSII$ . For the bug to end up back at $A$ , the difference between the number of $I$ 's and $O$ 's must be a multiple of $5$ .
So, the total number of ways is $1+2002+1001=3004$ which gives $\boxed{004}$ as the answer.

## Solution 2 (Official MAA)
Note that the set of sequences of moves the bug makes is in bijective correspondence with the set of strings of $X$ s and $Y$ s of length $15$ , where $X$ denotes a move which is either counterclockwise or inward along a spoke and $Y$ denotes a move which is either clockwise or outward along a spoke. (The proof of this basically boils down to the fact that which one depends on whether the bug is on the inner wheel or the outer wheel.) Now the condition that the bug ends at A implies that the difference between the number of $X$ s and the number of $Y$ s is a multiple of $5$ , and so we must have either $4$ , $9$ , or $14$ $X$ s within the first fourteen moves with the last move being an $X$ . This implies the answer is \[\binom{14}4+\binom{14}9+\binom{14}{14} = 3004\equiv \boxed{004}\pmod{1000}.\]

## Solution 3 (Similar To Solution 2 But Modified To Clarify)
Let an $O$ signal a move that ends in the outer circle and $I$ signal a move that ends in the inner circle. Now notice that for a string of $15$ moves to end at $A$ , the difference between $O$ 's and $I$ 's in the string must be a multiple of $5,$ and this is because the net displacement of the bug after its journey must be a multiple of $5$ , as that is one cycle around the wheel.
$15$ $I$ 's: Trivially $1$ case.
$5$ $O$ 's and $10$ $I$ 's: Since the string has to end in an $I$ for the bug to land on $A$ , there are a total of $\binom{14}{5}=2002$ ways to put $5$ $O$ 's in the first $14$ moves.
$10$ $O$ 's and $5$ $I$ 's: Similarly there are $\binom{14}{4}=1001$ ways to put $5-1=4$ $I$ 's in the first $14$ moves.
$15$ $O$ 's: Impossible since the string has to end with an I.
This brings us an answer of $1+2002+1001=3004 \equiv \boxed{004} \pmod{1000}$ .
-Solution by mathleticguyyyyyyyyy- ~Edited by ike.chen ~Edited again by nevergonnagiveup

## Solution 4 (Recursion)
Define $A_n$ to be the number of sequences of length $n$ that ends at $A$ and similarly for the other spokes. Also, let \[S_n=A_n+B_n+C_n+D_n+E_n+F_n+G_n+H_n+I_n+J_n\] At every point in the path, the bug has $2$ choices for its next move. Since $S_n$ represents the total number of paths we have $S_n=2^n$ . We can create a recursive formula for $A_n:$
\begin{align*} A_n&=J_{n-1}+E_{n-1} \\ &=(I_{n-2}+A_{n-2})+(D_{n-2}+F_{n-2}) \\ &=(H_{n-3}+B_{n-3})+(J_{n-3}+E_{n-3})+(G_{n-3}+C_{n-3})+(J_{n-3}+E_{n-3}) \\ &=(B_{n-3}+C_{n-3}+E_{n-3}+G_{n-3}+H_{n-3}+J_{n-3})+(J_{n-3}+E_{n-3}) \\ &=(S_{n-3}-(I_{n-3}+A_{n-3}+D_{n-3}+F_{n-3}))+A_{n-2} \\ &=2^{n-3}-(J_{n-2}+E_{n-2})+A_{n-2} \\ &=2^{n-3}-A_{n-1}+A_{n-2} \\ \end{align*} $A_0=0$ , $A_1=0$ , $A_2=1$ , $A_3=0$ , $A_4=3$ . Continuing the process yields $A_{15}=3\boxed{004}$ .
~ Nafer, minor edits by grogg007

## Solution 5 (Stars and Bars)
The points on the outer circle and the points on the inner circle have a one-to-one correspondence. Therefore, it is equivalent to the scenario of switching directions back and forth in the inner circle but changing directions to make up for travelling on spokes. If the ant changes directions $s$ times, the number of moves the ant makes is $15-s$ . Also note that is switches directions an even number of times, so we think of it in pairs:
Case 1: 0 pairs
The ant would have to only be in the inner circle and go in one direction. Hence there is $1$ way.
Case 2: 1 pair
This is equivalent to the ant making 13 moves in the inner circle where it switches directions 2 times (counterclockwise-clockwise-counterclockwise). Note that the number of counterclockwise and clockwise moves must be equivalent $\pmod{5}$ . Let the number of counterclockwise moves be $C$ and clockwise moves be $C'$ . The only two feasible solutions for $(C,C')$ are $(4,9)$ and $(9,4)$ . Therefore, we use stars and bars to obtain $10+5=15$ ways for this case.
Case 3: 2 pairs
The ant changes directions 4 times and makes 11 moves, so we obtain $(3,8)$ and $(8,3)$ using similar logic. Using stars and bars once again, we obtain $90+180=270$ ways for this case.
Case 4: 3 pairs
Again, the only solutions for $(C,C')$ are $(2,7)$ and $(7,2)$ . Using stars and bars, we obtain $360+720=1080$ .
Case 5: 4 pairs
The only solutions are $(1,6)$ and $(6,1)$ . Using stars and bars, we obtain $840+420=1260$ .
Case 6: 5 pairs
The only solutions are $(0,5)$ and $(5,0)$ . Using stars and bars, we obtain $252+126=378$ . Note that there are no more cases since $C$ and $C'$ have to be equivalent $\pmod{5}$ , which would need to make $C$ or $C'$ negative. Adding all the cases, we get $1+15+270+1080+1260+378=3004$ . Taking modulo $1000$ , we obtain $3004 \equiv \boxed{004} \pmod{1000}$
The process of using stars and bars was the number of ways to group the counterclockwise and clockwise moves. For instance, if there are $p$ pairs of switches, then based on the solutions for $(C,C')$ , we can divide $C$ into $p+1$ subsets and $C'$ into $p$ subsets. This is equivalent to putting $C$ objects in $p+1$ bins and $C'$ objects into $p$ bins where a bin can be empty which is modeled by consecutive switches. Then, we multiply both results. Therefore, for each $p$ , we compute $\dbinom{C+p}{p}\dbinom{C'+p-1}{p-1}$ and add them up.
~ Magnetoninja

## Solution 6
We can view the diagram as a collection of points on the complex plane that are connected by transformations/symmetries. The inner circle can be represented as the fifth roots of unity(WLOG let $A$ correspond to $1$ ) where moving between the inner circle can be mapped to multiplying by $e^{\frac{2i\pi}{5}}$ we can also view moving between circles as a multiplying by $-e^{-2i\pi} = -1.$
Therefore the generating function for the paths beginning at $1$ or $A$ can be seen as $(e^{\frac{2i\pi}{5}} - 1)^{15}.$
We want the positive real terms or the ones that end on $1$ and those add up to $\dbinom{15}{5}(e^{2i\pi/5})^5(-1)^{10} + \dbinom{15}{15}(e^{2i\pi/5})^{15} = 3004 \equiv \boxed{004} \pmod{1000}.$
~SailS

## Solution 7 (Official MAA, clarified)
Our motivation is that moving along the outer circle "counters" moving along the inner circle in terms of angular position. Hence, denote $I$ as moving along the inner circle OR moving from the outside circle to the inner circle. Also denote $O$ as moving along the outer circle OR moving from the inside circle to the outside circle.
Notice that eventually, moves that go from the inner circle to the outer circle must equal to moves that go from the outer circle from the inner circle. This is because we must always end up at the inner circle at the last move, meaning that every time we moved to the outer circle, we must have also eventually moved back to the inner circle.
With this in mind, we can now "ignore" moving between inner and outer circle. We find that $O \equiv I \pmod 5$ , since we must end up at our original angular position, and taking 5 moves in one direction lands us back in the same position.
Using this fact, we form $3$ cases:
$O - I = 5$ , $O + I = 15$ which gives us $O = 10$ . Since we have $10$ $O$ s and $5$ $I$ s, but the last move must be an $I$ , we have $\binom{14}{10}=1001$ ways for this case.
$O - I = -5$ , $O + I = 15$ which gives us $O = 5$ . We have $\binom{14}{5}=2002$ ways for this case.
$O - I = -15$ , $O + I = 15$ which gives us $O = 0$ . (aka only moving in the inner circle). We have $\binom{14}{0}=1$ ways for this case.
Ultimately, the total number of ways is $1001 + 2002 + 1 = 3004$ , and our answer is $\boxed{004}$ .
~xHypotenuse
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .