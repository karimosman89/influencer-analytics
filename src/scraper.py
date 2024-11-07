import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def scrape_influencer_data(url):
    """Scrapes influencer data from a given social media URL."""
    driver = webdriver.Chrome()  # Initialize Selenium WebDriver
    driver.get(url)
    time.sleep(3)  # Allow time for the page to load
    
    # Extract data with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    followers = soup.find('span', class_='follower-count').text  # Adjust selectors based on website
    engagement_rate = soup.find('span', class_='engagement-rate').text
    posts = soup.find_all('div', class_='post')  # Collect individual posts' data if needed
    
    driver.quit()
    return {'followers': followers, 'engagement_rate': engagement_rate, 'posts': len(posts)}

def batch_scrape(urls):
    """Scrapes data from multiple influencer URLs."""
    data = []
    for url in urls:
        influencer_data = scrape_influencer_data(url)
        data.append(influencer_data)
    return data

