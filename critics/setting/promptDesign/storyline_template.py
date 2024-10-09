createPlot = """
Given the premise: "{premise}", 
Craft a detailed narrative storyline that aligns with the premise and has the potential to be a best-selling novel.
Your outline should follow the format below

'Setting' is a description of the place and time of the story. 


format)
============================================================================================================================================
Premise: {premise}

Setting: 

Characters:
Name of Character A : Information of A character
Name of Character B : Information of B character
Name of Character C : Information of C character
...
Outline:
<label for='outline_1'>
1. Event A, B description Scene: location discription Characters: Character A, Character B, Character C

	a. Event A Scene: location A Characters: Character A, Character B

		i. Character A action Scene: Scene description. Characters: Character A

		ii. Character B action Scene: Scene description. Characters: Character B

	a. Event B Scene: location A Characters: Character A, Character C

		i. Character A action Scene: Scene description. Characters: Character A

		ii. Character C action Scene: Scene description. Characters: Character C
<label for='outline_2'>
2. ...

	a. ... Scene: ... Characters: ...

		i. ... Scene: ... Characters: ...

		ii. ... Scene: ... Characters: ...

	b. ... Scene: ... Characters: ...

		i. ... Scene: ... Characters: ...

		ii. ... Scene: ... Characters: ...
<label for='outline_3'>
3. ...

	a. ... Scene: ... Characters: ...

		i. ... Scene: ... Characters: ...

		ii. ... Scene: ... Characters: ...

	b. ... Scene: ... Characters: ...

		i. ... Scene: ... Characters: ...

		ii. ... Scene: ... Characters: ...
...
<applyStoryline>
============================================================================================================================================

example)
============================================================================================================================================
Premise: After the loss of her father, Shannon is determined to follow in his footsteps and become a successful author. However, when her first book is met with poor reviews, Shannon starts to doubt her talent. With the encouragement of her best friend, Shannon decides to write a second book, but this time she is going to write about what she knows best: her life.

Setting: The story is set in present day and takes place in Shannon's hometown of New York City.

Characters:
Shannon Chambers: Shannon Chambers is a young woman in her early twenties.
Samantha Shaw: Samantha Shaw is Shannon's agent and a successful literary agent.
Rebecca Saunders: Rebecca Saunders is Luke's mother and a successful editor.
Abby Fuller: Abby Fuller is Shannon's best friend and a successful journalist.
Charles Chambers: Charles Chambers is Shannon's late father and a successful author.
Luke Saunders: Luke Saunders is a young man who Shannon meets while working on her second book.


Outline:
<label for='outline_1'>
1. Shannon's father dies and her first book fails, leading her to doubt her talent. Scene:  Characters: Shannon Chambers, Charles Chambers

	a. Shannon's father dies and her first book fails to make a success. Scene:  Characters: Shannon Chambers, Charles Chambers

		i. Shannon's father dies. Scene: Shannon's hometown of New York City. Characters: Shannon Chambers

		ii. Shannon's first book fails to make a success. Scene: the publishing house where Shannon's agent works. Characters: Shannon Chambers

	b. Shannon starts to doubt her talent and wonders if she should give up writing. Scene:  Characters: Shannon Chambers

		i. Shannon wonders if she should give up writing. Scene: Shannon's apartment. Characters: Shannon Chambers

		ii. Shannon meets her agent, who encourages her to continue writing. Scene: the publishing house where Shannon's agent works. Characters: Shannon Chambers, Samantha Shaw
<label for='outline_2'>
2. Shannon's best friend encourages her to write a second book, this time about her life. Scene:  Characters: Shannon Chambers, Abby Fuller

	a. Shannon's best friend encourages her to write a second book about her life. Scene:  Characters: Shannon Chambers, Abby Fuller

		i. Shannon's best friend encourages her to write a second book. Scene: Shannon's home. Characters: Shannon Chambers, Abby Fuller

		ii. Shannon decides to write a second book about her life. Scene: Shannon's home. Characters: Shannon Chambers

	b. Shannon starts to write her second book, but finds it difficult to write about her life. Scene:  Characters: Shannon Chambers

		i. Shannon starts to write her second book. Scene: Shannon's home. Characters: Shannon Chambers

		ii. Shannon finds it difficult to write about her life. Scene: Shannon's home. Characters: Shannon Chambers
<label for='outline_3'>
3. Shannon meets Luke, a young man who helps her with her second book. Scene:  Characters: Shannon Chambers, Luke Saunders

	a. Shannon meets Luke and starts to develop feelings for him. Scene:  Characters: Shannon Chambers, Luke Saunders

		i. Shannon and Luke meet. Scene: Central Park. Characters: Shannon Chambers, Luke Saunders

		ii. Shannon starts to develop feelings for Luke. Scene: a coffee shop. Characters: Shannon Chambers, Luke Saunders

	b. Shannon's second book starts to take shape with Luke's help. Scene:  Characters: Shannon Chambers, Luke Saunders

		i. Shannon's second book starts to take shape with Luke's help. Scene: Shannon's apartment. Characters: Shannon Chambers, Luke Saunders

		ii. Shannon and Luke grow closer as Shannon writes her second book. Scene: Luke's apartment. Characters: Shannon Chambers, Luke Saunders

		iii. Shannon's second book starts to get attention from publishing houses. Scene: a publisher's office. Characters: Shannon Chambers
<label for='outline_4'>
4. Shannon's second book becomes a success, making her a published author. Scene:  Characters: Shannon Chambers

	a. Shannon's second book becomes a success. Scene:  Characters: Shannon Chambers

		i. Shannon finishes writing her second book. Scene: Shannon's home. Characters: Shannon Chambers

		ii. Samantha Shaw agrees to represent Shannon. Scene: Samantha's office. Characters: Samantha Shaw, Shannon Chambers

		iii. Rebecca Saunders agrees to edit Shannon's book. Scene: Rebecca's office. Characters: Rebecca Saunders, Shannon Chambers

	b. Shannon becomes a published author. Scene:  Characters: Shannon Chambers

		i. Shannon signs a book deal with a publisher. Scene: Shannon's home. Characters: Shannon Chambers

		ii. Shannon's book is released and met with critical acclaim. Scene: a bookstore. Characters: Shannon Chambers

		iii. Shannon's book sells well and goes on to become a bestseller. Scene: a bookstore. Characters: Shannon Chambers
<applyStoryline>
"""

persona_creator="""
I have to improve the storyline of my novel. 
I need experts to give your current storyline a critical evaluation so I can develop it.
These experts are someone who is relevant to the storyline I've presented. 
Create three persona for these experts, including their occupation, age and Brief background 
Also create a persona of a leader who checks the opinions of three experts and adopts the opinion of one.

Following below persona format.
============================================================================================================================================
<persona>
Expert 1.
	Profession: // ... Profession ... //
    Feedback Focus: // ... Feedback Focus ... //
    Feedback Focus Details: //... Expert 1's Feedback Focus Details... //
<<persona_split>>
Expert 2.
    Profession: // ... Profession ... //
    Feedback Focus: // ... Feedback Focus ... //
    Feedback Focus Details: //... Expert 2's Feedback Focus Details... //
<<persona_split>>
Expert 3.
    Profession: // ... Profession ... //
    Feedback Focus: // ... Feedback Focus ... //
    Feedback Focus Details: //... Expert 3's Feedback Focus Details... //
<<persona_split>>
Leader.
    Profession: // ... Profession ... //
    Feedback Focus: // ... Feedback Focus ... //
    Feedback Focus Details: //... Expert 4's Feedback Focus Details... //
<persona/>
============================================================================================================================================
My storyline)
============================================================================================================================================
{storyline}
"""

critic_prompt = """
Look at my storyline above and do two requests
1. First Request - Originality Questions for Storyline: 
You are seeking three questions that this storyline has 

"{critic_type}". 

These questions should encourage thinking about unique elements or perspectives that can be added to the story. Remember to align your suggestions and critiques with your "professional background" and "expertise", focusing on aspects that would realistically occur or be relevant in your field. 

2. Second Request - Evaluation and Selection of the Best Question: Out of the three questions provided, you want to identify the best one that improves the originality of the story. This evaluation will be based on three factors:
    
	- Originality: Does altering the storyline in response to this question enhance its originality by integrating "{critic_type}" into the narrative?
    - Coherence: Will adjustments made to the storyline based on this question improve its overall coherence and consistency?
    - Interesting: Does revising the storyline according to this question amplify the storyline's appeal and keep the readers more engaged?

The selected question will then be evaluated using these criteria.
"Note: When formulating questions, ensure they are as detailed as possible, closely related to the storyline."
Answer Format)
============================================================================================================================================
<question>
[First request]
--------------------------
1. ...
2. ...
3. ...
--------------------------
[Second request]
Question : 
....
Why:
<question/>
"""

inspector_prompt="""
[Information]
--------------------------
<3 Questions>
    1) 
    {first_critique}
    2) 
    {second_critique}
    3)
    {third_critique}
<Critiqued Storylines>
    {storyline}
--------------------------
[Request]
My request is ""Of the '3 questions' I posed , which are the best question to improve the Creativity of the 'Critiqued Storylines'? 
The story line should be original and creative, but it need to keep a consistent story.
Please score based on the evaluation factors below.""

    - Originality: Does altering the storyline in response to this question enhance its originality by integrating "original plot/setting/themes," "unusual story structure," and "unusual ending" into the narrative?
    - Coherence: Will adjustments made to the storyline based on this question improve its overall coherence and consistency?
    - Interesting: Does revising the storyline according to this question amplify the storyline's appeal and keep the readers more engaged?
    
Choose one best question and ask answer use below Answer Format.
Key Point: "Exclude questions that are not relevant to the genre of the original story. For example, exclude questions that change from a romance storyline to a fantasy novel story."
Answer Format)
============================================================================================================================================
<answer>
Question : // ... one question ... //
Originality: // ... Originality Score ... // , Coherence: // ... Coherent story ... //, Interesting: // ... Interesting story ... //
Why: // ... Why you choose this question? ... //
<answer/>
============================================================================================================================================
example)
<answer>
Question : 
What if Gabriel finds out that his apartment is haunted?
Why:
This question is quite eccentric because it is not a common occurrence for an apartment to be haunted. It is also odd because it is not something that is typically seen in stories about apartment living. The question is novel because it is a new take on the traditional story of a young man moving out of his parents' house and into his own apartment. Finally, the question is innovative because it introduces the element of ghosts into the story, which is something that is not typically seen in stories about apartment living.
<answer/>
"""

applyQA="""
I have a storyline that I need to modify based on specific feedback from a critical review. The task involves integrating insights from the given critique into the existing storyline while adhering to certain constraints and format.

Task:
Use the provided critical feedback to revise the given storyline. Ensure that the modifications align with the feedback's insights and maintain the original storyline's format.

Constraints:

1. Maintain the original format of the storyline as provided.
2. It is acceptable to change the order of the scenes as you see fit. 
3. The outline must contain detailed descriptions of the events.
4. It is acceptable to add scenes as you see fit. 

Provided Materials:

1.Critical Feedback: {final_critic}
2.Original Storyline: {storyline}

Revision Format:
--------------------------
Premise: : Original Storyline "Premise"

Setting : Original Storyline "Setting"

Characters:
Name of Character A : Information of A character
Name of Character B : Information of B character
Name of Character C : Information of C character
...

Outline:
1. Event A, B description. Scene: "location data or time data" . Characters: Character A, Character B, Character C

	a. Event A Scene: "location data or time data" Characters: Character A, Character B

	b. Event B Scene: "location data or time data" Characters: Character A, Character C

2. ...

	a. ... Scene: ... Characters: ...

	b. ... Scene: ... Characters: ...

3. ...

	a. ... Scene: ... Characters: ...

	b. ... Scene: ... Characters: ...
...
<applyStoryline>
--------------------------
"""
select_storyline_result="""
Here are two storyline excerpts.
You shouldn’t be concerned about the completeness of the plot.

{critic_set}

Task 1 question:
1) Overall, which story do you prefer/find more interesting? A / B ...
2) Overall, which story has a more coherent overarching plot? A / B ...
3) Overall, Which story has a more creative plot? A / B ...
4) Overall, which story’s plot is closer to the premise? A / B ...

After providing your explanation, output your final verdict by strictly following this format:
{select_generation} and ”[[TI]]” for a tie or unable to determine.

example)
1:[[A]], 2:[[A]], 3:[[B]] ...
"""

solo_critic_prompt = """
Look at my storyline above and do two requests
1. First Request - Originality Questions for Storyline: You are seeking nine questions that this storyline has "{critic_type}". These questions should encourage thinking about unique elements or perspectives that can be added to the story. Remember to align your suggestions and critiques with your "professional background" and "expertise", focusing on aspects that would realistically occur or be relevant in your field. 
2. Second Request - Evaluation and Selection of the Best three Question: Out of the three questions provided, you want to identify the best one that improves the originality of the story. This evaluation will be based on three factors:
    1) Originality: Does altering the storyline in response to this question enhance its originality by integrating "{critic_type}" into the narrative?
    2) Coherence: Will adjustments made to the storyline based on this question improve its overall coherence and consistency?
    3) Interesting: Does revising the storyline according to this question amplify the storyline's appeal and keep the readers more engaged?
	The selected question will then be evaluated using these criteria, and I will provide a score for each factor.
 
"Note: When formulating questions, ensure they are as detailed as possible, closely related to the storyline."
Answer Format)
============================================================================================================================================
<question>
[First request]
--------------------------
1. ...
2. ...
3. ...
...
8. ...
9. ...
--------------------------
[Second request]
1) 
Question : 
....
Why:

2) 
Question : 
....
Why:

3) 
Question : 
....
Why:
<question/>
"""

solo_inspector_prompt="""
[Information]
--------------------------
<3 Questions>
	{solo_critic}
<Critiqued Storylines>
    {storyline}
--------------------------
[Request]
My request is ""Of the '3 questions' I posed , which are the best question to improve the Creativity of the 'Critiqued Storylines'? 
The story line should be original and creative, but it need to keep a consistent story.
Please evaluate based on the creative factors below.""

    1) Originality: Does altering the storyline in response to this question enhance its originality by integrating "original plot/setting/themes," "unusual story structure," and "unusual ending" into the narrative?
    2) Coherence: Will adjustments made to the storyline based on this question improve its overall coherence and consistency?
    3) Interesting: Does revising the storyline according to this question amplify the storyline's appeal and keep the readers more engaged?
    
Choose one best question and ask answer use below Answer Format.
Key Point: "Exclude questions that are not relevant to the genre of the original story. For example, exclude questions that change from a romance storyline to a fantasy novel story."
Answer Format)
============================================================================================================================================
<answer>
Question : // ... one question ... //
Originality: // ... Originality Score ... // , Coherence: // ... Coherent story ... //, Interesting: // ... Interesting story ... //
Why: // ... Why you choose this question? ... //
<answer/>
============================================================================================================================================
example)
Question : 
What if Gabriel finds out that his apartment is haunted?
Score:
Why:
This question is quite eccentric because it is not a common occurrence for an apartment to be haunted. It is also odd because it is not something that is typically seen in stories about apartment living. The question is novel because it is a new take on the traditional story of a young man moving out of his parents' house and into his own apartment. Finally, the question is innovative because it introduces the element of ghosts into the story, which is something that is not typically seen in stories about apartment living.
"""

critieria_u_ending="""
(1) Unexpected Conclusions: This aspect includes sentences that wind up in an unusual or surprising way, challenging the reader's expectations set by the initial part of the sentence. 

(2) Humorous or Witty Conclusions: These are endings that incorporate humor or clever plays on words lending an element of surprise and entertainment. This feature contributes substantially to the overall unique voice of the writer. 

(3) Provocative or Intriguing Statements: This characteristic includes endings that are provocative or mysterious, prompting the reader to think deeper, question, and engage more with the content. 
"""

critieria_u_structure="""
(1) Non-linear timeline: Stories do not have to unfold in a straightforward, chronological manner. Experiment with flashbacks, time skips, and non-linear timelines to make the narrative more unexpected. 

(2) Shifting perspectives: Altering the narrative perspective throughout the story can provide fresh insights and create intrigue. This can include alternating between first-person and third-person views, or switching between different characters' perspectives. 

(3) Intertextuality: Include references to other works, stories within stories, or use allegory as a structural device. This can create layers of meanings and associations that enrich the narrative. 

(4) Metafiction: Break the fourth wall by having characters acknowledge they're part of a story or by discussing elements of storytelling within the plot. This can create a self-aware story that directly engages with readers. 
"""

critieria_originaltiy="""
(1) Unconventional Themes: This category includes themes that are not typically encountered in everyday discourse. This could include themes from different cultures, underground societies, or niche hobbies and interests.
   
(2) Unique Plot: Succinct plots that deviate from standard, commonly seen narratives score higher in this category. This could involve unexpected plot twists, unconventional story progression, or atypical character development.

(3) Diverse Settings: Diverse settings refer to the use of unfamiliar or striking locations and times - past, future, or entirely imaginative locations. These could range from sci-fi cityscapes, historical periods, to unique micro-settings such as a single room or a mystical forest.

(4) Authenticity: This feature measures the realness of the theme/plot/setting for the reader. The use of vivid descriptions, consistent details, and emotionally engaging elements can contribute to a more authentic feel. 
"""