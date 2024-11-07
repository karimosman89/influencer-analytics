import pandas as pd

def calculate_metrics(df):
    """Calculate important metrics like average engagement rate and follower growth."""
    df['engagement_rate'] = pd.to_numeric(df['engagement_rate'], errors='coerce')
    df['followers'] = pd.to_numeric(df['followers'], errors='coerce')

    metrics = {
        'average_engagement_rate': df['engagement_rate'].mean(),
        'average_followers': df['followers'].mean(),
        'follower_growth_rate': df['followers'].pct_change().mean()
    }
    return metrics

def filter_top_influencers(df, min_followers, min_engagement):
    """Filter influencers who meet minimum criteria for followers and engagement rate."""
    top_influencers = df[(df['followers'] >= min_followers) & (df['engagement_rate'] >= min_engagement)]
    return top_influencers

def engagement_vs_followers(df):
    """Correlation analysis between followers and engagement rate."""
    correlation = df['followers'].corr(df['engagement_rate'])
    return correlation

