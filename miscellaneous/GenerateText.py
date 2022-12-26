# Have you ever wondered if you just write some Topic and Python generates the whole text according to that topic? Well with this awesome automation script you can do that. This script uses the Transformer module that uses the GTP2 module in its background to generate the text by a given topic.

# Generate Text
# pip install transformers
from transformers import pipeline
def Generate_Text(txt):
    gen = pipeline("text-generation", model="gpt2")
    output = gen(txt, max_length=100, num_return_sequences=1)
    return output[0]['generated_text']
print(Generate_Text("Science of the future"))