# 2016 AIME I Problem 11

## Problem

Let $P(x)$ be a nonzero polynomial such that $(x-1)P(x+1)=(x+2)P(x)$ for every real $x$ , and $\left(P(2)\right)^2 = P(3)$ . Then $P(\tfrac72)=\tfrac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
Plug in $x=1$ to get $(1-1)P(1+1) = 0 = (1+2)P(1) \Rightarrow P(1) = 0$ . Plug in $x=0$ to get $(0-1)P(0+1) = (0+2)P(0)\Rightarrow P(0) = -\frac{1}{2}P(1) = 0$ . Plug in $x=-1$ to get $(-1-1)P(-1+1) = (-1+2)P(-1)\Rightarrow (-2)P(0)=P(-1)\Rightarrow P(-1) = 0$ . So $P(x) = x(x-1)(x+1)Q(x)$ for some polynomial $Q(x)$ . Using the initial equation, once again, \[(x-1)P(x+1) = (x+2)P(x)\] \[(x-1)((x+1)(x+1-1)(x+1+1)Q(x+1)) = (x+2)((x)(x-1)(x+1)Q(x))\] \[(x-1)(x+1)(x)(x+2)Q(x+1) = (x+2)(x)(x-1)(x+1)Q(x)\] \[Q(x+1) = Q(x)\] From here, we know that $Q(x) = C$ for a constant $C$ ( $Q(x)$ cannot be periodic since it is a polynomial), so $P(x) = Cx(x-1)(x+1)$ . We know that $\left(P(2)\right)^2 = P(3)$ . Plugging those into our definition of $P(x)$ : $(C \cdot 2 \cdot (2-1) \cdot (2+1))^2 = C \cdot 3 \cdot (3-1) \cdot (3+1) \Rightarrow (6C)^2 = 24C \Rightarrow 36C^2 - 24C = 0 \Rightarrow C = 0$ or $\frac{2}{3}$ . So we know that $P(x) = \frac{2}{3}x(x-1)(x+1)$ . So $P(\frac{7}{2}) = \frac{2}{3} \cdot \frac{7}{2} \cdot (\frac{7}{2} - 1) \cdot (\frac{7}{2} + 1) = \frac{105}{4}$ . Thus, the answer is $105 + 4 = \boxed{109}$ .

## Solution 2
From the equation we see that $x-1$ divides $P(x)$ and $(x+2)$ divides $P(x+1)$ so we can conclude that $x-1$ and $x+1$ divide $P(x)$ (if we shift the function right by 1, we get $(x-2)P(x) = (x+1)P(x-1)$ , and from here we can see that $x+1$ divides $P(x)$ ). This means that $1$ and $-1$ are roots of $P(x)$ . Plug in $x = 0$ and we see that $P(0) = 0$ so $0$ is also a root.
Suppose we had another root that is not one of those $3$ . Notice that the equation above indicates that if $r$ is a root then $r+1$ and $r-1$ is also a root. Then we'd get an infinite amount of roots! So that is bad. So we cannot have any other roots besides those three.
That means $P(x) = cx(x-1)(x+1)$ . We can use $P(2)^2 = P(3)$ to get $c = \frac{2}{3}$ . Plugging in $\frac{7}{2}$ is now trivial and we see that it is $\frac{105}{4}$ so our answer is $\boxed{109}$

## Solution 3
Although this may not be the most mathematically rigorous answer, we see that $\frac{P(x+1)}{P(x)}=\frac{x+2}{x-1}$ . Using a bit of logic, we can make a guess that $P(x+1)$ has a factor of $x+2$ , telling us $P(x)$ has a factor of $x+1$ . Similarly, we guess that $P(x)$ has a factor of $x-1$ , which means $P(x+1)$ has a factor of $x$ . Now, since $P(x)$ and $P(x+1)$ have so many factors that are off by one, we may surmise that when you plug $x+1$ into $P(x)$ , the factors "shift over," i.e. $P(x)=(A)(A+1)(A+2)...(A+n)$ , which goes to $P(x+1)=(A+1)(A+2)(A+3)...(A+n+1)$ . This is useful because these, when divided, result in $\frac{P(x+1)}{P(x)}=\frac{A+n+1}{A}$ . If $\frac{A+n+1}{A}=\frac{x+2}{x-1}$ , then we get $A=x-1$ and $A+n+1=x+2$ , $n=2$ . This gives us $P(x)=(x-1)x(x+1)$ and $P(x+1)=x(x+1)(x+2)$ , and at this point we realize that there has to be some constant $a$ multiplied in front of the factors, which won't affect our fraction $\frac{P(x+1)}{P(x)}=\frac{x+2}{x-1}$ but will give us the correct values of $P(2)$ and $P(3)$ . Thus $P(x)=a(x-1)x(x+1)$ , and we utilize $P(2)^2=P(3)$ to find $a=\frac{2}{3}$ . Evaluating $P \left ( \frac{7}{2} \right )$ is then easy, and we see it equals $\frac{105}{4}$ , so the answer is $\boxed{109}$

## Solution 4
Substituting $x=2$ into the given equation, we find that $P(3)=4P(2)=P(2)^2$ . Therefore, either $P(2)=0$ or $P(2)=4$ . Now for integers $n\ge 2$ , we know that \[P(n+1)=\frac{n+2}{n-1}P(n).\] Applying this repeatedly, we find that \[P(n+1)=\frac{(n+2)!/3!}{(n-1)!}P(2).\] If $P(2)=0$ , this shows that $P(x)$ has infinitely many roots, meaning that $P(x)$ is identically equal to zero. But this contradicts the problem statement. Therefore, $P(2)=4$ , and we find $P(n+1)=\frac{2}{3}(n+2)(n+1)n$ for all positive integers $n\ge2$ . This cubic polynomial matches the values $P(n+1)$ for infinitely many numbers, hence the two polynomials are identically equal. In particular, $P\left(\frac72\right)=\frac23\cdot\frac92\cdot\frac72\cdot\frac52=\frac{105}{4}$ , and the answer is $\boxed{109}$ .

## Solution 5
We can find zeroes of the polynomial by making the first given equation $0 = 0$ . Plugging in $x = 1$ and $x = -2$ gives us the zeroes $1$ and $-1$ , respectively. Now we can plug in these zeros to get more zeroes. $x = -1$ gives us the zero $0$ (no pun intended). $x = 1$ makes the equation $0 \cdot P(2) = 0$ , which means $P(2)$ is not necessarily $0$ . If $P(2) = 0$ , then plugging in $2$ to the equation yields $P(3) = 0$ , plugging in $3$ to the equation yields $P(4) = 0$ , and so on, a contradiction of "nonzero polynomial". So $2$ is not a zero. Note that plugging in $x = 0$ to the equation does not yield any additional zeros. Thus, the only zeroes of $P(x)$ are $-1, 0,$ and $1$ , so $P(x) = a(x + 1)x(x - 1)$ for some nonzero constant $a$ . We can plug in $2$ and $3$ into the polynomial and use the second given equation to find an equation for $a$ . $P(2) = 6a$ and $P(3) = 24a$ , so: \[(6a)^2 = 24a \implies 36a^2 = 24a \implies a = \frac23\] Plugging in $\frac72$ into the polynomial $\frac23(x + 1)x(x - 1)$ yields $\frac{105}{4}$ . $105 + 4 = \boxed{109}$ .

## Solution 6
Plug in $x=2$ yields $P(3)=4P(2)$ . Since also $(P(2))^2=P(3)$ , we have $P(2)=4$ and $P(3)=16$ . Plug in $x=3$ yields $2P(4)=5P(3)$ so $P(4)=40$ .
Repeat the action gives $P(2)=4$ , $P(3)=16$ , $P(4)=40$ , $P(5)=80$ , and $P(6)=140$ .
Since $P(x)$ is a polynomial, the $k$ th difference is constant, where $k=\deg(P(x))$ . Thus we can list out the 0th, 1st, 2nd, 3rd, ... differences until we obtain a constant.
\[4,16,40,80,140\] \[12,24,40,60\] \[12,16,20\] \[4,4,4\]
Since the 3rd difference of $P(x)$ is constant, we can conclude that $\deg(P(x))=3$ .
Let $P(x)=a_3x^3+a_2x^2+a_1x+a_0$ . Plug in the values for $x$ and solve the system of 4 equations gives $(a_3,a_2,a_1,a_0)=(\frac{2}{3},0,-\frac{2}{3},0)$
Thus $P(x)=\frac{2}{3}x^3-\frac{2}{3}x$ and $P(\frac{7}{2})=\frac{105}{4}\Longrightarrow m+n=\boxed{109}$
~ Nafer
-Note that the coefficient of $x^3$ is $\frac{2}{3}$ because $\frac{2}{3}\cdot\deg(x^3)!=\frac{2}{3}\cdot3!=4$ , the 3rd difference of P(x). ~inaccessibles
### Note(Key Idea)
Their are a couple of solution methods such as constant $n$ th differences and using intuition on the roots. But the main idea in this problem was the fact that, $P(\frac{7}{2})$ is hard to get by itself, cause we can only find the output for integral input values from the information we have.
Thus, we can solve for $P(x)$ , and this is best approached by finding its roots.
~Bigbrain_2009
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .