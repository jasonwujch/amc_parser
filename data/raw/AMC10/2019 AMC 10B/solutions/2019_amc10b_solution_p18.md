# 2019 AMC 10B Problem 18

## Problem

Henry decides one morning to do a workout, and he walks $\tfrac{3}{4}$ of the way from his home to his gym. The gym is $2$ kilometers away from Henry's home. At that point, he changes his mind and walks $\tfrac{3}{4}$ of the way from where he is back toward home. When he reaches that point, he changes his mind again and walks $\tfrac{3}{4}$ of the distance from there back toward the gym. If Henry keeps changing his mind when he has walked $\tfrac{3}{4}$ of the distance toward either the gym or home from the point where he last changed his mind, he will get very close to walking back and forth between a point $A$ kilometers from home and a point $B$ kilometers from home. What is $|A-B|$ ?

$\textbf{(A) } \frac{2}{3} \qquad \textbf{(B) } 1 \qquad \textbf{(C) } 1 \frac{1}{5} \qquad \textbf{(D) } 1 \frac{1}{4} \qquad \textbf{(E) } 1 \frac{1}{2}$

## Solution 1
Let the two points that Henry walks in between be $P$ and $Q$ , with $P$ being closer to home. As given in the problem statement, the distances of the points $P$ and $Q$ from his home are $A$ and $B$ respectively. By symmetry, the distance of point $Q$ from the gym is the same as the distance from home to point $P$ .
Thus, $A = 2 - B$ .
In addition, when he walks from point $Q$ to home, he walks $\frac{3}{4}$ of the distance, ending at point $P$ . Therefore, we know that $B - A = \frac{3}{4}B$ .
By substituting, we get $B - (2-B) = \frac{3}{4}\cdot B$ and we solve to get $B=\dfrac{8}{5}$ , so $A=2-\dfrac{8}{5}=\dfrac{2}{5}$ .
$|A-B|=\left|\dfrac{2}{5}-\dfrac{8}{5} \right|=\frac{6}{5}=\boxed{\textbf{(C) } 1 \frac{1}{5}}$ .

## Solution 2 (Not Rigorous)
We assume that Henry is walking back and forth exactly between points $P$ and $Q$ , with $P$ closer to Henry's home than $Q$ . Denote Henry's home as a point $H$ and the gym as a point $G$ . Then $HP:PQ = 1:3$ and $PQ:QG = 3:1$ , so $HP:PQ:QG = 1:3:1$ . Therefore, $|A-B| = PQ = \frac{3}{1+3+1} \cdot 2 = \frac{6}{5} = \boxed{\textbf{(C) } 1 \frac{1}{5}}$ .

## Solution 3 (Estimation)
Notice how the middle point is \( 2/1 = 1 \). So we write \( 1 = 100/100 \). We choose the points \( 101/100 \) and \( 99/100 \). The average of these points itself is \( 100/100 \). So we need to find a number close to \(100/100\), but not \(100/100\) exactly. The only number that satisfies this is $\boxed{\textbf{(C) } 1 \frac{1}{5}}$ , as it gives \( \frac{120}{100} \).
~Pinotation

## Solution 4 (not rigorous; similar to 2)
Since Henry is very close to walking back and forth between two points, let us denote $A$ closer to his house, and $B$ closer to the gym. Then, let us denote the distance from $A$ to $B$ as $x$ . If Henry was at $B$ and walked $\frac{3}{4}$ of the way, he would end up at $A$ , vice versa. Thus we can say that the distance from $A$ to the gym is $\frac{1}{4}$ the distance from $B$ to his house. That means it is $\frac{1}{3}x$ . This also applies to the other side. Furthermore, we can say $\frac{1}{3}x$ + $x$ + $\frac{1}{3}x$ = $2$ . We solve for $x$ and get $x=\frac{6}{5}$ . Therefore, the answer is $\boxed{\textbf{(C) } 1\frac{1}{5}}$ .
~aryam

## Solution 5
Let $A$ have a distance of $x$ from the home. Then, the distance to the gym is $2-x$ . This means point $B$ and point $A$ are $\frac{3}{4} \cdot (2-x)$ away from one another. It also means that Point $B$ is located at $\frac{3}{4} (2-x) + x.$ So, the distance between the home and point $B$ is also $\frac{3}{4} (2-x) + x.$
It follows that point $A$ must be at a distance of $\frac{3}{4} \left( \frac{3}{4} (2-x) + x \right)$ from point $B$ . However, we also said that this distance has length $\frac{3}{4} (2-x)$ . So, we can set those equal, which gives the equation: \[\frac{3}{4} \left( \frac{3}{4} (2-x) + x \right) = \frac{3}{4} (2-x).\]
Solving, we get $x = \frac{2}{5}$ . This means $A$ is at point $\frac{2}{5}$ and $B$ is at point $\frac{3}{4} \cdot \frac{8}{5} + \frac{2}{5} = \frac{8}{5}.$
So, $|A - B| = \frac{6}{5}=\boxed{\textbf{(C) } 1\frac{1}{5}}.$

## Solution 6 (Rigorous)
Let A be the point closer to Henry’s home, and B be the point closer to the gym. Define $(a_n)$ to be the position of Henry after $2n$ walks. Similarly, define $(b_n)$ to be the position of Henry after $2n - 1$ walks. Thus, $a_1 = \frac{1}{4} \cdot (\frac{3}{4} \cdot 2) = \frac{3}{8}$ and $b_1 = \frac{3}{4} \cdot 2 = \frac{3}{2}$ . We can also deduce that \[a_n = \frac{1}{4} ( \frac{3}{4} (2 - a_{n-1}) + a_{n-1} ) = \frac{1}{16} a_{n-1} + \frac{3}{8}\] ( $2 - a_{n-1}$ is Henry's distance to the gym, so we take $\frac{3}{4}$ of that and add it to our original position. Then, we take $\frac{1}{4}$ of that to obtain Henry's distance from home). Similarly, we can deduce that \[b_n = \frac{3}{4} (2 - \frac{1}{4} b_{n-1}) + \frac{1}{4} b_{n-1} = \frac{1}{16} b_{n-1} + \frac{3}{2}\] Now, we follow the standard procedure to convert this arithmetico geometric recursion into a closed form. Let $a_n - k = \frac{1}{16} (a_{n-1} -k)$ for some constant $k$ . Then, $a_n = \frac{1}{16} a_{n-1} + \frac{15}{16} k$ . So, $\frac{1}{16} a_{n-1} + \frac{15}{16} k = \frac{1}{16} a_{n-1} + \frac{3}{8} \Rightarrow k = \frac{3}{8} \cdot \frac{16}{15} = \frac{2}{5}$ . This means that \[a_n - \frac{2}{5} = \frac{1}{16} (a_{n-1} - \frac{2}{5}) \Rightarrow a_n - \frac{2}{5} = (\frac{1}{16})^{n-1} (a_1 - \frac{2}{5}) = (\frac{1}{16})^{n-1} (\frac{3}{8} - \frac{2}{5}) = (\frac{1}{16})^{n-1} \cdot -\frac{1}{40} \Rightarrow a_n = \frac{2}{5} - \frac{1}{16^{n-1} \cdot 40}\] Now, calculating \[\lim_{n \to \infty} a_n = \lim_{n \to \infty} \frac{2}{5} - \frac{1}{16^{n-1} \cdot 40} = \frac{2}{5} - \lim_{n \to \infty} \frac{1}{16^{n-1} \cdot 40} = \frac{2}{5} - 0 = \frac{2}{5}\] Thus, $A = \frac{2}{5}$ . Taking a similar process for $B$ , we derive that $b_n = \frac{8}{5} - \frac{1}{16^{n-1} \cdot 10}$ , so $B = \lim_{n \to \infty} \frac{8}{5} - \frac{1}{16^{n-1} \cdot 10} = \frac{8}{5}$ . Finally, $|A-B| = |\frac{2}{5} - \frac{8}{5}| = \boxed{\frac{6}{5}}$ .
~ CrazyVideoGamez
### Note
This problem can be estimated by drawing out a diagram. Also, it seems that finding symmetry can be rigorous or lucky, therefore one should understand the algebraic solutions.

## Solution 7
From symmetry, we see that $A+B=2$ after a sufficient amount of steps. Also, if Henry walks back and forth from $A$ to $B$ after a certain amount of time, then we also see that $A=1/4B$ . Then, we obtain the following:
$2-B=1/4B$ —> $2=5/4B$ —> $B=8/5$
$A=1/4(8/5)=2/5$ , $|A-B|=|2/5-8/5|=|-6/5|= \boxed{(C)6/5}$

## Video Solution by OmegaLearn
https://youtu.be/4WttvHavnkM?t=55
~ pi_is_3.14

## Video Solution by On The Spot STEM
https://youtu.be/45kdBy3htOg

## Video Solution by TheBeautyofMath
https://youtu.be/U5PjjZ-5MIQ
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .