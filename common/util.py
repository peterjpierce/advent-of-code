import datetime


def now():
    """Get a current datetime object."""
    return datetime.datetime.now()


def elapsed_since(start_time):
    """Get seconds since a given start_time."""
    return (now() - start_time).total_seconds()
