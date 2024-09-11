import string
import json

def check_password_strength(password, first_name, last_name):
    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digit = any(c.isdigit() for c in password)

    characters = [upper_case, lower_case, special, digit]
    length = len(password)
    score = 0

    try:
        with open('common.txt', 'r') as f:
            common = [line.strip() for line in f.read().splitlines()]
    except FileNotFoundError:
        common = []

    # Check if password contains first or last name
    if first_name.lower() in password.lower() or last_name.lower() in password.lower():
        return {"status": "error", "message": "Password cannot contain your first or last name", "score": 0}

    if password in common:
        return {"status": "error", "message": "Password was found in the common list.", "score": 0}

    if length > 128:
        return {"status": "error", "message": "Password is too long. Maximum allowed length is 128 characters.", "score": 0}
    elif length < 8:
        return {"status": "error", "message": "Password is too short. Minimum allowed length is 8 characters.", "score": 0}

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 16:
        score += 1
    if length > 20:
        score += 1
    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1

    if score < 4:
        return {"status": "warning", "message": "Your password is weak.", "score": score}
    elif score == 4:
        return {"status": "warning", "message": "Your password is fine, but you can make it stronger.", "score": score}
    elif 4 < score < 6:
        return {"status": "good", "message": "Your password is good.", "score": score}
    else:
        return {"status": "great", "message": "Your password is great.", "score": score}

def lambda_handler(event, context):
    # Extract data from event
    body = event.get('body', {})
    
    if isinstance(body, str):
        body = json.loads(body)  # Only parse if body is a string
    
    password = body.get('password')
    first_name = body.get('first_name')
    last_name = body.get('last_name')

    if not password or not first_name or not last_name:
        return {
            "statusCode": 400,
            "body": json.dumps({"status": "error", "message": "Password, first name, and last name are required."})
        }

    result = check_password_strength(password, first_name, last_name)
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }