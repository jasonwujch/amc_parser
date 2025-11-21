# 2021 AIME II Problem 7

## Problem

Let $a, b, c,$ and $d$ be real numbers that satisfy the system of equations \begin{align*} a + b &= -3, \\ ab + bc + ca &= -4, \\ abc + bcd + cda + dab &= 14, \\ abcd &= 30. \end{align*} There exist relatively prime positive integers $m$ and $n$ such that \[a^2 + b^2 + c^2 + d^2 = \frac{m}{n}.\] Find $m + n$ .

## Solution 1
From the fourth equation we get $d=\frac{30}{abc}.$ Substitute this into the third equation and you get $abc + \frac{30(ab + bc + ca)}{abc} = abc - \frac{120}{abc} = 14$ . Hence $(abc)^2 - 14(abc)-120 = 0$ . Solving, we get $abc = -6$ or $abc = 20$ . From the first and second equation, we get $ab + bc + ca = ab-3c = -4 \Longrightarrow ab = 3c-4$ . If $abc=-6$ , substituting we get $c(3c-4)=-6$ . If you try solving this you see that this does not have real solutions in $c$ , so $abc$ must be $20$ . So $d=\frac{3}{2}$ . Since $c(3c-4)=20$ , $c=-2$ or $c=\frac{10}{3}$ . If $c=\frac{10}{3}$ , then the system $a+b=-3$ and $ab = 6$ does not give you real solutions. So $c=-2$ . Since you already know $d=\frac{3}{2}$ and $c=-2$ , so you can solve for $a$ and $b$ pretty easily and see that $a^{2}+b^{2}+c^{2}+d^{2}=\frac{141}{4}$ . So the answer is $\boxed{145}$ .
~math31415926535 ~minor edit by Mathkiddie

## Solution 2
Note that $ab + bc + ca = -4$ can be rewritten as $ab + c(a+b) = -4$ . Hence, $ab = 3c - 4$ .
Rewriting $abc+bcd+cda+dab = 14$ , we get $ab(c+d) + cd(a+b) = 14$ . Substitute $ab = 3c - 4$ and solving, we get \[3c^{2} - 4c - 4d - 14 = 0.\] We refer to this as Equation 1.
Note that $abcd = 30$ gives $(3c-4)cd = 30$ . So, $3c^{2}d - 4cd = 30$ , which implies $d(3c^{2} - 4c) = 30$ or \[3c^{2} - 4c = \frac{30}{d}.\] We refer to this as Equation 2.
Substituting Equation 2 into Equation 1 gives, $\frac{30}{d} - 4d - 14 = 0$ .
Solving this quadratic yields that $d \in \left\{-5, \frac{3}{2}\right\}$ .
Now we just try these two cases:
For $d = \frac{3}{2}$ substituting in Equation 1 gives a quadratic in $c$ which has roots $c \in \left\{\frac{10}{3}, -2\right\}$ .
Again trying cases, by letting $c = -2$ , we get $ab = 3c-4$ , Hence $ab = -10$ . We know that $a + b = -3$ , Solving these we get $a = -5, b = 2$ or $a= 2, b = -5$ (doesn't matter due to symmetry in $a,b$ ).
So, this case yields solutions $(a,b,c,d) = \left(-5, 2 , -2, \frac{3}{2}\right)$ .
Similarly trying other three cases, we get no more solutions, Hence this is the solution for $(a,b,c,d)$ .
Finally, $a^{2} + b^{2} + c^{2} + d^{2} = 25 + 4 + 4 + \frac{9}{4} = \frac{141}{4} = \frac{m}{n}$ .
Therefore, $m + n = 141 + 4 = \boxed{145}$ .
~Arnav Nigam

## Solution 3
For simplicity purposes, we number the given equations $(1),(2),(3),$ and $(4),$ in that order.
Rearranging $(2)$ and solving for $c,$ we have \begin{align*} ab+(a+b)c&=-4 \\ ab-3c&=-4 \\ c&=\frac{ab+4}{3}. \hspace{14mm} (5) \end{align*} Substituting $(5)$ into $(4)$ and solving for $d,$ we get \begin{align*} ab\left(\frac{ab+4}{3}\right)d&=30 \\ d&=\frac{90}{ab(ab+4)}. \hspace{5mm} (6) \end{align*} Substituting $(5)$ and $(6)$ into $(3)$ and simplifying, we rewrite the left side of $(3)$ in terms of $a$ and $b$ only: \begin{align*} ab\left[\frac{ab+4}{3}\right] + b\left[\frac{ab+4}{3}\right]\left[\frac{90}{ab(ab+4)}\right] + \left[\frac{ab+4}{3}\right]\left[\frac{90}{ab(ab+4)}\right]a + \left[\frac{90}{ab(ab+4)}\right]ab &= 14 \\ ab\left[\frac{ab+4}{3}\right] + \underbrace{\frac{30}{a} + \frac{30}{b}}_{\text{Group them.}} + \frac{90}{ab+4} &= 14 \\ ab\left[\frac{ab+4}{3}\right] + \frac{30(a+b)}{ab} + \frac{90}{ab+4} &= 14 \\ ab\left[\frac{ab+4}{3}\right] + \underbrace{\frac{-90}{ab} + \frac{90}{ab+4}}_{\text{Group them.}} &= 14 \\ ab\left[\frac{ab+4}{3}\right] - \frac{360}{ab(ab+4)}&=14. \end{align*} Let $t=ab(ab+4),$ from which \[\frac{t}{3}-\frac{360}{t}=14.\] Multiplying both sides by $3t,$ rearranging, and factoring give $(t+18)(t-60)=0.$ Substituting back and completing the squares produce \begin{align*} \left[ab(ab+4)+18\right]\left[ab(ab+4)-60\right]&=0 \\ \left[(ab)^2+4ab+18\right]\left[(ab)^2+4ab-60\right]&=0 \\ \underbrace{\left[(ab+2)^2+14\right]}_{ab+2=\pm\sqrt{14}i\implies ab\not\in\mathbb R}\underbrace{\left[(ab+2)^2-64\right]}_{ab+2=\pm8}&=0 \\ ab&=6,-10. \end{align*} If $ab=6,$ then combining this with $(1),$ we know that $a$ and $b$ are the solutions of the quadratic $x^2+3x+6=0.$ Since the discriminant is negative, neither $a$ nor $b$ is a real number.
If $ab=-10,$ then combining this with $(1),$ we know that $a$ and $b$ are the solutions of the quadratic $x^2+3x-10=0,$ or $(x+5)(x-2)=0,$ from which $\{a,b\}=\{-5,2\}.$ Substituting $ab=-10$ into $(5)$ and $(6),$ we obtain $c=-2$ and $d=\frac32,$ respectively. Together, we have \[a^2+b^2+c^2+d^2=\frac{141}{4},\] so the answer is $141+4=\boxed{145}.$
~MRENTHUSIASM

## Solution 4 (Way Too Long)
Let the four equations from top to bottom be listed 1 through 4 respectively. We factor equation 3 like so: \[abc+d(ab+bc+ca)=14\] Then we plug in equation 2 to receive $abc-4d=14$ . By equation 4 we get $abc=\frac{30}{d}$ . Plugging in, we get $\frac{30}{d}-4d=14$ . Multiply by $d$ on both sides to get the quadratic equation $4d^2+14d-30=0$ . Solving using the quadratic equation, we receive $d=\frac{3}{2},d=-5$ . So, we have to test which one is correct. We repeat a similar process as we did above for equations 1 and 2. We factor equation 2 to get \[ab+c(a+b)=-4\] After plugging in equation 1, we get $ab-3c=-4$ . Now we convert it into a quadratic to receive $3c^2-4c-abc=0$ . The value of $abc$ will depend on $d$ . So we obtain the discriminant $16+12abc$ . Let $d = -5$ . Then $abc = \frac{30}{-5}$ , so $abc=-6$ , discriminant is $16-72$ , which makes this a dead end. Thus $d=\frac{3}{2}$ For $d=\frac{3}{2}$ , making $abc=20$ . This means the discriminant is just $256$ , so we obtain two values for $c$ as well. We get either $c=\frac{10}{3}$ or $c=-2$ . So, we must AGAIN test which one is correct. We know $ab=3c-4$ , and $a+b=-3$ , so we use these values for testing. Let $c=\frac{10}{3}$ . Then $ab=6$ , so $a=\frac{6}{b}$ . We thus get $\frac{6}{b}+b=-3$ , which leads to the quadratic $b^2+3b+6$ . The discriminant for this is $9-24$ . That means this value of $c$ is wrong, so $c=-2$ . Thus we get polynomial $b^2+3b-10$ . The discriminant this time is $49$ , so we get two values for $b$ . Through simple inspection, you may see they are interchangeable, as if you take the value $b=2$ , you get $a=-5$ . If you take the value $b=-5$ , you get $a=2$ . So it doesn't matter. That means the sum of all their squares is \[\frac{9}{4}+4+4+25=\frac{141}{4},\] so the answer is $141+4=\boxed{145}.$
~amcrunner

## Solution 5
Let the four equations from top to bottom be listed $(1)$ through $(4)$ respectively. Multiplying both sides of $(3)$ by $d$ and factoring some terms gives us $abcd + d^2(ab + ac + bc) = 14d$ . Substituting using equations $(4)$ and $(2)$ gives us $30 -4 d^2 = 14d$ , and solving gives us $d = -5$ or $d = \frac{3}{2}$ . Plugging this back into $(3)$ gives us $abc + d(ab + ac + bc) = abc + (-5)(-4) = abc + 20 = 14$ , or using the other solution for $d$ gives us $abc - 6 = 14$ . Solving both of these equations gives us $abc = -6$ when $d = -5$ and $abc = 20$ when $d = \frac{3}{2}$ .
Multiplying both sides of $(2)$ by $c$ and factoring some terms gives us $abc + c^2 (a + b) = abc -3c^2 = -4c$ . Testing $abc = -6$ will give us an imaginary solution for $c$ , so therefore $abc = 20$ and $d = \frac{3}{2}$ . This gets us $20 - 3c^2 = -4c$ . Solving for $c$ gives us $c = \frac{3}{10}$ or $c = -2$ . With a bit of testing, we can see that the correct value of $c$ is $c=-2$ . Now we know $a+b = -3$ and $ab + bc + ca = ab + c(a+b) = ab + 6 = -4$ , $ab = -10$ , and it is obvious that $a = -5$ and $b = 2$ or the other way around, and therefore, $a^2 + b^2 + c^2 + d^2 = 25 + 4 + 4 + \frac{9}{4} = \frac{141}{4}$ , giving us the answer $141 + 4 = \boxed{145}$ .
~hihitherethere minor edit by ~Gustyrustypro

## Video Solution
https://www.youtube.com/watch?v=2rrX1G7iZqg

## Video Solution by Interstigation
https://youtu.be/fGgbCgIHRHM
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .