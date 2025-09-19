def is_valid_email(email):
    # Must contain exactly one '@'
    if email.count('@') != 1:
        return False
    # Must contain at least one '.'
    if '.' not in email:
        return False
    # Must not start or end with special characters
    special_chars = {'@', '.'}
    if email[0] in special_chars or email[-1] in special_chars:
        return False
    return True

