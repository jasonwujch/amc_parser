# 2002 AIME I Problem 6

## Problem

The solutions to the system of equations

are $(x_1,y_1)$ and $(x_2,y_2)$ . Find $\log_{30}\left(x_1y_1x_2y_2\right)$ .

## Solution
Let $A=\log_{225}x$ and let $B=\log_{64}y$ .
From the first equation: $A+B=4 \Rightarrow B = 4-A$ .
Plugging this into the second equation yields $\frac{1}{A}-\frac{1}{B}=\frac{1}{A}-\frac{1}{4-A}=1 \Rightarrow A = 3\pm\sqrt{5}$ and thus, $B=1\pm\sqrt{5}$ .
So, $\log_{225}(x_1x_2)=\log_{225}(x_1)+\log_{225}(x_2)=(3+\sqrt{5})+(3-\sqrt{5})=6$ $\Rightarrow x_1x_2=225^6=15^{12}$ .
And $\log_{64}(y_1y_2)=\log_{64}(y_1)+\log_{64}(y_2)=(1+\sqrt{5})+(1-\sqrt{5})=2$ $\Rightarrow y_1y_2=64^2=2^{12}$ .
Thus, $\log_{30}\left(x_1y_1x_2y_2\right) = \log_{30}\left(15^{12}\cdot2^{12} \right) = \log_{30}\left(30^{12} \right) = \boxed{012}$ .
One may simplify the work by applying Vieta's formulas to directly find that $\log x_1 + \log x_2 = 6 \log 225, \log y_1 + \log y_2 = 2 \log 64$ .
These problems are copyrighted © by the Mathematical Association of America.