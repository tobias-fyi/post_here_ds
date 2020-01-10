"""takes raw text and obtains a prediction"""
import pickle
from .models import load_mvp
import pandas as pd





def predict(post: str, n: int = 5) -> dict:
    """
    Serve subreddit predictions.
    
    Parameters
    ----------
    post : string
        Selftext that needs a home.
    n    : integer
        The desired name of the output file,
        not including the '.pkl' extension.

    Returns
    -------
    Python dictionary formatted as follows:
        [{'subreddit': 'PLC', 'proba': 0.014454},
         ...
         {'subreddit': 'Rowing', 'proba': 0.005206}]

    """
    vocab, rfc, le = load_mvp()

    # Vectorize the post -> sparse doc-term matrix
    post_vec = vocab.transform([post])
    
    # Generate predicted probabilities from trained model
    proba = rfc.predict_proba(post_vec)
    
    #Wrangle into correct format
    return (pd
                .DataFrame(proba, columns=[le.classes_])  # Classes as column names
                .T  # Transpose so column names become index
                .reset_index()  # Pull out index into a column
                .rename(columns={"level_0": "name", 0: "proba"})  # Rename for aesthetics
                .sort_values(by="proba", ascending=False)  # Sort by probability
                .iloc[:n]  # n-top predictions to serve
                .to_dict(orient="records")
               )

# post2 = """I've been dreaming about writing my own stort story for a while but I want to give it an unexpected ending. I've read lots of books, but none of them had the plot twist I want. I want to read books with the best plot twists, so that I can analyze what makes a good plot twist and write my own story based on that points. I don't like romance novels and I mostly enjoy sci-fi or historical books but anything beside romance novels would work for me, it doesn't have to be my type of novel. I'm open to experience after all. I need your help guys. Thanks in advance."""

# print(predict(post2, 5))