# Cloud Function
Invoke Cloud Function HTTP API to set GKE node pool size.

Reference:
1. [Your First Function: Python](https://cloud.google.com/functions/docs/first-python)
2. [Method: projects.locations.clusters.nodePools.setSize](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools/setSize)
3. [Troubleshooting Cloud Functions](https://cloud.google.com/functions/docs/troubleshooting#logging)

## Headers
```text
Content-Type: application/json; charset=utf-8
```

## Body
```json
{
    "project_id": "PROJECT_NAME",
    "location": "ZONE_OR_REGIONAL",
    "cluster_id": "CLUSTER_NAME",
    "node_pool_id": "NODE_POOL_NAME",
    "node_count": NODE_SIZE_COUNT
}
```

## Environment List
* `PROJECT_NAME`
  * type: string
  * default: None
  * describe: GCP project name.
* `ZONE_OR_REGIONAL`
  * type: string
  * default: None
  * describe: GKE cluster location(zone or regional).
* `CLUSTER_NAME`
  * type: string
  * default: None
  * describe: GKE cluster name.
* `NODE_POOL_NAME`
  * type: string
  * default: None
  * describe: GKE node pool name which going to resize.
* `NODE_SIZE_COUNT`
  * type: number
  * default: None
  * describe: Resize number.

## Example
```json
{
    "project_id": "dev",
    "location": "asia-east1",
    "cluster_id": "dev-cluster",
    "node_pool_id": "default-pool",
    "node_count": 5
}
```

## Install requirements
```shell
python3 -m venv venv
source  venv/bin/activate
pip3 install -r requirements.txt
```