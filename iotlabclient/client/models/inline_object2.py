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


class InlineObject2(object):
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
        'experiment': 'ExperimentRequest',
        'files': 'list[file]'
    }

    attribute_map = {
        'experiment': 'experiment',
        'files': 'files'
    }

    def __init__(self, experiment=None, files=None):  # noqa: E501
        """InlineObject2 - a model defined in OpenAPI"""  # noqa: E501

        self._experiment = None
        self._files = None
        self.discriminator = None

        if experiment is not None:
            self.experiment = experiment
        if files is not None:
            self.files = files

    @property
    def experiment(self):
        """Gets the experiment of this InlineObject2.  # noqa: E501


        :return: The experiment of this InlineObject2.  # noqa: E501
        :rtype: ExperimentRequest
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this InlineObject2.


        :param experiment: The experiment of this InlineObject2.  # noqa: E501
        :type: ExperimentRequest
        """

        self._experiment = experiment

    @property
    def files(self):
        """Gets the files of this InlineObject2.  # noqa: E501

        firmware/script/scriptconfig files  # noqa: E501

        :return: The files of this InlineObject2.  # noqa: E501
        :rtype: list[file]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this InlineObject2.

        firmware/script/scriptconfig files  # noqa: E501

        :param files: The files of this InlineObject2.  # noqa: E501
        :type: list[file]
        """

        self._files = files

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
        if not isinstance(other, InlineObject2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
