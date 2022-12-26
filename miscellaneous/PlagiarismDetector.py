# Want to detect plagiarism between multiple text files and docs then this automation script is for your friend. The script uses the Scikit-learn module and below I mention the whole code that you can copy.

# Plagerism Detector
# pip install scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def Plagerism_Detector(files, student):
    results = set()
    v= lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
    similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])
    vectors = list(zip(files, v(student)))
    
    for stud, text_vector_a in vectors:
        n_vectors = vectors.copy()
        i = n_vectors.index((stud, text_vector_a))
        del n_vectors[i]
        for stud2 , vector2 in n_vectors:
            sim_score = similarity(text_vector_a, vector2)[0][1]
            stud_pair = sorted((stud, stud2))
            match_per = (stud_pair[0], stud_pair[1],sim_score)
            results.add(match_per)
    return results
student_files = ["student_1.txt", "student_2.txt", "student_3.txt"]
student_notes = []
for file in student_files:
    with open(file, "r") as f:
        student_notes.append(f.read())
results = Plagerism_Detector(student_files, student_notes)
for result in results:
    print("Result: ", result)