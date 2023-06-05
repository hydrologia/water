import collections
import os


class Config:
    """

    """

    # Endpoint
    endpoint = 'http://environment.data.gov.uk/water-quality/{branch}'

    # The reference query
    __ReferenceQuery = collections.namedtuple(typename='ReferenceQuery',
                                              field_names=['determinands', 'sampling_point_types',
                                                           'environment_agency_area', 'environment_agency_subarea',
                                                           'sampling_point'])

    reference_query = __ReferenceQuery(determinands='def/determinands.csv',
                                       sampling_point_types='sampling-point-types.csv',
                                       environment_agency_area='ea-area.csv',
                                       environment_agency_subarea='ea-subarea.csv', sampling_point='sampling-point.csv')

    # The reference data directories
    __ReferenceDirectory = collections.namedtuple(typename='ReferenceDirectory', field_names=['raw', 'structured'])

    reference_directory = __ReferenceDirectory(raw=os.path.join(os.getcwd(), 'data', 'references'),
                                               structured=os.path.join(os.getcwd(), 'warehouse', 'references'))
