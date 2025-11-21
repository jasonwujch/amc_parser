# 2010 AIME II Problem 7

## Problem

Let $P(z)=z^3+az^2+bz+c$ , where $a$ , $b$ , and $c$ are real. There exists a complex number $w$ such that the three roots of $P(z)$ are $w+3i$ , $w+9i$ , and $2w-4$ , where $i^2=-1$ . Find $|a+b+c|$ .

## Solution 1 (Vieta's)
Set $w=x+yi$ , so $x_1 = x+(y+3)i$ , $x_2 = x+(y+9)i$ , $x_3 = 2x-4+2yi$ .
Since $a,b,c\in{R}$ , the imaginary part of $a,b,c$ must be $0$ .
Start with a, since it's the easiest one to do: $y+3+y+9+2y=0, y=-3$ ,
and therefore: $x_1 = x$ , $x_2 = x+6i$ , $x_3 = 2x-4-6i$ .
Now, do the part where the imaginary part of c is 0 since it's the second easiest one to do: $x(x+6i)(2x-4-6i)$ . The imaginary part is $6x^2-24x$ , which is 0, and therefore $x=4$ , since $x=0$ doesn't work.
So now, $x_1 = 4, x_2 = 4+6i, x_3 = 4-6i$ ,
and therefore: $a=-12, b=84, c=-208$ . Finally, we have $|a+b+c|=|-12+84-208|=\boxed{136}$ .

## Solution 1b
Same as solution 1 except that when you get to $x_1 = x$ , $x_2 = x+6i$ , $x_3 = 2x-4-6i$ , you don't need to find the imaginary part of $c$ . We know that $x_1$ is a real number, which means that $x_2$ and $x_3$ are complex conjugates. Therefore, $x=2x-4$ .

## Solution 2 (casework)
Note that at least one of $w+3i$ , $w+9i$ , or $2w-4$ is real by complex conjugate roots. We now separate into casework based on which one.
Let $w=x+yi$ , where $x$ and $y$ are reals.
Case 1: $w+3i$ is real. This implies that $x+yi+3i$ is real, so by setting the imaginary part equal to zero we get $y=-3$ , so $w=x-3i$ . Now note that since $w+3i$ is real, $w+9i$ and $2w-4$ are complex conjugates. Thus $\overline{w+9i}=2w-4$ , so $\overline{x+6i}=2(x-3i)-4$ , implying that $x=4$ , so $w=4-3i$ .
Case 2: $w+9i$ is real. This means that $x+yi+9i$ is real, so again setting imaginary part to zero we get $y=-9$ , so $w=x-9i$ . Now by the same logic as above $w+3i$ and $2w-4$ are complex conjugates. Thus $\overline{w+3i}=2w-4$ , so $\overline{x-6i}=2(x-9i)-4$ , so $x+6i=2x-4-18i$ , which has no solution as $x$ is real.
Case 3: $2w-4$ is real. Going through the same steps, we get $y=0$ , so $w=x$ . Now $w+3i$ and $w+6i$ are complex conjugates, but $w=x$ , which means that $\overline{x+3i}=x+6i$ , so $x-3i=x+6i$ , which has no solutions.
Thus case 1 is the only one that works, so $w=4-3i$ and our polynomial is $(z-(4))(z-(4+6i))(z-(4-6i))$ . Note that instead of expanding this, we can save time by realizing that the answer format is $|a+b+c|$ , so we can plug in $z=1$ to our polynomial to get the sum of coefficients, which will give us $a+b+c+1$ . Plugging in $z=1$ into our polynomial, we get $(-3)(-3-6i)(-3+6i)$ which evaluates to $-135$ . Since this is $a+b+c+1$ , we subtract 1 from this to get $a+b+c=-136$ , so $|a+b+c|=\boxed{136}$ .
~chrisdiamond10

## Solution 3
By Vieta's we know the sum of the roots must be $-a$ , a real number. That means $4w+12i-4$ is a real number, meaning $w$ has an imaginary component of $-3i$ .
Now we write $w = x-3i$ . Then, $w+3i$ is the real root, meaning the other two are complex conjugates. We have $\overline{x+6i} = 2x-4-6i$ , and solving, we get $x=4$ . Then, $f(x) = (x-4)(x-4-6i)(x-4+6i) = (x-4)(x^2-8x+52)$ .
We get $|a+b+c| = |-12+84-208| = \boxed{136}$ .
-skibbysiggy
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .