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


class ProfileAliasAssociations(object):
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
        'profileassociations': 'list[ProfileAliasAssociation]'
    }

    attribute_map = {
        'profileassociations': 'profileassociations'
    }

    def __init__(self, profileassociations=None):  # noqa: E501
        """ProfileAliasAssociations - a model defined in OpenAPI"""  # noqa: E501

        self._profileassociations = None
        self.discriminator = None

        if profileassociations is not None:
            self.profileassociations = profileassociations

    @property
    def profileassociations(self):
        """Gets the profileassociations of this ProfileAliasAssociations.  # noqa: E501


        :return: The profileassociations of this ProfileAliasAssociations.  # noqa: E501
        :rtype: list[ProfileAliasAssociation]
        """
        return self._profileassociations

    @profileassociations.setter
    def profileassociations(self, profileassociations):
        """Sets the profileassociations of this ProfileAliasAssociations.


        :param profileassociations: The profileassociations of this ProfileAliasAssociations.  # noqa: E501
        :type: list[ProfileAliasAssociation]
        """

        self._profileassociations = profileassociations

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
        if not isinstance(other, ProfileAliasAssociations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
