import tweepy
import pandas as pd
from tweepy import OAuthHandler
import os

############################################################################################
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
csvfile = "Data.csv" # Change this to output into different files
filters = ['location','UK','England'] 
SearchTokens = ['Technology','Innovation','Hardware','Software']
#############################################################################################

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Attributes of a twitter user profile (this header is already in my file)
twitter_datafile_attr = ['follow_request_sent', 'profile_use_background_image',       'contributors_enabled', 'id', 'verified', 
                       'profile_image_url_https', 'profile_sidebar_fill_color', 'profile_text_color', 'followers_count', 
                       'profile_sidebar_border_color', 'id_str', 'default_profile_image', 'listed_count' 'is_translation_enabled', 
                       'utc_offset', 'statuses_count', 'description', 'friends_count', 'location', 'profile_link_color', 
                       'profile_image_url', 'notifications', 'geo_enabled', 'profile_background_color', 'profile_banner_url', 
                       'profile_background_image_url', 
                       'screen_name', 'lang', 'following', 'profile_background_tile', 'favourites_count', 'name', 'url', 'created_at', 
                       'profile_background_image_url_https', 'time_zone', 'protected', 'default_profile', 'is_translator']
class bot:
    def __init__(self,path):
        self.path = path
        if os.path.exists(path):
            self.df=pd.read_csv(path)
        else:
            self.df = pd.DataFrame(columns=['ID', 'Name', 'Twitter Handle', 'Twitter Page', 'Website', 'Bio', 'Num of following', 'Num of followers'])

    def newDBrow(self,ID,name,username,twitterLink,website,bio,following,followers):
        if not ID in self.df['ID'].values:
            new_row = pd.DataFrame([[ID,name,username,twitterLink,website,bio,following,followers]],columns=self.df.columns )
            self.df = self.df.append(new_row, ignore_index=True)
    
    def process_page(self,page,filters):
        for user in page:
            if filters[0]=='location':
                if user.location in filters[1:]:
                    self.newDBrow(user.id,user.name,user.screen_name,'https://twitter.com/'+user.screen_name,user.url,user.description,user.friends_count,user.followers_count)
        self.df.to_csv(self.path, index=False)
        
    def search_query(self,SearchTokens,num_of_pages,filters=['']):
        for Token in SearchTokens:
            for page in tweepy.Cursor(api.search_users, q=Token, count=100, tweet_mode='extended').pages(num_of_pages):
                self.process_page(page,filters)
    
    
max_pages = 51
twitbot = bot(csvfile)
twitbot.search_query(SearchTokens,max_pages,filters=filters)
print(twitbot.df)


        
