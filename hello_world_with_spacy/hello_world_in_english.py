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

# A slice of the Doc for "Hello World"
hello_world = doc[3:5]
print(hello_world.text)

# A slice of the Doc for "Hello World in English"
hello_world_in_english = doc[3:7]
print(hello_world_in_english.text)
