# 2003 AIME I Problem 11

## Problem

An angle $x$ is chosen at random from the interval $0^\circ < x < 90^\circ.$ Let $p$ be the probability that the numbers $\sin^2 x, \cos^2 x,$ and $\sin x \cos x$ are not the lengths of the sides of a triangle. Given that $p = d/n,$ where $d$ is the number of degrees in $\text{arctan}$ $m$ and $m$ and $n$ are positive integers with $m + n < 1000,$ find $m + n.$

## Solution
Note that the three expressions are symmetric with respect to interchanging $\sin$ and $\cos$ , and so the probability is symmetric around $45^\circ$ . Thus, take $0 < x < 45$ so that $\sin x < \cos x$ . Then $\cos^2 x$ is the largest of the three given expressions and those three lengths not forming a triangle is equivalent to a violation of the triangle inequality
\[\cos^2 x > \sin^2 x + \sin x \cos x\]
This is equivalent to
\[\cos^2 x - \sin^2 x > \sin x \cos x\]
and, using some of our trigonometric identities , we can re-write this as $\cos 2x > \frac 12 \sin 2x$ . Since we've chosen $x \in (0, 45)$ , $\cos 2x > 0$ so
\[2 > \tan 2x \Longrightarrow x < \frac 12 \arctan 2.\]
The probability that $x$ lies in this range is $\frac 1{45} \cdot \left(\frac 12 \arctan 2\right) = \frac{\arctan 2}{90}$ so that $m = 2$ , $n = 90$ and our answer is $\boxed{092}$ .

## Solution 2 (Complementary Counting)
We seek a complementary counting argument, where we look for the probability that $\sin^2 x$ , $\cos^2 x$ and $\sin x \cos x$ form the side lengths of a triangle.
By the triangle inequality, we must have the following three inequalities to be true: \[\sin^2 x + \cos^2 x > \sin x \cos x\] \[\sin^2 x + \sin x \cos x > \cos^2 x\] \[\cos^2 x + \sin x \cos x > \sin^2 x\] The first inequality will always hold since we have $\sin^2 x + \cos^2 x = 1$ , and $1 > \sin x \cos x$ for all $x$ (The maximum value of $\sin x \cos x$ is $\frac{1}{2}$ when $\sin x = \cos x = \frac{\sqrt{2}}{2}$ ).
Now, we examine the second inequality $\sin^2 x + \sin x \cos x > \cos^2 x$ . If we subtract $\sin^2 x$ from both sides, we have $\sin x \cos x > \cos^2 x - \sin^2 x$ . Aha! This resembles our sine and cosine double angle identities. Therefore, our inequality is now $\sin 2x > 2\cos 2x$ . We can divide both sides by $\cos 2x$ and we have $\tan 2x > 2$ . The solutions to this occur when $45 \geq x > \frac{\arctan 2}{2}$ .
(To understand why it must be $x >$ , we can draw the unit circle, and notice as x moves from $\frac{\arctan 2}{2}$ to $90$ , $\tan x$ approaches $\infty$ . We must cap $x$ at $45$ , since if $x > 45$ , $2x > 90$ , and $\tan x$ will be negative.)
Next, we examine the third inequality, $\cos^2 x + \sin x \cos x > \sin^2 x$ . Once again, we can get our double angle identities for sine and cosine by subtracting $\cos^2 2x$ from both sides. We have, $\sin x \cos x > \sin^2 x -\cos^2 x \to \sin 2x > -2\cos 2x$ .
Next, we again, divide by $\cos 2x$ to produce a $\tan 2x$ (we do this because one trig function is easier to deal with than 2). However, if $\cos 2x > 0$ , we do not need to flip the sign since $\sin 2x >0$ , and so if $\cos 2x >0$ , all values for which that is true satisfy the inequality. So we only consider if $\cos 2x < 0$ , and when we divide by a negative, we must flip the sign. Thus we have $\tan 2x < -2$ .
We can take the $\arctan$ of both sides, and we have $\frac{\arctan -2}{2}> x \geq 45$ . Once again, to better understand this, we can draw the angle $x$ for which $\tan 2x = -2$ , and we notice as $2x$ moves to $x=90$ , $\tan 2x$ approaches $- \infty$ . We must cap $x$ at $45$ since if $x<45$ , we have $\tan 2x > 0$ .
Notice that if we draw the terminal points for $\frac{\arctan 2}{2}$ and $\frac{\arctan -2}{2}$ , they have the same smaller angle with the x and y axis respectively. This means the range of degree measures for which our inequalities hold is $90 - \frac{\arctan 2}{2} > x > \frac{\arctan 2}{2}$ which has an area of $90 - \arctan 2$ . However, we want the complement of this, which has an area of $90 - (90 - \arctan 2) = \arctan 2$ . Therefore, the desired probability is $\frac{\arctan2}{90}$ , and so $m+n=2+90=92$ .
-BossLu99
These problems are copyrighted © by the Mathematical Association of America.