import requests
import json

"""
A method for creating status updates for the CI server.
Input: A json payload containing repository information, the current status of the CI server and an authorization token.
Output: A post request containing the new status of the CI server.
"""
def update_status(json_payload, status, auth_token):
	
	sha = json_payload['head_commit']['id'] 
	status_url = json_payload["repository"]['statuses_url'] 
	status_url_sha = status_url.replace('{sha}',sha) 
	post_url = status_url_sha[:8] + auth_token + ':x-oauth-basic@' + status_url_sha[8:]
	
	try:
		if status == 'pending':
			payload = {'state':status, 
			'description':'The CI service is currently running',
			'context': 'CI for group 17'}
		elif status == 'success':
			payload = {'state':status, 
			'description':'The build succeeded!',
			'context': 'CI for group 17'}
		elif status == 'failure':
			payload = {'state':status, 
			'description':'The build failed',
			'context': 'CI for group 17'}
		post_req = requests.post(post_url, json=payload)
		return post_req

	
	except Exception:
		return None
		