# 2015 AIME II Problem 14

## Problem

Let $x$ and $y$ be real numbers satisfying $x^4y^5+y^4x^5=810$ and $x^3y^6+y^3x^6=945$ . Evaluate $2x^3+(xy)^3+2y^3$ .

## Solution 1
The expression we want to find is $2(x^3+y^3) + x^3y^3$ .
Factor the given equations as $x^4y^4(x+y) = 810$ and $x^3y^3(x^3+y^3)=945$ , respectively. Dividing the latter by the former equation yields $\frac{x^2-xy+y^2}{xy} = \frac{945}{810}$ . Adding 3 to both sides and simplifying yields $\frac{(x+y)^2}{xy} = \frac{25}{6}$ . Solving for $x+y$ and substituting this expression into the first equation yields $\frac{5\sqrt{6}}{6}(xy)^{\frac{9}{2}} = 810$ . Solving for $xy$ , we find that $xy = 3\sqrt[3]{2}$ , so $x^3y^3 = 54$ . Substituting this into the second equation and solving for $x^3+y^3$ yields $x^3+y^3=\frac{35}{2}$ . So, the expression to evaluate is equal to $2 \times \frac{35}{2} + 54 = \boxed{089}$ .
Note that since the value we want to find is $2(x^3+y^3)+x^3y^3$ , we can convert $2(x^3+y^3)$ into an expression in terms of $x^3y^3$ , since from the second equation which is $x^3y^3(x^3+y^3)=945$ , we see that $2(x^3+y^3)=1890+x^6y^6,$ and thus the value is $\frac{1890+x^6y^6}{x^3y^3}.$ Since we've already found $x^3y^3,$ we substitute and find the answer to be 89.

## Solution 2
Factor the given equations as $x^4y^4(x+y) = 810$ and $x^3y^3(x+y)(x^2-xy+y^2)=945$ , respectively. By the first equation, $x+y=\frac{810}{x^4y^4}$ . Plugging this in to the second equation and simplifying yields $(\frac{x}{y}-1+\frac{y}{x})=\frac{7}{6}$ . Now substitute $\frac{x}{y}=a$ . Solving the quadratic in $a$ , we get $a=\frac{x}{y}=\frac{2}{3}$ or $\frac{3}{2}$ As both of the original equations were symmetric in $x$ and $y$ , WLOG, let $\frac{x}{y}=\frac{2}{3}$ , so $x=\frac{2}{3}y$ . Now plugging this in to either one of the equations, we get the solutions $y=\frac{3(2^{\frac{2}{3}})}{2}$ , $x=2^{\frac{2}{3}}$ . Now plugging into what we want, we get $8+54+27=\boxed{089}$

## Solution 3
Add three times the first equation to the second equation and factor to get $(xy)^3(x^3+3x^2y+3xy^2+y^3)=(xy)^3(x+y)^3=3375$ . Taking the cube root yields $xy(x+y)=15$ . Noting that the first equation is $(xy)^3\cdot(xy(x+y))=810$ , we find that $(xy)^3=\frac{810}{15}=54$ . Plugging this into the second equation and dividing yields $x^3+y^3 = \frac{945}{54} = \frac{35}{2}$ . Thus the sum required, as noted in Solution 1, is $54+\frac{35}{2}\cdot2 = \boxed{089}$ .

## Solution 4
As with the other solutions, factor. But this time, let $a=xy$ and $b=x+y$ . Then $a^4b=810$ . Notice that $x^3+y^3 = (x+y)(x^2-xy+y^2) = b(b^2-3a)$ , so we are looking for $2b(b^2-3a)+a^3$ . Now, if we divide the second equation by the first one, we get $7/6 = \frac{b^2-3a}{a}$ ; then $\frac{b^2}{a}=\frac{25}{6}$ . Therefore, $a = \frac{6}{25}b^2$ . Substituting $\frac{6}{25}b^2$ for $a$ in equation 1, simplifying, and then taking the cube root gives us $b^3 = \frac{5^3}{2}.$ Finding $a^3$ by cubing $a = \frac{6}{25}b^2$ on both sides and simplifying using our previous substitution, we get $a^3 = 54$ . Substituting this into the first equation and then dividing by $27$ , we get $2b(b^2 - 3a) = 35$ . Our final answer is $35+54=\boxed{089}$ .

## Solution 5
Factor the given equations as: \[x^4y^4(x+y)=810\] \[x^3y^3(x^3+y^3)=x^3y^3(x+y)(x^2-xy+y^2)=945\] We note that these expressions (as well as the desired expression) can be written exclusively in terms of $x+y$ and $xy$ . We make the substitution $s=x+y$ and $p=xy$ (for sum and product, respectively).
\[x^4y^4(x+y)=p^4s=810\] \[x^3y^3(x+y)(x^2-xy+y^2)=p^3(s)(s^2-3p)=s^3p^3-3p^4s=945\]
We see that $p^4s$ shows up in both equations, so we can eliminate it and find $sp$ , after which we can get $p^3$ from the first equation. If you rewrite the desired expression using $s$ and $p$ , it becomes clear that you don't need to actually find the values of $s$ and $p$ , but I will do so for the sake of completion.
\[s^3p^3=945+3p^4s\] \[s^3p^3=945+3(810)=3375\] \[sp=15\]
\[p^3=\frac{810}{sp}=54\] \[p=3\cdot2^{1/3}\] \[s=\frac{15}{p}=5\cdot2^{-1/3}\]
The desired expression can be written as: \[2(x^3+y^3)+(xy)^3=2(x+y)(x^2-xy+y^2)+(xy)^3\] \[2(s)(s^2-3p)+p^3=2s^3-6sp+p^3\]
Plugging in $s$ and $p$ , we get: \[2(5\cdot2^{-1/3})^3-6(15)+54=125-90+54=\boxed{089}\]
- gting

## Solution 6
Factor the first and second equations as $(xy)^4(x+y)=810$ and $(xy)^3(x+y)(x^2-xy+y^2)=945$ , respectively. Dividing them (allowed, since neither are $0$ ), we have \[\frac{xy}{x^2-xy+y^2}=\frac67\] or \[x^2-\frac{13}{6}xy+y^2=0.\] Plugging into the quadratic formula and solving for $x$ in terms of $y,$ we have \[x=\frac{\frac{13y}{6}\pm \sqrt{\frac{169y^2}{36}-4y^2}}{2}=\frac{2y}3 , \frac{3y}2 .\] WLOG, let $x=\frac{3y}2 .$ Plugging into our first equation, we have \[\left(\frac{3}{2}y\right)^4\left(\frac52 y\right)=810 \implies y^3 = 4 .\] Plugging this result (and the one for $x$ in terms of $y$ ) into our desired expression, we have
\begin{align*} 2x^3+(xy)^3+2y^3 &= \frac{27}{4}y^3 + \left(\frac{3}{2} y^2\right)^3 +2y^3 \\ &= \frac{35}{4}y^3 +\frac{27}{8}(y^3)^2 \\ &= 35+54 \\ &= \boxed{089} \end{align*} ~ASAB

## Solution 7
Take $w=x+y$ and $z=xy$ . Remark that \begin{align*} ~&2x^{3}+(xy)^{3}+2y^{3} \\ =~&2(x^{3}+y^{3})+(xy)^{3} \\ =~&2\left[(x+y)^{3}-3xy(x+y)\right]+(xy)^{3} \\ =~&2(w^{3}-3wz)+z^{3} \\ =~& 2w^{3}-6wz+z^{3}.\end{align*} The given equations imply that \[wz^{4}=810~~~\text{and}~~~(wz)^{3}-3wz^{4}=945.\] Substituting the first equation into the second, we have that $(wz)^{3}=945+3\cdot 810=3375$ , thus $wz=\sqrt[3]{3375}=15$ . Now \[z^{3}=\frac{wz^{4}}{wz}=\frac{810}{15}=54\] and \[w^{3}=\frac{3375}{54}=\frac{125}{2}.\] Thus \begin{align*}2w^{3}-6wz+z^{3}&=2\left(\frac{125}{2}\right)-6(15)+54 \\ &=125-90+54 \\ &=\boxed{89}.\end{align*}

## Solution 8
$x^4y^4(x+y)=810; x^3y^3(x^3+y^3)=945, \frac{x^2-xy+y^2}{xy}=\frac{7}{6}, \frac{x^2+y^2}{xy}=\frac{13}{6}$
Let $x^2+y^2=13k; xy=6k$ , then we can see $(x+y)^2-12k=13k, x+y=5\sqrt{k}$ , now, we see $x^4y^4\cdot (x+y)=1296k^4\cdot 5\sqrt{k}, k=\frac{1}{\sqrt[3]{4}}$ .
The rest is easy, $2(x^3+y^3)+x^3y^3=216k^3+2[(x+y)^3-3xy(x+y)]=216k^3+2\cdot 35k^{\frac{3}{2}}=\boxed{89}$
~bluesoul

## Solution 9
Let's first put the left hand sides of the equations in factored forms. Doing this we obtain $(xy)^4 \cdot (x + y) = 810$ and $(xy)(x + y)(x^2 - xy + y^2) = 945$ . Now, we will subtract and add the equations to gather information on $x$ and $y$ . When we subtract the equations and clean it up via factoring, we yield $(xy)^3 \cdot (x + y) \cdot (x - y)^2 = 115$ , and when we add them, we yield $(xy)^3 \cdot (x + y) \cdot (x^2 + y^2) = 1755$ . Now with some intuition, you should divide the equations to obtain $\frac{(x^2 + y^2)}{(x - y)^2} = 13$ . Now, we clean this up to obtain the following factoring of $0 = 2 \cdot (2x - 3y) \cdot (3x - 2y)$ . This implies that $x = \frac{3y}{2}$ . We plug that into the target expression to reduce it down to one variable, and get that target expression is $2x^3 + (xy)^3 + 2y^3 = \frac{27}{4} \cdot y^3 + \frac{27}{8} \cdot y^6 + 2y^3$ . This means that if we can find a way to get $y^3$ , then the rest is trivial. We get $y^3$ by plugging in $x = \frac{3y}{2}$ into $x^3 \cdot y^6 + y^3 \cdot x^6 = 945$ . However, this time we only factor as $(xy)^3 \cdot (x^3 + y^3)$ because we particularly want a cubic degree on $y$ . Plugging in $x = \frac{3y}{2}$ we get $y^3 = 4$ . Now lets plug this into our target expression to get $\frac{27}{4} \cdot 4 + \frac{27}{8} \cdot 4^2 + 2 \cdot 4 = \boxed{89}$ .
~triggod, $\LaTeX$ by MinecraftPlayer404

## Solution 10 (Newton sums)
Let $x, y$ be roots of some polynomial $P(\alpha)$ . Then we have that $P(\alpha) = (\alpha - x)(\alpha - y) \implies P(\alpha) = \alpha^2 - (x + y) \alpha + xy$ . Now from the first equation we have that $x + y = 810/(xy)^4$ . For convenience, denote $z = xy$ .
Define $P_k = x^k + y^k$ , where $x, y$ are roots of the above polynomial. Then we have that by Newton's formulas $P_k = (x + y)P_{k - 1} - xyP_{k - 2} = 810/z^4P_{k - 1} - zP_{k - 2}$ , where $P_0 = 2$ and $P_1 = x + y = 810/z^4$ . We desire $2P_3 + z^3$ . Now building up this recurrence;
\[P_2 = \frac{810}{z^4}P_1 - zP_0 = \frac{810^2}{z^8} - 2z.\] Then we have that \[P_3 = \frac{810}{z^4} \left(\frac{810^2}{z^8} - 3z \right).\] Plugging this value of $P_3$ into the second equation $z^3P_3 = 810$ , yields $z^9 = 164025$ . Now $z^3 = 54$ . To compute $P_3$ is now trivial, as returning this new value of $z$ into the second equation yields $P_3 = 35/2$ . Hence $z^3 + 2P_3 = 54 + 35 = \boxed{089}$ .
-th1nq3r

## Video Solution by mop 2024
https://youtu.be/7VHEGNRQKeI
~r00tsOfUnity
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .