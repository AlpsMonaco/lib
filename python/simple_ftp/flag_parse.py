# -*- coding:utf-8 -*-
import argparse
import config

"""
-m --method   模式 (server,client,upload)
-h --host     主机ip地址
-p --password 密码
-P --port     端口（21）
   --path     文件路径
"""

''' 
必定返回一个ftp服务信息的元组 (host, port, user, password,path)
'''


def ftp_flag_parse():
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument('-h', '--host', dest="host",
                        help="ftp host", default='')

    parser.add_argument('-P', '--port', dest="port",
                        help="ftp port", default=21)

    parser.add_argument('-u', '--user', dest="user",
                        help="ftp user", default='')

    parser.add_argument('-p', '--password', dest="password",
                        help="ftp password", default='')

    parser.add_argument('-a', '--path', metavar='target_path', default="",
                        help="target path,coule be upload path or ftp server serve path", dest='path')

    parser.add_argument('-c', '--config', const="./config.json",
                        nargs='?', help="config.json file path", dest="use_config", metavar='CONFIG')

    parser.add_argument('-m', '--mode', dest="mode",
                        help="ftp application behavirour: server,client,upload", default="upload", metavar='mode')

    parser.add_argument('--help', action="store_true",
                        dest="help", help="print help")

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        parser.exit(0)

    if args.use_config:
        return config.parse_json_file(args.use_config)
        pass

    return config.generate_ftp_info(args.host,
                                    args.port,
                                    args.user,
                                    args.password,
                                    args.path,
                                    args.mode)
    pass


if __name__ == "__main__":
    print(ftp_flag_parse())
    pass
