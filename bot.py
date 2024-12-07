import random
import time
from datetime import datetime
from instagrapi import Client

# Initialize the Instagram Client
cl = Client()

# save credentials from user 
myusername = input('Type Username : ')
mypassword = input('Type passsword : ')
#mytargetusername = input('Type target username : ')

# Login with session
def login_with_session():
    try:
        # Load session settings
        cl.load_settings("session.json")
        cl.login()
        print("Logged in using saved session.")
    except Exception as e:
        print(f"Failed to load session: {e}")
        # Fallback to manual login if session fails
        cl.login(myusername, mypassword)  # Replace with your credentials
        cl.dump_settings("session.json")
        print("New session saved.")

# Log follow activity to a file
def log_activity(username):
    with open("follow_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - Followed: {username}\n")
    print(f"Logged: {username}")

# Follow random users
def follow_random_users(daily_limit=50):
    followed = 0

    # Fetch your followers as a pool of accounts to follow
    user_id = cl.user_id_from_username("cristiano")  # Replace with your username
    print("Fetching followers...")
    followers = cl.user_followers(user_id, amount=500)

    if not followers:
        print("No followers found. Exiting...")
        return

    while followed < daily_limit:
        try:
            # Randomly select a user from the followers list
            user_id, user_data = random.choice(list(followers.items()))
            username = user_data.username

            # Follow the user
            cl.user_follow(user_id)
            print(f"Followed {username}")
            followed += 1

            # Log the follow activity
            log_activity(username)

            # Random delay between actions (20–40 minutes)
            delay = random.randint(1200, 2400)
            print(f"Waiting for {delay // 60} minutes before the next action...")
            time.sleep(delay)

        except Exception as e:
            print(f"Error while following user: {e}")

# Main script
if __name__ == "__main__":
    login_with_session()
    follow_random_users()
