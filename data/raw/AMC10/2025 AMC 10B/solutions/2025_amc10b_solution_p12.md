# 2025 AMC 10B Problem 12

## Problem

The figure below shows an equilateral triangle, a rhombus with a $60^\circ$ angle, and a regular hexagon, each of them containing some mutually tangent congruent disks. Let $T, R,$ and $H,$ respectively, denote the ratio in each case of the total area of the disks to the area of the enclosing polygon. Which of the following is true?

$\textbf{(A)}\ T=H=R \qquad \textbf{(B)}\ H<R=T \qquad \textbf{(C)}\ H=R<T\qquad \textbf{(D)}\ H<R<T \qquad \textbf{(E)}\ H<T<R \qquad$

[asy] /* Figure by reda */ unitsize(15); real r = 1 + sqrt(3); draw(r*dir(90) -- r*dir(210) -- r*dir(330) -- cycle); filldraw(circle(dir(90), sqrt(3)/2), mediumgrey); filldraw(circle(dir(210), sqrt(3)/2), mediumgrey); filldraw(circle(dir(330), sqrt(3)/2), mediumgrey); draw(shift(8, 0)*(r*dir(90) -- r*dir(180)/sqrt(3) -- r*dir(270) -- r*dir(0)/sqrt(3) -- cycle)); filldraw(shift(8, 0)*circle(dir(90)*r/3, r/3), mediumgrey); filldraw(shift(8, 0)*circle(dir(270)*r/3, r/3), mediumgrey); draw(shift(16, 0)*(r*dir(0) -- r*dir(60) -- r*dir(120) -- r*dir(180) -- r*dir(240) -- r*dir(300) -- cycle)); for (int i = 30; i <= 330; i = i + 60) { filldraw(shift(16, 0)*circle(r*dir(i)/sqrt(3), r/2/sqrt(3)), mediumgrey); } [/asy]

## Solution 1 (Divide Shapes Into Equilateral Triangles and Simple Observations.)
[asy] /* Figure by reda */ unitsize(15); real r = 1 + sqrt(3); draw(r*dir(90) -- r*dir(210) -- r*dir(330) -- cycle); filldraw(circle(dir(90), sqrt(3)/2), mediumgrey); filldraw(circle(dir(210), sqrt(3)/2), mediumgrey); filldraw(circle(dir(330), sqrt(3)/2), mediumgrey); draw(dir(90)+dir(-30)*sqrt(3) -- dir(90)+dir(210)*sqrt(3) ^^ dir(210)+dir(90)*sqrt(3) -- dir(210)+dir(-30)*sqrt(3) ^^ dir(330)+dir(90)*sqrt(3) -- dir(330)+dir(210)*sqrt(3), red+dashed); label("$T$", (0, -3.5)); draw(shift(8, 0)*(r*dir(90) -- r*dir(180)/sqrt(3) -- r*dir(270) -- r*dir(0)/sqrt(3) -- cycle)); filldraw(shift(8, 0)*circle(dir(90)*r/3, r/3), mediumgrey); filldraw(shift(8, 0)*circle(dir(270)*r/3, r/3), mediumgrey); draw(shift(8, 0)*(r*dir(180)/sqrt(3) -- r*dir(0)/sqrt(3)), dashed); label("$R$", (8, -3.5)); draw(shift(16, 0)*(r*dir(0) -- r*dir(60) -- r*dir(120) -- r*dir(180) -- r*dir(240) -- r*dir(300) -- cycle)); for (int i = 30; i <= 330; i = i + 60) { filldraw(shift(16, 0)*circle(r*dir(i)/sqrt(3), r/2/sqrt(3)), mediumgrey); draw(shift(16, 0)*((0, 0) -- r*dir(i - 30)), dashed); } label("$H$", (16, -3.5)); [/asy]
To solve this problem, we can dissect the different shapes into equilateral triangles. We can keep the first figure the same, and then divide the rhombus into two equilateral triangles (as a result of one of the angles equaling 60), with one circle in each that is tangent to its triangle. We can do the same for the hexagon, dividing it into six equilateral triangles with one circle in each, and each circle is tangent to the triangle that encloses it.
We can see that $H = R$ , since the proportion of the shaded circles to the unshaded portions in the rhombus and the hexagon is the same, as both are equal to an equilateral triangle with a circle inscribed in it, and therefore they have an equal ratio. We can use this to estimate that the ratio of the circle to the triangle is the largest for the first figure, as we can obviously see this through intuition and observation.
Furthermore, there is no answer choice for $T < H = R$ , and it is evidently not $H = R = T$ . Hence, the answer to the question is as follows: $\boxed{\textbf{(C)}\ H = R < T}.$
~EZ123
~imbetterthanyou (made some wording clearer)
~Strickenox (Minor edits)
~EZ123 (More minor edits, don't try to one-up me)
~Wen_Liang (Even more minor edits :D)
~EZ123 (EVEN MORE MINOR EDITS)
~Galactic_Saber (Minor edits, thought I would join)
~NumberNinja1234 (Minor grammar edit, had to do something)
~EZ123 (EVEN MORE MINOR EDITS --- Edited the solution label -- Don't try to one-up me)
~MathyPikachu (Minor edits to the people's edits above me)
~larryliao (I just filled in the problem statement)
~Boywithnuke (I'll join too, fixed grammar and looks)
~Wen_Liang (EVEN MORE :D)
~Hamburger_ (Capitalized the “I”s in the edits above)
~NumberNinja1234 (More grammar :D)
~Boywithnuke (Capitalized the M and the C in the edits above)
~Wen_Liang (definitely did something [wink wink])
~ChickensEatGrass (removed a comma)
~moonwatcher0201 (edited grammar of edits)
~AquaNotFoundPlayz (added colon)
~wawasd (best edit of all time)
~dragonmather (added "basically")
~JeremyLikesCats (removed "basically")
~InvalidResponse (grammar conciseness)
~Okpere_Jr (Blundered the question, and edited)
~vinceS (changed "a" to "an")
~LUCKYOKXIAO (specified "equilateral" triangle twice)
~vinceS (specified "equilateral" triangle in the solution label)
~sixtetris (minor edit)
~NumberNinja1234 (changed (-) to (~) at the start of 2 people's edits.)
~AAaAa_Aa (added 1 space) really necessary edit I know
~zoyshaikh (figured i'd join this and add the word "clearly")
~Wen_Liang (added space in front of parentheses)
~Wen_Liang again (removed a space in front of people's names)
~pisquared64 (specified "use this" to estimate)
~ToxicWaste (Changed "Therefore" to "Hence" :D) Note: Holy bandwagon, the list of peoples usernames is probably longer than the explanation at this point.
~zoyashaikh (Changed "this" to "the") ^above^ - i doubt it, but we might be able to get there soon
~ToxicWaste (Capitalized the "c" in "changed) ^above^ - Don't worry zoyashaikh, it will go fast
~zoyashaikh (Changed "Basic" to "Simple" in the title) ^above^ ok the list of people is 1963 characters while the solution is 984. oh hooray!
~piquared64 (Added "can" to the explanation)
~ToxicWaste (Capitalized the "a" and "c") ^^above^^ -See I was right!
~Soo9 (Deleted two words)
~PinkbIbtoy (Gave reasoning for splitting up the rhombus)
~t :) (Changed ; to ,)
~ reda_mandymath (add figure)
~zoyashaikh(changed "is" to "is as follows")
~NumberNinja1234 (Deleted a single word)
~NumberNinja1234 (FYI this is the 47th edit, all of these edits combined contain 350 words, and a total of 2,395 characters :)
~zoyashaikh (edited to add this comment : D)
~PinkbIbtoy (Very minor edits to title)
~zoyashaikh (edited the title a little)
~piquared64 (replaced "by" with "through")
~zoyashaikh (replaced "also" with "furthermore")
~imbetterthanyou (replaced "ratio" with "proportion" and changed "greatest" to "largest")
~NumberNinja1234 (changed "clearly" to "obviously")
~kfclover (minor $\LaTeX$ formatting)
~kfclover (minor $\LaTeX$ formatting)
~kfclover (minor $\LaTeX$ formatting)
~ldrcs (changed "obviously" to "evidently")
~ (added “can” and “as”)
~WaxyBoy (removed HumanBeingThatBreathesAir)

## Solution 2 (somewhat cheese)
Notice that there is only one answer choice that contains $H = R$ where they are all not equal. This means if we prove that $H = R$ and one of these two isn't equal to T, we have the answer $C$ . To do this, notice that the rhombus can be divided into two congruent equilateral triangles with inscribed circles. This is the exact same as the hexagon but with 6 triangles and 6 inscribed circles, proving that $H = R$ . We cannot do the same for the triangle, so the answer is $\boxed{\textbf{(C) }H=R < T}.$
~Bros1
~minor edit from imbetterthanyou (added the word "exact")

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs

## Video Solution (Fast and Easy)
https://www.youtube.com/watch?v=oy1ue0qliRY
~ Pi Academy
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .