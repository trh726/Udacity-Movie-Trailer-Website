import fresh_tomatoes
import media

#initializes the groundhog_day instance of the Movie class from the media module
groundhog_day = media.Movie("Groundhog Day",
"A weatherman finds himself inexplicably living the same day over and over again.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BZWIxNzM5YzQtY2FmMS00Yjc3LWI1ZjUtNGVjMjMzZTIxZTIxXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=tSVeDx9fk60")

#initializes the whiplash instance of the Movie class from the media module
whiplash = media.Movie("Whiplash",
"A promising young drummer enrolls at a cut-throat music conservatory.",
"https://t3.gstatic.com/images?q=tbn:ANd9GcS_IwW5-_mWA1PXiPG4qEhLC6Q3vntQd7Bzgs_YE7HHFifItn2T",
"https://www.youtube.com/watch?v=7d_jQycdQGo")

#initializes the the_princess_bride instance of the Movie class from the media module
the_princess_bride = media.Movie("The Princess Bride",
"While home sick in bed, a young boy's grandfather reads him a story called The Princess Bride.",
"https://t2.gstatic.com/images?q=tbn:ANd9GcQ-7X8TZY4t3-batXM4MNsd4Fcwvf4nKF4E_3jr-1XnUYYQTVEw",
"https://www.youtube.com/watch?v=njZBYfNpWoE")

#initializes the this_is_spinal_tap instance of the Movie class from the media module
this_is_spinal_tap = media.Movie("This Is Spinal Tap",
"Spinal Tap, one of England's loudest bands, is chronicled by film director Marty DeBergi on what proves to be a fateful tour.",
"http://static.rogerebert.com/uploads/movie/movie_poster/this-is-spinal-tap-1985/large_hTb29XWr5jm9itLcgkDaBfNvCpl.jpg",
"https://www.youtube.com/watch?v=N63XSUpe-0o")

#initializes the goon instance of the Movie class from the media module
goon = media.Movie("Goon",
"Labeled an outcast by his brainy family, a bouncer overcomes long odds to lead a team of under performing misfits to semi-pro hockey glory, beating the crap out of everything that stands in his way.",
"http://www.magnetreleasing.com/goon/images/photos/photo_10.jpg",
"https://www.youtube.com/watch?v=0dEUXY3yhHU&list=PL_v8ayiJr2AgzA1kDbqhgR7q2mmCZlybO")

#initializes the the_princess_bride instance of the Movie class from the media module
spotlight = media.Movie("Spotlight",
"The true story of how the Boston Globe uncovered the massive scandal of child molestation and cover-up within the local Catholic Archdiocese, shaking the entire Catholic Church to its core.",
"https://upload.wikimedia.org/wikipedia/en/f/f3/Spotlight_%28film%29_poster.jpg",
"https://www.youtube.com/watch?v=EwdCIpbTN5g")

#creates an array named movies of the above Movie class instances - is the argument used in the open_movies_page function
movies = [groundhog_day, whiplash, the_princess_bride, this_is_spinal_tap, goon, spotlight]
#calls the open_movies_page function from the fresh_tomatoes module - uses the movies array as an argument
fresh_tomatoes.open_movies_page(movies)
