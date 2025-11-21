# 2003 AIME I Problem 10

## Problem

Triangle $ABC$ is isosceles with $AC = BC$ and $\angle ACB = 106^\circ.$ Point $M$ is in the interior of the triangle so that $\angle MAC = 7^\circ$ and $\angle MCA = 23^\circ.$ Find the number of degrees in $\angle CMB.$

1 Problem

- 1 Problem

- 2 Solutions 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4 2.5 Solution 5 (Ceva) 2.6 Solution 6

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4

- 2.5 Solution 5 (Ceva)

- 2.6 Solution 6

## Solutions

## Solution 1
Take point $N$ inside $\triangle ABC$ such that $\angle CBN = 7^\circ$ and $\angle BCN = 23^\circ$ .
$\angle MCN = 106^\circ - 2\cdot 23^\circ = 60^\circ$ . Also, since $\triangle AMC$ and $\triangle BNC$ are congruent (by ASA), $CM = CN$ . Hence $\triangle CMN$ is an equilateral triangle , so $\angle CNM = 60^\circ$ .
Then $\angle MNB = 360^\circ - \angle CNM - \angle CNB = 360^\circ - 60^\circ - 150^\circ = 150^\circ$ . We now see that $\triangle MNB$ and $\triangle CNB$ are congruent. Therefore, $CB = MB$ , so $\angle CMB = \angle MCB = \boxed{83^\circ}$ .

## Solution 2
From the givens, we have the following angle measures : $m\angle AMC = 150^\circ$ , $m\angle MCB = 83^\circ$ . If we define $m\angle CMB = \theta$ then we also have $m\angle CBM = 97^\circ - \theta$ . Then apply the Law of Sines to triangles $\triangle AMC$ and $\triangle BMC$ to get
\[\frac{\sin 150^\circ}{\sin 7^\circ} = \frac{AC}{CM} = \frac{BC}{CM} = \frac{\sin \theta}{\sin (97^\circ - \theta)}\]
Clearing denominators , evaluating $\sin 150^\circ = \frac 12$ and applying one of our trigonometric identities to the result gives
\[\frac{1}{2} \cos (7^\circ - \theta )= \sin 7^\circ \sin \theta\]
and multiplying through by 2 and applying the double angle formulas gives
\[\cos 7^\circ\cos\theta + \sin7^\circ\sin\theta = 2 \sin7^\circ \sin\theta\]
and so $\cos 7^\circ \cos \theta = \sin 7^\circ \sin\theta \Longleftrightarrow \tan 7^{\circ} = \cot \theta$ ; since $0^\circ < \theta < 180^\circ$ , we must have $\theta = 83^\circ$ , so the answer is $\boxed{83}$ .

## Solution 3
Without loss of generality , let $AC = BC = 1$ . Then, using the Law of Sines in triangle $AMC$ , we get $\frac {1}{\sin 150} = \frac {MC}{\sin 7}$ , and using the sine addition formula to evaluate $\sin 150 = \sin (90 + 60)$ , we get $MC = 2 \sin 7$ .
Then, using the Law of Cosines in triangle $MCB$ , we get $MB^2 = 4\sin^2 7 + 1 - 4\sin 7(\cos 83) = 1$ , since $\cos 83 = \sin 7$ . So triangle $MCB$ is isosceles, and $\angle CMB = \boxed{83}$ .

## Solution 4
Note: A diagram would be much appreciated; I cannot make one since I'm bad at asymptote. Also, please make this less cluttered :) ~tauros
First, take point $E$ outside of $\triangle{ABC}$ so that $\triangle{CEB}$ is equilateral. Then, connect $A$ , $C$ , and $M$ to $E$ . Also, let $ME$ intersect $AB$ at $F$ . $\angle{MCE} = 83^\circ - 60^\circ = 23^\circ$ , $CE = AB$ , and (trivially) $CM = CM$ , so $\triangle{MCE} \cong \triangle{MCA}$ by SAS congruence. Also, $\angle{CMA} = \angle{CME} = 150^\circ$ , so $\angle{AME} = 60^\circ$ , and $AM = ME$ , making $\triangle{AME}$ also equilateral. (it is isosceles with a $60^\circ$ angle) $\triangle{MAF} \cong \triangle{EAF}$ by SAS ( $MA = AE$ , $AF = AF$ , and $m\angle{MAF} = m\angle{EAF} = 30^\circ$ ), and $\triangle{MAB} \cong \triangle{EAB}$ by SAS ( $MA = AE$ , $AB = AB$ , and $m\angle{MAB} = m\angle{EAB} = 30^\circ$ ). Thus, $\triangle{BME}$ is isosceles, with $m\angle{BME} = m\angle{BEM} = 60^\circ + 7^\circ = 67^\circ$ . Also, $\angle{EMB} + \angle {CMB} = \angle{CME} = 150^\circ$ , so $\angle{CME} = 150^\circ - 67^\circ = \boxed{83^\circ}$ .

## Solution 5 (Ceva)
Noticing that we have three concurrent cevians, we apply Ceva's theorem:
\[(\sin \angle ACM)(\sin \angle BAM)(\sin \angle CBM) = (\sin \angle CAM)(\sin \angle ABM)(\sin \angle BCM)\] \[(\sin 23)(\sin 30)(\sin x) = (\sin 7)(\sin 37-x)(\sin 83)\]
using the fact that $\sin 83 = \cos 7$ and $(\sin 7)(\cos 7) = 1/2 (\sin 14)$ we have:
\[(\sin 23)(\sin x) = (\sin 14)(\sin 37-x)\]
By inspection, $x=14^\circ$ works, so the answer is $180-83-14= \boxed{083}$

## Solution 6
Let $\angle{APC} = \theta^{\circ}$ Using sine rule on $\triangle{APB}, \triangle{APC}$ , letting $AP=d$ we get : $\frac{d}{1} = \frac{\sin{7^{\circ}}}{\sin{150^{\circ}}} = 2\sin{7^{\circ}}= \frac{\sin{14^{\circ}}}{\cos{7^{\circ}}}= \frac{\sin{14^{\circ}}}{\sin{83^{\circ}}}= \frac{\sin{(97-\theta)^{\circ}}}{\sin{\theta^{\circ}}}$ Simplifying, we get that $\cos{(14-\theta)^{\circ}}-\cos{(14+\theta)^{\circ}}=\cos{(14-\theta)^{\circ}}-\cos{(180-\theta)^{\circ}},$ from where $\cos{(14-\theta)^{\circ}}=\cos{(180-\theta)^{\circ}}$ Simplifying more, we get that $\sin{97^{\circ}} \cdot \sin{(\theta-83)^{\circ}} = 0$ , so $\theta = 83^{\circ}$ NOTE: The simplifications were carried out by the product-to-sum and sum-to-product identities ~Prabh1512
These problems are copyrighted © by the Mathematical Association of America.