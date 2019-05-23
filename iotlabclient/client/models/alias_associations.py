# coding: utf-8

"""
    IoT-LAB REST API

    REST API documentation of [IoT-LAB](http://www.iot-lab.info) testbed.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AliasAssociations(object):
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
        'associations': 'MobilityAliasAssociations'
    }

    attribute_map = {
        'associations': 'associations'
    }

    def __init__(self, associations=None):  # noqa: E501
        """AliasAssociations - a model defined in OpenAPI"""  # noqa: E501

        self._associations = None
        self.discriminator = None

        if associations is not None:
            self.associations = associations

    @property
    def associations(self):
        """Gets the associations of this AliasAssociations.  # noqa: E501


        :return: The associations of this AliasAssociations.  # noqa: E501
        :rtype: MobilityAliasAssociations
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this AliasAssociations.


        :param associations: The associations of this AliasAssociations.  # noqa: E501
        :type: MobilityAliasAssociations
        """

        self._associations = associations

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
        if not isinstance(other, AliasAssociations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other