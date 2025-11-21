# 2023 AMC 8 Problem 2

## Problem

A square piece of paper is folded twice into four equal quarters, as shown below, then cut along the dashed line. When unfolded, the paper will match which of the following figures? [asy] //Restored original diagram. Alter it if you would like, but it was made by TheMathGuyd, // Diagram by TheMathGuyd. I even put the lined texture :) // Thank you Kante314 for inspiring thicker arrows. They do look much better size(0,3cm); path sq = (-0.5,-0.5)--(0.5,-0.5)--(0.5,0.5)--(-0.5,0.5)--cycle; path rh = (-0.125,-0.125)--(0.5,-0.5)--(0.5,0.5)--(-0.125,0.875)--cycle; path sqA = (-0.5,-0.5)--(-0.25,-0.5)--(0,-0.25)--(0.25,-0.5)--(0.5,-0.5)--(0.5,-0.25)--(0.25,0)--(0.5,0.25)--(0.5,0.5)--(0.25,0.5)--(0,0.25)--(-0.25,0.5)--(-0.5,0.5)--(-0.5,0.25)--(-0.25,0)--(-0.5,-0.25)--cycle; path sqB = (-0.5,-0.5)--(-0.25,-0.5)--(0,-0.25)--(0.25,-0.5)--(0.5,-0.5)--(0.5,0.5)--(0.25,0.5)--(0,0.25)--(-0.25,0.5)--(-0.5,0.5)--cycle; path sqC = (-0.25,-0.25)--(0.25,-0.25)--(0.25,0.25)--(-0.25,0.25)--cycle; path trD = (-0.25,0)--(0.25,0)--(0,0.25)--cycle; path sqE = (-0.25,0)--(0,-0.25)--(0.25,0)--(0,0.25)--cycle; filldraw(sq,mediumgrey,black); draw((0.75,0)--(1.25,0),currentpen+1,Arrow(size=6)); //folding path sqside = (-0.5,-0.5)--(0.5,-0.5); path rhside = (-0.125,-0.125)--(0.5,-0.5); transform fld = shift((1.75,0))*scale(0.5); draw(fld*sq,black); int i; for(i=0; i<10; i=i+1) { draw(shift(0,0.05*i)*fld*sqside,deepblue); } path rhedge = (-0.125,-0.125)--(-0.125,0.8)--(-0.2,0.85)--cycle; filldraw(fld*rhedge,grey); path sqedge = (-0.5,-0.5)--(-0.5,0.4475)--(-0.575,0.45)--cycle; filldraw(fld*sqedge,grey); filldraw(fld*rh,white,black); int i; for(i=0; i<10; i=i+1) { draw(shift(0,0.05*i)*fld*rhside,deepblue); } draw((2.25,0)--(2.75,0),currentpen+1,Arrow(size=6)); //cutting transform cut = shift((3.25,0))*scale(0.5); draw(shift((-0.01,+0.01))*cut*sq); draw(cut*sq); filldraw(shift((0.01,-0.01))*cut*sq,white,black); int j; for(j=0; j<10; j=j+1) { draw(shift(0,0.05*j)*cut*sqside,deepblue); } draw(shift((0.01,-0.01))*cut*(0,-0.5)--shift((0.01,-0.01))*cut*(0.5,0),dashed); //Answers Below, but already Separated //filldraw(sqA,grey,black); //filldraw(sqB,grey,black); //filldraw(sq,grey,black); //filldraw(sqC,white,black); //filldraw(sq,grey,black); //filldraw(trD,white,black); //filldraw(sq,grey,black); //filldraw(sqE,white,black); [/asy]

[asy] // Diagram by TheMathGuyd. size(0,7.5cm); path sq = (-0.5,-0.5)--(0.5,-0.5)--(0.5,0.5)--(-0.5,0.5)--cycle; path rh = (-0.125,-0.125)--(0.5,-0.5)--(0.5,0.5)--(-0.125,0.875)--cycle; path sqA = (-0.5,-0.5)--(-0.25,-0.5)--(0,-0.25)--(0.25,-0.5)--(0.5,-0.5)--(0.5,-0.25)--(0.25,0)--(0.5,0.25)--(0.5,0.5)--(0.25,0.5)--(0,0.25)--(-0.25,0.5)--(-0.5,0.5)--(-0.5,0.25)--(-0.25,0)--(-0.5,-0.25)--cycle; path sqB = (-0.5,-0.5)--(-0.25,-0.5)--(0,-0.25)--(0.25,-0.5)--(0.5,-0.5)--(0.5,0.5)--(0.25,0.5)--(0,0.25)--(-0.25,0.5)--(-0.5,0.5)--cycle; path sqC = (-0.25,-0.25)--(0.25,-0.25)--(0.25,0.25)--(-0.25,0.25)--cycle; path trD = (-0.25,0)--(0.25,0)--(0,0.25)--cycle; path sqE = (-0.25,0)--(0,-0.25)--(0.25,0)--(0,0.25)--cycle; //ANSWERS real sh = 1.5; label("$\textbf{(A)}$",(-0.5,0.5),SW); label("$\textbf{(B)}$",shift((sh,0))*(-0.5,0.5),SW); label("$\textbf{(C)}$",shift((2sh,0))*(-0.5,0.5),SW); label("$\textbf{(D)}$",shift((0,-sh))*(-0.5,0.5),SW); label("$\textbf{(E)}$",shift((sh,-sh))*(-0.5,0.5),SW); filldraw(sqA,mediumgrey,black); filldraw(shift((sh,0))*sqB,mediumgrey,black); filldraw(shift((2*sh,0))*sq,mediumgrey,black); filldraw(shift((2*sh,0))*sqC,white,black); filldraw(shift((0,-sh))*sq,mediumgrey,black); filldraw(shift((0,-sh))*trD,white,black); filldraw(shift((sh,-sh))*sq,mediumgrey,black); filldraw(shift((sh,-sh))*sqE,white,black); [/asy]

## Solution
Notice that when we unfold the paper along the vertical fold line, we get the following shape:
[asy] size(90); path sq = (-0.5,0)--(0.5,0)--(0.5,0.5)--(-0.5,0.5)--cycle; path trE = (-0.25,0)--(0.25,0)--(0,0.25)--cycle; real sh = 1.5; filldraw(shift((sh,-sh))*sq,mediumgrey,black); filldraw(shift((sh,-sh))*trE,white,black); size(90); path sq = (-0.5,-0.5)--(0.5,-0.5)--(0.5,0.5)--(-0.5,0.5)--cycle; path sqE = (-0.25,0)--(0,-0.25)--(0.25,0)--(0,0.25)--cycle; real sh = 1.5; filldraw(shift((sh,-sh))*sq,mediumgrey,black); filldraw(shift((sh,-sh))*sqE,white,black); [/asy]
Therefore the answer is $\boxed{\textbf{(E)}}$ .
~MrThinker

## Solution 2
When you fold the paper in that specific way, it shows the top left square. That means that any cut you make on that folded part will look like that on that top left square. Since it is folded into four parts, the cut will reflect on all of the other 3 parts. Since there is a cut diagonally on the bottom right of that square, that will reflect on the other squares, making the shape of $\boxed{\textbf{(E)}}$ [asy] size(90); path sq = (-0.5,0)--(0.5,0)--(0.5,0.5)--(-0.5,0.5)--cycle; path trE = (-0.25,0)--(0.25,0)--(0,0.25)--cycle; real sh = 1.5; filldraw(shift((sh,-sh))*sq,mediumgrey,black); filldraw(shift((sh,-sh))*trE,white,black); size(90); path sq = (-0.5,-0.5)--(0.5,-0.5)--(0.5,0.5)--(-0.5,0.5)--cycle; path sqE = (-0.25,0)--(0,-0.25)--(0.25,0)--(0,0.25)--cycle; real sh = 1.5; filldraw(shift((sh,-sh))*sq,mediumgrey,black); filldraw(shift((sh,-sh))*sqE,white,black); [/asy]
~AliceDubbleYou

## Video Solution by CoolMathProblms
https://youtu.be/Pf93RGtKo1I?feature=shared&t=50
### *Easy Video Explanation by MathTalks_Now*
https://studio.youtube.com/video/PMOeiGLkDH0/edit

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=76 ~hsnacademy

## Video Solution by Math-X (Smart and Simple)
https://youtu.be/Ku_c1YHnLt0?si=ZucTBcN42MKGX2Ty&t=115 ~Math-X

## Video Solution (How to Creatively THINK!!!)
https://youtu.be/suFxwnH-ak8 ~Education the Study of everything

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=5658

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=EcrktBc8zrM

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=67

## Video Solution by WhyMath
https://youtu.be/z6SxQkQACjo?si=WJAMIdKzUO7oGLGc

## Video Solution by harungurcan
https://www.youtube.com/watch?v=35BW7bsm_Cg&t=97s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/octW02FH-iU
### See Also