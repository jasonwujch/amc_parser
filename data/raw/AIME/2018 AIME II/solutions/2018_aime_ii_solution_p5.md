# 2018 AIME II Problem 5

## Problem

Suppose that $x$ , $y$ , and $z$ are complex numbers such that $xy = -80 - 320i$ , $yz = 60$ , and $zx = -96 + 24i$ , where $i$ $=$ $\sqrt{-1}$ . Then there are real numbers $a$ and $b$ such that $x + y + z = a + bi$ . Find $a^2 + b^2$ .

## Solution 1 (Euler's formula and Substitution)
The First (pun intended) thing to notice is that $xy$ and $zx$ have a similar structure (i.e. the real and imaginary parts differ by a factor of 4), but are not exactly conjugates. So let's take out the magnitudes of both, and see if we can multiply a root of unity to get the other. It turns out that root of unity is $e^{\frac{3\pi i}{2}}$ . Anyway this results in getting that $\left(\frac{-3i}{10}\right)y=z$ .
Then substitute this into $yz$ to get, after some calculation, that $y=10e^{\frac{5\pi i}{4}}\sqrt{2}$ and $z=-3e^{\frac{7\pi i}{4}}\sqrt{2}$ . Then plug $z$ into $zx$ , you could do the same thing with $xy$ but $zx$ looks like it's easier due to it being smaller. Anyway you get $x=20+12i$ . Then add all three up, which it turns out easier than it seems because for $z$ and $y$ the $\sqrt{2}$ disappears after you expand the root of unity (e raised to a specific power).
Long story short, you get $x=20+12i, y=-3+3i, z=-10-10i \implies x+y+z=7+5i \implies a^2+b^2=\boxed{074}$ .
~First

## Solution 2
First we evaluate the magnitudes. $|xy|=80\sqrt{17}$ , $|yz|=60$ , and $|zx|=24\sqrt{17}$ . Therefore, $|x^2y^2z^2|=17\cdot80\cdot60\cdot24$ , or $|xyz|=240\sqrt{34}$ . Divide to find that $|z|=3\sqrt{2}$ , $|x|=4\sqrt{34}$ , and $|y|=10\sqrt{2}$ . [asy] draw((0,0)--(4,0)); dot((4,0),red); draw((0,0)--(-4,0)); draw((0,0)--(0,-4)); draw((0,0)--(-4,1)); dot((-4,1),red); draw((0,0)--(-1,-4)); dot((-1,-4),red); draw((0,0)--(4,4),red); draw((0,0)--(4,-4),red); [/asy] This allows us to see that the argument of $y$ is $\frac{\pi}{4}$ , and the argument of $z$ is $-\frac{\pi}{4}$ . We need to convert the polar form to a standard form. Simple trig identities show $y=10+10i$ and $z=3-3i$ . More division is needed to find what $x$ is. \[x=-20-12i\] \[x+y+z=-7-5i\] \[(-7)^2+(-5)^2=\boxed{74}\] \[QED\blacksquare\] Written by a1b2

## Solution 3 (Pretty easy, no hard stuff, just watch ur arithmetic) :)
Solve this system the way you would if the RHS of all equations were real. Multiply the first and 3rd equations out and then factor out $60$ to find $x^2$ , then use standard techniques that are used to evaluate square roots of irrationals. let \[x = c+di\] , then you get \[c^2 - d^2 = 256\] and \[2cd = 480\] Solve to get $x$ as $20+12i$ and $-20-12i$ . Both will give us the same answer, so use the positive one. Divide $-80-320i$ by $x$ , and you get $10+10i$ as $y$ . This means that $z$ is a multiple of $1-i$ to get a real product, so you find $z$ is $3-3i$ . Now, add the real and imaginary parts separately to get $-7-5i$ , and calculate $a^2 + b^2$ to get $\boxed{074}$ . ~minor latex improvements done by jske25 and jdong2006

## Solution 4
Dividing the first equation by the second equation given, we find that $\frac{xy}{yz}=\frac{x}{z}=\frac{-80-320i}{60}=-\frac{4}{3}-\frac{16}{3}i \implies x=z\left(-\frac{4}{3}-\frac{16}{3}i\right)$ . Substituting this into the third equation, we get $z^2=\frac{-96+24i}{-\frac{4}{3}-\frac{16}{3}i}=3\cdot \frac{-24+6i}{-1-4i}=3\cdot \frac{(-24+6i)(-1+4i)}{1+16}=3\cdot \frac{-102i}{17}=-18i$ . Taking the square root of this is equivalent to halving the argument and taking the square root of the magnitude. Furthermore, the second equation given tells us that the argument of $y$ is the negative of that of $z$ , and their magnitudes multiply to $60$ . Thus, we have $z=\sqrt{-18i}=3-3i$ and $3\sqrt{2}\cdot |y|=60 \implies |y|=10\sqrt{2} \implies y=10+10i$ . To find $x$ , we can use the previous substitution we made to find that $x=z\left(-\frac{4}{3}-\frac{16}{3}i\right)=-\frac{4}{3}\cdot (3-3i)(1+4i)=-4(1-i)(1+4i)=-4(5+3i)=-20-12i$ . Therefore, $x+y+z=(-20+10+3)+(-12+10-3)i=-7-5i \implies a^2+b^2=(-7)^2+(-5)^2=49+25=\boxed{074}$
Solution by ktong

## Solution 5
We are given that $xy=-80-320i$ . Thus $y=\frac{-80-320i}{x}$ . We are also given that $xz= -96+24i$ . Thus $z=\frac{-96+24i}{x}$ . We are also given that $yz$ = $60$ . Substitute $y=\frac{-80-320i}{x}$ and $z=\frac{-96+24i}{x}$ into $yz$ = $60$ . We have $\frac{(-80-320i)(-96+24i)}{x^2}=60$ . Multiplying out $(-80-320i)(-96+24i)$ we get $(1920)(8+15i)$ . Thus $\frac{1920(8+15i)}{x^2} =60$ . Simplifying this fraction we get $\frac{32(8+15i)}{x^2}=1$ . Cross-multiplying the fractions we get $x^2=32(8+15i)$ or $x^2= 256+480i$ . Now we can rewrite this as $x^2-256=480i$ . Let $x= (a+bi)$ .Thus $x^2=(a+bi)^2$ or $a^2+2abi-b^2$ . We can see that $a^2+2abi-b^2-256=480i$ and thus $2abi=480i$ or $ab=240$ .We also can see that $a^2-b^2-256=0$ because there is no real term in $480i$ . Thus $a^2-b^2=256$ or $(a+b)(a-b)=256$ . Using the two equations $ab=240$ and $(a+b)(a-b)=256$ we solve by doing system of equations that $a=-20$ and $b=-12$ . And $x=a+bi$ so $x=-20-12i$ . Because $y=\frac{-80-320i}{x}$ , then $y=\frac{-80-320i}{-20-12i}$ . Simplifying this fraction we get $y=\frac{-80(1+4i)}{-4(5+3i)}$ or $y=\frac{20(1+4i)}{(5+3i)}$ . Multiplying by the conjugate of the denominator ( $5-3i$ ) in the numerator and the denominator and we get $y=\frac{20(17-17i)}{34}$ . Simplifying this fraction we get $y=10-10i$ . Given that $yz$ = $60$ we can substitute $(10-10i)(z)=60$ We can solve for z and get $z=3+3i$ . Now we know what $x$ , $y$ , and $z$ are, so all we have to do is plug and chug. $x+y+z= (-20-12i)+(10+10i)+(3-3i)$ or $x+y+z= -7-5i$ Now $a^2 +b^2=(-7)^2+(-5)^2$ or $a^2 +b^2 = 74$ . Thus $74$ is our final answer.(David Camacho)

## Solution 6
We observe that by multiplying $xy,$ $yz,$ and $zx,$ we get $(xyz)^2=(-80-320i)(60)(-96+24i).$ Next, we divide $(xyz)^2$ by $(yz)^2$ to get $x^2.$ We have $x^2=\frac{(-80-320i)(60)(-96+24i)}{3600}=256+480i.$ We can write $x$ in the form of $a+bi,$ so we get $(a+bi)^2=256+480i.$ Then, $a^2-b^2+2abi=256+480i,$ $a^2-b^2=256,$ and $2ab=480.$ Solving this system of equations is relatively simple. We have two cases, $a=20, b=12,$ and $a=-20, b=-12.$ Case 1: $a=20, b=12,$ so $x=20+12i.$ We solve for $y$ and $z$ by plugging in $x$ to the two equations. We see $y=\frac{-80-320i}{20+12i}=-10-10i$ and $z=\frac{-96+24i}{20+12i}=-3+3i.$ $x+y+z=7+5i,$ so $a=7$ and $b=5.$ Solving, we end up with $7^2+5^2=\boxed{074}$ as our answer. Case 2: $a=-20, b=-12,$ so $x=-20-12i.$ Again, we solve for $y$ and $z.$ We find $y=\frac{-80-320i}{-20-12i}=10+10i,$ $z=\frac{-96+24i}{-20-12i}=3-3i,$ so $x+y+z=-7-5i.$ We again have $(-7)^2+(-5)^2=\boxed{074}.$ Solution by Airplane50

## Solution 7 (Based on advanced mathematical knowledge)
According to the Euler's Theory, we can rewrite $x$ , $y$ and $z$ as \[x=r_{1}e^{i{\theta}_1}\] \[y=r_{2}e^{i{\theta}_2}\] \[x=r_{3}e^{i{\theta}_3}\] As a result, \[|xy|=r_{1}r_{2}=\sqrt{80^2+320^2}=80\sqrt{17}\] \[|yz|=r_{2}r_{3}=60\] \[|xz|=r_{1}r_{3}=\sqrt{96^2+24^2}=24\sqrt{17}\] Also, it is clear that \[yz=r_{2}e^{i{\theta}_2}r_{3}e^{i{\theta}_3}=|yz|e^{i({\theta}_2+{\theta}_3)}=|yz|=60\] So ${\theta}_2+{\theta}_3=0$ , or \[{\theta}_2=-{\theta}_3\] Also, we have \[xy=-80\sqrt{17}e^{i\arctan{4}}\] \[yz=60\] \[xz=-24\sqrt{17}e^{i\arctan{-\frac{1}{4}}}\] So now we have $r_{1}r_{2}=80\sqrt{17}$ , $r_{2}r_{3}=60$ , $r_{1}r_{3}=24\sqrt{17}$ , ${\theta}_1+{\theta}_2=\arctan{4}$ and ${\theta}_1-{\theta}_2=\arctan {-\frac{1}{4}}$ . Solve these above, we get \[r_{1}=4\sqrt{34}\] \[r_{2}=10\sqrt{2}\] \[r_{3}=3\sqrt{2}\] \[{\theta}_2=\frac{\arctan{4}-\arctan{-\frac{1}{4}}}{2}=\frac{\frac{\pi}{2}}{2}=\frac{\pi}{4}\] So we can get \[y=r_{2}e^{i{\theta}_2}=10\sqrt{2}e^{i\frac{\pi}{4}}=10+10i\] \[z=r_{3}e^{i{\theta}_3}=r_{3}e^{-i{\theta}_2}=3\sqrt{2}e^{-i\frac{\pi}{4}}=3-3i\] Use $xy=-80-320i$ we can find that \[x=-20-12i\] So \[x+y+z=-20-12i+10+10i+3-3i=-7-5i\] So we have $a=-7$ and $b=-5$ .
As a result, we finally get \[a^2+b^2=(-7)^2+(-5)^2=\boxed{074}\]
~Solution by $BladeRunnerAUG$ (Frank FYC)

## Solution 8
We can turn the expression $x+y+z$ into $\sqrt{x^2+y^2+z^2+2xy+2yz+2xz}$ , and this would allow us to plug in the values after some computations.
Based off of the given products, we have
$xy^2z=60(-80-320i)$
$xyz^2=60(-96+24i)$
$x^2yz=(-96+24i)(-80-320i)$ .
Dividing by the given products, we have
$y^2=\frac{60(-80-320i)}{-96+24i}$
$z^2=\frac{60(-96+24i)}{-80-320i}$
$x^2=\frac{(-96+24i)(-80-320i)}{60}$ .
Simplifying, we get that this expression becomes $\sqrt{24+70i}$ . This equals $\pm{(7+5i)}$ , so the answer is $7^2+5^2=\boxed{74}$ .
$\textbf{-RootThreeOverTwo}$

## Solution 9 (A Little Rigorous, but Straightforward and Easy)
Multiplying $xy \cdot yz \cdot zx = (xyz)^2$ we obtain $60 \cdot 960(16+30i)$ (too lazy to do $60 \cdot 960$ , you don't need to). Taking the square root, we get $240\sqrt{16+30i}$ . Letting $(a+bi)^2=16+30i,$ we have $a^2+2abi-b^2=16+30i.$ Thus, $(a+b)(a-b)=16,$ and $2ab=30.$ Guessing and checking, we get $a+bi=5+3i$ . Therefore, $xyz=240(5+3i).$ Dividing this by each of the equations provided in the original problem, we get $x=20+12i,y=-10-10i,$ and $z=-3+3i$ . $20+12i-10-10i-3+3i=7+5i$ . Finally, $7^2+5^2=\boxed{074}.$
~SirAppel
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .