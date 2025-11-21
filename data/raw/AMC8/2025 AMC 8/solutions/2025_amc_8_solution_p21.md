# 2025 AMC 8 Problem 21

## Problem

The Konigsberg School has assigned grades 1 through 7 to pods $A$ through $G$ , one grade per pod. Some of the pods are connected by walkways, as shown in the figure below. The school noticed that each pair of connected pods has been assigned grades differing by 2 or more grade levels. (For example, grades 1 and 2 will not be in pods directly connected by a walkway.) What is the sum of the grade levels assigned to pods $C, E$ , and $F$ ?

[asy] // Asymptote by aoum size(6cm); void walkway(path w) { draw(w,black+3bp); draw(w,white+2bp); } void pod(pair P, string s, pen p=white) { path box = scale(.2)*((-1,-1)--(-1,1)--(1,1)--(1,-1)--cycle); filldraw(shift(P)*box,p,black); label("$"+s+"$",P); } pair A,B,C,D,E,F,G; C = (0.5,0); A = (1.5,2); B = (2,1); D = (2.5,0); E = (4,-0.5); F = (4.5,1); G = (3.5,2); walkway(A--B); walkway(B--C); walkway(A..(A+C)/2+(-.5,.5)..C); walkway(C--D); walkway(D--E); walkway(C..(C+E)/2+(-.2,-.5)..E); walkway(B--F); walkway(C--F); walkway(E..(E+F)/2+(.2,-.1)..F); walkway(A--F); walkway(A--G); walkway(G..(G+F)/2+(.2,.2)..F); pod(A,"A"); pod(B,"B"); pod(C,"C",lightgray); pod(D,"D"); pod(E,"E",lightgray); pod(F,"F",lightgray); pod(G,"G"); [/asy]

$\textbf{(A)}~12\qquad\textbf{(B)}~13\qquad\textbf{(C)}~14\qquad\textbf{(D)}~15\qquad\textbf{(E)}~16$

## Solution 1
The key observation for this solution is to observe that pods $C$ and $F$ both have degree 5; that is, they are connected to five other pods. This implies that $C$ and $F$ must contain grades 1 and 7 in either order (if $C$ or $F$ contained any of grades 2, 3, 4, 5, or 6, then there would only be four possible grades for five pods, a contradiction). It does not matter which grade $C$ and $F$ gets (see Solution 2 below), so we will assume that pod $C$ is assigned grade 1, and pod $F$ is assigned grade 7.
Next, pod $D$ is the only pod which is not adjacent to pod $F$ , so pod $D$ must be assigned grade 6. Similarly, pod $G$ must be assigned grade 2.
Lastly, we need to assign grades 3, 4, and 5 to pods $A$ , $B$ , and $E$ . Note that $A$ and $B$ are adjacent; therefore, pods $A$ and $B$ must contain grades 3 and 5. We conclude that $E$ must be assigned grade 4. The requested sum is $1+4+7 = \mathbf{(A)\,} 12$ .

## Solution 2 (Fast)
Suppose that we replaced each label $x$ with $8-x$ . That is, we replaced the grade $a$ assigned to $A$ with the grade $8-a$ , the grade $b$ assigned to $B$ with $8-b$ , and so on. We claim that if the initial labeling is valid (i.e., each pair of connected pods has grades differing by 2 or more), then so will the new labeling. This follows as if $|x-y| \ge 2$ , then $|(8-x)-(8-y)|=|-x+y| = |x-y| \ge 2$ . This shows that if there is an assignment $(a,b,c,d,e,f,g)$ of grades to the pods, where $\{a,b,\ldots,g\} = \{1,2,\ldots,7\}$ , then there is a second, valid assignment.
Because this is an AMC 8 problem and only one answer is correct, we can conclude that $c+e+f = (8-c)+(8-e)+(8-f)$ . Simplifying and solving for $c+e+f$ gives $c+e+f = \mathbf{(A)\,} 12$ .
-scrabbler94

## Video Solution 1 by Thinking Feet
https://youtu.be/PKMpTS6b988?t=3510

## Video Solution 2 in Less Than 2 Minutes by Dr. Xue's Math School
https://youtu.be/rx9kwqXeTbM
This is our first video posted on the AoPS website. Our goal is to help students learn more efficiently.

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/VP7g-s8akMY?si=qVENFSXALJsh0DvX&t=2948 ~hsnacademy

## Video Solution by Dr. David
https://youtu.be/OF3kt3zuYf0
### See Also