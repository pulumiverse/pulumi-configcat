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
    'GetConfigurationsResult',
    'AwaitableGetConfigurationsResult',
    'get_configurations',
    'get_configurations_output',
]

@pulumi.output_type
class GetConfigurationsResult:
    """
    A collection of values returned by getConfigurations.
    """
    def __init__(__self__, configs=None, id=None, name_filter_regex=None, product_id=None):
        if configs and not isinstance(configs, list):
            raise TypeError("Expected argument 'configs' to be a list")
        pulumi.set(__self__, "configs", configs)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name_filter_regex and not isinstance(name_filter_regex, str):
            raise TypeError("Expected argument 'name_filter_regex' to be a str")
        pulumi.set(__self__, "name_filter_regex", name_filter_regex)
        if product_id and not isinstance(product_id, str):
            raise TypeError("Expected argument 'product_id' to be a str")
        pulumi.set(__self__, "product_id", product_id)

    @property
    @pulumi.getter
    def configs(self) -> Sequence['outputs.GetConfigurationsConfigResult']:
        return pulumi.get(self, "configs")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nameFilterRegex")
    def name_filter_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_filter_regex")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        return pulumi.get(self, "product_id")


class AwaitableGetConfigurationsResult(GetConfigurationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationsResult(
            configs=self.configs,
            id=self.id,
            name_filter_regex=self.name_filter_regex,
            product_id=self.product_id)


def get_configurations(name_filter_regex: Optional[str] = None,
                       product_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['nameFilterRegex'] = name_filter_regex
    __args__['productId'] = product_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('configcat:index/getConfigurations:getConfigurations', __args__, opts=opts, typ=GetConfigurationsResult).value

    return AwaitableGetConfigurationsResult(
        configs=pulumi.get(__ret__, 'configs'),
        id=pulumi.get(__ret__, 'id'),
        name_filter_regex=pulumi.get(__ret__, 'name_filter_regex'),
        product_id=pulumi.get(__ret__, 'product_id'))
def get_configurations_output(name_filter_regex: Optional[pulumi.Input[Optional[str]]] = None,
                              product_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetConfigurationsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['nameFilterRegex'] = name_filter_regex
    __args__['productId'] = product_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('configcat:index/getConfigurations:getConfigurations', __args__, opts=opts, typ=GetConfigurationsResult)
    return __ret__.apply(lambda __response__: GetConfigurationsResult(
        configs=pulumi.get(__response__, 'configs'),
        id=pulumi.get(__response__, 'id'),
        name_filter_regex=pulumi.get(__response__, 'name_filter_regex'),
        product_id=pulumi.get(__response__, 'product_id')))
