import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK resources
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")

def main():
    # Task 1: Import confirmation
    print(f"NLTK library successfully imported. NLTK version: {nltk.__version__}")

    # Task 2: Stemming
    email_content = (
        "Our team will be working on the upcoming project deadlines. "
        "Please ensure that all deliverables are submitted before the end of the week."
    )

    porter_stemmer = PorterStemmer()
    stemmed_words = [porter_stemmer.stem(word) for word in nltk.word_tokenize(email_content)]

    print("\n--- Task 2: Stemming ---")
    print("Original Email Content:", email_content)
    print("Stemmed Email Content:", " ".join(stemmed_words))

    # Task 3: Lemmatization
    email_content_lemma = (
        "The team members are working on their tasks diligently. "
        "Please ensure that every report is submitted promptly."
    )

    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in nltk.word_tokenize(email_content_lemma)]

    print("\n--- Task 3: Lemmatization ---")
    print("Original Email Content:", email_content_lemma)
    print("Lemmatized Email Content:", " ".join(lemmatized_words))


if __name__ == "__main__":
    main()

