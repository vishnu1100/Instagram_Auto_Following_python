import random
import time
from datetime import datetime
from instagrapi import Client

# Login to Instagram
cl = Client()
cl.login("your_username", "your_password")

# Function to log activity
def log_activity(username):
    with open("follow_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - Followed: {username}\n")
    print(f"Logged: {username}")

# Function to follow random users and log actions
def follow_users_randomly(daily_limit=50, hashtags=["technology", "coding","music","gaming", "design"]):
    followed = 0
    
    while followed < daily_limit:
        # Randomly select a hashtag
        hashtag = random.choice(hashtags)
        results = cl.hashtag_search(hashtag)
        top_posts = cl.hashtag_medias_recent(results.pk, 1)  # Get 1 user at a time
        
        for post in top_posts:
            user_id = post.user.pk
            username = post.user.username
            
            # Follow the user
            cl.user_follow(user_id)
            print(f"Followed {username}")
            followed += 1
            
            # Log the follow
            log_activity(username)
            
            if followed >= daily_limit:
                break

            # Random delay between actions (20-40 minutes)
            delay = random.randint(1200, 2400)
            print(f"Waiting for {delay // 60} minutes...")
            time.sleep(delay)
        
        # Pause to simulate natural usage
        current_hour = datetime.now().hour
        if current_hour >= 0 and current_hour <= 6:  # Avoid activity between 12 AM - 6 AM
            print("Sleeping for the night...")
            time.sleep(3600 * (6 - current_hour))

# Run the bot
if __name__ == "__main__":
    follow_users_randomly()
