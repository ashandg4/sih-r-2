from textblob import TextBlob


def correct_sentence(sentence):
    blob = TextBlob(sentence)
    corrected_sentence = blob.correct()
    return str(corrected_sentence)


# Example usage
typed_sentence = input("Write the sentence: ")
corrected_sentence = correct_sentence(typed_sentence)
print("Original:", typed_sentence)
print("Corrected:", corrected_sentence)
