import pickle

tokenizer = pickle.load(open("deployement/models/cv.pkl", 'rb'))
model  = pickle.load(open("deployement/models/clf.pkl", 'rb'))

def make_prediction(email_text):
    if email_text == "":
        return ""
    tokenized_email = tokenizer.transform(email_text)
    prediction = model.predict(tokenized_email)
    prediction = 1 if prediction == 1 else -1
    return prediction

