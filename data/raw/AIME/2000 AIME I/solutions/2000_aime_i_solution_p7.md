# 2000 AIME I Problem 7

## Problem

Suppose that $x,$ $y,$ and $z$ are three positive numbers that satisfy the equations $xyz = 1,$ $x + \frac {1}{z} = 5,$ and $y + \frac {1}{x} = 29.$ Then $z + \frac {1}{y} = \frac {m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
We can rewrite $xyz=1$ as $\frac{1}{z}=xy$ .
Substituting into one of the given equations, we have \[x+xy=5\] \[x(1+y)=5\] \[\frac{1}{x}=\frac{1+y}{5}.\]
We can substitute back into $y+\frac{1}{x}=29$ to obtain \[y+\frac{1+y}{5}=29\] \[5y+1+y=145\] \[y=24.\]
We can then substitute once again to get \[x=\frac15\] \[z=\frac{5}{24}.\] Thus, $z+\frac1y=\frac{5}{24}+\frac{1}{24}=\frac{1}{4}$ , so $m+n=\boxed{005}$ .

## Solution 2
Let $r = \frac{m}{n} = z + \frac {1}{y}$ .
\begin{align*} (5)(29)(r)&=\left(x + \frac {1}{z}\right)\left(y + \frac {1}{x}\right)\left(z + \frac {1}{y}\right)\\ &=xyz + \frac{xy}{y} + \frac{xz}{x} + \frac{yz}{z} + \frac{x}{xy} + \frac{y}{yz} + \frac{z}{xz} + \frac{1}{xyz}\\ &=1 + x + z + y + \frac{1}{y} + \frac{1}{z} + \frac{1}{x} + \frac{1}{1}\\ &=2 + \left(x + \frac {1}{z}\right) + \left(y + \frac {1}{x}\right) + \left(z + \frac {1}{y}\right)\\ &=2 + 5 + 29 + r\\ &=36 + r \end{align*}
Thus $145r = 36+r \Rightarrow 144r = 36 \Rightarrow r = \frac{36}{144} = \frac{1}{4}$ . So $m + n = 1 + 4 = \boxed{5}$ .

## Solution 3
Since $x+(1/z)=5, 1=z(5-x)=xyz$ , so $5-x=xy$ . Also, $y=29-(1/x)$ by the second equation. Substitution gives $x=1/5$ , $y=24$ , and $z=5/24$ , so the answer is 4+1 which is equal to $5$ .

## Solution 4
(Hybrid between 1/2)
Because $xyz = 1, \hspace{0.15cm} \frac{1}{x} = yz, \hspace{0.15cm} \frac{1}{y} = xz,$ and $\hspace{0.05cm}\frac{1}{z} = xy$ . Substituting and factoring, we get $x(y+1) = 5$ , $\hspace{0.15cm}y(z+1) = 29$ , and $\hspace{0.05cm}z(x+1) = k$ . Multiplying them all together, we get, $xyz(x+1)(y+1)(z+1) = 145k$ , but $xyz$ is $1$ , and by the Identity property of multiplication, we can take it out. So, in the end, we get $(x+1)(y+1)(z+1) = 145k$ . And, we can expand this to get $xyz+xy+yz+xz+x+y+z+1 = 145k$ , and if we make a substitution for $xyz$ , and rearrange the terms, we get $xy+yz+xz+x+y+z = 145k-2$ This will be important.
Now, lets add the 3 equations $x(y+1) = 5, \hspace{0.15cm}y(z+1) = 29$ , and $\hspace{0.05cm}z(x+1) = k$ . We use the expand the Left hand sides, then, we add the equations to get $xy+yz+xz+x+y+z = k+34$ Notice that the LHS of this equation matches the LHS equation that I said was important. So, the RHS of both equations are equal, and thus $145k-2 = k+34$ We move all constant terms to the right, and all linear terms to the left, to get $144k = 36$ , so $k = \frac{1}{4}$ which gives an answer of $1+4 = \boxed{005}$
-AlexLikeMath

## Solution 5
Get rid of the denominators in the second and third equations to get $xz-5z=-1$ and $xy-29x=-1$ . Then, since $xyz=1$ , we have $\tfrac 1y-5z=-1$ and $\tfrac 1z-29x=-1$ . Then, since we know that $\tfrac 1z+x=5$ , we can subtract these two equations to get that $30x=6\implies x=5$ . The result follows that $z=\tfrac 5{24}$ and $y=24$ , so $z+\tfrac 1y=\tfrac 1{24}+\tfrac 5{24}=\tfrac 14$ , and the requested answer is $1+4=\boxed{005}.$

## Solution 6
Rewrite the equations in terms of x.
$x+\frac{1}{z}=5$ becomes $z=\frac{1}{x+5}$ .
$y+\frac{1}{x}=29$ becomes $y=29-\frac{1}{x}$
Now express $xyz=1$ in terms of x.
$\frac{1}{5-x}\cdot(29-\frac{1}{x})\cdot x=1$ .
This evaluates to $29x-1=5-x$ , giving us $x=\frac{1}{5}$ . We can now plug x into the other equations to get $y=24$ and $z=\frac{5}{24}$ .
Therefore, $z+\frac{1}{y}=\frac{5}{24}+\frac{1}{24}=\frac{6}{24}=\frac{1}{4}$ .
$1+4=\boxed{5}$ , and we are done. ~MC413551

## Solution 7
First, we have been given the value of $xyz$ , so we should probably figure out a way to use that. Before that, we replace $\dfrac{m}{n}$ , because why deal with $2$ variables when you don't have to. We multiply these $3$ equations to get: \[(x+\dfrac{1}{z})(y+\dfrac{1}{x})(z+\dfrac{1}{y}) \Longrightarrow xyz+x+y+z+\dfrac{1}{x}+\dfrac{1}{y}+\dfrac{1}{z} = 145a\] . Plugging the value in for $xyz$ , we get: \[2+x+y+z+\dfrac{1}{x}+\dfrac{1}{y}+\dfrac{1}{z}\] . Now, we need a way to get these other random terms out of there. We add the three equations to get \[x+y+z+\dfrac{1}{x}+\dfrac{1}{y}+\dfrac{1}{z} = 34+a\] . Plugging this back into the equation we found we get: \[36+a = 145a \Longrightarrow a = \dfrac{1}{4} \Longrightarrow \boxed{005}\]
-jb2015007
Erm, this is very similar to 2000 AMC 12 Q20 ackthually
These problems are copyrighted © by the Mathematical Association of America.