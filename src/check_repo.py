import json
import subprocess as s

def check(url, repo, branch):                                                                                                                                                                                                                                                                           
    s.run(['git', 'clone', url])                                 
    s.run(['git', '-C', repo, 'checkout', branch])           
    
    try:
        s.run(['test', '-f', 'src/scripts.sh'])
    except IOError:
        class Status(object):
            pass
        status = Status()
        status.returncode = 3
        status.stderr = 'Error: Missing compilation/test script file.'
        return status
    
    status = s.run(['sh', repo + '/src/scripts.sh'])        
    s.run(['rm', '-rf', repo])

    return status