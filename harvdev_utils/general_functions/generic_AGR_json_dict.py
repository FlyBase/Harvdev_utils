"""Module:: generic_AGR_json.

Synopsis:
    A module that returns a generic AGR data structure with metadata and data.
    The data will simply be an empty list.

Author(s):
    Gil dos Santos dossantos@morgan.harvard.edu
"""

import logging
from harvdev_utils.general_functions import timenow

log = logging.getLogger(__name__)


def generic_AGR_json_dict(database_release, strict_time):
    """Return a generic AGR data structure with metadata and data.

    Args:
        arg1 (str): The FlyBase "database_release" in "YYYY_NN" format.
        arg2 (str): The time, as generated by strict_rfc3339.now_to_rfc3339_localoffset() function.

    Returns:
        dict: A dictionary (generic AGR JSON object).

    """
    dataProviderdict = {}
    dataProviderdict['type'] = 'curated'
    dataProviderdict['crossReference'] = {}
    dataProviderdict['crossReference']['id'] = 'FB'
    dataProviderdict['crossReference']['pages'] = ['homepage']

    to_export_as_json = {}
    to_export_as_json['metaData'] = {}
    to_export_as_json['metaData']['dataProvider'] = dataProviderdict
    to_export_as_json['metaData']['dateProduced'] = strict_time
    to_export_as_json['metaData']['release'] = database_release
    to_export_as_json['data'] = []

    log.info('TIME: {}. Base JSON data structure created.'.format(timenow()))

    return to_export_as_json
