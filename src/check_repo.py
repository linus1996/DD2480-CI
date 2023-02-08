import subprocess as s

def check(url, repo, branch):                                                                                                                                                                                                                                                                           
    s.run(['git', 'clone', url])                                 
    s.run(['git', '-C', repo, 'checkout', branch])           
    
    status = None
    if(s.run(['test', '-f', 'scripts.sh']).returncode == 1):
        class Status(object):
            pass
        status = Status()
        status.returncode = 3
        status.stderr = 'Error: Missing compilation/test script file.'
    else:
        status = s.run(['sh', 'scripts.sh'])  

    s.run(['rm', '-rf', repo])
    if status.returncode == 0:
        status.stderr = 'Compilation and tests succeeded!'
    return status