# Install


MINT can be easily deployed on large Kubernetes clusters using Helm. Useful for production instances.

## Pre-requisites

- A Kubernetes `v1.16.3` cluster is required as well as Helm `v3.2.x`.

- A shared file system to host all analyses workspaces when running in a multinode deployment setup. Therefore, you should create an [`StorageClass`](https://kubernetes.io/docs/concepts/storage/storage-classes/#the-storageclass-resource) pointing to your storage backend. The `StorageClass` should meet the following requirements:
    - be named `<helm-release-prefix>-shared-volume-storage-class`;
    - be created in the same namespace as the one you will deploy MINT to.

!!! note
    If you do not have any particular distributed file system in your Kubernetes cluster, you can easily [deploy an NFS network file system following our documentation](../../../advanced-usage/storage-backends/nfs/).

## Deploy

**1.** Add MINT chart repository:

```console
$ helm repo add mint https://mintproject.github.io/mint      
"mint" has been added to your repositories
$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "mint" chart repository
Update Complete. ⎈ Happy Helming!⎈
```

**2.** Deploy MINT (note that you can pass any of the [supported values](https://github.com/mintproject/mint/blob/mint/helm/README.md)):

```console
$ helm install --devel mint mint/mint--wait
NAME: mint 
LAST DEPLOYED: Wed Mar 18 10:27:06 2020
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Thanks for flying MINT 🚀
```

!!! warning

    Note that the above `helm install` command used `mint` as the Helm release name. You can choose any other name provided that it is less than 13 characters long. (This is due to current limitation on the length of generated pod names.)

!!! note
    Note that you can deploy MINT in different namespaces by passing `--namespace` to `helm install`. Remember to pass `--create-namespace` if the namespace you want to use does not exist yet. For more information on how to work with namespaces see the [official documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

