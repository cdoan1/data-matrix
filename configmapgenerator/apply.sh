#!/bin/bash

if [ -z ${OBSERVATORIUM_URL} ]; then
  echo ""
  echo "OBSERVATORIUM_URL environment variable is undefined and required."
  exit 1
fi


clusterID=$(oc get clusterversion -o jsonpath='{.items[].spec.clusterID}{"\n"}')

if [ -z ${clusterID} ]; then
  echo "clusterID not defined. Ensure that you have kubectl sourced ..."
  exit 1
fi

sed -i.bak 's|        replacement: .*$|        replacement: '${clusterID}'|g' config.yaml && echo "updated config.yaml ..."
sed -i.bak 's|    - url: .*$|    - url: '${OBSERVATORIUM_URL}'|g' config.yaml && echo "updated config.yaml ..."

echo "clusterID: ${clusterID}"

kubectl kustomize .
# kubectl apply -k .
