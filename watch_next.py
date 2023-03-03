import spacy

# Language object containing all components and data needed to process text.
nlp = spacy.load('en_core_web_md')

# Function take in the description as a parameter
# Read fail 'movie.txt' and keep data(movies) into list in correct format (title[0],description[1])
# Tokenise each movie and compare descriptions.
# Return title of the most similar movie
def next_movie(description):
    split_list = []
    with open("movies.txt", "r") as file:
        for lines in file:
            split_list.append(lines.split(':'))

    similarity_list = []

    model_sentence = nlp(description)

    for i in range(0, len(split_list)):
        similarity_list.append(nlp(split_list[i][1]).similarity(model_sentence))

    max_similarity = max(similarity_list)
    max_similarity_index = similarity_list.index(max_similarity)
    return split_list[max_similarity_index][0]

# Movie description to comapare with
hulk_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""


# Call function
print("Next Movie Recommended to Watch: " + next_movie(hulk_description))