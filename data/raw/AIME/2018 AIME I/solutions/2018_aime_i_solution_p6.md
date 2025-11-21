# 2018 AIME I Problem 6

## Problem

Let $N$ be the number of complex numbers $z$ with the properties that $|z|=1$ and $z^{6!}-z^{5!}$ is a real number. Find the remainder when $N$ is divided by $1000$ .

## Solution 1
Let $a=z^{120}$ . This simplifies the problem constraint to $a^6-a \in \mathbb{R}$ . This is true if $\text{Im}(a^6)=\text{Im}(a)$ . Let $\theta$ be the angle $a$ makes with the positive x-axis. Note that there is exactly one $a$ for each angle $0\le\theta<2\pi$ . We are given $\sin\theta = \sin{6\theta}$ . Note that $\sin \theta = \sin (\pi - \theta)$ and $\sin \theta = \sin (\theta + 2\pi)$ . We can use these facts to create two types of solutions:
\[\sin \theta = \sin ((2m + 1)\pi - \theta)\]
which implies that $(2m+1)\pi-\theta = 6\theta$ and reduces to $\frac{(2m + 1)\pi}{7} = \theta$ . There are 7 solutions for this.
\[\sin \theta = \sin (2n\pi + \theta)\]
which implies that $2n\pi+\theta=6\theta$ and reduces to $\frac{2n\pi}{5} = \theta$ . There are 5 solutions for this, totaling 12 values of $a$ .
For each of these solutions for $a$ , there are necessarily $120$ solutions for $z$ . Thus, there are $12\cdot 120=1440$ solutions for $z$ , yielding an answer of $\boxed{440}$ .

## Solution 2
The constraint mentioned in the problem is equivalent to the requirement that the imaginary part is equal to $0$ . Since $|z|=1$ , let $z=\cos \theta + i\sin \theta$ , then we can write the imaginary part of $\Im(z^{6!}-z^{5!})=\Im(z^{720}-z^{120})=\sin\left(720\theta\right)-\sin\left(120\theta\right)=0$ . Using the sum-to-product formula, we get $\sin\left(720\theta\right)-\sin\left(120\theta\right)=2\cos\left(\frac{720\theta+120\theta}{2}\right)\sin\left(\frac{720\theta-120\theta}{2}\right)=2\cos\left(\frac{840\theta}{2}\right)\sin\left(\frac{600\theta}{2}\right)\implies \cos\left(\frac{840\theta}{2}\right)=0$ or $\sin\left(\frac{600\theta}{2}\right)=0$ . The former yields $840$ solutions, and the latter yields $600$ solutions, giving a total of $840+600=1440$ solution, so our answer is $\boxed{440}$ .

## Solution 3
As mentioned in solution one, for the difference of two complex numbers to be real, their imaginary parts must be equal. We use exponential form of complex numbers. Let $z = e^{i \theta}$ . We have two cases to consider. Either $z^{6!} = z^{5!}$ , or $z^{6!}$ and $z^{5!}$ are reflections across the imaginary axis. If $z^{6!} = z^{5!}$ , then $e^{6! \theta i} = e^{5! \theta i}$ . Thus, $720 \theta = 120 \theta$ or $600\theta = 0$ , giving us 600 solutions. (Equalities are taken modulo $2 \pi$ ) For the second case, $e^{6! \theta i} = e^{(\pi - 5!\theta)i}$ . This means $840 \theta = \pi$ , giving us 840 solutions. Our total count is thus $1440$ , yielding a final answer of $\boxed{440}$ .

## Solution 4
Because $|z| = 1,$ we know that $z\overline{z} = 1^2 = 1.$ Hence $\overline{z} = \frac 1 {z}.$ Because $z^{6!}-z^{5!}$ is real, it is equal to its complex conjugate. Hence $z^{6!}-z^{5!} = \overline{z^{6!}}-\overline{z^{5!}}.$ Substituting the expression we that we derived earlier, we get $z^{720}-z^{120} = \frac 1{z^{720}} - \frac 1{z^{120}}.$ This leaves us with a polynomial whose leading term is $z^{1440}.$ Hence our answer is $\boxed{440}$ .~Shen Kislay Kai 2022
Note: This is actually not rigorous, because how to we know that all of the roots of such a polynomial are distinct? One can proceed as follows. Factoring gives us that $(z^{840}+1)(z^{600}-1)=0,$ so this implies that $z^{840} = -1$ OR $z^{600}=1.$ To show no $z$ satisfies both of these conditions, notice that if $w^{840} = -1$ and $w^{600}=1$ for some complex number $w$ , then $w^{240} = w^{840-600} = -1,$ which implies that $w^{360} = w^{600-240}=-1,$ which implies that $w^{120}=w^{360-240}=1.$ This is a contradiction since then $w^{240}$ would also have to equal $(w^{120})^2 = 1.$ Therefore the total number of solutions is $840+600 = 1\boxed{440}.$ Minor Edit by ~ hazio Jheng
I'm pretty sure it works since fundamental theory of algebra counts multiplicity.

## Solution 5
Since $|z|=1$ , let $z=\cos \theta + i\sin \theta$ . For $z^{6!}-z^{5!}$ to be real, the imaginary parts of $z^{6!}$ and $z^{5!}$ must be equal, so $\sin 720\theta=\sin 120\theta$ . We need to find all solutions for $\theta$ in the interval $[0,2\pi)$ . This can be done by graphing $y=\sin 720\theta$ and $y=\sin 120\theta$ and finding their intersections. Since the period of $y=\sin 720\theta$ is $\frac{\pi}{360}$ and the period of $y=\sin 120\theta$ is $\frac{\pi}{60}$ , the common period of both graphs is $\frac{\pi}{60}$ . Therefore, we only graph the functions in the domain $[0, \frac{\pi}{60})$ . We can clearly see that there are twelve points of intersection. However, since we only graphed $\frac{1}{120}$ of the interval $[0,2\pi)$ , we need to multiply our answer by $120$ . The answer is $12 \cdot 120 = 1440 = \boxed{440} \pmod{1000}$ .

## Solution 6 (Official MAA)
If $z$ satisfies the given conditions, there is a $\theta \in [0,2\pi]$ such that $z=e^{i\theta}$ and $e^{720\theta i-120\theta i}$ is real. This difference is real if and only if either the two numbers $720\theta$ and $120\theta$ represent the same angle or the two numbers represent supplementary angles. In the first case there is an integer $k$ such that $720\theta=120\theta+2k\pi,$ which implies that $\theta$ is a multiple of $\tfrac{\pi}{300}.$ In the second case there is an integer $k$ such that $720\theta=-120\theta+(2k+1)\pi,$ which implies that $\theta$ is $\tfrac{\pi}{840}$ plus a multiple of $\tfrac{\pi}{420}.$ In the interval $[0,2\pi]$ there are $600$ values of $\theta$ that are multiples of $\tfrac{\pi}{300},$ there are $840$ values that are $\tfrac{\pi}{840}$ plus a multiple of $\tfrac{\pi}{420},$ and there are no values of $\theta$ that satisfy both of these conditions. Therefore there must be $600+840=1440$ complex numbers satisfying the given conditions. The requested remainder is $440.$

## Solution 7
$z^{720}-z^{120}=z^{120}(z^{600}-1)$ firstly we consider that $z^{600}-1=0$ obviously there are $600$ different roots
Then, we consider that $z^{720}=a+bi, z^{120}=-a+bi$ or $z^{720}=-a-bi, z^{120}=a-bi$ which leads to $840\theta=\pi+2k\pi, k\in N$ so there are $840$ roots, in all, $840+600 \equiv 440 ($ mod $1000)$ .
~bluesoul

## Video Solution
https://www.youtube.com/watch?v=iE8paW_ICxw
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .