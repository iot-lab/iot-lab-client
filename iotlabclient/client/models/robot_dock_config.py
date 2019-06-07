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


class RobotDockConfig(object):
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
        'x': 'float',
        'y': 'float',
        'theta': 'float',
        'frame_id': 'str'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'theta': 'theta',
        'frame_id': 'frame_id'
    }

    composed_hierarchy = {
        'anyOf': [],
        'allOf': ["Point", "RobotDockConfigAllOf"],
        'oneOf': [],
    }

    def __init__(self, x=None, y=None, theta=None, frame_id=None):  # noqa: E501
        """RobotDockConfig - a model defined in OpenAPI"""  # noqa: E501

        self._x = None
        self._y = None
        self._theta = None
        self._frame_id = None
        self.discriminator = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if theta is not None:
            self.theta = theta
        if frame_id is not None:
            self.frame_id = frame_id

    @property
    def x(self):
        """Gets the x of this RobotDockConfig.  # noqa: E501


        :return: The x of this RobotDockConfig.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this RobotDockConfig.


        :param x: The x of this RobotDockConfig.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this RobotDockConfig.  # noqa: E501


        :return: The y of this RobotDockConfig.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this RobotDockConfig.


        :param y: The y of this RobotDockConfig.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def theta(self):
        """Gets the theta of this RobotDockConfig.  # noqa: E501


        :return: The theta of this RobotDockConfig.  # noqa: E501
        :rtype: float
        """
        return self._theta

    @theta.setter
    def theta(self, theta):
        """Sets the theta of this RobotDockConfig.


        :param theta: The theta of this RobotDockConfig.  # noqa: E501
        :type: float
        """

        self._theta = theta

    @property
    def frame_id(self):
        """Gets the frame_id of this RobotDockConfig.  # noqa: E501


        :return: The frame_id of this RobotDockConfig.  # noqa: E501
        :rtype: str
        """
        return self._frame_id

    @frame_id.setter
    def frame_id(self, frame_id):
        """Sets the frame_id of this RobotDockConfig.


        :param frame_id: The frame_id of this RobotDockConfig.  # noqa: E501
        :type: str
        """

        self._frame_id = frame_id

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
        if not isinstance(other, RobotDockConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
