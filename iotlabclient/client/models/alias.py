# coding: utf-8

"""
    IoT-LAB REST API

    REST API documentation of [IoT-LAB](http://www.iot-lab.info) testbed.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Alias(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'alias': 'str',
        'nbnodes': 'int',
        'properties': 'AliasProperties'
    }

    attribute_map = {
        'alias': 'alias',
        'nbnodes': 'nbnodes',
        'properties': 'properties'
    }

    def __init__(self, alias=None, nbnodes=None, properties=None):  # noqa: E501
        """Alias - a model defined in OpenAPI"""  # noqa: E501

        self._alias = None
        self._nbnodes = None
        self._properties = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if nbnodes is not None:
            self.nbnodes = nbnodes
        if properties is not None:
            self.properties = properties

    @property
    def alias(self):
        """Gets the alias of this Alias.  # noqa: E501


        :return: The alias of this Alias.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this Alias.


        :param alias: The alias of this Alias.  # noqa: E501
        :type: str
        """
        if alias is not None and not re.search(r'^[0-9]$', alias):  # noqa: E501
            raise ValueError(r"Invalid value for `alias`, must be a follow pattern or equal to `/^[0-9]$/`")  # noqa: E501

        self._alias = alias

    @property
    def nbnodes(self):
        """Gets the nbnodes of this Alias.  # noqa: E501


        :return: The nbnodes of this Alias.  # noqa: E501
        :rtype: int
        """
        return self._nbnodes

    @nbnodes.setter
    def nbnodes(self, nbnodes):
        """Sets the nbnodes of this Alias.


        :param nbnodes: The nbnodes of this Alias.  # noqa: E501
        :type: int
        """

        self._nbnodes = nbnodes

    @property
    def properties(self):
        """Gets the properties of this Alias.  # noqa: E501


        :return: The properties of this Alias.  # noqa: E501
        :rtype: AliasProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Alias.


        :param properties: The properties of this Alias.  # noqa: E501
        :type: AliasProperties
        """

        self._properties = properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Alias):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
