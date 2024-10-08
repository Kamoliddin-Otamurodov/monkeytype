import requests
import csv
username = 'kolik2125'

def get_wpm_accuracy(username:str,time:int)->dict:
    url = f'https://api.monkeytype.com/users/{username}/profile'
    response = requests.get(url)
    # Get the JSON data from the response
    data = response.json()
 
    time = data['data']['personalBests']['time'][str(time)][0]
    # Get accuracy
    accuracy = time['acc']
    # Get wpm
    wpm = time['wpm']
    return {'wpm':wpm,'accuracy':accuracy}
    
# Read users info from csv file
def get_user_info(file_path:str)->dict:
    users = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header
        next(csv_reader)
        for row in csv_reader:
            users.append(
                {
                    'full_name': row[1],
                    'username': row[2],
                }
            )
    return users
    
def get_users_wpm_accuracy(users:dict,time:int)->dict:
    users_wpm_accuracy = {}
    for user in users:
        users_wpm_accuracy[user['username']] = get_wpm_accuracy(user['username'],time)
    return users_wpm_accuracy

users = get_user_info('monkeytype.csv')
users_wpm_accuracy = get_users_wpm_accuracy(users,15)
print(users_wpm_accuracy)
# print(get_wpm_accuracy(username,15))
