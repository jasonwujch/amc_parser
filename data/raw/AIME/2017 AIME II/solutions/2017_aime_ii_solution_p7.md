# 2017 AIME II Problem 7

## Problem

Find the number of integer values of $k$ in the closed interval $[-500,500]$ for which the equation $\log(kx)=2\log(x+2)$ has exactly one real solution.

## Solution 1
[asy] Label f; f.p=fontsize(5); xaxis(-3,3,Ticks(f,1.0)); yaxis(-3,26,Ticks(f,1.0)); real f(real x){return (x+2)^2;} real g(real x){return x*-1;} real h(real x){return x*-2;} real i(real x){return x*-3;} real j(real x){return x*8;} draw(graph(f,-2,3),green); draw(graph(g,-2,2),red); draw(graph(h,-2,1),red); draw(graph(i,-2,1/3),red); draw(graph(j,-0.25,3),red); [/asy] Note the equation $\log(kx)=2\log(x+2)$ is valid for $kx>0$ and $x>-2$ . $\log(kx)=2\log(x+2)=\log((x+2)^2)$ . The equation $kx=(x+2)^2$ is derived by taking away the outside logs from the previous equation. Because $(x+2)^2$ is always non-negative, $kx$ must also be non-negative; therefore this takes care of the $kx>0$ condition as long as $k\neq0$ , i.e. $k$ cannot be $0$ . Now, we graph both $(x+2)^2$ (the green graph) and $kx$ (the red graph for $k=-1,k=-2,k=-3,k=8$ ) for $x>-2$ . It is easy to see that all negative values of $k$ make the equation $\log(kx)=2\log(x+2)$ have only one solution. However, there is also one positive value of $k$ that makes the equation only have one solution, as shown by the steepest line in the diagram. We can show that the slope of this line is a positive integer by setting the discriminant of the equation $(x+2)^2=kx$ to be $0$ and solving for $k$ . Therefore, there are $500$ negative solutions and $1$ positive solution, for a total of $\boxed{501}$ .

## Solution 2
We use an algebraic approach. Since $\log(kx)=2\log(x+2)$ , then $kx = (x+2)^2$ (the converse isn't necessarily true!), or $x^2+(4-k)x+4=0$ . Our original equation has exactly one solution if and only if there is only one solution to the above equation, or one of the solutions is extraneous; it involves the computation of the log of a nonpositive number.
For the first case, this can only occur when it is a perfect square trinomial, or $k = 0, 8$ . However, $k = 0$ results in $\log(0)$ on the left side, which is invalid. $k = 8$ yields $x = 2$ , so that is one solution.
For the second case, we can use the quadratic formula. We have \[x = \frac{k-4 \pm \sqrt{k^2-8k}}2,\] so for there to be at least one real solution, the discriminant must be nonnegative, or $k < 0$ or $k > 8$ .
Note that if $k > 8$ , then both solutions to $x$ will be positive, and therefore both valid, which means all such $k$ are unsatisfactory.
We now wish to show that if $k < 0$ , then exactly one solution works. Note that whenever $k < 0$ , both "solutions" in $x$ are negative. One of the solutions to the equation is $x = \frac{k-4 + \sqrt{k^2-8k}}2$ . We wish to prove that $x + 2 > 0$ , or $x > -2$ (therefore the RHS in the original equation will be defined). Substituting, we have $\frac{k-4 + \sqrt{k^2-8k}}2 > -2$ , or $\sqrt{k^2 - 8k} > -k$ . Since both sides are positive, we can square both sides (if $k < 0$ , then $-k > 0$ ) to get $k^2-8k > k^2$ , or $8k < 0 \implies k < 0$ , which was our original assumption, so this solution satisfies the original equation. The other case is when $x = \frac{k-4 - \sqrt{k^2-8k}}2$ , which we wish to show is less that $-2$ , or $\frac{k-4 - \sqrt{k^2-8k}}2 < -2 \implies k < \sqrt{k^2-8k}$ . However, since the square root is defined to be positive, then this is always true, which implies that whenever $k < 0$ , there is exactly one real solution that satisfies the original equation. Combining this with $k \in [-500, 500]$ , we find that the answer is $500 + 1 = \boxed{501}$ .
### Note
The key to this solution is understanding that $\log(x+2)$ has a domain of $(-2, \infty),$ so in the second case, when there are two possible solutions of $x$ to $k<0,$ we notice that only the interval of the greater solution $(0,-2)$ works, which means that for any $k<0$ will have exactly one solution.
~mathboy282

## Reworded Solution 2
Immediately we notice if $k$ is non-zero we must have $kx, (x+2) > 0$ for our sole solution $x = x_0$ . Simplifying the logarithmic equation we get $kx = (x+2)^2 \rightarrow 0 = x^2 + (4-k)x + 4 \rightarrow x = \frac{k-4 \pm \sqrt{k^2 - 8k}}{2}$ . Then $k \leq 0$ or $k \geq 8$ . When $k = 8$ we have exactly one real solution (easily verifiable). Notice when $k > 8$ , both solutions to $x$ are positive, and so all such $k$ is not satisfactory. When $k < 0$ it can be shown that the greater solution to $x$ is in the interval $(0,-2)$ and the lesser solution is in the interval $(-2,-\infty)$ which is satisfactory. Then $k = 8,-1,-2,...,-500 \rightarrow \boxed{501}$ satisfactory integer values of $k$ .
~FRIDAY
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .