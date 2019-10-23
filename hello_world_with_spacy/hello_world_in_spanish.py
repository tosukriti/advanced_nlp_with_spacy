# Import the Spanish language class
from spacy.lang.es import Spanish

# Create the nlp object
nlp = Spanish()

# Process a text (this is Spanish for: "We are exploring hello world in Spanish.")
doc = nlp("Estamos explorando hello world en español.")

# Print the document text
print(doc.text)
