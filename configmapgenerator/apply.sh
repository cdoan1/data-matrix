#!/bin/bash

if [ -z ${SPOKE_CLUSTER_NAME} ] || [ -z ${OBSERVATORIUM_URL} ]; then
  echo ""
  echo "SPOKE_CLUSTER_NAME environment variable is undefined and required."
  echo "OBSERVATORIUM_URL environment variable is undefined and required."
  exit 1
fi

sed -i.bak 's|        replacement: .*$|        replacement: '${SPOKE_CLUSTER_NAME}'|g' config.yaml && echo "updated config.yaml ..."
sed -i.bak 's|    - url: .*$|    - url: '${OBSERVATORIUM_URL}'|g' config.yaml && echo "updated config.yaml ..."

kubectl kustomize .

