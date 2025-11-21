# 2014 AMC 10B Problem 23

## Problem

A sphere is inscribed in a truncated right circular cone as shown. The volume of the truncated cone is twice that of the sphere. What is the ratio of the radius of the bottom base of the truncated cone to the radius of the top base of the truncated cone?

$\text{(A) } \dfrac32 \quad \text{(B) } \dfrac{1+\sqrt5}2 \quad \text{(C) } \sqrt3 \quad \text{(D) } 2 \quad \text{(E) } \dfrac{3+\sqrt5}2$

[asy] real r=(3+sqrt(5))/2; real s=sqrt(r); real Brad=r; real brad=1; real Fht = 2*s; import graph3; import solids; currentprojection=orthographic(1,0,.2); currentlight=(10,10,5); revolution sph=sphere((0,0,Fht/2),Fht/2); //draw(surface(sph),green+white+opacity(0.5)); //triple f(pair t) {return (t.x*cos(t.y),t.x*sin(t.y),t.x^(1/n)*sin(t.y/n));} triple f(pair t) { triple v0 = Brad*(cos(t.x),sin(t.x),0); triple v1 = brad*(cos(t.x),sin(t.x),0)+(0,0,Fht); return (v0 + t.y*(v1-v0)); } triple g(pair t) { return (t.y*cos(t.x),t.y*sin(t.x),0); } surface sback=surface(f,(3pi/4,0),(7pi/4,1),80,2); surface sfront=surface(f,(7pi/4,0),(11pi/4,1),80,2); surface base = surface(g,(0,0),(2pi,Brad),80,2); draw(sback,gray(0.3)); draw(sfront,gray(0.5)); draw(base,gray(0.9)); draw(surface(sph),gray(0.4));[/asy]

## Solution 1
First, we draw the vertical cross-section passing through the middle of the frustum. Let the top base have a diameter of $2$ and the bottom base has a diameter of $2r$ .
[asy] size(7cm); pair A,B,C,D; real r = (3+sqrt(5))/2; real s = sqrt(r); A = (-r,0); B = (r,0); C = (1,2*s); D = (-1,2*s); draw(A--B--C--D--cycle); pair O = (0,s); draw(shift(O)*scale(s)*unitcircle); dot(O); pair X,Y; X = (0,0); Y = (0,2*s); draw(X--Y); label("$r-1$",(r/2+1/2,0),S); label("$1$",(Y+C)/2,N); label("$s$",(O+Y)/2,W); label("$s$",(O+X)/2,W); draw(B--C--(1,0)--cycle,blue+1bp); pair P = 0.73*C+0.27*B; draw(O--P); dot(P); label("$1$",(C+P)/2,NE); label("$r$",(B+P)/2,NE); [/asy]
Then using the Pythagorean theorem we have: $(r+1)^2=(2s)^2+(r-1)^2$ , which is equivalent to: $r^2+2r+1=4s^2+r^2-2r+1$ . Subtracting $r^2-2r+1$ from both sides, $4r=4s^2$ , and solving for $s$ , we end up with \[s=\sqrt{r}.\] Next, we can find the volume of the frustum (truncated cone) and the sphere. Since we know $V_{\text{frustum}}=2V_{\text{sphere}}$ , we can solve for $s$ using $V_{\text{frustum}}=\frac{\pi h}{3}(R^2+r^2+Rr)$ we get: \[V_{\text{frustum}}=\frac{\pi\cdot2\sqrt{r}}{3}(r^2+r+1)\] Using $V_{\text{sphere}}=\dfrac{4s^{3}\pi}{3}$ , we get \[V_{\text{sphere}}=\dfrac{4(\sqrt{r})^{3}\pi}{3}\] so we have: \[\frac{\pi\cdot2\sqrt{r}}{3}(r^2+r+1)=2\cdot\dfrac{4(\sqrt{r})^{3}\pi}{3}.\] Dividing by $\frac{2\pi\sqrt{r}}{3}$ , we get \[r^2+r+1=4r\] which is equivalent to \[r^2-3r+1=0\] by the Quadratic Formula, $r=\dfrac{3\pm\sqrt{(-3)^2-4\cdot1\cdot1}}{2\cdot1}$ , so \[r=\dfrac{3+\sqrt{5}}{2} \longrightarrow \boxed{\textbf{(E)}}\]

## Solution 2
Similar to above, draw a smaller cone top with the base of the smaller circle with radius $r_1$ and height $h$ . The smaller right triangle is similar to the blue highlighted one in Solution $1$ . Then $\frac{r_1}{r_2-r_1}=\frac{h}{2R}$ where $R$ is the radius of the sphere. Then $h=\frac{2Rr_1}{r_2-r_1}$ .
From the Pythagorean theorem on the blue triangle in Solution $1$ , we get similarly that $R=\sqrt{r_2r_1}$ .
From the volume requirements, we get that $\frac{8}{3}\pi R^3=\frac{\pi r_2^2(h+2R)-\pi r_1^2h}{3}$ which yields $8R^3=r_2^2(h+2R)-r_1^2h$ .
The small right triangle on top is similar to the big right triangle of the entire big cone. So $\frac{r_1}{r_2}=\frac{h}{h+2R}\implies h+2R=\frac{r_2h}{r_1}$ .
Substituting yields $8R^3=\frac{h(r_2^3-r_1^3)}{r_1}$ .
Substituting $R=\sqrt{r_2r_1}$ and $h=\frac{2Rr_1}{r_2-r_1}$ yields $8(r_2r_1)^{\frac{3}{2}}=2(r_2r_1)^{\frac{1}{2}}(r_2^2+r_2r_1+r_1^2)$ which yields $r_2^2-3r_2r_1+r_1^2=0$ .
Solving in $r_2$ yields $r_2=\frac{3r_1\pm r_1\sqrt{5}}{2}$ so $\frac{r_2}{r_1}=\frac{3+\sqrt{5}}{2}$ .

## Solution 3 (Safe Risks)
We can create a cross section right down the middle vertically of the truncated cone and sphere. The figure formed (excuse my horrendous editing skills) looks like below.
We can conjoin the bottom most points to form a kite. We can now use safe assumptions, a very common competition math technique that involves making estimated guesses to assume an answer. The kite has the shorter isosceles parts as length 3. We can assume the line \( AM = 3 \), and therefore line \( IE = 6 \). Then, triangle \( AIE \) is a 30-60-90 right angle triangle, and \( AE = 3\sqrt{3} \), which means that the radius of the bottom base of the truncated cone is \( 3\sqrt{3} \). We may apply the same logic to the top part of the trapezoid. Like the bottom, the length \( IM = IC = 3 \), and \( ID = \) some value that makes \( ICD \) a 30-60-90 right triangle, and therefore length \( CD = \sqrt{3} \).
Our ratio for the big radius to the small radius is \( 3\sqrt{3}/\sqrt{3} = 3 \). However, 3 isn't an answer :-(, so we do some educated guessing. For simplicity we say that \( \sqrt{5} = 2 \). We see that answer choice A is 3/2, B is also 3/2, C is \(\sqrt{3}\), D is 2, and E is 2.5. We see that E is closest to the ratio we got, and so our answer is $\boxed{\textbf{(E)}}$ .
~Pinotation

## Solution 4: Another Way of Simplifying the Equation in Solution 2
Similar to the previous solutions, we let $R$ , $r$ , and $s$ be the radii of the larger base, smaller base, and the sphere, respectively. By the Pythagorean Theorem, we have $s=\sqrt{Rr}$ . Let $H$ , $h$ be the heights of the large and small cones, respectively, then we have $H=h+2s$ and \[h=2s\left(\frac{r}{R-r}\right)==\frac{2sr}{R-r}=\frac{2\left(\sqrt{Rr}\right)r}{R-r}\] Thus we have the equation \[V_{large cone}-V_{small cone}=2V_{sphere}\] \[\frac{\pi R^2H}{3}-\frac{\pi r^2h}{3}=2\left(\frac{4\pi s^3}{3}\right)\] \[\pi R^2H-\pi r^2h=8\pi s^3\] \[R^2H-r^2h=8s^3\] Substituting the expressions for $H$ , $h$ , $s$ in order into the equation yields \[R^2\left(h+2s\right)+r^2h=8s^3\] \[R^2\left(\left(\frac{2sr}{R-r}\right)+2s\right)+r^2\left(\frac{2sr}{R-r}\right)=8s^3\] \[R^2\left(\frac{2sR}{R-r}\right)+r^2\left(\frac{2sr}{R-r}\right)=8s^3\] \[\frac{2sR^3-2sr^3}{R-r}=8s^3\] \[\frac{R^3-r^3}{R-r}=4s^2\] The numerator $R^3-r^3$ can be factored to yield \[\frac{\left(R-r\right)\left(R^2+Rr+r^2\right)}{R-r}=4s^2\] \[R^2+Rr+r^2{R-r}=4s^2\] \[R^2+Rr+r^2=4\left(\sqrt{Rr}\right)^2\] \[R^2+Rr+r^2=4Rr\] \[R^2-3Rr+r^2=0\] Solving the quadratic to obtain the ratio $\frac{R}{r}=\frac{3+\sqrt{5}}{2}$ $\boxed{\textbf{(E)}}$
~ Nafer

## Video Solution
https://youtu.be/3C5AYs7GoF4
### See Also