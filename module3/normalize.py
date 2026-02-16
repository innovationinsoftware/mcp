def normalize_username(user):
    """
    Normalize a username by converting it to lowercase and stripping leading/trailing whitespace.
    
    Parameters:
    user (str): The username to normalize.
    
    Returns:
    str: The normalized username.
    """
    if not isinstance(user, str):
        raise ValueError("Username must be a string.")
    
    return user.strip().lower()