import requests

def is_online(user):

    channelName = user

    contents = requests.get('https://www.twitch.tv/' + channelName).content.decode('utf-8')

    return 'isLiveBroadcast' in contents