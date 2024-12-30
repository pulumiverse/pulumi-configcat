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
    'GetTagsResult',
    'AwaitableGetTagsResult',
    'get_tags',
    'get_tags_output',
]

@pulumi.output_type
class GetTagsResult:
    """
    A collection of values returned by getTags.
    """
    def __init__(__self__, id=None, name_filter_regex=None, product_id=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name_filter_regex and not isinstance(name_filter_regex, str):
            raise TypeError("Expected argument 'name_filter_regex' to be a str")
        pulumi.set(__self__, "name_filter_regex", name_filter_regex)
        if product_id and not isinstance(product_id, str):
            raise TypeError("Expected argument 'product_id' to be a str")
        pulumi.set(__self__, "product_id", product_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nameFilterRegex")
    def name_filter_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_filter_regex")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter
    def tags(self) -> Sequence['outputs.GetTagsTagResult']:
        """
        A tag list block defined as below.
        """
        return pulumi.get(self, "tags")


class AwaitableGetTagsResult(GetTagsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagsResult(
            id=self.id,
            name_filter_regex=self.name_filter_regex,
            product_id=self.product_id,
            tags=self.tags)


def get_tags(name_filter_regex: Optional[str] = None,
             product_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagsResult:
    """
    ## # get_tags Resource

    Use this data source to access information about existing **Tags**.
    ## Example Usage

    ```python
    import pulumi
    import pulumi_configcat as configcat

    my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
    my_tags = configcat.get_tags(product_id=my_products.products[0].product_id,
        name_filter_regex="Test")
    pulumi.export("tagId", my_tags.tags[0].tag_id)
    ```

    ## Endpoints used

    - [List Tags](https://api.configcat.com/docs/#tag/Tags/operation/get-tags)


    :param str name_filter_regex: Filter the Tags by name.
    :param str product_id: The ID of the Product.
    """
    __args__ = dict()
    __args__['nameFilterRegex'] = name_filter_regex
    __args__['productId'] = product_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('configcat:index/getTags:getTags', __args__, opts=opts, typ=GetTagsResult).value

    return AwaitableGetTagsResult(
        id=pulumi.get(__ret__, 'id'),
        name_filter_regex=pulumi.get(__ret__, 'name_filter_regex'),
        product_id=pulumi.get(__ret__, 'product_id'),
        tags=pulumi.get(__ret__, 'tags'))
def get_tags_output(name_filter_regex: Optional[pulumi.Input[Optional[str]]] = None,
                    product_id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetTagsResult]:
    """
    ## # get_tags Resource

    Use this data source to access information about existing **Tags**.
    ## Example Usage

    ```python
    import pulumi
    import pulumi_configcat as configcat

    my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
    my_tags = configcat.get_tags(product_id=my_products.products[0].product_id,
        name_filter_regex="Test")
    pulumi.export("tagId", my_tags.tags[0].tag_id)
    ```

    ## Endpoints used

    - [List Tags](https://api.configcat.com/docs/#tag/Tags/operation/get-tags)


    :param str name_filter_regex: Filter the Tags by name.
    :param str product_id: The ID of the Product.
    """
    __args__ = dict()
    __args__['nameFilterRegex'] = name_filter_regex
    __args__['productId'] = product_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('configcat:index/getTags:getTags', __args__, opts=opts, typ=GetTagsResult)
    return __ret__.apply(lambda __response__: GetTagsResult(
        id=pulumi.get(__response__, 'id'),
        name_filter_regex=pulumi.get(__response__, 'name_filter_regex'),
        product_id=pulumi.get(__response__, 'product_id'),
        tags=pulumi.get(__response__, 'tags')))
