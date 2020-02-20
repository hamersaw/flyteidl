# coding: utf-8

"""
    flyteidl/service/admin.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyteadmin.models.admin_matchable_resource import AdminMatchableResource  # noqa: F401,E501


class AdminProjectDomainAttributesDeleteRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'project': 'str',
        'domain': 'str',
        'resource_type': 'AdminMatchableResource'
    }

    attribute_map = {
        'project': 'project',
        'domain': 'domain',
        'resource_type': 'resource_type'
    }

    def __init__(self, project=None, domain=None, resource_type=None):  # noqa: E501
        """AdminProjectDomainAttributesDeleteRequest - a model defined in Swagger"""  # noqa: E501

        self._project = None
        self._domain = None
        self._resource_type = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if domain is not None:
            self.domain = domain
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def project(self):
        """Gets the project of this AdminProjectDomainAttributesDeleteRequest.  # noqa: E501

        Unique project id which this set of attributes references.  # noqa: E501

        :return: The project of this AdminProjectDomainAttributesDeleteRequest.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this AdminProjectDomainAttributesDeleteRequest.

        Unique project id which this set of attributes references.  # noqa: E501

        :param project: The project of this AdminProjectDomainAttributesDeleteRequest.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def domain(self):
        """Gets the domain of this AdminProjectDomainAttributesDeleteRequest.  # noqa: E501

        Unique domain id which this set of attributes references.  # noqa: E501

        :return: The domain of this AdminProjectDomainAttributesDeleteRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AdminProjectDomainAttributesDeleteRequest.

        Unique domain id which this set of attributes references.  # noqa: E501

        :param domain: The domain of this AdminProjectDomainAttributesDeleteRequest.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def resource_type(self):
        """Gets the resource_type of this AdminProjectDomainAttributesDeleteRequest.  # noqa: E501


        :return: The resource_type of this AdminProjectDomainAttributesDeleteRequest.  # noqa: E501
        :rtype: AdminMatchableResource
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AdminProjectDomainAttributesDeleteRequest.


        :param resource_type: The resource_type of this AdminProjectDomainAttributesDeleteRequest.  # noqa: E501
        :type: AdminMatchableResource
        """

        self._resource_type = resource_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AdminProjectDomainAttributesDeleteRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdminProjectDomainAttributesDeleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
