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


class ArchiRadioString(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    A8_AT86RF231 = "a8:at86rf231"
    ARDUINO_ZERO_XBEE = "arduino-zero:xbee"
    FIREFLY_MULTI = "firefly:multi"
    FRDM_KW41Z_MULTI = "frdm-kw41z:multi"
    M3_AT86RF231 = "m3:at86rf231"
    MICROBIT_BLE = "microbit:ble"
    NRF51DK_BLE = "nrf51dk:ble"
    NRF52DK_BLE = "nrf52dk:ble"
    NRF52840DK_MULTI = "nrf52840dk:multi"
    NRF52840MDK_MULTI = "nrf52840mdk:multi"
    PHYNODE_KW2XRF = "phynode:kw2xrf"
    RTL_SDR_NONE = "rtl-sdr:none"
    ST_LRWAN1_SX1276 = "st-lrwan1:sx1276"
    ST_IOTNODE_MULTI = "st-iotnode:multi"
    SAMR21_AT86RF233 = "samr21:at86rf233"
    SAMR30_AT86RF212B = "samr30:at86rf212b"
    WSN430_CC1101 = "wsn430:cc1101"
    WSN430_CC2420 = "wsn430:cc2420"

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """ArchiRadioString - a model defined in OpenAPI"""  # noqa: E501
        self.discriminator = None

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
        if not isinstance(other, ArchiRadioString):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
