# 2014 AIME I Problem 6

## Problem

The graphs $y=3(x-h)^2+j$ and $y=2(x-h)^2+k$ have y-intercepts of $2013$ and $2014$ , respectively, and each graph has two positive integer x-intercepts. Find $h$ .

## Solution 1
Begin by setting $x$ to 0, then set both equations to $h^2=\frac{2013-j}{3}$ and $h^2=\frac{2014-k}{2}$ , respectively. Notice that because the two parabolas have to have positive x-intercepts, $h\ge32$ .
We see that $h^2=\frac{2014-k}{2}$ , so we now need to find a positive integer $h$ which has positive integer x-intercepts for both equations.
Notice that if $k=2014-2h^2$ is -2 times a square number, then you have found a value of $h$ for which the second equation has positive x-intercepts. We guess and check $h=36$ to obtain $k=-578=-2(17^2)$ .
Following this, we check to make sure the first equation also has positive x-intercepts (which it does), so we can conclude the answer is $\boxed{036}$ .

## Solution 2
Let $x=0$ and $y=2013$ for the first equation, resulting in $j=2013-3h^2$ . Substituting back in to the original equation, we get $y=3(x-h)^2+2013-3h^2$ .
Now we set $y$ equal to zero, since there are two distinct positive integer roots. Rearranging, we get $2013=3h^2-3(x-h)^2$ , which simplifies to $671=h^2-(x-h)^2$ . Applying difference of squares, we get $671=(2h-x)(x)$ .
Now, we know that $x$ and $h$ are both integers, so we can use the fact that $671=61\times11$ , and set $2h-x=11$ and $x=61$ (note that letting $x=11$ gets the same result). Therefore, $h=\boxed{036}$ .
Note that we did not use the second equation since we took advantage of the fact that AIME answers must be integers. However, one can enter $h=36$ into the second equation to verify the validity of the answer.
Note on the previous note: we still must use the second equation since we could also use $671=671\times1$ , yielding $h=336.$ This answer however does not check out with the second equation which is why it is invalid.

## Solution 3
Similar to the first two solutions, we deduce that $\text{(-)}j$ and $\text{(-)}k$ are of the form $3a^2$ and $2b^2$ , respectively, because the roots are integers and so is the $y$ -intercept of both equations. So the $x$ -intercepts should be integers also.
The first parabola gives \[3h^2+j=3\left(h^2-a^2\right)=2013\] \[h^2-a^2=671\] And the second parabola gives \[2h^2+k=2\left(h^2-b^2\right)=2014\] \[h^2-b^2=1007\]
We know that $671=11\cdot 61$ and that $1007=19\cdot 53$ . It is just a fitting coincidence that the average of $11$ and $61$ is the same as the average of $19$ and $53$ . That is $\boxed{036}$ .
To check, we have \[(h-a)(h+a)=671=11\cdot 61\] \[(h-b)(h+b)=1007=19\cdot 53\] Those are the only two prime factors of $671$ and $1007$ , respectively. So we don't need any new factorizations for those numbers.
$h+a=61,h-a=11\implies (h,a)=\{36,25\}$
$h+b=53,h-b=19\implies (h,b)=\{36,17\}$
Thus the common integer value for $h$ is $\boxed{036}$ .
\[y=3(x-h)^2+j\rightarrow y=3(x-11)(x-61)=3x^2-216x+2013\] \[y=2(x-h)^2+k\rightarrow y=2(x-19)(x-53)=2x^2-144x+2014\]

## Solution 4
First, we expand both equations to get $y=3x^2-6hx+3h^2+j$ and $y=2x^2-4hx+2h^2+k$ . The $y$ -intercept for the first equation can be expressed as $3h^2+j$ . From this, the x-intercepts for the first equation can be written as
\[x=h \pm \sqrt{(-6h)^2-4*3(3h^2+j)}=h \pm \sqrt{36h^2-12(2013)}=h \pm \sqrt{36h^2-24156}\]
Since the $x$ -intercepts must be integers, $\sqrt{36h^2-24156}$ must also be an integer. From solution 1, we know $h$ must be greater than or equal to 32. We can substitute increasing integer values for $h$ starting from 32; we find that $h=36$ .
We can test this result using the second equation, whose $x$ -intercepts are \[x=h \pm \sqrt{(-4h)^2-4*2(2h^2+k)}=h \pm \sqrt{16h^2-8(2014)}=h \pm \sqrt{16h^2-16112}\] Substituting 36 in for $h$ , we get $h=36 \pm 68$ , which satisfies the requirement that all x-intercepts must be (positive) integers.
Thus, $h=\boxed{036}$ .

## Solution 5
We have the equation $y=3(x-h)^2 + j.$
We know: $(x,y):(0,2013)$ , so $h^2=2013/3 - j/3$ after plugging in the values and isolating $h^2$ . Therefore, $h^2=671-j/3$ .
Lets call the x-intercepts $x_1$ , $x_2$ . Since both $x_1$ and $x_2$ are positive there is a relationship between $x_1$ , $x_2$ and $h$ . Namely, $x_1+x_2=2h$ . The is because: $x_1-h=-(x_2-h)$ ,
Similarly, we know: $(x,y):(x_1,0)$ , so $j=-3(x_1-h)^2$ . Combining the two equations gives us \[h^2=671+(x_1-h)^2\] \[h^2=671+x_1^2-2x_1h+h^2\] \[h=(671+x_1^2)/2x_1.\]
Now since we have this relationship, $2h=x_1+x_2$ , we can just multiply the last equation by 2(so that we get $2h$ on the left side) which gives us \[2h=671/x_1+x_1^2/x^1\] \[2h=671/x_1+x_1\] \[x_1+x_2=671/x_1+x_1\] \[x_2=671/x_1\] \[x_1x_2=671.\] Prime factorization of 671 gives 11 and 61. So now we know $x_1=11$ and $x_2=61$ . Lastly, we plug in the numbers,11 and 61, into $x_1+x_2=2h$ , so $\boxed{h=36}$ .

## Solution 6 (Vieta's solution)
First, we start of exactly like solutions above and we find out that $j=2013-3h^2$ and $k=2014-2h^2$ We then plug j and k into $3(x-h)^2+j$ and $y=2(x-h)^2+k$ respectively. After that, we get two equations, $y=3x^2-6xh+2013$ and $y=2x^2-4xh+2014$ . We can apply Vieta's. Let the roots of the first equation be $a, b$ and the roots of the second equation be $c, d$ . Thus, we have that $a\cdot b=1007$ , $a+b=2h$ and $c\cdot d=671$ , $c+d=2h$ . Simple evaluations finds that $\boxed{h=36}$
~Jske25
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .