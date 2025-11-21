# 2023 AMC 10B Problem 22

## Problem

How many distinct values of $x$ satisfy $\lfloor{x}\rfloor^2-3x+2=0$ , where $\lfloor{x}\rfloor$ denotes the largest integer less than or equal to $x$ ?

$\textbf{(A) } \text{an infinite number} \qquad \textbf{(B) } 4 \qquad \textbf{(C) } 2 \qquad \textbf{(D) } 3 \qquad \textbf{(E) } 0$

## Solution 1
To further grasp at this equation, we rearrange the equation into \[\lfloor{x}\rfloor^2=3x-2.\] Thus, $3x-2$ is a perfect square and nonnegative. It is now much more apparent that $x \ge 2/3,$ and that $x = 2/3$ is a solution.
Additionally, by observing the RHS, $x<4,$ as \[\lfloor{4}\rfloor^2 > 3\cdot4,\] since squares grow quicker than linear functions.
Now that we have narrowed down our search, we can simply test for intervals $[2/3,1], [1,2],[2,3],[3,4).$ This intuition to use intervals stems from the fact that $x=1,2$ are observable integral solutions.
Notice how there is only one solution per interval, as $3x-2$ increases while $\lfloor{x}\rfloor^2$ stays the same.
Finally, we see that $x=3$ does not work, however, through setting $\lfloor{x}\rfloor^2 = 9,$ $x = 11/3$ is a solution and within our domain of $[3,4).$
This provides us with solutions $\left(\frac23, 1, 2, \frac{11}{3}\right),$ thus the final answer is $\boxed{(\text{B}) \ 4}.$
~mathbrek, happyhari

## Solution 2
This solution only works if you understand the graph of \( \lfloor x \rfloor \). If you are unfamiliar with that concept, please refer to solution 1.
We quickly see that \( \lfloor x \rfloor^2 = 3x - 2 \). We need the solutions that fulfill \( \lfloor x \rfloor^2 \) and \( 3x - 2 \). We quickly draw the system of equations.
Looking at our graph, we see that there are 4 intersections, implying that there are $\boxed{(\text{B}) \ 4}$ solutions that work.
~Pinotation
~Graph by Pinotation

## Solution 3 (Desperation)
Notice there has to be a solution for $x$ between $(2,-3)$ and $(1,2)$ because of the floors. There is also no way $2$ solutions exist because of the quadratic, and when we add them together, we get $\boxed{(\text{B}) \ 4}.$ ~perion, minor grammar edit by Ynsg.

## Solution 4 (Three Cases)
First, let's take care of the integer case--clearly, only $x=1,2$ work. Then, we know that $3x$ must be an integer. Set $x=\frac{a}3$ . Now, there are two cases for the value of $\lfloor x\rfloor$ . Case 1: $\lfloor x\rfloor=\frac{a-1}{3}$ \[\frac{a^2-2a+1}{9}=a-2\rightarrow a^2-2a+1=9a-18\rightarrow a^2-11a+19=0.\] There are no solutions in this case. Case 2: $\lfloor x\rfloor=\frac{a-2}{3}$ \[\frac{a^2-4a+4}{9}=a-2\rightarrow a^2-4a+4=9a-18\rightarrow a^2-13a+22=0.\] This case provides $\frac23$ and $\frac{11}3$ as two more solutions. Our final answer is thus $\boxed{4}$ .
~wuwang2002 & minor edit by catkeyboard

## Solution 5
First, $x=2,1$ are trivial solutions
We assume from the shape of a parabola and the nature of the floor function that any additional roots will be near 2 and 1
We can now test values for $\lfloor{x}\rfloor$ :
$\lfloor{x}\rfloor=0$
We have $0-3x+2=0$ . Solving, we have $x=\frac{2}{3}$ . We see that $\lfloor{\frac{2}{3}}\rfloor=0$ , so this solution is valid
$\lfloor{x}\rfloor=-1$
We have $1-3x+2=0$ . Solving, we have $x=1$ . $\lfloor{1}\rfloor\neq-1$ , so this is not valid. We assume there are no more solutions in the negative direction and move on to $\lfloor{x}\rfloor=3$
$\lfloor{x}\rfloor=3$
We have $9-3x+2=0$ . Solving, we have $x=\frac{11}{3}$ . We see that $\lfloor{\frac{11}{3}}\rfloor=3$ , so this solution is valid
$\lfloor{x}\rfloor=4$
We have $16-3x+2=0$ . Solving, we have $x=6$ . $\lfloor{6}\rfloor\neq4$ , so this is not valid. We assume there are no more solutions.
Our final answer is $\boxed{\textbf{(B) }4}$
~kjljixx

## Solution 6
Denote $a = \lfloor x \rfloor$ . Denote $b = x - \lfloor x \rfloor$ . Thus, $b \in \left[ 0 , 1 \right)$ .
The equation given in this problem can be written as \[ a^2 - 3 \left( a + b \right) + 2 = 0 . \]
Thus, \begin{align*} 3 b & = a^2 - 3 a + 2 . \end{align*}
Because $b \in \left[ 0 , 1 \right)$ , we have $3 b \in \left[ 0 , 3 \right)$ . Thus, \[ a^2 - 3 a + 2 = 0, 1, \mbox{ or } 2 . \]
If $a^2-3a+2=0$ , $(a-2)(a-1)=0$ so $a$ can be $1, 2$ .
If $a^2-3a+2=1$ , $a^2-3a+1=0$ which we find has no integer solutions after finding the discriminant.
If $a^2-3a+2=2$ , $a^2-3a=0$ -> $a(a-3)=0$ so $a$ can also be $0, 3$ .
Therefore, $a = 1$ , 2, 0, 3. Therefore, the number of solutions is $\boxed{\textbf{(B) 4}}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 7 (Quick)
A quadratic equation can have up to 2 real solutions. With the $\lfloor{x}\rfloor$ , it could also help generate another pair. We have to verify that the solutions are real and distinct.
First, we get the trivial solution by ignoring the floor. $(x-2)(x-1) = 0$ , we get $(2,1)$ as our first pair of solutions.
Up to this point, we can rule out A,E.
Next, we see that $\lfloor{x}\rfloor^2-3x=0.$ This implies that $-3x$ must be an integer. We can guess and check $x$ as $\dfrac{k}{3}$ which yields $\left(\dfrac{2}{3},\dfrac{11}{3}\right).$
So we got 4 in total $\left(\dfrac{2}{3},1,2,\dfrac{11}{3}\right)$ , meaning that our answer is $\boxed{(\text{B}) \ 4}$ .
~Technodoggo ~Aqf243 (minor edit)

## Solution 8
$x=1, 2$ are trivial solutions. Let $x=n+f$ for some integer $n$ and some number $f$ such that $-1<f<1$ . \[\lfloor{x}\rfloor^2-3x+2= \lfloor{n+f}\rfloor^2-3(n+f)+2=n^2+-3(n+f)+2.\] So now we have \[n^2-3(n+f)+2 = 0,\] which we can rewrite as \[n(n-3)=3f-2.\] Since $n$ is an integer, $n(n-3)$ is an integer, so $3f-2$ is an integer. Since $-1<f<1$ , the only possible values of $f$ are $\frac{1}{3}$ , $\frac{2}{3}$ , $-\frac{1}{3}$ , and $-\frac{2}{3}$ . Plugging in each value, we find that the only value of $f$ that produces integer solutions for $n$ is $f=\frac{2}{3}$ . If $f=\frac{2}{3}$ , $n=0$ or $n=3$ . Hence, there is a total of 4 possible solutions, so the answer is $\boxed{\textbf{(B) }4}$ . ~azc1027

## Solution 9
We rewrite the equation as ${\lfloor x\rfloor}^2-3\lfloor x\rfloor-3\{x\}+2=0$ , where $\{x\}$ is the fractional part of $x$
Denote $\lfloor x\rfloor = x_1$ and $\{x\} = x_2.$ Thus \[{x_1}^2-3{x_1}-3{x_2}+2=0.\]
By definition, $0\leq x_2\leq 1$ . We then have ${x_1}^2-3{x_1}+2=3{x_2}$ and therefore $0\leq {x_1}^2-3{x_1}+2\leq 3$ .
Solving, we have $\left[\frac{3-\sqrt{13}}{2},1\right]\cup \left[2,\frac{3+\sqrt{13}}{2}\right]$ . But since $x_1$ is an integer, we have $x_1$ can only be $0,1,2,$ or $3$ .
Testing, we see these values of $x_1$ work, and therefore the answer is just $\boxed{\textbf{(B) }4}$ .
~ESAOPS

## Similar approach as Solution 9
Use the fact that $x = \lfloor x \rfloor + \{x\}$ . Thus we have \[(\lfloor x \rfloor^2 - 3\lfloor x \rfloor + 2) - 3\{x\} = 0.\]
Noting that $0 \leq \{x\} < 1$ , we get
\[0 \leq (\lfloor x \rfloor - 2)(\lfloor x \rfloor - 1) < 3.\]
From there, it is not too hard to see that the only values of $\lfloor x \rfloor$ that satisfy this condition (while also noting that $\lfloor x \rfloor$ must be an integer) are 3, 2, 1, and 0, yielding 4 values.
~mathboy282

## Solution 10 (Very Fast)
We know that for integer values of x, the graph is just $x^2-3x+2$ . From the interval $[x, x+1]$ , the square stays the same, so the graph has a line segment that goes down by 3 and right by 2. This is very easy to graph, so we see that there are 4 solutions. Or, we notice that only $x = 0, 1, 2, 3$ results in a $x^2-3x+2$ in the interval $[0, 3]$ .That is $\boxed{\textbf{(B) }4}$ solutions.
~Xyco

## Solution 11
Define $[x] = n,$ and define the fractional part of $x$ as $x(f).$
Thus $\lfloor{x}\rfloor^2-3x+2=0$ is \[n^2-3(n+x(f))+2=0.\] Expanding, \[n^2-3n-3x(f)+2=0.\] We realize $n^2-3n+2$ must always be an integer so for $n^2-3n+2$ to equal zero, $3x(f)$ must also equal an integer. Therefore, $x(f)$ must be $\frac{1}{3}, \frac{2}{3},$ or $0.$ Plugging in $x(f)=0$ gives \[n^2-3n-3(0)+2=0,\] which simplifies to \[n^2-3n+2=0.\] Continuing, plugging in $x(f)=\frac{1}{3}$ gives \[n^2-3n-3\left(\frac{1}{3}\right)+2=0,\] which simplifies to \[n^2-3n+1.\] Finally, substituting $x(f)=\frac{2}{3}$ gives \[n^2-3n-3\left(\frac{2}{3}\right)+2=0,\] which simplifies to \[n^2-3n=0.\] We know $n$ must be a integer, so we can just solve for $n$ and only utilize the integers we end up with.
We get two integers $n$ if $x(f)=0:$ $n=1,2.$ We know $n+x(f)=x$ by definition, and plugging the values of $n$ and $x(f)$ into this equation gives us two solutions for $x:$ \[x=1,2.\]
We don't get any integers $n$ if $x(f)=\frac{1}{3}.$ We use the quadratic discriminant, $\sqrt{b^{2}-4ac}$ to get an expression which yields a non-integer value, $\sqrt{3^{2}-4(1)(1)},$ which means this case is invalid.
We get two integers $n$ if $x(f)=\frac{2}{3}:$ $n=0,3.$ We know $n+x(f)=x$ by definition, and plugging the values of $n$ and $x(f)$ into this equation gives us two solutions for $x:$ \[x=\frac{2}{3},\frac{11}{3}.\]
We end up with a total of four solutions which are $x=1,2, \frac{2}{3}, \frac{11}{3}.$
Our answer is
~formatting by belindazhu13

## Solution 12 (Based on graph)
For $\lfloor x \rfloor^2 - 3x + 2 = 0$ , there is a discontinuity at each integer value of $x$ , and it also lies on the non-floor version of the function. Between each integer $x$ and the next forms a line with a slope of $-3$ . This simplifies the task of sketching the function's graph. Note that the points at $1$ and $2$ are considered intersections because they are points on the left side of each integer interval that exactly lie on $y = 0$ . Thus, we conclude there are $4$ intersection points, and the answer is $\boxed{(\text{B}) \ 4}$ .
~ Athmyx

## Video Solution 1 by OmegaLearn
https://youtu.be/wAYcpn-Q_KQ

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=DvHGEXBjf0Y

## Video Solution
https://youtu.be/ONRoop23LIY
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .