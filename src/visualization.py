import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_followers_vs_engagement(df):
    """Scatter plot of followers vs. engagement rate to analyze influence."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='followers', y='engagement_rate', data=df)
    plt.title("Followers vs Engagement Rate")
    plt.xlabel("Number of Followers")
    plt.ylabel("Engagement Rate (%)")
    plt.show()

def plot_follower_growth(df):
    """Line plot to show follower growth over time."""
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='followers', data=df)
    plt.title("Follower Growth Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Followers")
    plt.show()

def plot_top_influencers(df):
    """Bar plot to display top influencers by engagement rate."""
    top_influencers = df.nlargest(10, 'engagement_rate')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='engagement_rate', y='influencer', data=top_influencers)
    plt.title("Top Influencers by Engagement Rate")
    plt.xlabel("Engagement Rate (%)")
    plt.ylabel("Influencer")
    plt.show()

