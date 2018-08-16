"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media


def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    silenthill = media.Movie("Silent Hill",
                             "A woman, rose, goes in search" +
                             "for her adopted daughter within the confines" +
                             "of a strange,"
                             "desolated town Called Silent Hill",
                             "https://vignette.wikia.nocookie.net/silent/" +
                             "images/3/3b/Walkinsh.jpg/revision/latest" +
                             "?cb=20141128110555",
                             "https://www.youtube.com/watch?v=Y2M8iYL8suw",
                             "December, 8, 2015")

    losthighway = media.Movie("Lost Highway",
                              "After a bizarre encounter at a party, a jazz" +
                              "saxophonist is framed for the murder of his" +
                              "wifeand sent to prison, where he inexplicably" +
                              "morphs into a young mechanic and begins leading"
                              "a new life.",
                              "https://img.moviepostershop.com/lost-highway-" +
                              "movie-poster-1997-1010730374.jpg",
                              "https://www.youtube.com/watch?v=1nKjO9QCSid",
                              "February, 21, 1997")

    paloalto = media.Movie("Palo Alto",
                           "The life and struggles of a group of adolescents" +
                           "living in Palo Alto.",
                           "https://i.pinimg.com/736x/f3/c8/0e/f3c80ef6056" +
                           "bad88529fd9d9add37cc0--gia-coppola-emma-" +
                           "roberts.jpg",
                           "https://www.youtube.com/watch?v=sTqMUu1iTIo",
                           "May, 9, 2014")

    themlaandlouise = media.Movie("Thelma and Louise",
                                  "Two best friends set out on an adventure," +
                                  "but it soon turns around to a terrifying" +
                                  "escape from being hunted by the police," +
                                  "as these two girls escape for the crimes" +
                                  "they committed.",
                                  "https://cdn.shopify.com/s/files/1/0630/" +
                                  "8509/products/pst0502TandL_large.jpg?v=" +
                                  "1470942122",
                                  "https://www.youtube.com/watch?v=" +
                                  "2iBFmKlO4BY",
                                  "May, 24, 1991")

    mrandmrssmith = media.Movie("Mr. and Mrs. Smith",
                                "A bored married couple is surprised to learn"
                                "that they are both assassins hired by" +
                                "competing agencies to kill each other.",
                                "https://upload.wikimedia.org/" +
                                "wikipedia/en/f/" +
                                "fd/Mr_and_Mrs_Smith_poster.png",
                                "https://www.youtube.com/watch?v=_V3jNIRYihE",
                                "June, 10, 2005")

    lacaraoculta = media.Movie("La Cara Oculta",
                               "Shattered by the unexpected news, an" +
                               "aspiring" +
                               "orchestra conductor is puzzled" +
                               "by his girlfriend's mysterious and seemingly" +
                               "inexplicable case of disappearance.",
                               "https://resizing.flixster.com/0quba9IOsuM"
                               "uvKgAoZse0Gz7CLk=/206x305/v1.bTsx" +
                               "MTE2NTUyNzt" +
                               "qOzE3ODU5OzEyMDA7NDUwOzYwMA",
                               "https://www.youtube.com/watch?v=hWq_1Pj0QDM",
                               "September, 16, 2011")

    # Store the Movie objects in a list.
    movies = [silenthill, losthighway, paloalto, themlaandlouise,
              mrandmrssmith, lacaraoculta]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)
if __name__ == '__main__':
    main()