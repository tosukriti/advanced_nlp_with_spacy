# Import the English language class
from spacy.lang.en import English

# Create the nlp object
nlp = English()

# Process a text
doc = nlp("We are exploring Hello World in English.")

# Print the document text
print(doc.text)
