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

__all__ = ['SegmentArgs', 'Segment']

@pulumi.input_type
class SegmentArgs:
    def __init__(__self__, *,
                 comparator: pulumi.Input[str],
                 comparison_attribute: pulumi.Input[str],
                 comparison_value: pulumi.Input[str],
                 product_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Segment resource.
        :param pulumi.Input[str] comparator: The [comparator](https://configcat.com/docs/advanced/targeting/#comparator) of the Segment.
        :param pulumi.Input[str] comparison_attribute: The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute) of the Segment.
        :param pulumi.Input[str] comparison_value: The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value) of the Segment.
        :param pulumi.Input[str] product_id: The ID of the Product.
        :param pulumi.Input[str] description: The description of the Segment.
        :param pulumi.Input[str] name: The name of the Segment.
        """
        pulumi.set(__self__, "comparator", comparator)
        pulumi.set(__self__, "comparison_attribute", comparison_attribute)
        pulumi.set(__self__, "comparison_value", comparison_value)
        pulumi.set(__self__, "product_id", product_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def comparator(self) -> pulumi.Input[str]:
        """
        The [comparator](https://configcat.com/docs/advanced/targeting/#comparator) of the Segment.
        """
        return pulumi.get(self, "comparator")

    @comparator.setter
    def comparator(self, value: pulumi.Input[str]):
        pulumi.set(self, "comparator", value)

    @property
    @pulumi.getter(name="comparisonAttribute")
    def comparison_attribute(self) -> pulumi.Input[str]:
        """
        The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute) of the Segment.
        """
        return pulumi.get(self, "comparison_attribute")

    @comparison_attribute.setter
    def comparison_attribute(self, value: pulumi.Input[str]):
        pulumi.set(self, "comparison_attribute", value)

    @property
    @pulumi.getter(name="comparisonValue")
    def comparison_value(self) -> pulumi.Input[str]:
        """
        The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value) of the Segment.
        """
        return pulumi.get(self, "comparison_value")

    @comparison_value.setter
    def comparison_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "comparison_value", value)

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
        The description of the Segment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Segment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SegmentState:
    def __init__(__self__, *,
                 comparator: Optional[pulumi.Input[str]] = None,
                 comparison_attribute: Optional[pulumi.Input[str]] = None,
                 comparison_value: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Segment resources.
        :param pulumi.Input[str] comparator: The [comparator](https://configcat.com/docs/advanced/targeting/#comparator) of the Segment.
        :param pulumi.Input[str] comparison_attribute: The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute) of the Segment.
        :param pulumi.Input[str] comparison_value: The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value) of the Segment.
        :param pulumi.Input[str] description: The description of the Segment.
        :param pulumi.Input[str] name: The name of the Segment.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        if comparator is not None:
            pulumi.set(__self__, "comparator", comparator)
        if comparison_attribute is not None:
            pulumi.set(__self__, "comparison_attribute", comparison_attribute)
        if comparison_value is not None:
            pulumi.set(__self__, "comparison_value", comparison_value)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if product_id is not None:
            pulumi.set(__self__, "product_id", product_id)

    @property
    @pulumi.getter
    def comparator(self) -> Optional[pulumi.Input[str]]:
        """
        The [comparator](https://configcat.com/docs/advanced/targeting/#comparator) of the Segment.
        """
        return pulumi.get(self, "comparator")

    @comparator.setter
    def comparator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comparator", value)

    @property
    @pulumi.getter(name="comparisonAttribute")
    def comparison_attribute(self) -> Optional[pulumi.Input[str]]:
        """
        The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute) of the Segment.
        """
        return pulumi.get(self, "comparison_attribute")

    @comparison_attribute.setter
    def comparison_attribute(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comparison_attribute", value)

    @property
    @pulumi.getter(name="comparisonValue")
    def comparison_value(self) -> Optional[pulumi.Input[str]]:
        """
        The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value) of the Segment.
        """
        return pulumi.get(self, "comparison_value")

    @comparison_value.setter
    def comparison_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comparison_value", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Segment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Segment.
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


class Segment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comparator: Optional[pulumi.Input[str]] = None,
                 comparison_attribute: Optional[pulumi.Input[str]] = None,
                 comparison_value: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates and manages a **Segment**. [What is a Segment in ConfigCat?](https://configcat.com/docs/advanced/segments)

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_configcat as configcat

        config = pulumi.Config()
        product_id = config.require("productId")
        my_segment = configcat.Segment("my_segment",
            product_id=product_id,
            name="Beta users",
            description="Beta users' description",
            comparison_attribute="email",
            comparator="sensitiveIsOneOf",
            comparison_value="betauser1@example.com,betauser2@example.com")
        pulumi.export("segmentId", my_segment.id)
        ```

        ## Import

        Segments can be imported using the SegmentId. Get the SegmentId using the [List Segments API](https://api.configcat.com/docs/#tag/Segments/operation/get-segments) for example.

        ```sh
        $ pulumi import configcat:index/segment:Segment example 08d86d63-2726-47cd-8bfc-59608ecb91e2
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comparator: The [comparator](https://configcat.com/docs/advanced/targeting/#comparator) of the Segment.
        :param pulumi.Input[str] comparison_attribute: The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute) of the Segment.
        :param pulumi.Input[str] comparison_value: The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value) of the Segment.
        :param pulumi.Input[str] description: The description of the Segment.
        :param pulumi.Input[str] name: The name of the Segment.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SegmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates and manages a **Segment**. [What is a Segment in ConfigCat?](https://configcat.com/docs/advanced/segments)

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_configcat as configcat

        config = pulumi.Config()
        product_id = config.require("productId")
        my_segment = configcat.Segment("my_segment",
            product_id=product_id,
            name="Beta users",
            description="Beta users' description",
            comparison_attribute="email",
            comparator="sensitiveIsOneOf",
            comparison_value="betauser1@example.com,betauser2@example.com")
        pulumi.export("segmentId", my_segment.id)
        ```

        ## Import

        Segments can be imported using the SegmentId. Get the SegmentId using the [List Segments API](https://api.configcat.com/docs/#tag/Segments/operation/get-segments) for example.

        ```sh
        $ pulumi import configcat:index/segment:Segment example 08d86d63-2726-47cd-8bfc-59608ecb91e2
        ```

        :param str resource_name: The name of the resource.
        :param SegmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SegmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comparator: Optional[pulumi.Input[str]] = None,
                 comparison_attribute: Optional[pulumi.Input[str]] = None,
                 comparison_value: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SegmentArgs.__new__(SegmentArgs)

            if comparator is None and not opts.urn:
                raise TypeError("Missing required property 'comparator'")
            __props__.__dict__["comparator"] = comparator
            if comparison_attribute is None and not opts.urn:
                raise TypeError("Missing required property 'comparison_attribute'")
            __props__.__dict__["comparison_attribute"] = comparison_attribute
            if comparison_value is None and not opts.urn:
                raise TypeError("Missing required property 'comparison_value'")
            __props__.__dict__["comparison_value"] = comparison_value
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
        super(Segment, __self__).__init__(
            'configcat:index/segment:Segment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            comparator: Optional[pulumi.Input[str]] = None,
            comparison_attribute: Optional[pulumi.Input[str]] = None,
            comparison_value: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            product_id: Optional[pulumi.Input[str]] = None) -> 'Segment':
        """
        Get an existing Segment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comparator: The [comparator](https://configcat.com/docs/advanced/targeting/#comparator) of the Segment.
        :param pulumi.Input[str] comparison_attribute: The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute) of the Segment.
        :param pulumi.Input[str] comparison_value: The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value) of the Segment.
        :param pulumi.Input[str] description: The description of the Segment.
        :param pulumi.Input[str] name: The name of the Segment.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SegmentState.__new__(_SegmentState)

        __props__.__dict__["comparator"] = comparator
        __props__.__dict__["comparison_attribute"] = comparison_attribute
        __props__.__dict__["comparison_value"] = comparison_value
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["product_id"] = product_id
        return Segment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def comparator(self) -> pulumi.Output[str]:
        """
        The [comparator](https://configcat.com/docs/advanced/targeting/#comparator) of the Segment.
        """
        return pulumi.get(self, "comparator")

    @property
    @pulumi.getter(name="comparisonAttribute")
    def comparison_attribute(self) -> pulumi.Output[str]:
        """
        The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute) of the Segment.
        """
        return pulumi.get(self, "comparison_attribute")

    @property
    @pulumi.getter(name="comparisonValue")
    def comparison_value(self) -> pulumi.Output[str]:
        """
        The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value) of the Segment.
        """
        return pulumi.get(self, "comparison_value")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the Segment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Segment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Output[str]:
        """
        The ID of the Product.
        """
        return pulumi.get(self, "product_id")

