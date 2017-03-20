# Create Movie instance from Movie class,put all movie instances into a
# list name "moives". send "movie" list to html framework function and call it.


# import Movie class from media file,import html framework from fresh_tomatoes
import media
import fresh_tomatoes

# Add 1st movie instances, toy_story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/\
                        Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=nCqtQLmJTl0")

# Add 2nd movie instances, Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/\
                     Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=ZUgjaUZBP7o")

# Add 3rd movie instances, School of Rock
school_of_rock = media.Movie("School of Rock",
                             "USA",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/\
                             1/11/School_of_Rock_Poster.jpg/220px-School_of_\
                             Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=q75FeMDy7Vg")

# Add 4th movie instances, School of Rock
kong = media.Movie("kong:skull island",
                   "Kong: Skull Island Final Trailer (2017): Check out the \
                   new Kong: Skull Island trailer starring Tom Hiddleston, \
                   Samuel L. Jackson, and Brie Larson!",
                   "https://i.ytimg.com/vi/rV7KX3LsmTk/hqdefault.jpg?custom\
                   =true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh\
                   =saBn7XGH4LKK_iLfg7MWAfiPsvM",
                   "https://www.youtube.com/watch?v=rV7KX3LsmTk")

# Add 5th movie instances, THE MUMMY Extended
THE_MUMMY_Extended = media.Movie("THE MUMMY Extended Trailer 2017",
                                 "THE MUMMY Extended Trailer 2017",
                                 "https://i.ytimg.com/vi/PLa2ulPAuI4/hqdefault\
                                 .jpg?custom=true&w=246&h=138&stc=true&jpg444=\
                                 true&jpgq=90&sp=68&sigh=-owV6OaHi8-ekElIGm5oA\
                                 Izieuc",
                                 "https://www.youtube.com/watch?v=PLa2ulPAuI4")

# Add 6th movie instances, Transformers 5
Transformers_5 = media.Movie("Transformers 5",
                             "Transformers 5",
                             "https://i.ytimg.com/vi/IaAoZ74WggI/hqdefault.jpg?\
                             custom=true&w=246&h=138&stc=true&jpg444=true&jpgq\
                             =90&sp=68&sigh=WSZ4EHoz1eCuBsNJNBwzwtdFRPU",
                             "https://www.youtube.com/watch?v=IaAoZ74WggI")

# Add 7th movie instances, he Outcasts
The_Outcasts = media.Movie("The Outcasts",
                           "After falling victim to a humiliating prank by \
                           the high school Queen Bee, best friends and \
                           world-class geeks, Mindy and Jodi, decide to \
                           get their revenge by uniting the outcasts of \
                           the school against her and her circle of friends.",
                           "https://i.ytimg.com/vi/kPpi158vPIo/hqdefault.jpg\
                           ?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq\
                           =90&sp=68&sigh=XwNOS1kipjBWCGSyPYWZvTBqTHM",
                           "https://www.youtube.com/watch?v=kPpi158vPIo")

# Add 8th movie instances, Deadpool 2
Deadpool_2 = media.Movie("Deadpool 2",
                         "Filme da Marvel Deadpool 2 - Se Gostar Deixa seu\
                          Like e se Inscreve no Canal !!! Tmj.",
                         "https://i.ytimg.com/vi/gWAN0JJmygQ/hqdefault.jpg?\
                         custom=true&w=246&h=138&stc=true&jpg444=true&jpgq\
                         =90&sp=68&sigh=leQvz3kE7WSXuAjUY8dD6o2V37o",
                         "https://www.youtube.com/watch?v=gWAN0JJmygQ")
# put all movie instances into a list name "moives"
movies = [toy_story, avatar, school_of_rock, kong, THE_MUMMY_Extended,
          Transformers_5, The_Outcasts, Deadpool_2]

#
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
