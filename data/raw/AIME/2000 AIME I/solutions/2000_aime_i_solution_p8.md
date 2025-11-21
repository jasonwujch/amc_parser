# 2000 AIME I Problem 8

## Problem

A container in the shape of a right circular cone is $12$ inches tall and its base has a $5$ -inch radius . The liquid that is sealed inside is $9$ inches deep when the cone is held with its point down and its base horizontal. When the liquid is held with its point up and its base horizontal, the height of the liquid is $m - n\sqrt [3]{p},$ from the base where $m,$ $n,$ and $p$ are positive integers and $p$ is not divisible by the cube of any prime number. Find $m + n + p$ .

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4

## Solution

## Solution 1
The scale factor is uniform in all dimensions, so the volume of the liquid is $\left(\frac{3}{4}\right)^{3}$ of the container. The remaining section of the volume is $\frac{1-\left(\frac{3}{4}\right)^{3}}{1}$ of the volume, and therefore $\frac{\left(1-\left(\frac{3}{4}\right)^{3}\right)^{1/3}}{1}$ of the height when the vertex is at the top.
So, the liquid occupies $\frac{1-\left(1-\left(\frac{3}{4}\right)^{3}\right)^{1/3}}{1}$ of the height, or $12-12\left(1-\left(\frac{3}{4}\right)^{3}\right)^{1/3}=12-3\left(37^{1/3}\right)$ . Thus $m+n+p=\boxed{052}$ .

## Solution 2
(Computational) The volume of a cone can be found by $V = \frac{\pi}{3}r^2h$ . In the second container, if we let $h',r'$ represent the height, radius (respectively) of the air (so $12 -h'$ is the height of the liquid), then the volume of the liquid can be found by $\frac{\pi}{3}r^2h - \frac{\pi}{3}(r')^2h'$ .
By similar triangles , we find that the dimensions of the liquid in the first cone to the entire cone is $\frac{3}{4}$ , and that $r' = \frac{rh'}{h}$ ; equating,
\begin{align*}\frac{\pi}{3}\left(\frac{3}{4}r\right)^2 \left(\frac{3}{4}h\right) &= \frac{\pi}{3}\left(r^2h - \left(\frac{rh'}{h}\right)^2h'\right)\\ \frac{37}{64}r^2h &= \frac{r^2}{h^2}(h')^3 \\ h' &= \sqrt[3]{\frac{37}{64} \cdot 12^3} = 3\sqrt[3]{37}\end{align*}
Thus the answer is $12 - h' = 12-3\sqrt[3]{37}$ , and $m+n+p=\boxed{052}$ .

## Solution 3
From the formula $V=\frac{\pi r^2h}{3}$ , we can find that the volume of the container is $100\pi$ . The cone formed by the liquid is similar to the original, but scaled down by $\frac{3}{4}$ in all directions, so its volume is $100\pi*\frac{27}{64}=\frac{675\pi}{16}$ . The volume of the air in the container is the volume of the container minus the volume of the liquid, which is $\frac{925\pi}{16}$ , which is $\frac{37}{64}$ of the volume of the container. When the point faces upwards, the air forms a cone at the top of the container. This cone must have $\sqrt[3]{\frac{37}{64}}=\frac{\sqrt[3]{37}}{4}$ of the height of the container. This means that the height of the liquid is $12\left(1-\frac{\sqrt[3]{37}}{4}\right)=12-3\sqrt[3]{37}$ inches, so our answer is $\boxed{052}$ . Solution by Zeroman

## Solution 4
We find that the volume of the cone is $100\pi$ .
The volume of the cone with height 9 is $\frac{675}{16}\pi$ .
The difference between the two volumes is $\frac{925}{16}\pi$ . Note that this is the volume of the cone essentially 'on top of' the frustum described in the problem when the liquid is held with the base horizontal.
We can express the volume as $x^2\pi\cdot\frac{12}{5}x\cdot\frac{1}{3}$ , where x is the radius of the cone.
Solving this equation, we get $x=\frac{5\sqrt[3]{37}}{4}$ . The height of this cone is $\frac{12}{5}$ of the radius.
Then we subtract the value from the height, 12, to get our answer: $12-3\sqrt[3]{37}$ .
Therefore, our answer is $12+3+37=\boxed{52}$ . ~MC413551
These problems are copyrighted © by the Mathematical Association of America.