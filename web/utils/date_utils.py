from datetime import datetime

def format_date(date):
    """
    Format a date object into a readable string format (e.g., "Jan 1, 2024").
    """
    return date.strftime('%b %d, %Y')