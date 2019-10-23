# Import the English language class
from spacy.lang.en import English

# Create the nlp object
nlp = English()

# Process a text
doc = nlp("We are exploring Hello World in English.")

# Print the document text
print(doc.text)

# Select the first token
first_token = doc[0]

# Print the first token's text
print(first_token.text)
