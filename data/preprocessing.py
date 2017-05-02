import json


SEPARATOR = " +++$+++ "


class Movie():
    
    def __init__(self,
                 id=None,
                 title=None,
                 year=None,
                 rating=None,
                 votes=None,
                 genres=[]):
        self.id = id
        self.title = title
        self.year = year
        self.rating = rating
        self.votes = votes
        self.genres = genres

    def __repr__(repr):
        return "Title: {}\n Year: {}\n Rating: {}\n votes: {}\n Genre: {}".format(
            self.title, self.year, self.rating, self.votes, str(self.genres))


class Character():

    def __init__(self,
                 id=None,
                 name=None,
                 movie_id=None,
                 movie_title=None,
                 gender="?",
                 position="?"):
        self.id = id
        self.name = name
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.gender = None if gender == "?" else gender
        self.position = None if position == "?" else position

    #def tojson(self):
        
    def __repr__(self):
        return "Name: {}\n Movie: {}\n Genre: {}\n Position: {}".format(
            self.name, self.movie_title, self.gender, self.position)
        

class Line():

    def __init__(self,
                 id=None,
                 character_id=None,
                 movie_id=None,
                 character_name=None,
                 text=None):
        self.id = id
        self.character_id = character_id
        self.movie_id = movie_id
        self.character_id = character_id
        self.text = text

    def __repr__(self):
        return "[{}] {}: {}".format(
            self.movie_id, self.character_id, self.text)


class Movies():
    """
     class that contains list of movies

    """

    def __init__(self):
        self.movies = {}

    def __getitem__(self, i):
        if isinstance(i, int):
            key = self.movies.keys()[i]
            return self.movies[key]
        return self.movies[i]
    
    def add_movie(self, movie):
        self.movies[movie.id] = movie

    def __dict__(self):
        results = []
        for m in self.movies.values():
            results.append(m.__dict__)
        return results

    
class Characters():
    """ class that contains list of characters
    """

    def __init__(self):
        self.characters = {}

    def __getitem__(self, i):
        if isinstance(i, int):
            key = self.characters.keys()[i]
            return self.characters[key]
        return self.characters[i]

    def __dict__(self):
        results = []
        for c in self.characters.values():
            results.append(c.__dict__)
        return results

    def __iter__(self):
        for c in self.characters.values():
            yield c
    
    def add_character(self, character):
        # Adds new character
        self.characters[character.id] = character

    def prettify_json(self):
        results = []
        for c in self.characters.values():
            r = c.__dict__
            r['display'] = "{} - {}".format(r['name'], r['movie_title'])
            results.append(r)
        return results
        
class Lines():

    def __init__(self):
        self.d = {}

    def __getitem__(self, i):
        pass

    def __dict__(self):
        pass

    def __iter__(self):
        return self.d.values()
    
    def add_line(self, line):
        self.d[line.id] = line

    def search(self, ch_id, m_id):
        results = []
        for k, v in self.d.iteritems():
            if v.character_id == ch_id and v.movie_id == m_id:
                results.append(v.text)
        return results

class Data():
    """
    Main datastructure
    """
    
    def __init__(
            self,
            movie_id = None,
            movie_title = None,
            movie_year = None,
            rating = None,
            votes = None,
            genres = None,
            character_id = None,
            character_name = None,
            gender = None,
            position = None,
            lines = []):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.movie_year = movie_year
        self.rating = rating
        self.votes = votes
        self.genres = genres
        self.character_id = character_id
        self.character_name = character_name
        self.gender = gender
        self.position = position
        self.lines = lines

    def __dict__():
        return {
            'movie_id': self.movie_id,
            'movie_title': self.movie_title,
            'movie_year': self.movie_year,
            'rating': self.rating,
            'votes': self.votes,
            'genres': self.genres,
            'character_id': self.character_id,
            'character_name': self.character_name,
            'gender': self.gender,
            'position': self.position,
            'lines': self.lines
        }
    
def parse_movie_titles(file_name='movie_titles_metadata.txt'):
    # Function to parse movie titles into a Movies class

    movies = Movies()
    f = open(file_name, 'r')
    #print f
    #print f.readlines()
    prev = ""
    for l in f.readlines():
        try:
            l = l.encode('utf-8')
        except:
            # To decode weird characters
            l = l.decode('ISO-8859-1')
            l = l.encode('utf-8')
                
        s = l.split(SEPARATOR)
        movie = Movie(id = s[0],
                      title = s[1],
                      year = s[2],
                      rating = s[3],
                      votes = s[4],
                      genres = s[5]
                      )
        movies.add_movie(movie)

    return movies

def parse_movie_characters(file_name='movie_characters_metadata.txt'):
    # Function to parse characters into an object
    characs = Characters()
    f = open(file_name, 'r')
    for l in f.readlines():
        try:
            l = l.encode('utf-8')
        except:
            l = l.decode('ISO-8859-1')
            l = l.encode('utf-8')
        s = l.split(SEPARATOR)
        c = Character(id = s[0],
                      name = s[1],
                      movie_id = s[2],
                      movie_title = s[3],
                      gender = s[4],
                      position = s[5]
                      )
        characs.add_character(c)

    return characs

'''
now filtering out movie-specifc jargon!
'''
def parse_movie_lines(file_name='movie_lines.txt'):
    # Function to parse movie lines into an object
    lines  = Lines()
    wordToDifferentMovies = {}
    f = open(file_name, 'r')
    for l in f.readlines():
        try:            
            l = l.decode('cp1252')
        except:
            l = l.decode('ISO-8859-1')
            l = l.encode('utf-8')
        s = l.split(SEPARATOR)
        # GET which movies each word has appeared in, and store it in a set
        for wor in s[4].split():
            worl = wor.lower()
            wordToDifferentMovies[worl] = wordToDifferentMovies.get(worl,set())
            wordToDifferentMovies[worl].add(s[2])
    # get if the sets for each word's appearances > min limit & store it.
    MIN_APPEARANCES = 4
    wordsAboveThreshold = {k:len(wordToDifferentMovies[k])>MIN_APPEARANCES for k in wordToDifferentMovies.keys()}
    f.close()
    f = open(file_name, 'r')
    above = 0
    below = 0
    for l in f.readlines():
        try:            
            l = l.decode('cp1252')
        except:
            l = l.decode('ISO-8859-1')
            l = l.encode('utf-8')
        s = l.split(SEPARATOR)
        # given each word, make sure its appeared in 
        # above a certain threshold of movies (currently 5)
        # keep the valid words to store as text.
        textToUse = []
        for wor in s[4].split():
            worl = wor.lower()
            if wordsAboveThreshold[worl]:
                textToUse.append(wor)
                above+=1
            else:
                below+=1
        line = Line(
            id = s[0],
            character_id = s[1],
            movie_id = s[2],
            character_name = s[3],
            text = " ".join(textToUse))
        lines.add_line(line)
    # print above,"ABOVE"
    # print below,"BELOW"
    # Original code w/o movie-specific jargon.
    # for l in f.readlines():
    #     try:            
    #         l = l.decode('cp1252')
    #     except:
    #         l = l.decode('ISO-8859-1')
    #         l = l.encode('utf-8')
    #     s = l.split(SEPARATOR)
    #     line = Line(
    #         id = s[0],
    #         character_id = s[1],
    #         movie_id = s[2],
    #         character_name = s[3],
    #         text = s[4])
    #     lines.add_line(line)
    return lines

def lookup_lines(ch_id, m_id, lines):
    tmp = lines.search(ch_id, m_id)
    if len(tmp) < 1:
        return ""
    results = ""
    for r in tmp:
        results += " "
        results += r.strip()
    
    return results

def make_data_structure(movies, characs, lines):
    # construct movies hash map
    ds = []
    for i, c in enumerate(characs):
        print i
        d = Data(movie_id = c.movie_id,
                 movie_title = movies[c.movie_id].title,
                 movie_year = movies[c.movie_id].year,
                 rating = movies[c.movie_id].rating,
                 votes = movies[c.movie_id].votes,
                 genres = movies[c.movie_id].genres,
                 character_id = c.id,
                 character_name = c.name,
                 gender = c.gender,
                 position = c.position,
                 lines = lookup_lines(c.id, c.movie_id, lines)
                 )
        ds.append(d.__dict__)
    ds = sorted(ds, key=lambda d:("character_id" not in d, d.get("character_id")))
    return ds
        
        


print "Parsing movies....\n"
movies = parse_movie_titles()

print "Parsing characters....\n"
characs = parse_movie_characters()


print "Parsing lines....\n"
lines = parse_movie_lines()

print "Serializing characters...\n"
def save_characters():
    with open('characters2.json', 'w') as outfile:
        json.dump(characs.prettify_json(), outfile)
    
print "Serializing data...\n"
def save_data():
    with open('data_sorted_keys.json', 'w') as outfile2:
        json.dump(make_data_structure(movies, characs, lines), outfile2)

        
save_data()
