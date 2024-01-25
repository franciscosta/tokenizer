The first step I'm looking for here
Is to take in tokens if they have a partial
A partial is a special character that denotes something
In this case, this is the start of a new line
The partial for the start of a new line is \
If I see that, I start collecting the token in a buffer
If the next token creates the full new line char
Then I switch the state of the object

Thing is, the next character might not have the sensitive character anymore. But 