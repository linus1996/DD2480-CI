import subprocess as s
from sys import stderr

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
    if(s.run(['test', '-f', 'src/scripts.sh']).returncode == 1):
        class Status(object):
            pass
        status = Status()
        status.returncode = 3
        status.stderr = 'Error: Missing compilation/test script file.'
    else:
        status = s.run(['sh', 'src/scripts.sh'], stderr=s.PIPE)
        # _, std_err = status.communicate()
        status.stderr = status.stderr.decode()
        # with open('<stderr>', 'r') as f:
        #     status.stderr = f.read()
        #     print(status.stderr)
        # status.stderr = status.stderr.communicate()[0]

    s.run(['rm', '-rf', repo])
    if status.returncode == 0:
        status.stderr = 'Compilation and tests succeeded!'
    return status