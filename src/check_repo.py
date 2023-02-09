import subprocess as s

def check(url, repo, branch): 
    """
    A method for compiling and testing a repository branch.
    Input: url for cloning repository, repository name and branch name.
    Output: status code and message for potential errors.
    Returncode 0 means successful compilation and testing.
    Returncode 1 means compilation error.
    Returncode 2 means failed tests.
    Returncode 3 means missing/invalid script file for running the check.
    """
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