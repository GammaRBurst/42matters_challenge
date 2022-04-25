# Challenge 2: Word Count in PySpark

## Question
The goal of this task is to count the words of a given dataset.  
The tasks to do are:

1. Download the data set over which to run word count from the following link: [biographies.list.gz](https://s3.amazonaws.com/products-42matters/test/biographies.list.gz)
1. Implement a PySpark program that counts the number of occurrences of each word in the provided file. Only lines starting with the "BG:" should be considered, and a whitespace tokenizer should be used for tokenizing the text.

### Deliverables
- Code
- Documentation that explains how to run the code
- The result of the word count

## Documentation

### Run with Docker
This option is better suited for users who just want to execute the code once and see the results. `Docker` has to be installed to proceed.

Open a terminal and `cd` into the directory for this challenge. From here execute

    docker image build -t challenge2-grb .

to build the docker image. The name `challenge2-grb` can be changed according to personal preferences and other images already installed on the system.  
**Note**: Linux users may have to use `sudo` to execute `docker` commands.

To run the program, execute this next line

    docker run --volume absolute_local_path:/home/app/result --name challenge2-grb_container challenge2-grb

where `absolute_local_path` is the absolute path of the current directory (or any other directory where you want to write the output CSV file). Linux and Mac users can use the following code to avoid typing the whole path.

    docker run --volume $(pwd):/home/app/result --name challenge2-grb_container challenge2-grb

**Warning**: Depending on your internet connection and your computer, compiling and executing this program may require a few minutes.

## Results
The resulting word count can be found in the [word_count.csv](word_count.csv) file. The results are arranged from most to least frequent word. As can be seen already from the first lines, some of the entries are obvious duplicates to our human eye, e.g. "*the*" and "*The*", or "*(qv)*", "*(qv).*" and "*(qv),*".  
The CSV file produced assumes that this level of specification is expected, but it can be easily adapted to be case-insensitive and to remove all non-letter and non-digit characters (`[^a-z0-9]`).

