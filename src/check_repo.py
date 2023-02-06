import json
import subprocess as s

def check(payload):                                                        
                                                                                                                             
    branch = payload['ref'].split('/')[-1]
    url = payload['repository']['clone_url']
    repo = payload['repository']['name']
                                                                                                      
    s.run(['git', 'clone', url])                                 
    s.run(['git', '-C', repo, 'checkout', branch])           
    
    if(s.run(['test', '-f', 'scripts.sh']) == 1):
        return 'Error: Missing compilation/test script file.'
    
    status = s.run(['sh', repo + '/scripts.sh']).returncode         
    s.run(['rm', '-rf', repo])

    return status