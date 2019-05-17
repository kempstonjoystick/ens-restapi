# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StdResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, status: int=None, message: str=None, action: str=None):  # noqa: E501
        """StdResponse - a model defined in Swagger

        :param status: The status of this StdResponse.  # noqa: E501
        :type status: int
        :param message: The message of this StdResponse.  # noqa: E501
        :type message: str
        :param action: The action of this StdResponse.  # noqa: E501
        :type action: str
        """
        self.swagger_types = {
            'status': int,
            'message': str,
            'action': str
        }

        self.attribute_map = {
            'status': 'status',
            'message': 'message',
            'action': 'action'
        }

        self._status = status
        self._message = message
        self._action = action

    @classmethod
    def from_dict(cls, dikt) -> 'StdResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The stdResponse of this StdResponse.  # noqa: E501
        :rtype: StdResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> int:
        """Gets the status of this StdResponse.


        :return: The status of this StdResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this StdResponse.


        :param status: The status of this StdResponse.
        :type status: int
        """

        self._status = status

    @property
    def message(self) -> str:
        """Gets the message of this StdResponse.


        :return: The message of this StdResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this StdResponse.


        :param message: The message of this StdResponse.
        :type message: str
        """

        self._message = message

    @property
    def action(self) -> str:
        """Gets the action of this StdResponse.


        :return: The action of this StdResponse.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str):
        """Sets the action of this StdResponse.


        :param action: The action of this StdResponse.
        :type action: str
        """
        allowed_values = ["PUT", "POST", "GET", "DELETE"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action
