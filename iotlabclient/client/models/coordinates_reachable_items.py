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


class CoordinatesReachableItems(object):
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
        'point_name': 'str',
        'reachable': 'bool'
    }

    attribute_map = {
        'point_name': 'pointName',
        'reachable': 'reachable'
    }

    def __init__(self, point_name=None, reachable=None):  # noqa: E501
        """CoordinatesReachableItems - a model defined in OpenAPI"""  # noqa: E501

        self._point_name = None
        self._reachable = None
        self.discriminator = None

        if point_name is not None:
            self.point_name = point_name
        if reachable is not None:
            self.reachable = reachable

    @property
    def point_name(self):
        """Gets the point_name of this CoordinatesReachableItems.  # noqa: E501


        :return: The point_name of this CoordinatesReachableItems.  # noqa: E501
        :rtype: str
        """
        return self._point_name

    @point_name.setter
    def point_name(self, point_name):
        """Sets the point_name of this CoordinatesReachableItems.


        :param point_name: The point_name of this CoordinatesReachableItems.  # noqa: E501
        :type: str
        """

        self._point_name = point_name

    @property
    def reachable(self):
        """Gets the reachable of this CoordinatesReachableItems.  # noqa: E501


        :return: The reachable of this CoordinatesReachableItems.  # noqa: E501
        :rtype: bool
        """
        return self._reachable

    @reachable.setter
    def reachable(self, reachable):
        """Sets the reachable of this CoordinatesReachableItems.


        :param reachable: The reachable of this CoordinatesReachableItems.  # noqa: E501
        :type: bool
        """

        self._reachable = reachable

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
        if not isinstance(other, CoordinatesReachableItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
