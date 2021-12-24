import logging
import traceback
from googleapiclient import discovery


def set_node_pool_size(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    project_id = request_json['project_id']
    location = request_json['location']
    cluster_id = request_json['cluster_id']
    node_pool_id = request_json['node_pool_id']
    node_count = request_json['node_count']

    service = discovery.build('container', 'v1')

    # The name (project, location, cluster, node pool id) of the node pool to set
    # size.
    # Specified in the format 'projects/*/locations/*/clusters/*/nodePools/*'.
    name = f'projects/{project_id}/locations/{location}/clusters/{cluster_id}/nodePools/{node_pool_id}'

    set_node_pool_size_request_body = {
        "nodeCount": node_count
    }
    try:
        request = service.projects().locations().clusters().nodePools().setSize(name=name, body=set_node_pool_size_request_body)
        response = request.execute()
        return response
    except Exception:
        error_message = traceback.format_exc().replace('\n', '  ')
        logging.error(error_message)
        return 'Error'
