import random
import time
import logging
from datetime import datetime
from instagrapi import Client

# Configure logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize the Instagram Client
cl = Client()

# Save credentials from user
myusername = input("Type Username: ")
mypassword = input("Type Password: ")

# Login function
def login():
    try:
        # Log in directly with provided credentials
        cl.login(myusername, mypassword)
        logging.info("Logged in successfully.")
    except Exception as e:
        logging.error(f"Login failed: {e}")
        exit(1)  # Exit if login fails

# Log follow activity to a file
def log_activity(username):
    with open("follow_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - Followed: {username}\n")
    logging.info(f"Logged: {username}")

# Follow random users
def follow_random_users(daily_limit=50):
    followed = 0

    # Fetch a pool of accounts to follow
    user_id = cl.user_id_from_username("cristiano")  # Replace with your target username
    logging.info("Fetching followers...")
    followers = cl.user_followers(user_id, amount=500)

    if not followers:
        logging.warning("No followers found. Exiting...")
        return

    while followed < daily_limit:
        try:
            # Randomly select a user from the followers list
            user_id, user_data = random.choice(list(followers.items()))
            username = user_data.username

            # Follow the user
            cl.user_follow(user_id)
            logging.info(f"Followed {username}")
            followed += 1

            # Log the follow activity
            log_activity(username)

            # Random delay between actions (20–40 minutes)
            delay = random.randint(1200, 2400)
            logging.info(f"Waiting for {delay // 60} minutes before the next action...")
            time.sleep(delay)

        except Exception as e:
            logging.error(f"Error while following user: {e}")

# Main script
if __name__ == "__main__":
    login()
    follow_random_users()
