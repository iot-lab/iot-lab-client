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


class InlineObject1(object):
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
        'model': 'Model',
        'script': 'file'
    }

    attribute_map = {
        'model': 'model',
        'script': 'script'
    }

    def __init__(self, model=None, script=None):  # noqa: E501
        """InlineObject1 - a model defined in OpenAPI"""  # noqa: E501

        self._model = None
        self._script = None
        self.discriminator = None

        if model is not None:
            self.model = model
        if script is not None:
            self.script = script

    @property
    def model(self):
        """Gets the model of this InlineObject1.  # noqa: E501


        :return: The model of this InlineObject1.  # noqa: E501
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this InlineObject1.


        :param model: The model of this InlineObject1.  # noqa: E501
        :type: Model
        """

        self._model = model

    @property
    def script(self):
        """Gets the script of this InlineObject1.  # noqa: E501

        the script that will be started on the robot  # noqa: E501

        :return: The script of this InlineObject1.  # noqa: E501
        :rtype: file
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this InlineObject1.

        the script that will be started on the robot  # noqa: E501

        :param script: The script of this InlineObject1.  # noqa: E501
        :type: file
        """

        self._script = script

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
        if not isinstance(other, InlineObject1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
