import requests

def update_status(sha, status_url, status, auth_token):
    
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
        return post_req

    except Exception:
        return None
        