#!/bin/bash

clusterimageset_latest() {
    export latest43=$(oc get clusterimageset | grep 4.3 | sort -r | head -n 1 | awk '{print $2}')
    export latest44=$(oc get clusterimageset | grep 4.4 | sort -r | head -n 1 | awk '{print $2}')
    export latest45=$(oc get clusterimageset | grep 4.5 | sort -r | head -n 1 | awk '{print $2}')
    export latest46=$(oc get clusterimageset | grep 4.6 | sort -r | head -n 1 | awk '{print $2}')
    servers="$latest43 $latest44 $latest45 $latest46"
    for s in $servers ; do echo $s ; done | sort -R
}

clusterimageset_latest