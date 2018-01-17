README

Introduction:

If you run 'SI506_finalproject.py' like 'python SI506_finalproject.py [keyword]' ([keyword] should be substituted by whatever you plan to search), the project will search the keyword you input and find the first five articles with the most keywords. Then, the program will use the longest words in each of the five articles to search for 20 photos each word on Flickr and store the information of these ~100 photos (some photos may not exist any more) in a CSV file.

Files:

1. SI506_finalproject.py
2. SI506finalproject_cache.json
3. sample_longest_word.txt
4. sample_Photo.csv

Modules:

1. requests
2. json
3. sys

Instruction:

You just need to run SI506_finalproject.py like this:
	python SI506_finalproject.py [keyword]
Specifically, [keyword] should be replaced by any keyword you would like to search.

REQUIREMENTS LIST:
* Get and cache data from 2 REST APIs (list the lines where the functions to get & cache data begin and where they are invoked):
Line 28 to line 41 for NYT
Line 107 to line 121 for Flickr

* Define at least 2 classes, each of which fulfill the listed requirements:
Line 43 to line 76 for NYT
Line 161 to line 185 for Flickr

* Create at least 1 instance of each class:
Line 79 to line 81 for NYT
Line 197 to line 199 for Flickr

* Invoke the methods of the classes on class instances:
Line 83 for NYT
Line 201 and line 206 for Flickr

* At least one sort with a key parameter:
Line 82 and line 201

* Define at least 2 functions outside a class (list the lines where function definitions begin):
Line 14, line 21, line 90, line 98, line 123, and line 151

* Invocations of functions you define:
Line 27, line 78, line 106, line 149, line 191, line 165, line 169, and line 177

* Create a readable file:
Line 203 to line 206

END REQUIREMENTS LIST

* Put any citations you need below. If you borrowed code from a 506 problem set directly, or from the textbook directly, note that. If you borrowed code from a friend/classmate or worked in depth with a friend/classmate, note that. If you borrowed code from someone else's examples on a website, note that.
Cite  "params_unique_combination" function from 506 textbook
Cite "get_flickr_data" from Problem Set 7
Cite "Photo" class from Problem Set 8

* Explain in a couple sentences what should happen as a RESULT of your code running: what CSV or text file will it create? What information does it contain? What should we expect from it in terms of how many lines, how many columns, which headers...?
It should create a csv file named 'Photo.csv', which contains photo title, username, and all the tags that it has and the number of tags. See example output file in sample_Photo.csv for more information.

* Make sure you include a SAMPLE version of the file this project outputs (this should be in your list of submitted files above!).

* Is there anything else we need to know or that you want us to know about your project? Include that here!
Since the search result differs from time to time, there might be some bugs that I have not yet discovered. For example, my project ran successfully when I first finished it several weeks ago, however, when I ran it again these days, some bugs appeared, because some photos stored in my cache file no longer exists. So, if there is still some problem with my project, please let me know to ensure the code runs properly.
