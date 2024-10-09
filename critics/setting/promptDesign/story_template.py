persona_creator="""
I have to improve the storyline of my novel. 
I need experts to give your current storyline a critical evaluation so I can develop it.
These experts are someone who is relevant to the storyline I've presented. 
Create three persona for these experts, including their occupation, age and Brief background 
Also create a persona of a leader who checks the opinions of three experts and adopts the opinion of one.

Following below persona format.
---------------------------------
Expert 1.
	Profession: // ... Profession ... //
    Feedback Focus:  // ... Expert 1's Feedback Focus ... //
    Feedback Focus Details: //... Expert 1's Feedback Focus Details... //

Expert 2.
	Profession: // ... Profession ... //
    Feedback Focus:  // ... Expert 2's Feedback Focus ... //
    Feedback Focus Details: //... Expert 2's Feedback Focus Details... //

Leader.
	Profession: // ... Profession ... //
    Feedback Focus:  // ... Leader's Feedback Focus ... //
    Feedback Focus Details: //... Leader's Feedback Focus Details... //
</endpersona>
---------------------------------

For reference, here is my story: {story}. The experts and leader should provide insights that help me deepen the narrative and develop the story further.
"""

refine_prompt_image="""
Sentence)
{story}
===================
Please review the following 'Original Sentences' from my draft and suggest revisions with explanations for each.
However, when fixing a sentence, consider the following creativity features.

Creativity Feature:
(1) Insight: This category contains words such as “think,” “know,” “consider”—words that can be used to describe thoughts, feelings, and internal images (“I imagined opening my arms and leaping off the balcony”).
(2) See: This contains words such as “view” or “saw,” which can describe visual images.
(3) Hear: This contains words such as “listen” and “hearing,” which are relevant to describe sound experiences*.*
(4) Feel: This contains words, such as “feels” or “touch,” that can describe feelings and bodily sensations (e.g., “she feels a strange tingling sensation”).
(5) Body: This contains words, such as “cheek” or “hands,” that are useful to describe feelings and bodily sensations (e.g., “My mouth was dry, and I felt my knees buckle.”).

Expected Response Format of refined sentence
---------------------------------
Original Sentence: <<Insert Sentence Here>>
Suggested Revision: <<Your Input>>
Reason for Change: [Your Explanation]
"""

refine_prompt_voice="""
Sentence)
===================
Please review the following 'five sentences' from my draft and suggest revisions with explanations for each.
However, when fixing a sentence, consider the following below creativity features.

Creativity Feature:
(1) Informal language: This category comprises informal language such as swear words, netspeak (“lol”), and nonfluencies like “er,” “umm,” relevant to the scoring of Voice. 
(2) Unusual words: Choice of particular or unusual words (e.g., rare or old-fashioned words or informal words
(3) Noteworthy sentence structures: Number of words per sentence, Punctuation, and Use of commas specifically 
(4) Authenticity: This variable measures how personal and honest a person's language sounds to listeners.

Expected Response Format of refined sentence
---------------------------------
Original Sentence: <<Insert Sentence Here>>
Suggested Revision: <<Your Input>>
Reason for Change: [Your Explanation]
"""

choose_critic="""
I have a story that has undergone sentence refinements by a literary expert to enhance its creativity, considering specific 'Image' and 'Voice' creativity features. I need assistance in evaluating these changes to determine which are most effective in strengthening the narrative quality.
Image creativity feature)
(1) Insight: This category contains words such as “think,” “know,” “consider”—words that can be used to describe thoughts, feelings, and internal images (“I imagined opening my arms and leaping off the balcony”)*.*
(2) See: This contains words such as “view” or “saw,” which can describe visual images*.*
(3) Hear: This contains words such as “listen” and “hearing,” which are relevant to describe sound experiences*.*
(4) Feel: This contains words, such as “feels” or “touch,” that can describe feelings and bodily sensations (e.g., “she feels a strange tingling sensation”)*.*
(5) Body: This contains words, such as “cheek” or “hands,” that are useful to describe feelings and bodily sensations (e.g., “My mouth was dry, and I felt my knees buckle.”).
Voice creativity feature)
(1) Informal language: This category comprises informal language such as swear words, netspeak (“lol”), and nonfluencies like “er,” “umm,” relevant to the scoring of Voice. 
(2) Unusual words: Choice of particular or unusual words (e.g., rare or old-fashioned words or informal words
(3) Noteworthy sentence structures: Number of words per sentence, Punctuation, and Use of commas specifically 
(4) Authenticity: This variable measures how personal and honest a person's language sounds to listeners.

Task:
From the list of 2 sentence refinements provided, select one sentence that most effectively enhance the narrative quality of the story. For each chosen refinement, provide a reason explaining why it strengthens the story.

Sentence Refinements for Review:

[First Set of Refinements related to 'Image Creativity Feature']
{Image_refinement}
[Second Set of Refinements related to 'Voice Creativity Feature']
{Voice_refinement}

Expected Response Format:
---------------------------------
Original Sentence: "[Insert Sentence Here]"
Suggested Revision: "[Chosen Refinement]"
---------------------------------
Please base your selections on the impact of these refinements on the story's overall creativity and narrative quality, considering the original story and the specified creativity features."
example)
Original Sentence: "Silence was all-encompassing."
Suggested Revision: "The suffocating silence enveloped her completely."
Reason for Choice: I chose this sentence refinement because it enhances the "Hear" creativity feature by incorporating sensory language that vividly portrays the oppressive presence of silence. The use of the word "suffocating" adds a stronger and more evocative description, intensifying the impact on Aimee's experience.
"""