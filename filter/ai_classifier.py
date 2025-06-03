import fasttext

model = fasttext.load_model("core/model.bin")  # Your pre-trained FastText model

def classify_message(text):
    label = model.predict(text)[0][0]  # e.g., '__label__loan query'
    return label.replace("__label__", "")
