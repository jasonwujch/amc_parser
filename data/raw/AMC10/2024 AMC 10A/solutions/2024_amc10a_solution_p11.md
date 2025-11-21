# 2024 AMC 10A Problem 11

## Problem

How many ordered pairs of integers $(m, n)$ satisfy $\sqrt{n^2 - 49} = m$ ?

$\textbf{(A)}~1\qquad\textbf{(B)}~2\qquad\textbf{(C)}~3\qquad\textbf{(D)}~4\qquad\textbf{(E)}~\text{infinitely many}$

## Solution 1
Note that $m$ is a nonnegative integer.
We square, rearrange, and apply the difference of squares formula to the given equation: \[(n+m)(n-m)=49.\] It is clear that $n+m\geq n-m,$ so $(n+m,n-m)=(49,1),(7,7),(-7,-7),(-1,-49).$ Each ordered pair $(n+m,n-m)$ gives one ordered pair $(m,n),$ so there are $\boxed{\textbf{(D)}~4}$ such ordered pairs $(m,n).$
Remark
From $(n+m,n-m)=(49,1),(7,7),(-7,-7),(-1,-49),$ we get $(m,n)=(24,25),(0,7),(0,-7),(24,-25),$ respectively.
~MRENTHUSIASM

## Solution 2
Squaring both sides of the given equation gives \[n^2-49=m^2\rightarrow n^2-m^2=49\rightarrow (n+m)(n-m)=49\] Splitting $49$ into its factors (keep in mind it doesn't ask for positive integers, so the factors can be double negative, too) gives six cases:
$(1\cdot49)$
$(7\cdot7)$
$(49\cdot1)$
$(-1\cdot -49)$
$(-7\cdot -7)$
$(-49\cdot -1)$ .
Note that the square root in the problem doesn't have $\pm$ with it. Therefore, if there are two solutions, $(n,m)$ and $(n,-m)$ , then these together are to be counted as one solution. The solutions expressed as $(n,m)$ are:
$(25,24)$
$(25,-24)$
$(7,0)$
$(-7,0)$
$(-25,24)$
$(-25,-24)$ .
$(25,24)$ and $(25,-24)$ are to be counted as one, same for $(-25,24)$ and $(-25,-24)$ . Therefore, the solution is $\boxed{\textbf{(D)}~4}$ .
~Tacos_are_yummy_1

## Solution 3 (Crazy Rush)
From looking at the problem, it's obvious that $(\pm7,0)$ are already solutions. From squaring and rearranging, we get \[n^2-m^2=49.\] We know that the difference between two consecutive squares is always odd, and for each pair of increasing consecutive squares, the difference starts from $3$ and increases by $2$ each time. This means that there is an existing pair, $(\pm n,m)$ of consecutive squares that will satisfy this equation.
Also note that the answer cannot be infinity because the difference between two squares will increase as the two squares get higher, consecutive or not.
Therefore, the solutions $(\pm7,0)$ and $(\pm n,m)$ where $n$ and $m$ are consecutive that have a square difference of $49,$ give the answer of $\boxed{\textbf{(D)}~4}.$
~Tacos_are_yummy_1
Minor Note: Looking at the problem, it is obvious that $-7$ and $7$ are solutions and you can eliminate $1,3,$ and infinite. You can assume that there is more than $2$ solutions because when determining square expressions, these problems usually always have more than an obvious solution.
~breakingbread

## Solution 4 (Quick)
Clearly, $(7,0)$ and $(-7,0)$ are solutions. Notice that $49 = 7^2$ . Remembering our Pythagorean triples, we realize $(25, 24)$ is a solution as well, and by extension, so is $(-25, 24)$ . Since 7 is not part of any other Pythagorean triple, we can conclude the answer is $\boxed{\textbf{(D)}~4}$ .
~i_am_suk_at_math_2

## Solution 5 (idk why someone would ever use this)
Since in $n^2-49$ there are no restrictions of the sign of $n$ , we know that the solution will come in pairs, with negative and positive $n$ . Therefore, the answer will not be $1$ or $3$ . We can further confirm that it is not $1$ , since the problem would probably ask for an operation of $n$ and $m$ instead of the number of solutions. We can also guess it is not $2$ , since then the problem would ask for the sum of one of the variables in the solutions. It seems improbable that over the integers there would be infinite answers. So the answer is $\boxed{\textbf{(D) }4}$
~megaboy6679
(do not ever use this)

## Solution 6 (Pythagorean Theorem)
Rearranging the equation gives
\[m^2+7^2=n^2\]
This is a classic Pythagorean Theorem equation, where $7$ is a leg and $m$ and $n$ are the two remaining legs. All we have to do is to find triples that satisfy this equation. It is common knowledge that $(7, 24, 25)$ is a triple, thus $(24, 25)$ and $(-24, -25)$ are two solutions. Another one is $(0, 7, 7)$ , so $(0, 7)$ and $(0, -7)$ are two other solutions. We can be sure that there are no other triples to find because $4$ is the highest answer choice, otherwise it would be "infinitely many", which isn't plausible. Therefore, the answer is $\boxed{\textbf{(D) }4}$ .
~MrThinker

## Solution 7
Square both sides giving $n^2-49=m^2$ , then rearrange the equation into a quadratic: $n^2-49-m^2=0$ . then find the Delta ( $b^2-4ac$ ) where $a,b,$ and $c$ are the coefficients of the quadratic in the respective order. Calculating it we get $2401-4=2397$ , since this is a positive number it means there are two solutions but both solutions can be both $m$ or $n$ , so the answer is $\boxed{\textbf{(D) }4}$ .
~twinotter

## Solution 8 (Graphing)
We can rewrite the equation as $y=\sqrt{x^{2}-49}$ and graph it to find integer solutions. It is a hyperbola of standard form $\frac{x^{2}}{49}-\frac{y^{2}}{49}=1$ . Note that the graph of the function does not exist below the y-axis. We find that where $\left|x\right|>25$ integer solutions are impossible, since the difference between the function and its asymptote $y=x$ in that region is less than one and always decreasing; thus, since $y=x$ is always an integer, $\sqrt{x^{2}-49}$ must be a fractional amount less than that integer, so we can rule out option E (infinite integer solutions). We notice that the roots are a solution $\left(\pm7,\ 0\right)$ , as well as $\left(\pm25,\ 24\right)$ , making four solutions. $4$ is already the maximum possible answer choice (having ruled out E), so we know there are no more solutions. Thus, the answer is $\boxed{\textbf{(D) }4}$ .
~ZingiberiMaracandae

## Video Solution
https://youtu.be/l3VrUsZkv8I
~MC

## Video Solution by Pi Academy
https://youtu.be/ABkKz0gS1MU?si=ZQBgDMRaJmMPSSMM

## Video Solution 1 by Power Solve
https://youtu.be/G91MyH1CycE

## Video Solution by Daily Dose of Math
https://youtu.be/Ne1qOZNRxfY
~Thesmartgreekmathdude

## Video Solution by SpreadTheMathLove
https://youtu.be/fUw--t6CQW4?si=9OOkJ0R0bVckY_IX

## Video Solution by Dr. David
https://youtu.be/t6vkQN7F1-E

## Video solution by TheNeuralMathAcademy
https://www.youtube.com/watch?v=4b_YLnyegtw&t=1732s
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .