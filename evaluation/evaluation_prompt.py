two_comp_plan="""
Here are two storyline excerpts.
You shouldn’t be concerned about the completeness of the plot.
Storyline A:
${storyline_A}

Storyline B:
${storyline_B}


Answer the following question:
1) Overall, which story do you prefer/find more interesting? A / B / C
2) Overall, which story has a more coherent overarching plot? A / B / C
3) Overall, which story has a more creative plot? A / B / C
4) Overall, Are both storylines closer to the premise? BY / OA / OB / BN / UN

After providing your explanation, output your final verdict by strictly following this format:
”[[A]]” if storyline A is better, ”[[B]]” if storyline B is better, and ”[[C]]” for a tie or unable to determine.
"[[BY]]" if storyline A,B are eqaully closer to premise, "[[OA]]" if only storyline A is close to the premise, "[[OB]]" if only stroline B is closer to the premise, "[[BN]]" if neither is close to the premise, "[[UN]]" if unable to determine.
example)
1:[[A]], 2:[[B]], 3:[[B]], 4:[[BY]]
"""

two_comp_sent="""
Here are two sentence excerpts.

Sentence A:
${sentence_A}

Sentence B:
${sentence_B}


Answer the following question:
1) Overall, which sentence has better Coherence? A / B/ C
2) Overall, which sentence has better Writing Style Consistency? A / B / C
3) Overall, which sentence has better Interesting? A / B / C
4) Between these two sentences, which one exhibits greater creative expression? BY / OA / OB / BN / UN

After providing your explanation, output your final verdict by strictly following this format:
”[[A]]” if sentence A is better, ”[[B]]” if sentence B is better, and ”[[C]]” for a tie or unable to determine.
"[[BY]]" if sentence A,B are eqaully closer to premise, "[[OA]]" if only sentence A is close to the premise, "[[OB]]" if only stroline B is closer to the premise, "[[BN]]" if neither is close to the premise, "[[UN]]" if unable to determine.
example)
1:[[A]], 2:[[B]], 3:[[B]], 4:[[BY]]
"""



three_comp_plan="""
Here are five storyline excerpts.
You shouldn’t be concerned about the completeness of the plot.
Storyline A:
${storyline_A}


Storyline B:
${storyline_B}


Storyline C:
${storyline_C}


Storyline D:
${storyline_D}


Storyline E:
${storyline_E}


Answer the following question:
1) Overall, which story do you prefer/find more interesting? A / B/ C / D / E / TI
2) Overall, which story has a more coherent overarching plot? A / B / C / D / E / TI
3) Overall, which story has a more creative plot? A / B / C / D / E / TI


After providing your explanation, output your final verdict by strictly following this format:
”[[A]]” if storyline A is better, ”[[B]]” if storyline B is better, ”[[C]]” if storyline C is better, ”[[D]]” if storyline D is better,”[[E]]” if storyline E is better, and ”[[TI]]” for a tie or unable to determine.
example)
1:[[A]], 2:[[B]], 3:[[D]]
"""


persona_comparision="""
Here are two storyline excerpts.
You shouldn’t be concerned about the completeness of the plot.
Storyline A:
${storyline_A}

Storyline B:
${storyline_B}


Answer the following question:
1) Overall, which story do you prefer/find more interesting? A / B/ C
2) Overall, which story has a more coherent overarching plot? A / B / C
3) Overall, which story has a more creative plot? A / B / C
4) Overall, Are both storylines closer to the premise? BY / OA / OB / BN / UN

Metrics explanation:
(1) Interesting: How does the story plan engag and captivate readers, making them find the narrative interesting?
(2) Coherent: How well are the paragraphs organized and connected with each other?
(3) Creative:: How does the originality and inventiveness of the storyline offer a fresh perspective compared to typical narratives?

After providing your explanation, output your final verdict by strictly following this format:
”[[A]]” if storyline A is better, ”[[B]]” if storyline B is better, and ”[[C]]” for a tie or unable to determine.
"[[BY]]" if storyline A,B are eqaully closer to premise, "[[OA]]" if only storyline A is close to the premise, "[[OB]]" if only stroline B is closer to the premise, "[[BN]]" if neither is close to the premise, "[[UN]]" if unable to determine.
example)
1:[[A]], 2:[[B]], 3:[[B]], 4:[[BY]]
"""