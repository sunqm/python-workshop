# Final Project
In the final project, your goal is to develop a full-featured API (application programming interface) 
library to allow downloading and presenting organization and people data from Crunchbase. 

## Background
From Wikipedia: 
> Crunchbase is a platform for finding business information about private and public companies. Crunchbase information includes investments and funding information, founding members and individuals in leadership positions, mergers and acquisitions, news, and industry trends.

Crunchbase has its own API but we will be using Rapidapi to access the data. Rapidapi is a 
marketplace for API that allows users to access different APIs with a single authentication
key and SDK.

## Project requirements
Create a new Github project named cbapi. In it you will need to design an develop a package that provides 
functionalities to retrieve both organization and people data through the 
[ODM endpoints](https://rapidapi.com/crunchbase-team1-crunchbase/api/crunchbase?endpoint=5b203ce0e4b05b36a9cbf685) 
in Rapidapi. The very basic function to support will be to provide a method that can return a number of 
organizations/people. Note that due to the large number of records, the response from the Crunchbase API are paginated.
That means you will need to iterate through the pages to obtain the records you need. 

To gain access to Rapidapi, you will need to register for an account and obtain your own access key. Please
keep the key in a safe place. DO NOT distribute it with your code. There is a simple 
[tutorial](https://rapidapi.com/blog/crunchbase-api-python-automated-sales-pipeline/) that can get you started. 

## Some Tips
* Try to make the project as full-fledged as possible. Your project can actually become useful in the Github community! 
For example, try to have README, setup.py, requirements.txt, unit tests, etc. You can even learn to set up continuous integration.
A very good example to follow is [yfinance](https://github.com/ranaroussi/yfinance).
* There are optional parameters that can be passed to the Crunchbase API, such as "name" that can be used to filter 
organizations by text query. Think of how to integrate them into your library.
* I recommend using "requests" library to make HTTP calls to the API. There are example code in Rapidapi.
* Fetching results page-by-page can be slow. Have an option to leverage multi-threading to speed it up?
* A suitable output format would be pandas DataFrame. For a large amount of data, returning a generator is also a good idea.
Think about how to make your API more versatile and powerful.
* Learn to use Github properly. Since this is a much larger project than your previous homework, you may want to develop
this project iteratively. Make some progress and push the changes to remote frequently. Develop the habit of leveraging 
version control system to gain productivity.
* At the end of the day, it is your own project and you decide how it should be designed and used. So try to make it as perfect
as possible!
