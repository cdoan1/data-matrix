# README.md

* add `apply.sh` convience script to create a configmap using kustomize
* use environment variables to override the OBSERVATORIUM_URL and the SPOKE_CLUSTER_NAME

## Usage

```bash
export OBSERVATORIUM_URL=http://xxxx
export SPOKE_CLUSTER_NAME=foobar
./apply.sh
```
