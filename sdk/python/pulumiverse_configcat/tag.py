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

__all__ = ['TagArgs', 'Tag']

@pulumi.input_type
class TagArgs:
    def __init__(__self__, *,
                 product_id: pulumi.Input[str],
                 color: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Tag resource.
        :param pulumi.Input[str] product_id: The ID of the Product.
        :param pulumi.Input[str] color: The color of the Tag. Default value. `panther`. Valid values: `panther`|`whale`|`salmon`|`lizard`|`canary`|`koala`.
        :param pulumi.Input[str] name: The name of the Tag.
        """
        pulumi.set(__self__, "product_id", product_id)
        if color is not None:
            pulumi.set(__self__, "color", color)
        if name is not None:
            pulumi.set(__self__, "name", name)

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
    def color(self) -> Optional[pulumi.Input[str]]:
        """
        The color of the Tag. Default value. `panther`. Valid values: `panther`|`whale`|`salmon`|`lizard`|`canary`|`koala`.
        """
        return pulumi.get(self, "color")

    @color.setter
    def color(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "color", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Tag.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TagState:
    def __init__(__self__, *,
                 color: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Tag resources.
        :param pulumi.Input[str] color: The color of the Tag. Default value. `panther`. Valid values: `panther`|`whale`|`salmon`|`lizard`|`canary`|`koala`.
        :param pulumi.Input[str] name: The name of the Tag.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        if color is not None:
            pulumi.set(__self__, "color", color)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if product_id is not None:
            pulumi.set(__self__, "product_id", product_id)

    @property
    @pulumi.getter
    def color(self) -> Optional[pulumi.Input[str]]:
        """
        The color of the Tag. Default value. `panther`. Valid values: `panther`|`whale`|`salmon`|`lizard`|`canary`|`koala`.
        """
        return pulumi.get(self, "color")

    @color.setter
    def color(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "color", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Tag.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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


class Tag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates and manages a **Tag**.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_configcat as configcat

        config = pulumi.Config()
        product_id = config.require("productId")
        my_tag = configcat.Tag("my_tag",
            product_id=product_id,
            name="Created by Terraform",
            color="panther")
        pulumi.export("tagId", my_tag.id)
        ```

        ## Import

        Tags can be imported using the TagId. Get the TagId using e.g. the [List Tags API](https://api.configcat.com/docs/#tag/Tags/operation/get-tags).

        ```sh
        $ pulumi import configcat:index/tag:Tag example 1234
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] color: The color of the Tag. Default value. `panther`. Valid values: `panther`|`whale`|`salmon`|`lizard`|`canary`|`koala`.
        :param pulumi.Input[str] name: The name of the Tag.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates and manages a **Tag**.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_configcat as configcat

        config = pulumi.Config()
        product_id = config.require("productId")
        my_tag = configcat.Tag("my_tag",
            product_id=product_id,
            name="Created by Terraform",
            color="panther")
        pulumi.export("tagId", my_tag.id)
        ```

        ## Import

        Tags can be imported using the TagId. Get the TagId using e.g. the [List Tags API](https://api.configcat.com/docs/#tag/Tags/operation/get-tags).

        ```sh
        $ pulumi import configcat:index/tag:Tag example 1234
        ```

        :param str resource_name: The name of the resource.
        :param TagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagArgs.__new__(TagArgs)

            __props__.__dict__["color"] = color
            __props__.__dict__["name"] = name
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
        super(Tag, __self__).__init__(
            'configcat:index/tag:Tag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            color: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            product_id: Optional[pulumi.Input[str]] = None) -> 'Tag':
        """
        Get an existing Tag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] color: The color of the Tag. Default value. `panther`. Valid values: `panther`|`whale`|`salmon`|`lizard`|`canary`|`koala`.
        :param pulumi.Input[str] name: The name of the Tag.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TagState.__new__(_TagState)

        __props__.__dict__["color"] = color
        __props__.__dict__["name"] = name
        __props__.__dict__["product_id"] = product_id
        return Tag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def color(self) -> pulumi.Output[str]:
        """
        The color of the Tag. Default value. `panther`. Valid values: `panther`|`whale`|`salmon`|`lizard`|`canary`|`koala`.
        """
        return pulumi.get(self, "color")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Tag.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Output[str]:
        """
        The ID of the Product.
        """
        return pulumi.get(self, "product_id")

