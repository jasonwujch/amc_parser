# 2011 AMC 10B Problem 18

## Problem

Rectangle $ABCD$ has $AB = 6$ and $BC = 3$ . Point $M$ is chosen on side $AB$ so that $\angle AMD = \angle CMD$ . What is the degree measure of $\angle AMD$ ?

$\textbf{(A)}\ 15 \qquad\textbf{(B)}\ 30 \qquad\textbf{(C)}\ 45 \qquad\textbf{(D)}\ 60 \qquad\textbf{(E)}\ 75$

## Solution 1
It is given that $\angle AMD \sim \angle CMD$ . Since $\angle AMD$ and $\angle CDM$ are alternate interior angles and $\overline{AB} \parallel \overline{DC}$ , $\angle AMD \cong \angle CDM \longrightarrow \angle CMD \cong \angle CDM$ . Use the Base Angle Theorem to show $\overline{DC} \cong \overline{MC}$ . We know that $ABCD$ is a rectangle , so it follows that $\overline{MC} = 6$ . We notice that $\triangle BMC$ is a $30-60-90$ triangle, and $\angle BMC = 30^{\circ}$ . If we let $x$ be the measure of $\angle AMD,$ then \begin{align*} 2x + 30 &= 180\\ 2x &= 150\\ x &= \boxed{\textbf{(E)} 75} \end{align*}
### Easier Way to Continue
After finding $MC = 6,$ we can continue using trigonometry as follows.
We know that $\angle{BMC} = 180-2x$ and so $\sin (180-2x) = \frac{3}{6} = \frac{1}{2}$
It is obvious that $\sin (30) = \frac{1}{2}$ and so $180-2x=30.$
Solving, we have $x = \boxed{75}$
~mathboy282

## Solution 2 (with trig, not recommended)
Let $\angle{DMC} = \angle{AMD} = \theta$ . If we let $AM = x$ , we have that $MD = \sqrt{x^2 + 9}$ , by the Pythagorean Theorem, and similarily, $MC = \sqrt{x^2 - 12x + 45}$ . Applying the law of cosine, we see that \[2x^2 + 54 - 12x - 2 \sqrt{x^4 - 12x^3 + 54x^2 - 108x + 405} \cdot \cos (\theta) = 36\] and \[\tan (\theta) = \frac{3}{x}\] YAY!!! We have two equations for two variables... that are relatively difficult to deal with. Well, we'll try to solve it. First of all, note that $\sin (\theta) = \frac{3}{\sqrt{x^2+9}}$ , so solving for $\cos (\theta)$ in terms of $x$ , we get that $\cos (\theta) = \frac{x \cdot \sqrt{x^2 + 9}}{x^2 + 9}$ . The equation now becomes
\[2x^2 + 54 - 12x - 2 \sqrt{x^4 - 12x^3 + 54x^2 - 108x + 405} \cdot \frac{x \cdot \sqrt{x^2 + 9}}{x^2 + 9} = 36\] Simplifying, we get
\[4x^4 - 48x^3 + 216x^2 - 432x + 324\]
Now, we apply the quartic formula to get
\[x = 6 \pm 3 \sqrt{3}\]
We can easily see that $x = 6 + 3 \sqrt{3}$ is an invalid solution. Thus, $x = 6 - 3 \sqrt{3}$ .
Finally, since $\tan (\theta) = \frac{3}{6 - 3 \sqrt{3}} = 2 + \sqrt{3}$ , $\theta = \frac{5 + 12n}{12} \pi$ , where $n$ is any integer. Converting to degrees, we have that $\theta = 75 + 180n$ . Since $0 < \theta < 90$ , we have that $\theta = \boxed{75}$ . $\square$
~ilovepi3.14

## Solution 3(Easier Trig)
We have $DC=CM=6$ . By the Pythagorean Theorem, $BM=\sqrt{6^2-3^2}=3\sqrt{3}$ , and thus $AM=6-3\sqrt{3}$ , We have $\tan(AMD)=\frac{6-3\sqrt{3}}{3}=2+\sqrt{3}$ , or $\angle AMD=\boxed{75}$ ~awsomek

## Solution 4 (elimination)
Let $\angle AMD=\angle DMC=\theta$ . Thus, $\angle BMC=180-2\theta\implies\angle MCB=2\theta-90$ . Since all angles should be positive, $\theta>45^\circ$ , narrowing the options to D and E. Trying $60^\circ$ (option D), $\Delta AMD$ is a 30-60-90 triangle. $AD=3$ , so it follows that $AM=\sqrt3$ . Since $\angle BMC=180-2\theta$ , $\angle BMC=60^\circ$ , too. However, that would imply that $\Delta MBC$ is also a $30-60-90$ triangle, which would, in turn, imply that $MB=3\sqrt3$ , since $BC=3$ . We know that $AM+MB=AB$ and $AB=6,$ but we know that $AM=\sqrt3$ and $MB=3\sqrt3$ . $AM+MB$ is clearly not $6$ , so this is not possible. Thus, the answer must be $\boxed{\textbf{(E)}~75}$ . ~ Technodoggo

## Solution 5 (guesstimation)
We draw a diagram. It seems that they are larger than 60 degrees. We try 75, and with the knowledge that $\text{sin}(75^\circ)\approx 0.96$ , and $\text{cos}(75^\circ)\approx 0.26$ , so we have $\text{cot}(75^\circ)\approx \frac{4}{15}$ , and this gives us missing side lengths of 0.8, 5.2, 5.9, and 3.1, which happens to satisfy all equations. So, $\boxed{\textbf{E}}$

## Solution 6 (using trig to express related sides)
Let \(\angle AMD=\angle CMD=x\). Then, \(\angle BMC=180-2x\). \(\tan (x)=\frac{AD}{AM}=\frac{3}{AM}\). Thus, we have \(AM=\frac{3}{\tan (x)}\). Similarly, \(\tan (180-2x)=\frac{BC}{BM}=\frac{3}{BM}\). Thus, we have \(BM=\frac{3}{\tan (180-2x)}\). Using the fact that \(\tan (180-2x)=-\tan (2x)\), we can write \(BM\) as \(\frac{-3}{\tan (2x)}\). Since \(AM+BM=6\), we have \(\frac{3}{\tan (x)}-\frac{3}{\tan (2x)}=6\). \(\tan (2x)=\frac{2\tan x}{1-\tan ^{2}x}\), so \(\frac{3}{\tan (x)}-\frac{3(1-\tan ^{2}x)}{2\tan (x)}=6\). Multiplying both sides by \(2\tan (x)\), we have \(6-3+3\tan ^{2}(x)=12\tan (x)\). Therefore, \(\tan ^{2}(x)-4\tan (x)+1=0\). Solving the quadratic, we have \(\tan (x)=2\pm \sqrt{3}\). If \(\tan (x)=2-\sqrt{3}\), then \(AM=\frac{3}{2-\sqrt{3}}=6+3\sqrt{3}\), which is larger than the side length of \(6\). Therefore, \(\tan (x)=2+\sqrt{3}\), and since \(x\) is between \(0\) and \(180\) degrees, \(x=75\) degrees. ~Spiritmoon_OSU
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .