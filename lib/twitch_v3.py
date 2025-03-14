import requests

def get_app_access_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f'Error getting access token: {response.text}')

def get_twitch_channel_info(broadcaster_id, client_id, client_secret):
    access_token = get_app_access_token(client_id, client_secret)
    url = f'https://api.twitch.tv/helix/channels?broadcaster_id={broadcaster_id}'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Client-Id': client_id
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': response.status_code, 'message': response.text}
