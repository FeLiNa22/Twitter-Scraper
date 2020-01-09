# Twitter-Scraper
Python - tweepy bot used to scrape data from twitter profiles
Makes use of search tokens and filters to scrape twitter users bio's for marketing purposes.
Do not abuse this script for spamming or other illegal purposes :)

## Inital Setup

     1.) Apply for a twitter developer account here https://developer.twitter.com/en/apply-for-access
     2.) Login to your account and copy and paste the consumer key, consumer secret key , access token, access secret into the TwitterScraper.py file.
     3.) Change the filters and search tokens to whatever you want, this will be used in the script to make sure you only gather data of twitter profiles that are relevant to the search.
     
     The script has the dependancies tweepy and pandas as python modules
     You can install these by doing the following : 
     # Enter the directory of the project and type in command line 
     ------------------------------------->
     1.)  pip install -r requirements.txt
    
## Running the script
    # Enter the directory of the project and type in command line
    ------------------------------------->
    1.) sudo python TwitterScraper.py
    2.) The Data.csv file should be populated with all the twitter data that has been scraped

## FeLiNa 
    
    I have added an example file (ExampleDataScraped.csv) to show the kind of data this scraper will return
    
