# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs

__all__ = [
    'GetPermissionGroupsResult',
    'AwaitableGetPermissionGroupsResult',
    'get_permission_groups',
    'get_permission_groups_output',
]

@pulumi.output_type
class GetPermissionGroupsResult:
    """
    A collection of values returned by getPermissionGroups.
    """
    def __init__(__self__, id=None, name_filter_regex=None, permission_groups=None, product_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name_filter_regex and not isinstance(name_filter_regex, str):
            raise TypeError("Expected argument 'name_filter_regex' to be a str")
        pulumi.set(__self__, "name_filter_regex", name_filter_regex)
        if permission_groups and not isinstance(permission_groups, list):
            raise TypeError("Expected argument 'permission_groups' to be a list")
        pulumi.set(__self__, "permission_groups", permission_groups)
        if product_id and not isinstance(product_id, str):
            raise TypeError("Expected argument 'product_id' to be a str")
        pulumi.set(__self__, "product_id", product_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Internal ID of the data source. Do not use.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nameFilterRegex")
    def name_filter_regex(self) -> Optional[str]:
        """
        Filter the Permission Groups by name.
        """
        return pulumi.get(self, "name_filter_regex")

    @property
    @pulumi.getter(name="permissionGroups")
    def permission_groups(self) -> Sequence['outputs.GetPermissionGroupsPermissionGroupResult']:
        return pulumi.get(self, "permission_groups")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        """
        The ID of the Product.
        """
        return pulumi.get(self, "product_id")


class AwaitableGetPermissionGroupsResult(GetPermissionGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPermissionGroupsResult(
            id=self.id,
            name_filter_regex=self.name_filter_regex,
            permission_groups=self.permission_groups,
            product_id=self.product_id)


def get_permission_groups(name_filter_regex: Optional[str] = None,
                          product_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPermissionGroupsResult:
    """
    Use this data source to access information about existing **Permission Groups**. [What is a Permission Group in ConfigCat?](https://configcat.com/docs/advanced/team-management/team-management-basics/#permissions--permission-groups-product-level)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_configcat as configcat

    config = pulumi.Config()
    product_id = config.require("productId")
    my_permission_groups = configcat.get_permission_groups(product_id=product_id,
        name_filter_regex="Administrators")
    pulumi.export("permissionGroupId", my_permission_groups.permission_groups[0].permission_group_id)
    ```


    :param str name_filter_regex: Filter the Permission Groups by name.
    :param str product_id: The ID of the Product.
    """
    __args__ = dict()
    __args__['nameFilterRegex'] = name_filter_regex
    __args__['productId'] = product_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('configcat:index/getPermissionGroups:getPermissionGroups', __args__, opts=opts, typ=GetPermissionGroupsResult).value

    return AwaitableGetPermissionGroupsResult(
        id=pulumi.get(__ret__, 'id'),
        name_filter_regex=pulumi.get(__ret__, 'name_filter_regex'),
        permission_groups=pulumi.get(__ret__, 'permission_groups'),
        product_id=pulumi.get(__ret__, 'product_id'))
def get_permission_groups_output(name_filter_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                 product_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPermissionGroupsResult]:
    """
    Use this data source to access information about existing **Permission Groups**. [What is a Permission Group in ConfigCat?](https://configcat.com/docs/advanced/team-management/team-management-basics/#permissions--permission-groups-product-level)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_configcat as configcat

    config = pulumi.Config()
    product_id = config.require("productId")
    my_permission_groups = configcat.get_permission_groups(product_id=product_id,
        name_filter_regex="Administrators")
    pulumi.export("permissionGroupId", my_permission_groups.permission_groups[0].permission_group_id)
    ```


    :param str name_filter_regex: Filter the Permission Groups by name.
    :param str product_id: The ID of the Product.
    """
    __args__ = dict()
    __args__['nameFilterRegex'] = name_filter_regex
    __args__['productId'] = product_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('configcat:index/getPermissionGroups:getPermissionGroups', __args__, opts=opts, typ=GetPermissionGroupsResult)
    return __ret__.apply(lambda __response__: GetPermissionGroupsResult(
        id=pulumi.get(__response__, 'id'),
        name_filter_regex=pulumi.get(__response__, 'name_filter_regex'),
        permission_groups=pulumi.get(__response__, 'permission_groups'),
        product_id=pulumi.get(__response__, 'product_id')))
