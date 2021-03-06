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


class AliasProperties(object):
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
        'archi': 'ArchiRadioString',
        'mobile': 'bool',
        'site': 'str'
    }

    attribute_map = {
        'archi': 'archi',
        'mobile': 'mobile',
        'site': 'site'
    }

    def __init__(self, archi=None, mobile=None, site=None):  # noqa: E501
        """AliasProperties - a model defined in OpenAPI"""  # noqa: E501

        self._archi = None
        self._mobile = None
        self._site = None
        self.discriminator = None

        if archi is not None:
            self.archi = archi
        if mobile is not None:
            self.mobile = mobile
        if site is not None:
            self.site = site

    @property
    def archi(self):
        """Gets the archi of this AliasProperties.  # noqa: E501


        :return: The archi of this AliasProperties.  # noqa: E501
        :rtype: ArchiRadioString
        """
        return self._archi

    @archi.setter
    def archi(self, archi):
        """Sets the archi of this AliasProperties.


        :param archi: The archi of this AliasProperties.  # noqa: E501
        :type: ArchiRadioString
        """

        self._archi = archi

    @property
    def mobile(self):
        """Gets the mobile of this AliasProperties.  # noqa: E501


        :return: The mobile of this AliasProperties.  # noqa: E501
        :rtype: bool
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this AliasProperties.


        :param mobile: The mobile of this AliasProperties.  # noqa: E501
        :type: bool
        """

        self._mobile = mobile

    @property
    def site(self):
        """Gets the site of this AliasProperties.  # noqa: E501


        :return: The site of this AliasProperties.  # noqa: E501
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this AliasProperties.


        :param site: The site of this AliasProperties.  # noqa: E501
        :type: str
        """
        if site is not None and not re.search(r'^[a-z0-9]*$', site):  # noqa: E501
            raise ValueError(r"Invalid value for `site`, must be a follow pattern or equal to `/^[a-z0-9]*$/`")  # noqa: E501

        self._site = site

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
        if not isinstance(other, AliasProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
