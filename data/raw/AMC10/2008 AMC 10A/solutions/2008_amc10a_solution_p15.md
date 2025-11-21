# 2008 AMC 10A Problem 15

## Problem

Yesterday Han drove 1 hour longer than Ian at an average speed 5 miles per hour faster than Ian. Jan drove 2 hours longer than Ian at an average speed 10 miles per hour faster than Ian. Han drove 70 miles more than Ian. How many more miles did Jan drive than Ian?

$\mathrm{(A)}\ 120\qquad\mathrm{(B)}\ 130\qquad\mathrm{(C)}\ 140\qquad\mathrm{(D)}\ 150\qquad\mathrm{(E)}\ 160$

## Solution 1
Set the time Ian traveled as $I$ , and set Han's speed as $H$ . Therefore, Jan's speed is $H+5.$
We get the following equation for how much Han is ahead of Ian: $H+5I = 70.$
The expression for how much Jan is ahead of Ian is: $2(H+5)+10I.$
This simplifies to: $2H+10+10I.$
However, this is just $2(H+5I)+10.$
Substitute, from the first equation, $H+5I$ as $70.$
Therefore, the answer is $140 + 10$ , which is $150$ , or $\boxed{\mathrm{(D)}}$

## Solution 2
We let Ian's speed and time equal $I_s$ and $I_t$ , respectively. Similarly, let Han's and Jan's speed and time be $H_s$ , $H_t$ , $J_s$ , $J_t$ . The problem gives us 5 equations :
\begin{align} H_s&=I_s+5 \\ H_t&=I_t+1 \\ J_s&=I_s+10 \\ J_t&=I_t+2 \\ H_s \cdot H_t & =I_s \cdot I_t+70 \end{align}
Substituting equations $(1)$ and $(2)$ into $(5)$ gives:
\[(I_s+5)(I_t+1)=I_s I_t+70 \Longrightarrow I_s I_t+I_s+5I_t+5=I_s I_t+70 \Longrightarrow I_s+5I_t=65 \quad (*)\]
We are asked the difference between Jan's and Ian's distances, or
\[J_s J_t-I_s I_t=x,\]
Where $x$ is the difference between Jan's and Ian's distances and the answer to the problem. Substituting $(3)$ and $(4)$ equations into this equation gives:
\[(I_s+10)(I_t+2)-I_s I_t=x \Longrightarrow I_s I_t+2I_s+10I_t+20-I_s I_t=x \Longrightarrow\]
\[2I_s+10I_t+20=x \Longrightarrow 2(I_s+5I_t)+20=x\]
Substituting $(*)$ into this equation gives:
\[2(65)+20=x \Longrightarrow 130+20=x \Longrightarrow 150=x\]
Therefore, the answer is $150$ miles or $\boxed{\mathrm{(D)}}$ .

## Solution 3
Let Ian drive $D$ miles, at a speed of $R$ , for some time $T$ (in hours). Hence, we have $D=RT$ . We can find a similar equation for Han, who drove $D + 70$ miles, at a rate of $R+5$ , for $T+1$ hours, giving us $D + 70 = (R + 5)(T + 1)$ . We can do the same for Jan, giving us $D + x = (R + 10)(T + 2)$ , where $x$ is how much further Jan traveled than Ian. We now have three equations: \[D= RT\] \[D + 70 = (R+5)(T+1) = RT + R + 5T + 5\] \[D + x = (R + 10)(T + 2) = RT + 10 T + 2R + 20.\] Substituting $RT$ for $D$ in the second and third equations and cancelling gives us: \[70 = 5T + R + 5 \Longrightarrow 5T + R = 65\] \[x = 10T + 2R + 20 \Longrightarrow x = 2(5T + R ) + 20 \Longrightarrow x= 2(65) + 20 = 150.\] Since $x = 150$ , our answer is $\boxed{\mathrm{(D)}}$ .

## Solution 4
Let Ian drive $d$ miles, $t$ hours, and at speed $s$ .
Ian's Equation: $d=s \cdot t.$
Han drove 70 more miles, traveled 5 miles per hour faster and traveled 1 more hour than Ian.
Han's Equation: $d+70=(s+5) \cdot (t+1).$
Let Jan have driven $m$ miles. Jan also has driven 10 miles per hour faster and traveled 2 more hours than Ian.
Jan's Equation: $m=(s+10) \cdot (t+2).$
Let's group the equations together:
$(1) \phantom{a} d=s \cdot t$
$(2) \phantom{a} d+70=(s+5) \cdot (t+1)$
$(3) \phantom{a} m=(s+10) \cdot (t+2)$
Let's see what we want to find: We want to find $n$ . The equation is $m=d+n$ where $n$ is the number of more miles traveled by Jan than Ian.
Onto the calculating part.
Expanding the second equation, we get
$d+70=st+5t+s+5.$
Note that $st=d$ by the first equation, so substituting we get
$d+70=d+5t+s+5.$
Simplifying gets us
$(4) \phantom{a} s+5t=65.$
(Note for the above process: You could have substituted $d$ with $st$ but that would lead you to the same result since $d-d=st-st=0.$ )
Let's look at the third equation. Expanding, we get
$m=st+10t+2s+20.$
Since we want $n$ we want the equation $m=d+n$ . We write the expanded third equation into this form since $st=d.$
$(5) \phantom{a} m=d+(10t+2s+20)$ .
Let's take a closer look at the $n$ section of the equation:
$(6) \phantom{a} n=10t+2s+20$
This looks very similar to equation 4, if you multiply equation 4 by $2$ you get
$(7) \phantom{a} 10t+2s=130$ .
Plugging equation 7 into equation 6 we have
$n=(10t+2s)+20 \Rightarrow n=130+20$
Calculating gets us
$(8) \phantom{a} n=150.$
Substituting equation 8 into equation 5 gets us
$m=d+n \Rightarrow m=d+150.$
The $n$ term is $150$ which is what we want to find so the answer is $\boxed{\mathrm{(D) 150}}.$
~mathboy282

## Solution 5 (quick solution)
Since Han drove for $1$ hour and drove $70$ miles more than Ian during that hour, we know that Ian's speed is $65$ miles per hour since Han drove $5$ mph faster than him. Now Jan went $10$ mph faster than Ian for $2$ hours, so we can tell that she drove $75 \cdot 2$ miles more than Ian, therefore the answer is $\boxed{\mathrm{(D) 150}}.$
~Dynosol
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .