# 2009 AIME I Problem 12

## Problem

In right $\triangle ABC$ with hypotenuse $\overline{AB}$ , $AC = 12$ , $BC = 35$ , and $\overline{CD}$ is the altitude to $\overline{AB}$ . Let $\omega$ be the circle having $\overline{CD}$ as a diameter. Let $I$ be a point outside $\triangle ABC$ such that $\overline{AI}$ and $\overline{BI}$ are both tangent to circle $\omega$ . The ratio of the perimeter of $\triangle ABI$ to the length $AB$ can be expressed in the form $\frac {m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solution 1
First, note that $AB=37$ ; let the tangents from $I$ to $\omega$ have length $x$ . Then the perimeter of $\triangle ABI$ is equal to \[2(x+AD+DB)=2(x+37).\] It remains to compute $\dfrac{2(x+37)}{37}=2+\dfrac{2}{37}x$ .
Observe $CD=\dfrac{12\cdot 35}{37}=\dfrac{420}{37}$ , so the radius of $\omega$ is $\dfrac{210}{37}$ . We may also compute $AD=\dfrac{12^{2}}{37}$ and $DB=\dfrac{35^{2}}{37}$ by similar triangles. Let $O$ be the center of $\omega$ ; notice that \[\tan(\angle DAO)=\dfrac{DO}{AD}=\dfrac{210/37}{144/37}=\dfrac{35}{24}\] so it follows \[\sin(\angle DAO)=\dfrac{35}{\sqrt{35^{2}+24^{2}}}=\dfrac{35}{\sqrt{1801}}\] while $\cos(\angle DAO)=\dfrac{24}{\sqrt{1801}}$ . By the double-angle formula $\sin(2\theta)=2\sin\theta\cos\theta$ , it turns out that \[\sin(\angle BAI)=\sin(2\angle DAO)=\dfrac{2\cdot 35\cdot 24}{1801}=\dfrac{1680}{1801}\]
Using the area formula $\dfrac{1}{2}ab\sin(C)$ in $\triangle ABI$ , \[[ABI]=\left(\dfrac{1}{2}\right)\left(\dfrac{144}{37}+x\right)(37)\left(\dfrac{1680}{1801}\right)=\left(\dfrac{840}{1801}\right)(144+37x).\] But also, using $rs$ , \[[ABI]=\left(\dfrac{210}{37}\right)(37+x).\] Now we can get \[\dfrac{[ABI]}{210}=\dfrac{4(144+37x)}{1801}=\dfrac{37+x}{37}\] so multiplying everything by $37\cdot 1801=66637$ lets us solve for $x$ : \[21312+5476x=66637+1801x.\] We have $x=\dfrac{66637-21312}{5476-1801}=\dfrac{45325}{3675}=\dfrac{37}{3}$ , and now \[2+\dfrac{2}{37}x=2+\dfrac{2}{3}=\dfrac{8}{3}\] giving the answer, $\boxed{011}$ .

## Solution 2
Let $O$ be center of the circle and $P$ , $Q$ be the two points of tangent such that $P$ is on $BI$ and $Q$ is on $AI$ . We know that $AD:CD = CD:BD = 12:35$ .
Since the ratios between corresponding lengths of two similar diagrams are equal, we can let $AD = 144, CD = 420$ and $BD = 1225$ . Hence $AQ = 144, BP = 1225, AB = 1369$ and the radius $r = OD = 210$ .
Since we have $\tan OAB = \frac {35}{24}$ and $\tan OBA = \frac{6}{35}$ , we have $\sin {(OAB + OBA)} = \frac {1369}{\sqrt {(1801*1261)}},$ $\cos {(OAB + OBA)} = \frac {630}{\sqrt {(1801*1261)}}$ .
Hence $\sin I = \sin {(2OAB + 2OBA)} = \frac {2*1369*630}{1801*1261}$ . let $IP = IQ = x$ , then we have Area $(IBC)$ = $(2x + 1225*2 + 144*2)*\frac {210}{2}$ = $(x + 144)(x + 1225)* \sin {\frac {I}{2}}$ . Then we get $x + 1369 = \frac {3*1369*(x + 144)(x + 1225)}{1801*1261}$ .
Now the equation looks very complex but we can take a guess here. Assume that $x$ is a rational number (If it's not then the answer to the problem would be irrational which can't be in the form of $\frac {m}{n}$ ) that can be expressed as $\frac {a}{b}$ such that $(a,b) = 1$ . Look at both sides; we can know that $a$ has to be a multiple of $1369$ and not of $3$ and it's reasonable to think that $b$ is divisible by $3$ so that we can cancel out the $3$ on the right side of the equation.
Let's see if $x = \frac {1369}{3}$ fits. Since $\frac {1369}{3} + 1369 = \frac {4*1369}{3}$ , and $\frac {3*1369*(x + 144)(x + 1225)}{1801*1261} = \frac {3*1369* \frac {1801}{3} * \frac {1261*4}{3}} {1801*1261} = \frac {4*1369}{3}$ . Amazingly it fits!
Since we know that $3*1369*144*1225 - 1369*1801*1261 < 0$ , the other solution of this equation is negative which can be ignored. Hence $x = 1369/3$ .
Hence the perimeter is $1225*2 + 144*2 + \frac {1369}{3} *2 = 1369* \frac {8}{3}$ , and $BC$ is $1369$ . Hence $\frac {m}{n} = \frac {8}{3}$ , $m + n = 11$ .

## Solution 3
As in Solution $1$ , let $P$ and $Q$ be the intersections of $\omega$ with $BI$ and $AI$ respectively.
First, by pythagorean theorem, $AB = \sqrt{12^2+35^2} = 37$ . Now the area of $ABC$ is $1/2*12*35 = 1/2*37*CD$ , so $CD=\frac{420}{37}$ and the inradius of $\triangle ABI$ is $r=\frac{210}{37}$ .
Now from $\triangle CDB \sim \triangle ACB$ we find that $\frac{BC}{BD} = \frac{AB}{BC}$ so $BD = BC^2/AB = 35^2/37$ and similarly, $AD = 12^2/37$ .
Note $IP=IQ=x$ , $BP=BD$ , and $AQ=AD$ . So we have $AI = 144/37+x$ , $BI = 1225/37+x$ . Now we can compute the area of $\triangle ABI$ in two ways: by heron's formula and by inradius times semiperimeter, which yields
$rs=210/37(37+x) = \sqrt{(37+x)(37-144/37)(37-1225/37)x}$
$210/37(37+x) = 12*35/37 \sqrt{x(37+x)}$
$37+x = 2 \sqrt{x(x+37)}$
$x^2+74x+1369 = 4x^2 + 148x$
$3x^2 + 74x - 1369 = 0$
The quadratic formula now yields $x=37/3$ . Plugging this back in, the perimeter of $ABI$ is $2s=2(37+x)=2(37+37/3) = 37(8/3)$ so the ratio of the perimeter to $AB$ is $8/3$ and our answer is $8+3=\boxed{011}$
Note: If you don't want to solve the quadratic, you can continue with $37+x = 2 \sqrt{x(x+37)}$ and divide both sides by $\sqrt{x+37}$ to get $\sqrt{37+x} = 2 \sqrt{x}$ . Square both sides to get $37+x = 4x$ and solve to get $x=\frac{37}{3}$ .

## Solution 4
As in Solution $2$ , let $P$ and $Q$ be the intersections of $\omega$ with $BI$ and $AI$ respectively.
Recall that the distance from a point outside a circle to that circle is the same along both tangent lines to the circle drawn from the point.
Recall also that the length of the altitude to the hypotenuse of a right-angle triangle is the geometric mean of the two segments into which it cuts the hypotenuse.
Let $x = \overline{AD} = \overline{AQ}$ . Let $y = \overline{BD} = \overline{BP}$ . Let $z = \overline{PI} = \overline{QI}$ . The semi-perimeter of $ABI$ is $x + y + z$ . Since the lengths of the sides of $ABI$ are $x + y$ , $y + z$ and $x + z$ , the square of its area by Heron's formula is $(x+y+z)xyz$ .
The radius $r$ of $\omega$ is $\overline{CD}/2$ . Therefore $r^2 = xy/4$ . As $\omega$ is the in-circle of $ABI$ , the area of $ABI$ is also $r(x+y+z)$ , and so the square area is $r^2(x+y+z)^2$ .
Therefore \[(x+y+z)xyz = r^2(x+y+z)^2 = \frac{xy(x+y+z)^2}{4}\] Dividing both sides by $xy(x+y+z)/4$ we get: \[4z = (x+y+z),\] and so $z = (x+y)/3$ . The semi-perimeter of $ABI$ is therefore $\frac{4}{3}(x+y)$ and the whole perimeter is $\frac{8}{3}(x+y)$ . Now $x + y = \overline{AB}$ , so the ratio of the perimeter of $ABI$ to the hypotenuse $\overline{AB}$ is $8/3$ and our answer is $8+3=\boxed{011}$

## Solution 5
[asy] size(300); defaultpen(linewidth(0.4)+fontsize(10)); pen s = linewidth(0.8)+fontsize(8); pair A,B,C,D,O,X; C=origin; A=(0,12); B=(18,0); D=foot(C,A,B); O = (C+D)/2; real r = length(D-C)/2; path c = CR(O, r); pair OA = (O+A)/2; real rA = length(A-O)/2; pair Ap = OP(CR(OA,rA), c); pair OB = (O+B)/2; real rB = length(B-O)/2; pair Bp = OP(CR(OB,rB), c); X=extension(A,Ap,B,Bp); draw(A--B--C--A, s); draw(C--D^^B--O--A^^Ap--O--X, gray+0.25); draw(c^^A--X--B); dot("$A$", A, N); dot("$B$", B, SE); dot("$C$", C, SW); dot("$D$", D, 0.2*(D-C)); dot("$I$", X, 0.5*(X-C)); dot("$P$", Ap, 0.3*(Ap-O)); dot("$Q$", Bp, 0.3*(Bp-O)); dot("$O$", O, W); label("$\beta$",B,10*dir(157)); label("$\alpha$",A,5*dir(-55)); label("$\theta$",X,5*dir(55)); [/asy] Let $AP=AD=x$ , let $BQ=BD=y$ , and let $IP=IQ=z$ . Let $OD=r$ . We find $AB=37$ . Let $\alpha$ , $\beta$ , and $\theta$ be the angles $OAD$ , $OBD$ , and $OPI$ respectively. Then $\alpha + \beta + \theta = 90^\circ$ , so \[\theta = 90^\circ - (\alpha+\beta).\] The perimeter of $\triangle ABI$ is $2(x+y+z)=2(37+z)$ . The desired ratio is then \[\rho = 2\left(1+\frac z{37}\right)\] We need to find $z$ . In $\triangle OPI$ , $z=r\cot\theta = r\tan (\alpha+\beta)$ . We get \[\tan\alpha = \frac{OD}{AD} = \frac 12 \frac{CD}{AD} = \frac 12 \tan A = \frac 12 \frac{BC}{AC} = \frac{35}{24}.\] Similarly, $\tan\beta = \tfrac 6{35}$ . Then \[z = r\cdot \tan (\alpha+\beta) = r\cdot \frac{\tan\alpha + \tan\beta}{1-\tan\alpha\tan\beta}= \frac{37^2\cdot r}{18\cdot 35}\] Computing $[ABC]$ in two ways we get $CD = \tfrac{12\cdot 35}{37}$ , so $r=\tfrac{6\cdot 35}{37}$ . Using this value of $r$ we get $z=\tfrac {37}3$ . Thus \[\rho = 2\left(1+\frac 1{3}\right) = \frac 8{3},\] and $8+3=\boxed{011}$ .

## Solution 6
This solution is not a real solution and is solving the problem with a ruler and compass.
Draw $AC = 4.8, BC = 14, AB = 14.8$ . Then, drawing the tangents and intersecting them, we get that $IA$ is around $6.55$ and $IB$ is around $18.1$ . We then find the ratio to be around $\frac{39.45}{14.8}$ . Using long division, we find that this ratio is approximately 2.666, which you should recognize as $\frac{8}{3}$ . Since this seems reasonable, we find that the answer is $\boxed{11}$ ~ilp

## Solution 7
Denoting three tangents has length $h_1,h_2,h_3$ while $h_1,h_3$ lies on $AB$ with $h_1>h_3$ .The area of $ABC$ is $1/2*12*35 = 1/2*37*CD$ , so $CD=\frac{420}{37}$ and the inradius of $\triangle ABI$ is $r=\frac{210}{37}$ .As we know that the diameter of the circle is the height of $\triangle ACB$ from $C$ to $AB$ . Assume that $\tan\alpha=\frac{h_1}{r}$ and $\tan\beta=\frac{h_3}{r}$ and $\tan\omega=\frac{h_2}{r}$ . But we know that $\tan(\alpha+\beta)=-\tan(180-\alpha-\beta)=-\tan\omega$ According to the basic computation, we can get that $\tan(\alpha)=\frac{35}{6}$ ; $\tan(\beta)=\frac{24}{35}$ So we know that $\tan(\omega)=\frac{1369}{630}$ according to the tangent addition formula. Hence, it is not hard to find that the length of $h_2$ is $\frac{37}{3}$ . According to basic addition and division, we get the answer is $\frac{8}{3}$ which leads to $8+3=\boxed{11}$ ~bluesoul

## Solution 8 (no trig and intuitive)
Notice $CD$ is the altitude of $\triangle ABC$ , and so $CD = \frac{AC \cdot BC}{AB} = \frac{210}{37}.$ This means in the inradius of the circle is $r=\frac{CD}{2}=\frac{210}{37}.$
Next, by $\triangle ABC \sim \triangle ACD \sim \triangle CBD$ , we have $AD=CD \cdot \frac{12}{35} = \frac{144}{37}$ and $BD = CD \cdot \frac{35}{12} = \frac{1225}{37}$ .
Lastly, denote the tangent point of $AI, BI$ with the circle as $P, Q$ respectively. Then by the properties of inscribed circles, we have that $AP=AD=\frac{144}{37}$ and $BQ=BD=\frac{1225}{37}$ , and $PI=QI=x$ . We want to make an algebraic expression utilizing what we know about ABI.
We use the inradius formula: $r = \frac{[\triangle ABI]}{s}$ . We have $s=37+x$ . With Heron's (very basic calculations) we get $[\triangle ABI] = \sqrt{(x+37)(x)(\frac{1225}{37})(\frac{144}{37})} = \frac{420}{37} \sqrt{x(37+x)}.$ Using the inradius formula, we get \[\frac{210}{37} = \frac{\frac{420}{37} \sqrt{x(37+x)}}{37+x}\] which simplifies to $x=\frac{37}{3}$ . The answer is then $\frac{8}{3}. \boxed{11}$ ~ brocolimanx
These problems are copyrighted © by the Mathematical Association of America.