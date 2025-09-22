Before running anything:
    - Ensure MyVirtEnv1 is activated (source MyVirtEnv1/bin/activate in terminal)
      Or if accessing from your own machine:
        - Create a new virtual environment (python3 -m venv your_custom_env_name_here --system-site-packages in terminal)
        - Activate the environment (source your_custom_env_name_here/bin/activate in terminal)
        - Change directories to homework1 and run the command: pip install -r requirements.txt

        OR, manually

        - Install pytest with pip (python3 -m pip install pytest in terminal)
        - Install BeautifulSoup4 with pip (python3 -m pip install BeautifulSoup4 in terminal)

To run each task:
    1) Open the terminal
    2) Change to the src directory (cd /homework1/src in terminal)
    3) In the terminal type the command: python3 taskX.py (with X being the number of the task you want to run) 

To run the tests for each task:
    To run them all at once:
        1) Open the terminal
        2) Change to the homework1 directory (cd homework1 in terminal)
        3) In the terminal type the command: pytest --no-header -v (this will run all tests for each task and will give a fairly
        decent summary for each one)

    To run each one seperately:
        1) Open the terminal
        2) Change to the tests directory (cd homework1/tests in terminal)
        3) In the terminal type the command: pytest test_taskX.py --no-header -v (With X being the task you'd like to run 
        tests for)

I used ChatGPT to bounce ideas off of and for explaining functions of packages I have not used.
