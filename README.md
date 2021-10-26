# Sentiment-Comparison-Engine
Compares 2 things to see which one is more popular.

#User Story: As a person who constantly tries to be trendy, I would like to know which among 2 things is more popular on the internet.

#User Story: As a developer, I want the users to be able to compare words like "Batman" & "Superman" to settle the debate once and for all on which is more popular based on sentiment scores.

#

*How does the program work?

1. First, a user will input two keywords, e.g. Batman and Superman.

2. We will then download the latest, real-time tweets relating to those two keywords using the Twitter API.  

3. Next, the TextBlob library for calculating the tweets'
 sentiments (NLP part). This tells us how people feel about the specified keywords at this moment in time. 

4. Lastly,  the program compares the scores of the two keywords and tells us what thing people feel more positively about RIGHT NOW!
