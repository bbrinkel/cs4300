Before running anything:
    Ensure homework2_virtual_env is activated:
        - In the homework1 directory type the command source homework2_virtual_env/bin/activate

    Or if you want to create a new virtual environment:
        - Create a new virtual environment (python3 -m venv your_custom_env_name_here --system-site-packages in terminal)
        - Activate the environment (source your_custom_env_name_here/bin/activate in terminal)
        - Change directories to homework2 and run the command: python3 -m pip install -r requirements.txt

        OR, manually

            - Install pytest with pip (python3 -m pip install pytest in terminal)
            - Install BeautifulSoup4 with pip (python3 -m pip install BeautifulSoup4 in terminal)

For Using UI (I unfortunately wasn't able to deploy, so you'll have to run the project in the container):
    - Should be in homework2 directory
    - In the terminal, navigate to the django_movie_app_directory (cd django_movie_app_directory)
    - Run the command to start the project: python3 manage . py runserver 0.0.0.0:3000
    - Navigate to the DevEdu App portion of the container through the DevEdu dashboard (App button)

    - You should now be at the movies page with a list of movies! Click the "book now" button of one on the right side.
    - You will then be sent to the seat booking page, where you can chose a seat (any of the availible buttons):
        - However, you must first enter your username or name in the box above the grid of buttons, or else you won't be able
        to book.
        - When you click a seat button, you'll be sent right to the next page.

    - You should now be at the Booking History page, and it will show you your booking history.
    - If you'd like to cancel a booking, hit the "remove" button on the right side of the chosen booking.
    - Or if you'd like to check another User's history, hit the "Find Other User History" button at the bottom of the list.
        - This will keep you on the same page, but get rid of any list and give you a box to enter a name.
            - The same affect will happen if you are to hit the "History" button in the Navigation bar.

    - To go back to the movies list page, simply hit the "Movies" button in the Navitation bar, and you can start the process
    over again!
    
For Using API:
    - Should be in homework2 directory
    - In the terminal, navigate to the django_movie_app_directory (cd django_movie_app_directory)
    - Run the command to start the project: python3 manage . py runserver 0.0.0.0:3000
    - Navigate to the DevEdu App portion of the container through the DevEdu dashboard (App button)

    - You should now be at the movies page with a list of movies! But we're not staying here:

    For endpoint /api/movies/:
        - In your browsers URL bar, add '/api/movies/' after devedu.io (but remove anything after .io before you do (If needed))
        - Now you should be at the UI for accessing the endpoint's calls, more specifically on the list page where
        it shows the JSON data for all movies in the DB.
        - At the bottom of this page, you have the option to Create a new movie to the list by adding the various arguments
        - You also have the ability to Update, or Delete a specific movie if you type its ID in the URL bar after '/api/movies/'
        Example: '/api/movies/2/'.
            - Hit the red "Delete" button in the upper right corner if you would like to delete it. To update, change the arguments
            of the movie in the fields at the bottom and hit the "Post" button.

    For endpoint /api/seats/:
        - In your browsers URL bar, add '/api/seats/' after devedu.io (but remove anything after .io before you do (If needed))
        - Now you should be at the UI for accessing the endpoint's calls, more specifically on the list page where
        it shows the JSON data for all booked seats and their corresponding movies.
        - If you would like to view a specific seat's availibility, after '/api/seats/' type query parameters "movie" and "seat"
        in the URL bar (Where movie is the title of the movie and seat is the number). Example '/api/seats/?movie=Jaws&seat=A1'.
        (It will show you the results in the JSON data)

        OR

        - If you would like to view which seats are booked of a specific movie, simply only give the "movie" query parameter.
        Example '/api/seats/?movie=Jaws'

        - Now, if you would like to add a booking, on any of these pages, you can enter data at the fields near the bottom of
        the page. It will give you a success or error message depending on if you were able to book the movie or not in the 
        JSON data.

    For endpoint /api/bookings/:
        - In your browsers URL bar, add '/api/bookings/' after devedu.io (but remove anything after .io before you do (If needed))
        - Now you should be at the UI for accessing the endpoint's calls, more specifically on the list page where
        it shows the JSON data for all bookings of a user.
            - By default, this list will give message "You must specify a "user" parameter when looking for history",
            - So to get the history of a specific user, add the query parameter "user" after '/api/bookings/' in the URL
            bar. Example '/api/bookings/?user=Bob'. (It will show up as JSON data)

        - If you want to add a booking, similarly to the seats endpoint, if you would like to add a booking, 
        on any of these pages, you can enter data at the fields near the bottom of the page. It will give you a success 
        or error message depending on if you were able to book the movie or not in the JSON data.


For running tests:
    - Type ctrl-c in the terminal to stop the django project.
    - Still being in the django_movie_app_directory, type the command './manage.py test'
    - This will go through various test cases, testing the various models and API endpoints.

I would like to cite chatGPT for helping me figure out a lot of things in this assignment. I did of course
read and use various documentation sources, but chatGPT helped me figure out lots of things about viewsets,
serializers, html, bootstrap, and was very big in helping me with testcases.

        

        

