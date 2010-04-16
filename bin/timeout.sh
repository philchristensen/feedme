#!/bin/sh 
# timeout script 
# 
cycle_kill () { 
    PID=$1 
} 

timeout() {
    PID=$1 
    TIMEOUT=$2
    RETVAL=0 
    
    sleep $TIMEOUT
    
    for signal in "TERM" "INT" "HUP" "KILL"; do 
        kill -$signal $PID 
        RETVAL=$? 
        [ $RETVAL -eq 0 ] && break 
        echo "warning: kill failed: pid=$PID, signal=$signal" >&2 
        sleep 1 
    done 

    return $RETVAL 
} 

usage() { 
    echo "usage: timeout seconds command args ..." 
    exit 1 
} 

[[ $# -lt 2 ]] && usage 
seconds=$1; shift 

eval "$@" & 
timeout $! $seconds
