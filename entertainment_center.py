import requests
import json
import media
import fresh_tomatoes


def getdata(movieid, youtubeid):
    """ the function obtain the moive information via api website.

    Args:
        movieid (str): global moive's id.
        youtubeid (str): video's id in Youtube.

    Returns:
        Return a tuple of moive's value.

    """
    res = requests.get('http://www.omdbapi.com/?i={}&'
                       'apikey=46f7964d'.format(movieid))
    jd = json.loads(res.text.strip('var data='))
    name = jd['Title']
    year = jd['Year']
    rated = jd['Rated']
    plot = jd['Plot']
    image_url = jd['Poster']
    youtube_url = "https://www.youtube.com/watch?v={}".format(youtubeid)
    return (name, year, image_url, youtube_url, rated, plot)

# call the function get the information and saved in the list
inf = getdata("tt3896198", "2cv2ueYnKjg")
# create an instance of the moive
galaxy2 = media.Movie(inf[0],
                      inf[1],
                      inf[2],
                      inf[3],
                      inf[4],
                      inf[5])

inf = getdata("tt3470600", "Wm7qEjEny0w")
sing = media.Movie(inf[0],
                   inf[1],
                   inf[2],
                   inf[3],
                   inf[4],
                   inf[5])

inf = getdata("tt0478970", "pWdKf3MneyI")
ant_man = media.Movie(inf[0],
                      inf[1],
                      inf[2],
                      inf[3],
                      inf[4],
                      inf[5])

inf = getdata("tt3501632", "ue80QwXMRHg")
thor3 = media.Movie(inf[0],
                    inf[1],
                    inf[2],
                    inf[3],
                    inf[4],
                    inf[5])

inf = getdata("tt2294629", "FLzfXQSPBOg")
frozen = media.Movie(inf[0],
                     inf[1],
                     inf[2],
                     inf[3],
                     inf[4],
                     inf[5])

inf = getdata("tt3521164", "LKFuXETZUsI")
moana = media.Movie(inf[0],
                    inf[1],
                    inf[2],
                    inf[3],
                    inf[4],
                    inf[5])

# create the list of all the moive's name
movies = [galaxy2, thor3, ant_man, sing, frozen, moana]

# call the fresh tomatoes to open the website
fresh_tomatoes.open_movies_page(movies)
