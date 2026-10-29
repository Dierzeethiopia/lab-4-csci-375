<><><><><><><><><><><><><><><><><><><><><

1.

    Ex. 1:
    Input: zeus - greek + norse
    Output: odin zeus
    Explanation: Zeus is a major god in Greek mythology and Odin is a major god in Norse mythology. The model seems to capture the r/ship between gods and their mythological traditions.

    Ex. 2:
    Input: shakespeare - england + russia
    Output: tolstoy russia
    Explanation: Shakespeare is a famous English writer and Tolstoy is a famous Russian writer. Changing the country appears to move the vector toward a writer associated with Russia.

    Ex. 3
    Input: football - america + india
    Output: cricket rugby
    Explanation: Football is highly associated with American sports culture and cricket is mosty popular in India. The result suggests that the model has learned associations between sports and countries.

    Ex 4: BONUS
    Input: painter - canvas + music
    Output: composer musician
    Explanation: A painter paints using materials like canvas and a composer creates music. The model appears to capture a relationship between different kinds of artistic work.

<><><><><><><><><><><><><><><><><><><><><

2. 

    Input: doctor - man + woman
    Output: doctor nurse
    Explanation: In my believe, GloVe learns relationships between words by looking at how often they appear near each other in Wikipedia and news articles. For ex., doctors might often be described using words like "he" and "his", while nurses might appear more often with "she" and "her". At the same time, both professions appear around similar words like "hospital", "patient", and "treatment.". Over time, these patterns can make the model associate doctors more with men and nurses more with women. This might explain why "nurse" appears as the second closest word, even though "doctor" is still the closest. The model isn't actually deciding which jobs men or women should have. It's just learning patterns from the language people use, including stereotypes that may be present in that language.

<><><><><><><><><><><><><><><><><><><><><

3.

Successfuls
------------

    1: nervous about exams
    {
        0.923   Up late doing homework.. #NoSleep
        0.917   Math can be sooo stressful -___- Still doin my math hw , ughhh !
        0.916   so tired of studying #mustsurvivethistest
        0.914   Didn't study for my psych test ... Seriously debating not going. #fail
    }
    Explanation: The query is about exam anxiety and the program finds tweets about like stressful homework, late night studying, worrying about tests... Several results don't contain either nervous or exams so this is a good demonstration of semantic similarity rather than exact keyword matching.


    2: missing someone special
    {
        0.948   That sad moment when you find an old conversation between you and someone you don't talk to anymore. #memories
        0.948   #ThingsWeAllHate Knowing the person you love is with someone else..
        0.947   RT @ItsAYYSIAN: That moment of pain when you see your CRUSH flirting with someone else...
        0.947   I actually miss having feelings for someone
    }
    Explanation: These tweets relate to missing someone, loneliness or romantic feelings. The first three express related experiences without directly repeating the full query. This suggests the embeddings can capture emotional associations between different expressions.



Unsuccessfuls
-------------

    1: piece of cake
    {
        0.959   Buyin the sandwich bag full of "pink cookies" 4 .25 from the Candy-Lady #HoodMemories
        0.950   VINTAGE Easy Bake Oven -- Original Box with Like New Oven and Accessories
        0.945   Chinese meat bun is the best food ever~
    }
    Explantion: This search didn't work the way I intended. I used "piece of cake" to mean something very easy, but most of the results were about food, baking, eating... This probably happened because the program adds the vectors for each word separately instead of understanding the phrase as an idiom. The words "piece" and "cake" are associated with food so the search returned tweets about cookies, ovens, and other foods rather than easy tasks.


    2: cold feet
    {
        0.940   cold
        0.940   I'm cold #burr
        0.927   my feet are cold >_<
    }
    Explanation: I expected tweets about people feeling nervous or hesitant about doing something, but the results were mostly about being physically cold. One tweet ("my feet are cold") matches the literal meaning of the words but not the idiom I intended. This shows a limitation of adding word vectors together thatt the program can recognize related words without understanding what they mean when used together as an expression.

<><><><><><><><><><><><><><><><><><><><><