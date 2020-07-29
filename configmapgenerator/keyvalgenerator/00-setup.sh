#!/bin/bash

NAME=k.yaml

cat > $NAME <<EOF
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

configMapGenerator:
EOF

for i in {1..4000}
do
echo $i
cat >> $NAME <<EOF
- name: spoke50-cm-$i
  namespace: spoke50-ns
  files:
  - keyvalue.txt
EOF
done

cat >> $NAME <<EOF
generatorOptions:
  annotations:
    kustomize.generated.resource: "true"
EOF

