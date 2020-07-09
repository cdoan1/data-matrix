# data-matrix

# version-v-tested.csv

```
date,release,driver,provider,topology,result
1,quay.io/openshift-release-dev/ocp-release:4.3.27-x86_64,2.0.0-123,aws,spoke,pass
2,quay.io/openshift-release-dev/ocp-release:4.3.28-x86_64,2.0.0-123,azure,spoke,pass
3,quay.io/openshift-release-dev/ocp-release:4.4.10-x86_64,2.0.0-124,gcp,spoke,pass
4,quay.io/openshift-release-dev/ocp-release:4.5.0-rc.6-x86_64,2.0.0-127,gcp,spoke,pass

```

* keeps track of all release versions deployed
* log `failed`, but when looking for what `release` to pick up, strip out all rows with `failed`
