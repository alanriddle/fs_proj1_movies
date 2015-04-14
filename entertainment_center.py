import fresh_tomatoes
from media import Movie


# Create Movie instances
forbidden_planet = Movie(
    'Forbidden Planet',
    'http://upload.wikimedia.org/wikipedia/commons/5/50/Forbiddenplanetposter.jpg',
    'https://www.youtube.com/watch?v=8y4crGU7dkg')

avatar = Movie(
    'Avatar',
    'http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY')

blade_runner = Movie(
    'Blade Runner',
    'http://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg',
    'https://www.youtube.com/watch?v=iYhJ7Mf2Oxs')

aliens = Movie(
    'Aliens',
    'http://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg',
    'https://www.youtube.com/watch?v=LSHAgmGR-Ig')

how_to_train_your_dragon = Movie(
    'How to Train Your Dragon',
    'http://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg',
    'https://www.youtube.com/watch?v=oKiYuIsPxYk')

blackfish = Movie(
    'Blackfish',
    'http://upload.wikimedia.org/wikipedia/en/b/bd/BLACKFISH_Film_Poster.jpg',
    'https://www.youtube.com/watch?v=G93beiYiE74')

let_the_right_one_in = Movie(
    'Let the Right One In',
    'http://upload.wikimedia.org/wikipedia/en/c/c9/Let_the_Right_One_In_%28Swedish%29.jpg',
    'https://www.youtube.com/watch?v=ICp4g9p_rgo')

the_princess_bride = Movie(
    'The Princess Bride',
    'http://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg',
    'https://www.youtube.com/watch?v=Hd4nNjEiOk4')

cronos = Movie(
    'Cronos',
    'http://upload.wikimedia.org/wikipedia/en/3/3c/Cronos.jpg',
    'https://www.youtube.com/watch?v=wy1CSVv_i7c')


# Put movies in a list
movie_list = [forbidden_planet, avatar, blade_runner, aliens, how_to_train_your_dragon,
              blackfish, let_the_right_one_in, the_princess_bride, cronos]

# sort movies by title in alphabetical order
sorted_movies = sorted(movie_list, key=lambda movie:movie.title)


def main():
    # Create an html file and open it in a web browser.
    #
    # The html file will display artwork for each movie with the movie title
    # beneath the artwork.  When the artwork is clicked on, the youtube trailer
    # will play.

    fresh_tomatoes.open_movies_page(sorted_movies)


if __name__ == "__main__":
        main()
