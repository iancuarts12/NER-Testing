import spacy

text = [
    'John goes for a walk in Berlin',
    'Mike is going to the store',
    'Elon Musk is the CEO at Twitter',
    'Bob Smith is the guy behind XYZ-Sofa',
    'Adrian is the person behind NER'
]

nlp = spacy.load('en_core_web_md')

ner_labels = nlp.get_pipe('ner').labels
print(ner_labels)


trained_nlp = spacy.load('ner_custom_modl')

test_text = [
    "I know how to install toilet.",
    "I repair some some air conditioners.",
    "I am doing some LED light installations",
    "I was once a  plumber that commonly does drain unclogging and toilet maintenance.",
    "I am good at furnitures, I repaired some cushions.",
    "In sofa sets, what I usually do is spring replacement.",
    "Nicholas Andrei Yee is good in installing toilet",
    "The plumber is currently performing Sink and Faucet Maintenance for the apartment complex. Today, he is focusing on Faucet Installation in three units and Leak Fixing under the kitchen sink in another. Plumbing services are essential for property upkeep."
]

for text in test_text:
    doc = trained_nlp(text)
    print(f'Text: {text}')
    print('Entities',[(ent.text, ent.label_) for ent in doc.ents])
    print()