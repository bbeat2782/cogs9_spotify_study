# Part 1: Song #
class Song:
    """
    Implementation of a Song
    """

    def __init__(self, decade, popularity, duration):
        """
        Constructor of Song

        Parameter:
        decade (int): decade that the song is released
        popularity (int): int between 0 - 100
        """
        self.decade = decade
        self.popularity = popularity
        self.duration = duration

    def get_decade(self):
        """ Getter the decade """
        return self.decade

    def get_popularity(self):
        """ Getter for the popularity """
        return self.popularity
    
    def get_duration(self):
        """ Getter for the duration """
        return self.duration

    def __gt__(self,other):
        pass


# Part 2: Song Classifier #
class KNNClassifier:
    """
    Implementation of KNN Classifier
    """

    def __init__(self, n_neighbors):
        """
        Constructor of KNNClassifier

        Parameter:
        n_neighbors (int): defines the size of the nearest neighborhood
        """
        self.n_neighbors = n_neighbors
        self.data = None

    def fit(self, data):
        """
        Fit the classifier by storing all training data in the classifier
        instance

        Paramerter:
        data (list): list of (song, label) tuples, where song is a Song 
                        instance and label is a decade in string
        """
        
        assert len(data) > self.n_neighbors and self.data == None

        self.data = data
        

    @staticmethod
    def distance(song1, song2):
        """
        Returns the Euclidean distance between Song song1 and song2

        Parameters:
        song1 (Song): Song that we want to get distance from song2
        song2 (Song): Song that we want to get distance from song1
        """
        if not (isinstance(song1, Song) and isinstance(song2, Song)):
            raise ValueError('Input is not Song instance')
    
        duration1, duration2 = song1.get_duration(), song2.get_duration()
        year1, year2 = song1.get_decade(), song2.get_decade()

        diff_square = (duration1 - duration2)**2 + (year1 - year2)**2
        return diff_square**(1/2)


    @staticmethod
    def vote(candidates):
        """
        Find the most popular label from a list of candidates label. Meaning, 
        find the nearest neighbors. If there is a tie when determining the 
        majority label, it returns any of them

        Parameter:
        candidates()
        """
        count, idx_lab, inc_rate, idx_zero = {}, 2, 1, 0

        for candidate in candidates:
            if candidate not in count:
                count[candidate] = inc_rate
            else:
                count[candidate] +=  inc_rate
        
        sorted_count = sorted(count, key=count.get, reverse=True)

        return sorted_count[idx_zero]


    def predict(self, song):
        """
        Predict the label of the given song using the KNN classification
        algorithm.

        Parameter:
        song (Song): song that we will predict
        """
        if self.data is None:
            raise TypeError('There is not data to use')

        start, end = 0, self.n_neighbors

        dist = [(KNNClassifier.distance(d_tuple[0], song), \
                        d_tuple[0], d_tuple[1]) \
                        for d_tuple in self.data]
        dist.sort()
        min_dist = [dist[i] for i in range(start, end)]
        min_dist_lab = [t[2] for t in min_dist]
        label = KNNClassifier.vote(min_dist_lab)
        return label
