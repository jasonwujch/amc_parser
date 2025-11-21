# 2020 AMC 8 Problem 22

## Problem

When a positive integer $N$ is fed into a machine, the output is a number calculated according to the rule shown below.

[asy] size(300); defaultpen(linewidth(0.8)+fontsize(13)); real r = 0.05; draw((0.9,0)--(3.5,0),EndArrow(size=7)); filldraw((4,2.5)--(7,2.5)--(7,-2.5)--(4,-2.5)--cycle,gray(0.65)); fill(circle((5.5,1.25),0.8),white); fill(circle((5.5,1.25),0.5),gray(0.65)); fill((4.3,-r)--(6.7,-r)--(6.7,-1-r)--(4.3,-1-r)--cycle,white); fill((4.3,-1.25+r)--(6.7,-1.25+r)--(6.7,-2.25+r)--(4.3,-2.25+r)--cycle,white); fill((4.6,-0.25-r)--(6.4,-0.25-r)--(6.4,-0.75-r)--(4.6,-0.75-r)--cycle,gray(0.65)); fill((4.6,-1.5+r)--(6.4,-1.5+r)--(6.4,-2+r)--(4.6,-2+r)--cycle,gray(0.65)); label("$N$",(0.45,0)); draw((7.5,1.25)--(11.25,1.25),EndArrow(size=7)); draw((7.5,-1.25)--(11.25,-1.25),EndArrow(size=7)); label("if $N$ is even",(9.25,1.25),N); label("if $N$ is odd",(9.25,-1.25),N); label("$\frac N2$",(12,1.25)); label("$3N+1$",(12.6,-1.25)); [/asy] For example, starting with an input of $N=7,$ the machine will output $3 \cdot 7 +1 = 22.$ Then if the output is repeatedly inserted into the machine five more times, the final output is $26.$ \[7 \to 22 \to 11 \to 34 \to 17 \to 52 \to 26\] When the same $6$ -step process is applied to a different starting value of $N,$ the final output is $1.$ What is the sum of all such integers $N?$ \[N \to \rule{0.5cm}{0.15mm} \to \rule{0.5cm}{0.15mm} \to \rule{0.5cm}{0.15mm} \to \rule{0.5cm}{0.15mm} \to \rule{0.5cm}{0.15mm} \to 1\] $\textbf{(A) }73 \qquad \textbf{(B) }74 \qquad \textbf{(C) }75 \qquad \textbf{(D) }82 \qquad \textbf{(E) }83$

## Solution 1
We start with final output of $1$ and work backward, taking cares to consider all possible inputs that could have resulted in any particular output. This produces following set of possibilities each stage: \[\{1\}\rightarrow\{2\}\rightarrow\{4\}\rightarrow\{1,8\}\rightarrow\{2,16\}\rightarrow\{4,5,32\}\rightarrow\{1,8,10,64\}\] where, for example, $2$ must come from $4$ (as there is no integer $n$ satisfying $3n+1=2$ ), but $16$ could come from $32$ or $5$ (as $\frac{32}{2} = 3 \cdot 5 + 1 = 16$ , and $32$ is even while $5$ is odd). By construction, last set in this sequence contains all the numbers which will lead to number $1$ to end of the $6$ -step process, and sum is $1+8+10+64=\boxed{\textbf{(E) }83}$ .

## Solution 2 (variant of Solution 1)
As in Solution 1, we work backwards from $1$ , this time showing the possible cases in a tree diagram:
[asy] // Upper branches draw((-6, 1.5)--(-5, 1)--(-3, 1)--(-2,0)--(0, 0)); draw((-6, 0.5)--(-5, 1)); // Lower branches draw((-6, -1.5)--(-5, -1.5)--(-4, -1)--(-3, -1)--(-2, 0)); draw((-6, -0.5)--(-5, -0.5)--(-4, -1)); label("$1$", (0, 0), UnFill(0.1mm)); label("$2$", (-1, 0), UnFill(0.1mm)); label("$4$", (-2, 0), UnFill(0.1mm)); // Upper branches label("$1$", (-3, 1), UnFill(0.1mm)); label("$2$", (-4, 1), UnFill(0.1mm)); label("$4$", (-5, 1), UnFill(0.1mm)); label("$\textbf{8}$", (-6, 1.5), UnFill(0.1mm)); label("$\textbf{1}$", (-6, 0.5), UnFill(0.1mm)); // Lower branches label("$8$", (-3, -1), UnFill(0.1mm)); label("$16$",(-4, -1), UnFill(0.1mm)); label("$5$", (-5, -0.5), UnFill(0.1mm)); label("$32$", (-5, -1.5), UnFill(0.1mm)); label("$\textbf{10}$", (-6, -0.5), UnFill(0.1mm)); label("$\textbf{64}$", (-6, -1.5), UnFill(0.1mm)); [/asy]
The possible numbers are those at the "leaves" of the tree (the ends of the various branches), which are $1$ , $8$ , $64$ , and $10$ . Thus the answer is $1+8+64+10=\boxed{\textbf{(E) }83}$ .

## Solution 3 (algebraic)
We begin by finding the inverse of the function that the machine uses. Call the input $I$ and the output $O$ . If $I$ is even, $O=\frac{I}{2}$ , and if $I$ is odd, $O=3I+1$ . We can therefore see that $I=2O$ when $I$ is even and $I=\frac{O-1}{3}$ when $I$ is odd. Therefore, starting with $1$ , if $I$ is even, $I=2$ , and if $I$ is odd, $I=0$ , but the latter is not valid since $0$ is not actually odd. This means that the 2nd-to-last number in the sequence has to be $2$ . Now, substituting $2$ into the inverse formulae, if $I$ is even, $I=4$ (which is indeed even), and if $I$ is odd, $I=\frac{1}{3}$ , which is not an integer. This means the 3rd-to-last number in the sequence has to be $4$ . Substituting in $4$ , if $I$ is even, $I=8$ , but if $I$ is odd, $I=1$ . Both of these are valid solutions, so the 4th-to-last number can be either $1$ or $8$ . If it is $1$ , then by the argument we have just made, the 5th-to-last number has to be $2$ , the 6th-to-last number has to be $4$ , and the 7th-to-last number, which is the first number, must be either $1$ or $8$ . In this way, we have ultimately found two solutions: $N=1$ and $N=8$ .
On the other hand, if the 4th-to-last number is $8$ , substituting $8$ into the inverse formulae shows that the 5th-to-last number is either $16$ or $\frac{7}{3}$ , but the latter is not an integer. Substituting $16$ shows that if $I$ is even, $I=32$ , but if I is odd, $I=5$ , and both of these are valid. If the 6th-to-last number is $32$ , then the first number must be $64$ , since $\frac{31}{3}$ is not an integer; if the 6th-to-last number is $5,$ then the first number has to be $10$ , as $\frac{4}{3}$ is not an integer. This means that, in total, there are $4$ solutions for $N$ , specifically, $1$ , $8$ , $10$ , and $64$ , which sum to $\boxed{\textbf{(E) }83}$ .
### Remark
This function is known as the Collatz conjecture stating that every counting number ( $1$ , $2$ , $3$ , $4$ , $...$ ) will eventually output the sequence ( $4$ , $2$ , $1$ , $4$ , $2$ , $1$ ， $...$ ) if put through the function enough times. It is an unsolved conjecture but has been tested by brute force for every starting number up to $2^{68}$ . Some people had tried multiple times, only to fail.

## Video Solution by Mathionaire (Clear and fast explanation)
https://www.youtube.com/watch?v=BdeoMh1PKp0&t=98s
~Mathionaire

## Video Solution by TheMathGeek (Working backwards- Takes 1 minute only!!)
https://www.youtube.com/watch?v=xjRLOvV4IL8&t=1s
~TheMathGeek

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/UnVo6jZ3Wnk?si=l0KAetejsLeFS2We&t=4703
~Math-X

## Video Solution (🚀 Just 2 minutes! 🚀)
https://youtu.be/fEux4gUZFbM
~ Education, the Study of Everything

## Video Solution
https://youtu.be/Tf_80QNGmsI
Please like and subscribe!

## Video Solution by OmegaLearn
https://youtu.be/ytTRdD-LVlo?t=755
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=tItOXq9kvu4 ~David

## Video Solution by Mathiscool
https://www.youtube.com/watch?v=aLq7LrZZGhc

## Video Solution by WhyMath
https://youtu.be/ZrDCymOhDdI
~savannahsolver

## Video Solutions
https://youtu.be/lhDFmiKNPBg ~ The Learning Royal

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=1347
~Interstigation

## Video Solution by STEMbreezy
https://youtu.be/wq8EUCe5oQU?t=83
~STEMbreezy
### Note
This problem is related to a famous unsolved problem, the Collatz Conjecture , also known as the Hailstone Problem , which essentially asks whether or not integer $n$ , repeatedly put in the machine arbitrarily many times, will eventually reach $1$ .