def ftp_exit(code=0, msg=''):
    if code != 0:
        msg = 'Error: ' + msg
        pass
    print(msg)
    exit(code)
