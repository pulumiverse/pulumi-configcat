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
    'GetProductsResult',
    'AwaitableGetProductsResult',
    'get_products',
    'get_products_output',
]

@pulumi.output_type
class GetProductsResult:
    """
    A collection of values returned by getProducts.
    """
    def __init__(__self__, id=None, name_filter_regex=None, products=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name_filter_regex and not isinstance(name_filter_regex, str):
            raise TypeError("Expected argument 'name_filter_regex' to be a str")
        pulumi.set(__self__, "name_filter_regex", name_filter_regex)
        if products and not isinstance(products, list):
            raise TypeError("Expected argument 'products' to be a list")
        pulumi.set(__self__, "products", products)

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
    @pulumi.getter
    def products(self) -> Sequence['outputs.GetProductsProductResult']:
        """
        A product list block defined as below.
        """
        return pulumi.get(self, "products")


class AwaitableGetProductsResult(GetProductsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProductsResult(
            id=self.id,
            name_filter_regex=self.name_filter_regex,
            products=self.products)


def get_products(name_filter_regex: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProductsResult:
    """
    ## # get_products Resource

    Use this data source to access information about existing **Products**. [What is a Product in ConfigCat?](https://configcat.com/docs/main-concepts)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_configcat as configcat

    my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
    pulumi.export("productId", my_products.products[0].product_id)
    ```

    ## Endpoints used

    - [List Products](https://api.configcat.com/docs/#tag/Products/operation/get-products)


    :param str name_filter_regex: Filter the Products by name.
    """
    __args__ = dict()
    __args__['nameFilterRegex'] = name_filter_regex
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('configcat:index/getProducts:getProducts', __args__, opts=opts, typ=GetProductsResult).value

    return AwaitableGetProductsResult(
        id=pulumi.get(__ret__, 'id'),
        name_filter_regex=pulumi.get(__ret__, 'name_filter_regex'),
        products=pulumi.get(__ret__, 'products'))
def get_products_output(name_filter_regex: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetProductsResult]:
    """
    ## # get_products Resource

    Use this data source to access information about existing **Products**. [What is a Product in ConfigCat?](https://configcat.com/docs/main-concepts)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_configcat as configcat

    my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
    pulumi.export("productId", my_products.products[0].product_id)
    ```

    ## Endpoints used

    - [List Products](https://api.configcat.com/docs/#tag/Products/operation/get-products)


    :param str name_filter_regex: Filter the Products by name.
    """
    __args__ = dict()
    __args__['nameFilterRegex'] = name_filter_regex
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('configcat:index/getProducts:getProducts', __args__, opts=opts, typ=GetProductsResult)
    return __ret__.apply(lambda __response__: GetProductsResult(
        id=pulumi.get(__response__, 'id'),
        name_filter_regex=pulumi.get(__response__, 'name_filter_regex'),
        products=pulumi.get(__response__, 'products')))
