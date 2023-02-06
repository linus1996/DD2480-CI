import json
import subprocess as s

def check(url, repo, branch):                                                                                                                                                                                                                                                                           
    s.run(['git', 'clone', url])                                 
    s.run(['git', '-C', repo, 'checkout', branch])           
    
    if(s.run(['test', '-f', 'scripts.sh']) == 1):
        return 'Error: Missing compilation/test script file.'
    
    status = s.run(['sh', repo + '/scripts.sh'])        
    s.run(['rm', '-rf', repo])

    return status