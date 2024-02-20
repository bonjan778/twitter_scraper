from ntscraper import Nitter

def display_and_save_tweets_info(tweets_data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        if 'tweets' in tweets_data and tweets_data['tweets']:
            for tweet in tweets_data['tweets']:
                user_info = f"User: {tweet['user']['name']} ({tweet['user']['username']})"
                date_info = f"Date: {tweet['date']}"
                text_info = f"Text: {tweet['text']}\n"

                print(user_info)
                file.write(user_info + '\n')

                print(date_info)
                file.write(date_info + '\n')

                print(text_info)
                file.write(text_info + '\n')

                if tweet['pictures']:
                    pictures_info = "Pictures:"
                    print(pictures_info)
                    file.write(pictures_info + '\n')
                    for pic in tweet['pictures']:
                        picture = f" - {pic}"
                        print(picture)
                        file.write(picture + '\n')

                if tweet['is-retweet']:
                    retweet_info = "This is a retweet."
                    print(retweet_info)
                    file.write(retweet_info + '\n')

                stats_info = f"Stats: Comments: {tweet['stats']['comments']}, Retweets: {tweet['stats']['retweets']}, Quotes: {tweet['stats']['quotes']}, Likes: {tweet['stats']['likes']}\n"
                print(stats_info)
                file.write(stats_info + '\n')

                separator = "--------------------------------------------------\n"
                print(separator)
                file.write(separator)
        else:
            no_tweets_info = "No tweets to display."
            print(no_tweets_info)
            file.write(no_tweets_info + '\n')


scraper = Nitter(log_level=1, skip_instance_check=False)
random_instance = scraper.get_random_instance()

francetravail_tweets = scraper.get_tweets("FranceTravail", mode='user', number=10, instance=random_instance)

display_and_save_tweets_info(francetravail_tweets, "/home/user/francetravail_tweets")