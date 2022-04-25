# Challenge 3: Movie View Estimation in Python

## Question
The goal of this task is to implement a model in python to estimate the number of views a movie has.  
You have the following data available:

- Movies list of 250 movies: [top-250-movie-ratings.csv](https://github.com/WittmannF/imdb-tv-ratings/blob/master/top-250-movie-ratings.csv) which contains the position of 250 movies as well as their rating count and other information
- A limited number of movie views data
    - Forrest Gump: 10000000 views
    - The Usual Suspects: 7500000 views
    - Rear Window: 6000000 views
    - North by Northwest: 4000000 views
    - The Secret in Their Eyes: 3000000 views
    - Spotlight: 1000000 views

### Deliverables
- Code
- Documentation that explains how to run the code
- Description about the chosen approach and its pros and cons
- Short discussion about alternative approaches you might have considered and their pros and cons

## Documentation

### Run with Docker
This option is better suited for users who just want to execute the code once and see the results. `Docker` has to be installed to proceed.

Open a terminal and `cd` into the directory for this challenge. From here execute

    docker image build -t challenge3-grb .

to build the docker image. The name `challenge3-grb` can be changed according to personal preferences and other images already installed on the system.  
**Note**: Linux users may have to use `sudo` to execute `docker` commands.

To run the program, execute this next line

    docker run --volume absolute_local_path:/home/app/result --name challenge3-grb_container challenge3-grb

where `absolute_local_path` is the absolute path of the current directory (or any other directory where you want to write the output CSV file). Linux and Mac users can use the following code to avoid typing the whole path.

    docker run --volume $(pwd):/home/app/result --name challenge3-grb_container challenge3-grb

### Run on the Local Machine
This option is better suited for developers who want a fast and simple way to play with the code.

Optionally, create and activate a new virtual environment.

    python -m venv .venv
    source .venv/bin/activate

Install the required packages.

    pip install -r requirements.txt

Run the script.

    python main.py

If you activated a virtual environment, you can deactivate it with:

    deactivate

## Discussion
The limited number of known movie views constraints the possible approaches to this problem. The solution chosen is linear regression, the simplest possible approach, using *Rating Count*, *Rating*, and *Year* as independent variables, and *Views* as the dependent variable.

As a side remark, the three independent variables are likely not completely independent from one another. It's easy for example to see that an older movie is likely to have a higher rating count, because the movie had more time to accumulate ratings. As another example, it can be imagined that the rating can depend on the rating count. The relation is likely not linear, for example voters may feel more compelled to vote movies with very high or very low scores than movies with an average one.

Despite this, it was chosen not to perform a dimensionality reduction on the dataset because the dataset is sufficiently small both in dimensions and entries that the impact of such approach is likely negligible.

Although the lack of data reduces the choice to only the linear regression approach, the result is far from perfect. As can be seen in the [top-250-movie-ratings-prediction.csv](top-250-movie-ratings-prediction.csv) file, the predictions for the six known movies is off at the second significant digit, meaning that the average absolute error is at least 10%, and actually close to 40%.

Another effect that illustrates the limits of this model is the fact that some movies have negative predicted views. While replacing these negative results with zeroes could have been an easy patch to adopt, it was chosen to not change these numbers, to avoid masking the problem.

