import requests

def update_status(sha, status_url, status, auth_token):
    """
	A method for creating status updates for the CI server.
	Input: A json payload containing repository information, the current status of the CI server and an authorization token.
	Output: A post request containing the new status of the CI server.
	"""
    status_url_sha = status_url.replace('{sha}',sha) 
    post_url = status_url_sha[:8] + auth_token + ':x-oauth-basic@' + status_url_sha[8:]
    
    try:
        if status == 'pending':
            payload = {'state':status, 
            'description':'CI server is running',
            'context': 'CI python server for group 17'}
        elif status == 'success':
            payload = {'state':status, 
            'description':'Build success',
            'context': 'CI python server for group 17'}
        elif status == 'failure':
            payload = {'state':status, 
            'description':'Build failed',
            'context': 'CI python server for group 17'}
        post_req = requests.post(post_url, json=payload)
        print("Status set with return code", post_req)
        return post_req

    except Exception:
        print("Couldn't set status D:")
        return None
        