""" Main class for DWM """

##########################################################################
# Constants
##########################################################################

LOOKUP_TYPES = ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                'fieldSpecificLookup', 'normLookup', 'normIncludes']

DERIVE_TYPES = ['deriveValue', 'copyValue', 'deriveRegex', 'deriveIncludes']

DERIVE_OPTIONS = ['overwrite', 'blankIfNoMatch']

UDF_POSITIONS = ['beforeGenericValLookup', 'beforeGenericValRegex',
                 'beforeFieldSpecificLookup', 'beforeFieldSpecificRegex',
                 'beforeNormLookup', 'beforeNormRegex',
                 'beforeNormIncludes', 'beforeDerive', 'afterAll']

##########################################################################
# DWM
##########################################################################


class Dwm(object):
    """ class for DWM config """

    def __init__(self, name, mongo, fields=None, udfs=None):
        """
        Set configuration for DWM runtime

        :param str name: Name of configuration; for logging
        :param MongoClient mongo: MongoDB connection
        :param list fields: list of field configurations (dict)
        :param dict udfs: dict of udfs to run
        """

        if fields is None:
            fields = []

        if udfs is None:
            udfs = {}

        # validate input values
        for field in fields:
            # lookup values
            for lookup in fields[field]['lookup']:
                if lookup not in LOOKUP_TYPES:
                    raise ValueError('Invalid lookup type %s' % lookup)

            # derive types and options
            for derive in fields[field]['derive']:
                if derive['type'] not in DERIVE_TYPES:
                    raise ValueError('Invalid derive type %s' %
                                     derive['type'])
                for opt in derive['options']:
                    if opt not in DERIVE_OPTIONS:
                        raise ValueError('Invalid derive option %s' % opt)

        for udf in udfs:
            if udf not in UDF_POSITIONS:
                raise ValueError('Invalid UDF position %s' % udf)


        self.name = name
        self.mongo = mongo
        self.fields = fields
        self.udfs = udfs
