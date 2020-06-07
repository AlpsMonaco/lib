from flag_parse import ftp_flag_parse
from server import start_ftp_server
from client import start_ftp_client
from exception import ftp_exit

if __name__ == "__main__":
    ftp_info = ftp_flag_parse()

    ftp_mode = ftp_info[0]
    ftp_tuple = ftp_info[1]

    if ftp_mode == 'server':
        start_ftp_server(ftp_tuple)
        pass
    elif ftp_mode == 'client':
        start_ftp_client(ftp_tuple)
        pass
    elif ftp_mode == 'upload':
        pass
    else:
        ftp_exit(1, 'mode error')
        pass
    ftp_exit(0, 'Good bye')
    pass
