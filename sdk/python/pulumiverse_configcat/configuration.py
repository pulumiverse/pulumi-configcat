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

__all__ = ['ConfigurationArgs', 'Configuration']

@pulumi.input_type
class ConfigurationArgs:
    def __init__(__self__, *,
                 order: pulumi.Input[int],
                 product_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Configuration resource.
        :param pulumi.Input[int] order: The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
        :param pulumi.Input[str] product_id: The ID of the Product.
        :param pulumi.Input[str] description: The description of the Config.
        :param pulumi.Input[str] name: The name of the Config.
        """
        pulumi.set(__self__, "order", order)
        pulumi.set(__self__, "product_id", product_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def order(self) -> pulumi.Input[int]:
        """
        The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: pulumi.Input[int]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Input[str]:
        """
        The ID of the Product.
        """
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "product_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Config.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Config.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ConfigurationState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 product_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Configuration resources.
        :param pulumi.Input[str] description: The description of the Config.
        :param pulumi.Input[str] name: The name of the Config.
        :param pulumi.Input[int] order: The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if product_id is not None:
            pulumi.set(__self__, "product_id", product_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Config.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Config.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[int]]:
        """
        The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Product.
        """
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_id", value)


class Configuration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # Configuration Resource

        Creates and manages a **Config**. [What is a Config in ConfigCat?](https://configcat.com/docs/main-concepts)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_configcat as configcat
        import pulumiverse_configcat as configcat

        my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
        my_config = configcat.Configuration("my_config",
            product_id=my_products.products[0].product_id,
            name="My config",
            description="My config description",
            order=0)
        pulumi.export("configId", my_config.id)
        ```

        ## Endpoints used

        * [Get Config](https://api.configcat.com/docs/#tag/Configs/operation/get-config)
        * [Create Config](https://api.configcat.com/docs/#tag/Configs/operation/create-config)
        * [Update Config](https://api.configcat.com/docs/#tag/Configs/operation/update-config)
        * [Delete Config](https://api.configcat.com/docs/#tag/Configs/operation/delete-config)

        ## Import

        Configs can be imported using the ConfigId. Get the ConfigId using the [List Configs API](https://api.configcat.com/docs/#tag/Configs/operation/get-configs) for example.

        ```sh
        $ pulumi import configcat:index/configuration:Configuration example 08d86d63-2726-47cd-8bfc-59608ecb91e2
        ```
        Read more about importing.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Config.
        :param pulumi.Input[str] name: The name of the Config.
        :param pulumi.Input[int] order: The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Configuration Resource

        Creates and manages a **Config**. [What is a Config in ConfigCat?](https://configcat.com/docs/main-concepts)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_configcat as configcat
        import pulumiverse_configcat as configcat

        my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
        my_config = configcat.Configuration("my_config",
            product_id=my_products.products[0].product_id,
            name="My config",
            description="My config description",
            order=0)
        pulumi.export("configId", my_config.id)
        ```

        ## Endpoints used

        * [Get Config](https://api.configcat.com/docs/#tag/Configs/operation/get-config)
        * [Create Config](https://api.configcat.com/docs/#tag/Configs/operation/create-config)
        * [Update Config](https://api.configcat.com/docs/#tag/Configs/operation/update-config)
        * [Delete Config](https://api.configcat.com/docs/#tag/Configs/operation/delete-config)

        ## Import

        Configs can be imported using the ConfigId. Get the ConfigId using the [List Configs API](https://api.configcat.com/docs/#tag/Configs/operation/get-configs) for example.

        ```sh
        $ pulumi import configcat:index/configuration:Configuration example 08d86d63-2726-47cd-8bfc-59608ecb91e2
        ```
        Read more about importing.

        :param str resource_name: The name of the resource.
        :param ConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigurationArgs.__new__(ConfigurationArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if order is None and not opts.urn:
                raise TypeError("Missing required property 'order'")
            __props__.__dict__["order"] = order
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
        super(Configuration, __self__).__init__(
            'configcat:index/configuration:Configuration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            order: Optional[pulumi.Input[int]] = None,
            product_id: Optional[pulumi.Input[str]] = None) -> 'Configuration':
        """
        Get an existing Configuration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Config.
        :param pulumi.Input[str] name: The name of the Config.
        :param pulumi.Input[int] order: The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConfigurationState.__new__(_ConfigurationState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["order"] = order
        __props__.__dict__["product_id"] = product_id
        return Configuration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Config.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Config.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def order(self) -> pulumi.Output[int]:
        """
        The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Output[str]:
        """
        The ID of the Product.
        """
        return pulumi.get(self, "product_id")

