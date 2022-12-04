import numpy as np

class Movie:
    def __init__(self, id, title, description, mean_rate, poster_url):
        self.id = id
        self.title = title
        self.description = description
        self.mean_rate = mean_rate
        self.poster_url = poster_url
        
    def __str__(self):
        return f"Title : {self.title},\nDescription : {self.description},\nMean rate: {self.mean_rate},\nPoster URL : {self.poster_url}"
    
    def set_replacement_text_for_nan_rate(self):
        if np.isnan(self.mean_rate):
            self.mean_rate = "This film has not been rated yet."
        else:
            self.mean_rate = str(self.mean_rate) + "/100"
        
