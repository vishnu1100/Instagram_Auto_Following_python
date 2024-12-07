import random
import time
from datetime import datetime
from instagrapi import Client

# Login to Instagram
cl = Client()
cl.login("wdwewaerewd", "MA/E2LEM7/gi*?i")  # Replace with your Instagram credentials

# Safe API call wrapper
def safe_api_call(func, *args, retries=3, **kwargs):
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"API call failed: {e}")
            if attempt < retries - 1:
                print(f"Retrying... ({attempt + 1}/{retries})")
                time.sleep(2 ** attempt)
            else:
                raise

# Function to log activity
def log_activity(username):
    with open("follow_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - Followed: {username}\n")
    print(f"Logged: {username}")

# Function to follow random users
def follow_random_users(daily_limit=50):
    followed = 0

    # Fetch the user's followers safely
    user_id = cl.user_id_from_username("wdwewaerewd")  # Replace with your username
    try:
        followers = safe_api_call(cl.user_followers, user_id, amount=500)
    except Exception as e:
        print(f"Error fetching followers: {e}")
        return
    
    if not followers:
        print("No followers found. Exiting...")
        return

    while followed < daily_limit:
        try:
            # Randomly select a user from the followers list
            user_id, user_data = random.choice(list(followers.items()))
            username = user_data.username
            
            # Follow the user
            safe_api_call(cl.user_follow, user_id)
            print(f"Followed {username}")
            followed += 1
            
            # Log the follow activity
            log_activity(username)

            # Random delay between actions (20-40 minutes)
            delay = random.randint(1200, 2400)
            print(f"Waiting for {delay // 60} minutes...")
            time.sleep(delay)

        except Exception as e:
            print(f"Error while following user: {e}")
        
        # Pause to simulate natural usage
        current_hour = datetime.now().hour
        if current_hour >= 0 and current_hour <= 6:  # Avoid activity between 12 AM - 6 AM
            print("Sleeping for the night...")
            time.sleep(3600 * (6 - current_hour))

# Run the bot
if __name__ == "__main__":
    follow_random_users()
