from ntscraper import Nitter
import json


scraper = Nitter(log_level=1, skip_instance_check=False)

github_hash_tweets = scraper.get_tweets("pemilu 2024", mode='term', number=2)
profile_information = scraper.get_profile_info("@MMargani5")

with open('data.json', 'w') as f:
    json.dump(github_hash_tweets, f)

with open('data_profile.json', 'w') as f:
    json.dump(profile_information, f)
