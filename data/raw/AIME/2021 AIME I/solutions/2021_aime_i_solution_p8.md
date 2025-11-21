# 2021 AIME I Problem 8

## Problem

Find the number of integers $c$ such that the equation \[\left||20|x|-x^2|-c\right|=21\] has $12$ distinct real solutions.

## Solution 1 (Piecewise Function: Analysis and Graph)
We take cases for the outermost absolute value, then rearrange: \[\left|20|x|-x^2\right|=c\pm21.\] Let $f(x)=\left|20|x|-x^2\right|.$ We rewrite $f(x)$ as a piecewise function without using absolute values: \[f(x) = \begin{cases} \left|-20x-x^2\right| & \mathrm{if} \ x \le 0 \begin{cases} 20x+x^2 & \mathrm{if} \ x\le-20 \\ -20x-x^2 & \mathrm{if} \ -20<x\leq0 \end{cases} \\ \left|20x-x^2\right| & \mathrm{if} \ x > 0 \begin{cases} 20x-x^2 & \mathrm{if} \ 0<x\leq20 \\ -20x+x^2 & \mathrm{if} \ x>20 \end{cases} \end{cases}.\] We graph $y=f(x)$ with all extremum points labeled, as shown below. The fact that $f(x)$ is an even function ( $f(x)=f(-x)$ holds for all real numbers $x,$ so the graph of $y=f(x)$ is symmetric about the $y$ -axis) should facilitate the process of graphing. [asy] /* Made by MRENTHUSIASM */ size(1200,300); real xMin = -65; real xMax = 65; real yMin = -50; real yMax = 125; draw((xMin,0)--(xMax,0),black+linewidth(1.5),EndArrow(5)); draw((0,yMin)--(0,yMax),black+linewidth(1.5),EndArrow(5)); label("$x$",(xMax,0),(2,0)); label("$y$",(0,yMax),(0,2)); real f(real x) { return abs(20*abs(x)-x^2); } real g(real x) { return 21; } real h(real x) { return -21; } draw(graph(f,-25,25),red,"$y=\left|20|x|-x^2\right|$"); draw(graph(g,-65,65),blue,"$y=\pm21$"); draw(graph(h,-65,65),blue); pair A[]; A[0] = (-20,0); A[1] = (-10,100); A[2] = (0,0); A[3] = (10,100); A[4] = (20,0); for(int i = 0; i <= 4; ++i) { dot(A[i],red+linewidth(4.5)); } label("$(-20,0)$",A[0],(-1.5,-1.5),red,UnFill); label("$(-10,100)$",A[1],(-1.5,1.5),red); label("$(0,0)$",A[2],(0,-1.5),red,UnFill); label("$(10,100)$",A[3],(1.5,1.5),red); label("$(20,0)$",A[4],(1.5,-1.5),red,UnFill); add(legend(),point(E),40E,UnFill); [/asy] Since $f(x)=c\pm21$ has $12$ distinct real solutions, it is clear that each case has $6$ distinct real solutions geometrically. We shift the graphs of $y=\pm21$ up $c$ units, where $c\geq0:$
- For $f(x)=c+21$ to have $6$ distinct real solutions, we need $0\leq c<79.$
- For $f(x)=c-21$ to have $6$ distinct real solutions, we need $21<c<121.$
Taking the intersection of these two cases gives $21<c<79,$ from which there are $79-21-1=\boxed{057}$ such integers $c.$
~MRENTHUSIASM

## Solution 2 (Graphing)
Graph $y=|20|x|-x^2|$ (If you are having trouble, look at the description in the next two lines and/or the diagram in Solution 1). Notice that we want this to be equal to $c-21$ and $c+21$ .
We see that from left to right, the graph first dips from very positive to $0$ at $x=-20$ , then rebounds up to $100$ at $x=-10$ , then falls back down to $0$ at $x=0$ .
The positive $x$ are symmetric, so the graph re-ascends to $100$ at $x=10$ , falls back to $0$ at $x=10$ , and rises to arbitrarily large values afterwards.
Now we analyze the $y$ (varied by $c$ ) values. At $y=k<0$ , we will have no solutions, as the line $y=k$ will have no intersections with our graph.
At $y=0$ , we will have exactly $3$ solutions for the three zeroes.
At $y=n$ for any $n$ strictly between $0$ and $100$ , we will have exactly $6$ solutions.
At $y=100$ , we will have $4$ solutions, because local maxima are reached at $x= \pm 10$ .
At $y=m>100$ , we will have exactly $2$ solutions.
To get $12$ distinct solutions for $y=|20|x|-x^2|=c \pm 21$ , both $c +21$ and $c-21$ must produce $6$ solutions.
Thus $0<c-21$ and $c+21<100$ , so $c \in \{ 22, 23, \dots , 77, 78 \}$ is required.
It is easy to verify that all of these choices of $c$ produce $12$ distinct solutions (none overlap), so our answer is $\boxed{057}$ .

## Solution 3 (Graphing)
Let $y = |x|.$ Then the equation becomes $\left|\left|20y-y^2\right|-c\right| = 21$ , or $\left|y^2-20y\right| = c \pm 21$ . Note that since $y = |x|$ , $y$ is nonnegative, so we only care about nonnegative solutions in $y$ . Notice that each positive solution in $y$ gives two solutions in $x$ ( $x = \pm y$ ), whereas if $y = 0$ is a solution, this only gives one solution in $x$ , $x = 0$ . Since the total number of solutions in $x$ is even, $y = 0$ must not be a solution. Hence, we require that $\left|y^2-20y\right| = c \pm 21$ has exactly $6$ positive solutions and is not solved by $y = 0.$
If $c < 21$ , then $c - 21$ is negative, and therefore cannot be the absolute value of $y^2 - 20y$ . This means the equation's only solutions are in $\left|y^2-20y\right| = c + 21$ . There is no way for this equation to have $6$ solutions, since the quadratic $y^2-20y$ can only take on each of the two values $\pm(c + 21)$ at most twice, yielding at most $4$ solutions. Hence, $c \ge 21$ . $c$ also can't equal $21$ , since this would mean $y = 0$ would solve the equation. Hence, $c > 21.$
At this point, the equation $y^2-20y = c \pm 21$ will always have exactly $2$ positive solutions, since $y^2-20y$ takes on each positive value exactly once when $y$ is restricted to positive values (graph it to see this), and $c \pm 21$ are both positive. Therefore, we just need $y^2-20y = -(c \pm 21)$ to have the remaining $4$ solutions exactly. This means the horizontal lines at $-(c \pm 21)$ each intersect the parabola $y^2 - 20y$ in two places. This occurs when the two lines are above the parabola's vertex $(10,-100)$ . Hence we have \begin{align*} -(c + 21) &> -100 \\ c + 21 &< 100 \\ c &< 79. \end{align*} Hence, the integers $c$ satisfying the conditions are those satisfying $21 < c < 79.$ There are $\boxed{057}$ such integers.
Note: Be careful of counting at the end, you may mess up and get $59$ .

## Solution 4 (Algebra)
Removing the absolute value bars from the equation successively, we get \begin{align*} \left|\left|20|x|-x^2\right|-c\right|&=21 \\ \left|20|x|-x^2\right|&= c \pm21 \\ 20|x|-x^2 &= \pm c \pm 21 \\ x^2 \pm 20x \pm c \pm21 &= 0. \end{align*} The discriminant of this equation is \[\sqrt{400-4(\pm c \pm 21)}.\] Equating the discriminant to $0$ , we see that there will be two distinct solutions to each of the possible quadratics above only in the interval $-79 < c < 79$ . However, the number of zeros the equation $ax^2+b|x|+k$ has is determined by where $ax^2+bx+k$ and $ax^2-bx+k$ intersect, namely at $(0,k)$ . When $k>0$ , $a>0$ , $ax^2+b|x|+k$ will have only $2$ solutions, and when $k<0$ , $a>0$ , then there will be $4$ real solutions, if they exist at all. In order to have $12$ solutions here, we thus need to ensure $-c+21<0$ , so that exactly $2$ out of the $4$ possible equations of the form $ax^2+b|x|+k$ given above have y-intercepts below $0$ and only $2$ real solutions, while the remaining $2$ equations have $4$ solutions. This occurs when $c>21$ , so our final bounds are $21<c<79$ , giving us $\boxed{057}$ valid values of $c$ .
### Remark
The graphs of $F(x)=\left||20|x|-x^2|-c\right|$ and $G(x)=21$ are shown here in Desmos: https://www.desmos.com/calculator/i6l98lxwpp
Move the slider around for $21<c<79$ to observe how they intersect for $12$ times.
~MRENTHUSIASM

## Video Solution
https://youtu.be/6k-uR71_jg0 ~mathproblemsolvingskills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .