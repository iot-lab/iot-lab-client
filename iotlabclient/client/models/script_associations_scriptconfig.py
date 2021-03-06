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


class ScriptAssociationsScriptconfig(object):
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
        'scriptconfigname': 'str',
        'sites': 'list[str]'
    }

    attribute_map = {
        'scriptconfigname': 'scriptconfigname',
        'sites': 'sites'
    }

    def __init__(self, scriptconfigname=None, sites=None):  # noqa: E501
        """ScriptAssociationsScriptconfig - a model defined in OpenAPI"""  # noqa: E501

        self._scriptconfigname = None
        self._sites = None
        self.discriminator = None

        if scriptconfigname is not None:
            self.scriptconfigname = scriptconfigname
        if sites is not None:
            self.sites = sites

    @property
    def scriptconfigname(self):
        """Gets the scriptconfigname of this ScriptAssociationsScriptconfig.  # noqa: E501


        :return: The scriptconfigname of this ScriptAssociationsScriptconfig.  # noqa: E501
        :rtype: str
        """
        return self._scriptconfigname

    @scriptconfigname.setter
    def scriptconfigname(self, scriptconfigname):
        """Sets the scriptconfigname of this ScriptAssociationsScriptconfig.


        :param scriptconfigname: The scriptconfigname of this ScriptAssociationsScriptconfig.  # noqa: E501
        :type: str
        """

        self._scriptconfigname = scriptconfigname

    @property
    def sites(self):
        """Gets the sites of this ScriptAssociationsScriptconfig.  # noqa: E501


        :return: The sites of this ScriptAssociationsScriptconfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this ScriptAssociationsScriptconfig.


        :param sites: The sites of this ScriptAssociationsScriptconfig.  # noqa: E501
        :type: list[str]
        """

        self._sites = sites

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
        if not isinstance(other, ScriptAssociationsScriptconfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
