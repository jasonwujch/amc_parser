# 2006 AMC 10A Problem 12

## Problem

Rolly wishes to secure his dog with an 8-foot rope to a square shed that is 16 feet on each side. His preliminary drawings are shown.

[asy] size(150); pathpen = linewidth(0.6); defaultpen(fontsize(10)); D((0,0)--(16,0)--(16,-16)--(0,-16)--cycle); D((16,-8)--(24,-8)); label('Dog', (24, -8), SE); MP('I', (8,-8), (0,0)); MP('8', (16,-4), W); MP('8', (16,-12),W); MP('8', (20,-8), N); label('Rope', (20,-8),S); D((0,-20)--(16,-20)--(16,-36)--(0,-36)--cycle); D((16,-24)--(24,-24)); MP("II", (8,-28), (0,0)); MP('4', (16,-22), W); MP('8', (20,-24), N); label("Dog",(24,-24),SE); label("Rope", (20,-24), S); [/asy]

Which of these arrangements give the dog the greater area to roam, and by how many square feet?

$\textbf{(A) } I,\,\textrm{ by }\,8\pi\qquad \textbf{(B) } I,\,\textrm{ by }\,6\pi\qquad \textbf{(C) } II,\,\textrm{ by }\,4\pi\qquad \textbf{(D) } II,\,\textrm{ by }\,8\pi\qquad \textbf{(E) } II,\,\textrm{ by }\,10\pi$

## Solution
[asy] size(150); pathpen = linewidth(0.7); defaultpen(linewidth(0.7)+fontsize(10)); filldraw(arc((16,-8),8,-90,90)--cycle, rgb(0.9,0.9,0.6)); filldraw(arc((16,-26),8,-90,90)--cycle, rgb(0.9,0.9,0.6)); filldraw(arc((16,-22),4,90,180)--(16,-22)--cycle, rgb(0.9,0.9,0.6)); D((0,0)--(16,0)--(16,-16)--(0,-16)--cycle); D((16,-8)--(24,-8)); label('Dog', (24, -8), SE); MP('I', (8,-8), (0,0)); MP('8', (16,-4), W); MP('8', (16,-12),W); MP('8', (20,-8), N); label('Rope', (20,-8),S); pair sD = (0,-2); D(shift(sD)*((0,-20)--(16,-20)--(16,-36)--(0,-36)--cycle)); D(shift(sD)*((16,-24)--(24,-24))); MP("II", (8,-28)+sD, (0,0)); MP('4', (16,-22)+sD, W); MP('8', (20,-24)+sD, N); label("Dog",(24,-24)+sD,SE); label("Rope", (20,-24)+sD, S); [/asy] Let us first examine the area of both possible arrangements. The rope outlines a circular boundary that the dog may dwell in. Arrangement $I$ allows the dog $\frac12\cdot(\pi\cdot8^2) = 32\pi$ square feet of area. Arrangement $II$ allows $32\pi$ square feet plus a little more on the top part of the fence. So we already know that Arrangement $II$ allows more freedom - only thing left is to find out how much. The extra area can be represented by a quarter of a circle with radius 4. So the extra area is $\frac14\cdot(\pi\cdot4^2) = 4\pi$ . Thus the answer is $\boxed{\textbf{(C) } II,\,\textrm{ by }\,4\pi}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .