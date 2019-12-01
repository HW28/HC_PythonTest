# HC_PythonTest

## Instructions<br/>

0 - Install the libraries of the file "HC_PythonTest/PythonDevelopExercise/src/requeriments.txt" <br/>
1 - Add the excel file with the data at folder "HC_PythonTest/PythonDevelopExercise/src/in/" <br/>
2 - Set de Twitter API Keys at function twitter_api of "HC_PythonTest/PythonDevelopExercise/src/functions.py" <br/>
3 - Execute in a terminal the script "main.py" ( Terminal command - python main.py) 4 - In case we want to store the output <br/>("HC_PythonTest/PythonDevelopExercise/src/out/" ) , execute - python main.py > out/$Name_of_file<br/>
4 - Unit Test changes before execute:<br/>
   &nbsp;&nbsp; 4.1 - Modify the screen name of the test for the owner of the input Twitter API keys: <br/>
   &nbsp;&nbsp;&nbsp;       a) test_tweetwoimage (line 23)<br/>
   &nbsp;&nbsp;&nbsp;       b) test_tweetimage_text (line 36)<br/>
   &nbsp;&nbsp; 4.2 - Modify the number of tweets at test_obtain_excel_data by the number of input data at the excel input file<br/>
   &nbsp;&nbsp; 4.3 - Modify the Tweets Text Message at  the functions:
   &nbsp;&nbsp;&nbsp;       a) test_tweetwoimage (line 20)<br/>
   &nbsp;&nbsp;&nbsp;       b) test_tweetimage_text (line 31)<br/>
5 - Execute in a terminal the script "unit_tests.py" (Terminal command -python -m unittest unit_tests.py)<br/>
## Results:<br/>

### Part 1<br/>
The tweets have been tested at twitter account: @swh_28 (https://twitter.com/swh_28) <br/>
At the folder "HC_PythonTest/PythonDevelopExercise/src/out/" - there is an example of results. <br/>
Observations of the program: <br/>
In case the tweet is too long it will split into different parts <br/>
If the image isn't available or it isn't an URL, it will send only the text If the date is outdated, it will send an error message and pass to the next tweet<br/>

### Part 2 <br/>
The results of part 2 are at pdf "Ex 2- SYSTEM DESIGN DIAGRAM.pdf" from folder "HC_PythonTest/"<br/>
