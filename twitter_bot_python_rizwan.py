from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import random

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

random_news = ["https://www.google.com/search?q=artificial+intelligence+news",
               "https://www.google.com/search?q=chatgpt+news",
               "https://www.google.com/search?q=ai+investment+news",
               "https://www.google.com/search?q=ai+bubble+news"
               ]

random_article = random.choice(random_news)
driver.get(random_article)
driver.maximize_window()

# Wait for the first article headline to be visible
wait = WebDriverWait(driver, 5)
article_headline = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "WlydOe")))

# Get the href attribute of the first article headline
href_link = article_headline.get_attribute("href")
print(href_link)

# Navigate to Twitter
driver.get("https://twitter.com")

# You can continue interacting with Twitter, for example, by logging in or searching for specific content.
# Here's an example of logging into Twitter.
# Replace 'your_username' and 'your_password' with your actual Twitter credentials.
import time
time.sleep(5)
# Locate the username and password input fields
# Locate the username and password input fields
from selenium.webdriver.common.keys import Keys
username_input = driver.find_element(By.NAME, "text")
username_input.send_keys("enter_user_name")
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button'][contains(.,'Next')]"))).click()
time.sleep(5)
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("enter_password")
time.sleep(5)

# Submit the login form
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button'][contains(.,'Log in')]"))).click()
time.sleep(5)


tweet_reply = [
    "Wow! I just read this article today, and it's absolutely mind-blowing! It's fascinating how AI is revolutionizing the world. What are your thoughts?",
    "I stumbled upon this article today, and it's a true game-changer! The advancements in AI are reshaping industries and opening up new possibilities. It's a must-read!",
    "Just finished reading this incredible article today! It highlights the amazing potential of AI and how it's transforming various aspects of our lives. It's definitely worth sharing!",
    "Kudos to the author of this thought-provoking article I read today! It truly showcases the power of AI and how it's pushing boundaries to solve complex problems. What do you think?",
    "This article caught my attention today, and I can't stop thinking about it! It explores the exciting world of AI and how it's shaping the future. Share your thoughts!",
    "Today's read is a real eye-opener! It delves into the fascinating advancements in AI and how they're revolutionizing different industries. What's your take on it?",
    "Just finished reading this thought-provoking article that made me ponder the limitless possibilities of AI. It's incredible to see how far we've come. Have you read it too?",
    "I found this article today that sheds new light on the transformative impact of AI. It's really intriguing and opens up new avenues for discussion. I'd love to hear your opinions!",
    "I just read this article today, and it's a definite must-read! It provides fresh perspectives on the AI revolution and its implications for our future. What's your perspective on it?",
    "I delved into this captivating article today that highlights the awe-inspiring capabilities of AI. It's truly amazing to witness the potential and impact of this technology. Share your thoughts!",
    "I discovered this article today that offers fresh insights into the AI revolution. It's thought-provoking and raises important questions about the future. What are your thoughts?",
    "Just finished reading this intriguing article that got me thinking about the potential and challenges of AI. It's a topic that requires deep reflection. Any thoughts on it?",
    "Came across this enlightening article today, and it's a must-read for everyone interested in AI! It explores the latest advancements and their impact on society. Share your insights!",
    "Today's read is an eye-opening exploration of AI's impact on our lives. It dives into the ethical considerations and the evolving relationship between humans and AI. Let's discuss!",
    "I'm truly blown away by this article I read today! It highlights incredible breakthroughs in AI that push the boundaries of what we thought was possible. What's your reaction?",
    "I just read this thought-provoking article that challenges conventional wisdom about AI. It offers a fresh perspective and opens up new avenues for exploration. Join the conversation!",
    "Today's read is absolutely mind-blowing! I highly recommend it to everyone interested in AI. It showcases the latest advancements and sparks exciting possibilities. Share your thoughts!",
    "This article I stumbled upon today is a real game-changer! It reveals the limitless potential of AI and its impact on various aspects of our lives. What do you think about it?",
    "Just finished reading this insightful article that left me with a lot to ponder about AI and its implications. It's a thought-provoking read. What are your thoughts?",
    "Today's read is pure gold! Don't miss out on this enlightening article about the latest developments in AI. It provides valuable insights and sparks interesting discussions. Share your opinions!"
]


random_tweet = random.choice(tweet_reply)
tweet = random_tweet + href_link


autotw1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
autotw1.click()

element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
ActionChains(driver).move_to_element(element).send_keys(tweet).perform()
time.sleep(5)
button2 = driver.find_element(By.CSS_SELECTOR,"div[data-testid='tweetButtonInline']")
button2.click()

import datetime

file = open(r"C:\Users\Reese\OneDrive\Desktop\Twitter Bot\rizwan_ye_bot_run.txt", 'a')
file.write(f'{datetime.datetime.now()} - The script ran \n')
driver.quit()
