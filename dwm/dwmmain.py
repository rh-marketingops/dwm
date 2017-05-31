""" Main class for DWM """

from .cleaning import DataLookup
from .cleaning import RegexLookup
from .cleaning import IncludesLookup

from .wrappers import DeriveDataLookupAll


##########################################################################
# Constants
##########################################################################

LOOKUP_TYPES = ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                'fieldSpecificLookup', 'normLookup', 'normRegex',
                'normIncludes']

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
            fields = {}

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
                    raise ValueError('Invalid derive type %s' % derive['type'])

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


    def get_field_list(self):
        """
        Retrieve list of all fields currently configured
        """

        list_out = []
        for field in self.fields:
            list_out.append(field)

        return list_out

    @staticmethod
    def data_lookup_method(fields_list, mongo_db_obj, hist, record,
                           lookup_type):
        """

        :param fields_list:
        :param mongo_db_obj:
        :param hist:
        :param record:
        :param lookup_type:
        """

        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in fields_list:

                    if lookup_type in fields_list[field]['lookup']:

                        field_val_new, hist = DataLookup(
                            fieldVal=record[field],
                            db=mongo_db_obj,
                            lookupType=lookup_type,
                            fieldName=field,
                            histObj=hist)

                        record[field] = field_val_new

        return record, hist

    @staticmethod
    def data_regex_method(fields_list, mongo_db_obj, hist, record, lookup_type):
        """

        :param fields_list:
        :param mongo_db_obj:
        :param hist:
        :param record:
        :param lookup_type:
        """

        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in fields_list:

                    if lookup_type in fields_list[field]['lookup']:

                        field_val_new, hist = RegexLookup(
                            fieldVal=record[field],
                            db=mongo_db_obj,
                            fieldName=field,
                            lookupType=lookup_type,
                            histObj=hist)

                        record[field] = field_val_new

        return record, hist

    def _val_g_lookup(self, record, hist=None):
        """
        Perform generic validation lookup

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """

        record, hist = self.data_lookup_method(fields_list=self.fields,
                                               mongo_db_obj=self.mongo,
                                               hist=hist,
                                               record=record,
                                               lookup_type='genericLookup')
        return record, hist

    def _val_g_regex(self, record, hist=None):
        """
        Perform generic validation regex

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """

        record, hist = self.data_regex_method(fields_list=self.fields,
                                              mongo_db_obj=self.mongo,
                                              hist=hist,
                                              record=record,
                                              lookup_type='genericRegex')
        return record, hist

    def _val_fs_lookup(self, record, hist=None):
        """
        Perform field-specific validation lookup

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """

        record, hist = self.data_lookup_method(fields_list=self.fields,
                                               mongo_db_obj=self.mongo,
                                               hist=hist,
                                               record=record,
                                               lookup_type=
                                               'fieldSpecificLookup')

        return record, hist

    def _val_fs_regex(self, record, hist=None):
        """
        Perform field-specific validation regex

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """

        record, hist = self.data_regex_method(fields_list=self.fields,
                                              mongo_db_obj=self.mongo,
                                              hist=hist,
                                              record=record,
                                              lookup_type='fieldSpecificRegex')
        return record, hist

    def _norm_lookup(self, record, hist=None):
        """
        Perform generic validation lookup

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """

        record, hist = self.data_lookup_method(fields_list=self.fields,
                                               mongo_db_obj=self.mongo,
                                               hist=hist,
                                               record=record,
                                               lookup_type='normLookup')
        return record, hist

    def _norm_regex(self, record, hist=None):
        """
        Perform generic validation regex

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """

        record, hist = self.data_regex_method(fields_list=self.fields,
                                              mongo_db_obj=self.mongo,
                                              hist=hist,
                                              record=record,
                                              lookup_type='normRegex')
        return record, hist

    def _norm_include(self, record, hist=None):
        """
        Normalization 'normIncludes' replace 'almost' values based on at least
        one of the following: includes strings, excludes strings, starts with
        string, ends with string

        :param record:
        :param hist:
        :return:
        """

        check_match = False

        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in self.fields:

                    if 'normIncludes' in self.fields[field]['lookup']:

                        field_val_new, hist, check_match = IncludesLookup(
                            fieldVal=record[field],
                            lookupType='normIncludes',
                            db=self.mongo,
                            fieldName=field,
                            histObj=hist)

                        record[field] = field_val_new

        return record, hist, check_match

    def _derive(self, record, hist=None):
        """

        :param record:
        :param hist:
        :return:
        """

        hist_obj_upd = {}

        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in self.fields:
                    field_val_new, hist_obj_upd = DeriveDataLookupAll(
                        data=field,
                        configFields=record[field],
                        db=self.mongo,
                        histObj=hist
                    )

                    record[field] = field_val_new

        return record, hist_obj_upd

    def _apply_udfs(self, record, hist, udf_type):
        """

        :param record:
        :param hist:
        :return:
        """

        def function_executor(func, *args):
            """

            :param func:
            :param args:
            :return:
            """

            result, result_hist = func(*args)

            return result, result_hist

        if udf_type in self.udfs:

            cust_function_list_obj = self.udfs[udf_type]

            for cust_function in cust_function_list_obj:
                record, hist = function_executor(cust_function, record, hist)

        return record, hist

    def run(self, record, hist=None):
        """

        :param record:
        :param hist:
        :return:
        """

        if hist is None:
            hist = {}

        if record:
            # Run user-defined functions for beforeGenericValLookup
            record, hist = self._apply_udfs(record=record,
                                            hist=hist,
                                            udf_type='beforeGenericValLookup')

            # Run generic validation lookup
            record, hist = self._val_g_lookup(record=record, hist=hist)

            # Run user-defined functions for beforeGenericValRegex
            record, hist = self._apply_udfs(record=record,
                                            hist=hist,
                                            udf_type='beforeGenericValRegex')

            # Run generic validation regex
            record, hist = self._val_g_regex(record=record, hist=hist)

            # Run user-defined functions for beforeFieldSpecificLookup
            record, hist = self._apply_udfs(record=record,
                                            hist=hist,
                                            udf_type='beforeFieldSpecificLookup')

            # Run field-specific validation lookup
            record, hist = self._val_fs_lookup(record=record, hist=hist)

            # Run user-defined functions for beforeFieldSpecificLookup
            record, hist = self._apply_udfs(record=record,
                                            hist=hist,
                                            udf_type='beforeFieldSpecificRegex')

            # Run field-specific validation regex
            record, hist = self._val_fs_regex(record=record, hist=hist)

            # Run user-defined functions for beforeNormLookup
            record, hist = self._apply_udfs(record=record,
                                            hist=hist,
                                            udf_type='beforeNormLookup')

            # Run normalization lookup
            record, hist = self._norm_lookup(record=record, hist=hist)

            # Run user-defined functions for beforeNormRegex
            record, hist = self._apply_udfs(record=record,
                                            hist=hist,
                                            udf_type='beforeNormRegex')

            # Run normalization regex
            record, hist = self._norm_regex(record=record, hist=hist)

            # Run user-defined functions for beforeNormIncludes
            record, hist = self._apply_udfs(record=record,
                                            hist=hist,
                                            udf_type='beforeNormIncludes')

            # Run normalization includes
            record, hist, check_match = self._norm_include(record=record,
                                                           hist=hist)

            # Run user-defined functions for beforeNormIncludes
            record, hist = self._apply_udfs(record=record,
                                            hist=hist,
                                            udf_type='beforeDerive')

            # Fill gaps / refresh derived data
            record, hist = self._derive(record=record, hist=hist)

            # Run user-defined functions for beforeNormIncludes
            record, hist = self._apply_udfs(record=record,
                                            hist=hist,
                                            udf_type='afterAll')

            return record, hist

        return None, hist
