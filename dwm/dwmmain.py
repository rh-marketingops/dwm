""" Main class for DWM """

import sys
import collections

from .cleaning import DataLookup
from .cleaning import RegexLookup
from .cleaning import DeriveDataLookup
from .cleaning import DeriveDataCopyValue
from .cleaning import DeriveDataRegex
from .cleaning import IncludesLookup

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

    def __init__(self, name, mongo, fields=None, udfs=None, field_order=None):
        """
        Set configuration for DWM runtime

        :param str name: Name of configuration; for logging
        :param MongoClient mongo: MongoDB connection
        :param dict fields: dict of field configurations (dict)
        :param dict udfs: dict of udfs to run
        """

        if fields is None:
            self.fields = {}
        elif field_order is not None:
            ordered_fields = collections.OrderedDict()
            for order in field_order:
                ordered_fields.update({order: fields[order]})
            self.fields = ordered_fields
        else:
            self.fields = fields

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
        # self.fields = fields
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
        Method to lookup the replacement value given a single input value from
        the same field.

        :param dict fields_list: Fields configurations
        :param MongoClient mongo_db_obj: MongoDB collection object
        :param dict hist: existing input of history values object
        :param dict record: values to validate
        :param str lookup_type: Type of lookup
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
        Method to lookup the replacement value based on regular expressions.

        :param dict fields_list: Fields configurations
        :param MongoClient mongo_db_obj: MongoDB collection object
        :param dict hist: existing input of history values object
        :param dict record: values to validate
        :param str lookup_type: Type of lookup
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

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """

        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in self.fields:

                    if 'normIncludes' in self.fields[field]['lookup']:

                        field_val_new, hist, _ = IncludesLookup(
                            fieldVal=record[field],
                            lookupType='normIncludes',
                            db=self.mongo,
                            fieldName=field,
                            histObj=hist)

                        record[field] = field_val_new

        return record, hist

    def _derive(self, record, hist=None):
        """
        Derivation filters like 'deriveValue' to replace given input values
        from one or more fields. In case 'copyValue' copy value to the target
        field from given an input value from one field. 'deriveRegex' replace
        given an input value from one field, derive target field value using
        regular expressions. If 'deriveIncludes' applies then given an input
        value from one field, derive target field based on at least one of the
        following: includes strings, excludes strings, starts with string,
        ends with string

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """

        def check_derive_options(option, derive_set_config):
            """
            Check derive option is exist into options list and return relevant
            flag.
            :param str option: drive options value
            :param list derive_set_config: options list
            :return boolean: True or False based on option exist into options
            list
            """

            return option in derive_set_config

        hist_obj = {}

        if hist is None:
            hist = {}

        for field in record:

            field_val_new = field_val = record[field]

            if field in self.fields:

                for derive_set in self.fields[field]['derive']:

                    check_match = False

                    derive_set_config = derive_set

                    if set.issubset(set(derive_set_config['fieldSet']),
                                    record.keys()):

                        # sorting here to ensure sub document match from
                        # query

                        derive_input = {val: record[val] for val in
                                        derive_set_config['fieldSet']}

                        if derive_set_config['type'] == 'deriveValue':

                            overwrite_flag = check_derive_options(
                                'overwrite',
                                derive_set_config["options"])

                            blank_if_no_match_flag = check_derive_options(
                                'blankIfNoMatch',
                                derive_set_config["options"])

                            field_val_new, hist_obj, check_match = \
                                DeriveDataLookup(
                                    fieldName=field,
                                    db=self.mongo,
                                    deriveInput=derive_input,
                                    overwrite=overwrite_flag,
                                    fieldVal=record[field],
                                    histObj=hist,
                                    blankIfNoMatch=blank_if_no_match_flag)

                        elif derive_set_config['type'] == 'copyValue':

                            overwrite_flag = check_derive_options(
                                'overwrite',
                                derive_set_config["options"])

                            field_val_new, hist_obj, check_match = \
                                DeriveDataCopyValue(
                                    fieldName=field,
                                    deriveInput=derive_input,
                                    overwrite=overwrite_flag,
                                    fieldVal=record[field],
                                    histObj=hist)

                        elif derive_set_config['type'] == 'deriveRegex':

                            overwrite_flag = check_derive_options(
                                'overwrite',
                                derive_set_config["options"])

                            blank_if_no_match_flag = check_derive_options(
                                'blankIfNoMatch',
                                derive_set_config["options"])

                            field_val_new, hist_obj, check_match = \
                                DeriveDataRegex(
                                    fieldName=field,
                                    db=self.mongo,
                                    deriveInput=derive_input,
                                    overwrite=overwrite_flag,
                                    fieldVal=record[field],
                                    histObj=hist,
                                    blankIfNoMatch=blank_if_no_match_flag)

                        elif derive_set_config['type'] == 'deriveIncludes':

                            overwrite_flag = check_derive_options(
                                'overwrite',
                                derive_set_config["options"])

                            blank_if_no_match_flag = check_derive_options(
                                'blankIfNoMatch',
                                derive_set_config["options"])

                            field_val_new, hist_obj, check_match = \
                                IncludesLookup(
                                    fieldVal=record[field],
                                    lookupType='deriveIncludes',
                                    deriveFieldName= \
                                        derive_set_config['fieldSet'][0],
                                    deriveInput=derive_input,
                                    db=self.mongo,
                                    fieldName=field,
                                    histObj=hist,
                                    overwrite=overwrite_flag,
                                    blankIfNoMatch=blank_if_no_match_flag)

                    if check_match or field_val_new != field_val:
                        record[field] = field_val_new
                        break

        return record, hist_obj

    def _apply_udfs(self, record, hist, udf_type):
        """
        Excute user define processes, user-defined functionalty is designed to
        applyies custome trasformations to data.

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """

        def function_executor(func, *args):
            """
            Execute user define function
            :param python method func: Function obj
            :param methods arguments args: Function arguments
            """

            result, result_hist = func(*args)

            return result, result_hist

        if udf_type in self.udfs:

            cust_function_od_obj = collections.OrderedDict(
                sorted(
                    self.udfs[udf_type].items()
                )
            )

            for cust_function in cust_function_od_obj:

                record, hist = function_executor(
                    cust_function_od_obj[cust_function],
                    record,
                    hist
                )

        return record, hist

    def run(self, record, hist=None):
        """
        By passing the input record to be cleaned, and returns the input record
        after cleaning with history(dictionary).

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
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
            record, hist = self._norm_include(record=record, hist=hist)

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
