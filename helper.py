from tgtg import TgtgClient
from json import load, dump
from typing import Union


def get_credentials(email: str, to_json: bool = True) -> Union[dict, None]:
    """
    Helper function: Get the credentials for a specific email address
    Returns json file with access_token, refresh_token and user_id which are used to build the tgtg client
    You should run this function only once, then you can build client from the credentials.json file
    """
    # Get the credentials from the tgtg API
    client = TgtgClient(email=email)
    print('Getting credentials...')
    print('You should receive an email from tgtg. Please validate the login by clicking the link inside the email.')
    credentials = client.get_credentials()
    if to_json:
        # Save the credentials to a json file
        f = open('credentials.json', 'w')
        dump(credentials, f)
        f.close()
        print('Credentials saved to credentials.json')
    else:
        return credentials
    
if __name__ == '__main__':
    # Get your credentials
    get_credentials(email='siomchen3@gmail.com')