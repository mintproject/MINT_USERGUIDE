# Install


MINT can be easily deployed on large Kubernetes clusters using Helm. Useful for production instances.

## Pre-requisites

- A Kubernetes `v1.16.3` cluster is required as well as Helm `v3.2.x`.

- A Google Maps API Key. [How to obtain it?](https://developers.google.com/maps/documentation/javascript/get-api-key)
- 
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

**2.** Configure MINT 

Create a file called `values.yaml` and you can pass any of the [supported values](https://github.com/mintproject/mint/tree/main/helm#readme).

For example, to change the Welcome Message:

```yaml
welcome_message: Welcome to MINT
google:
  maps:
    key: CHANGEME
```


**3.** Deploy MINT (note that you can pass any of the [supported values](https://github.com/mintproject/mint/tree/main/helm#readme):



```console
$ helm install --devel mint mint/MINT -f values.yaml --wait
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

