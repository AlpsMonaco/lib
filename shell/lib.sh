#!/bin/bash

function print_err() {
    echo -e "\033[31merror:$1\033[0m"
}

function print_info() {
    echo -e "\033[37m$1\033[0m"
}

function err_exit() {
    print_err "$1"
    exit 1
}

function die() {
    print_err "$1"
    exit 1
}

# $1文件名 $2 文本，保留\n
function stdout_file() {
    echo -e $2 >$1
}

# $1 user $2 pass $3 host $4 port $5 [database/file] [$6 file]
function mysql_exec_file(){
    if [ $# -eq 5 ]; then
        mysql --default-character-set=utf8 -u$1 -p$2 -h$3 -P$4 < "$5"
    elif [ $# -eq 6 ]; then
        mysql --default-character-set=utf8 -u$1 -p$2 -h$3 -P$4 -D$5 < "$6"
    else
        err_exit "mysql need 5 or 6 correct args to execute."
    fi
}

# $1 user $2 pass $3 host $4 port $5 [database/cmd] [$6 cmd]
function mysql_exec_command(){
    if [ $# -eq 5 ]; then
        mysql --default-character-set=utf8 -u$1 -p$2 -h$3 -P$4 -e "$5"
    elif [ $# -eq 6 ]; then
        mysql --default-character-set=utf8 -u$1 -p$2 -h$3 -P$4 -D$5 -e "$6"
    else
        err_exit "mysql need 5 or 6 correct args to execute."
    fi
}

function check_error(){
    if [ $? -ne 0 ]; then
        err_exit "Command contains error!"
    fi
}


# 获得指定目录下的所有文件夹，并去掉结尾的/
# $1 path
function get_all_dir(){
    local RESULT
    DIR_ARR="`ls $1 -F | grep "/$"`"
    
    for i in $DIR_ARR; do
        RESULT="$RESULT$i"
        RESULT="${RESULT%%\/} "
    done

    echo ${RESULT%%\ }
}

# 模糊匹配，杀死进程
# $1 需要匹配的进程名
function fuzzy_kill(){
    PROCESS_NAME=$1
    PID_ARR=`ps -ef | grep $PROCESS_NAME | grep -v grep | awk '{print $2}'`

    for i in ${PID_ARR[@]}; do
        kill $i
    done
}

# 类似fuzzy_kill，不过是kill -9 强杀
function fuzzy_force_kill(){
    PROCESS_NAME=$1
    PID_ARR=`ps -ef | grep $PROCESS_NAME | grep -v grep | awk '{print $2}'`

    for i in ${PID_ARR[@]}; do
        kill -9 $i
    done
}