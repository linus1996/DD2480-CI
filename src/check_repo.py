import json
import subprocess as s

def check(url, repo, branch):                                                                                                                                                                                                                                                                           
    s.run(['git', 'clone', url])                                 
    s.run(['git', '-C', repo, 'checkout', branch])           
    
    status = None
    try:
        s.run(['test', '-f', 'src/scripts.sh'])
        status = s.run(['sh', repo + '/src/scripts.sh'])  
    except IOError:
        class Status(object):
            pass
        status = Status()
        status.returncode = 3
        status.stderr = 'Error: Missing compilation/test script file.'
    finally:
        s.run(['rm', '-rf', repo])

    return status