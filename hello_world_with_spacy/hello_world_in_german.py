# Import the German language class
from spacy.lang.de import German

# Create the nlp object
nlp = German()

# Process a text (this is German for: "We are exploring hello world in German.")
doc = nlp("Wir erkunden die Hallo Welt auf Deutsch.")

# Print the document text
print(doc.text)
