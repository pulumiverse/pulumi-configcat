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

__all__ = ['IntegrationArgs', 'Integration']

@pulumi.input_type
class IntegrationArgs:
    def __init__(__self__, *,
                 integration_type: pulumi.Input[str],
                 product_id: pulumi.Input[str],
                 configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Integration resource.
        :param pulumi.Input[str] integration_type: The integration type of the Integration. Possible values: `dataDog`, `slack`, `amplitude`, `mixPanel`, `segment`,
               `pubNub`.
        :param pulumi.Input[str] product_id: The ID of the Product.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] configs: List of Config IDs that are connected with this Integration. If the list is empty, all of the Configs are connected.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: List of Environment IDs that are connected with this Integration. If the list is empty, all of the Environments are
               connected.
        :param pulumi.Input[str] name: The name of the Integration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Parameters of the integration. The Parameters dictionary differs for each IntegrationType. See available options per
               integration type at the Example usage section.
        """
        pulumi.set(__self__, "integration_type", integration_type)
        pulumi.set(__self__, "product_id", product_id)
        if configs is not None:
            pulumi.set(__self__, "configs", configs)
        if environments is not None:
            pulumi.set(__self__, "environments", environments)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)

    @property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> pulumi.Input[str]:
        """
        The integration type of the Integration. Possible values: `dataDog`, `slack`, `amplitude`, `mixPanel`, `segment`,
        `pubNub`.
        """
        return pulumi.get(self, "integration_type")

    @integration_type.setter
    def integration_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_type", value)

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
    def configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Config IDs that are connected with this Integration. If the list is empty, all of the Configs are connected.
        """
        return pulumi.get(self, "configs")

    @configs.setter
    def configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "configs", value)

    @property
    @pulumi.getter
    def environments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Environment IDs that are connected with this Integration. If the list is empty, all of the Environments are
        connected.
        """
        return pulumi.get(self, "environments")

    @environments.setter
    def environments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "environments", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Integration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Parameters of the integration. The Parameters dictionary differs for each IntegrationType. See available options per
        integration type at the Example usage section.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)


@pulumi.input_type
class _IntegrationState:
    def __init__(__self__, *,
                 configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 integration_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 product_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Integration resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] configs: List of Config IDs that are connected with this Integration. If the list is empty, all of the Configs are connected.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: List of Environment IDs that are connected with this Integration. If the list is empty, all of the Environments are
               connected.
        :param pulumi.Input[str] integration_type: The integration type of the Integration. Possible values: `dataDog`, `slack`, `amplitude`, `mixPanel`, `segment`,
               `pubNub`.
        :param pulumi.Input[str] name: The name of the Integration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Parameters of the integration. The Parameters dictionary differs for each IntegrationType. See available options per
               integration type at the Example usage section.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        if configs is not None:
            pulumi.set(__self__, "configs", configs)
        if environments is not None:
            pulumi.set(__self__, "environments", environments)
        if integration_type is not None:
            pulumi.set(__self__, "integration_type", integration_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if product_id is not None:
            pulumi.set(__self__, "product_id", product_id)

    @property
    @pulumi.getter
    def configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Config IDs that are connected with this Integration. If the list is empty, all of the Configs are connected.
        """
        return pulumi.get(self, "configs")

    @configs.setter
    def configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "configs", value)

    @property
    @pulumi.getter
    def environments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Environment IDs that are connected with this Integration. If the list is empty, all of the Environments are
        connected.
        """
        return pulumi.get(self, "environments")

    @environments.setter
    def environments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "environments", value)

    @property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> Optional[pulumi.Input[str]]:
        """
        The integration type of the Integration. Possible values: `dataDog`, `slack`, `amplitude`, `mixPanel`, `segment`,
        `pubNub`.
        """
        return pulumi.get(self, "integration_type")

    @integration_type.setter
    def integration_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Integration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Parameters of the integration. The Parameters dictionary differs for each IntegrationType. See available options per
        integration type at the Example usage section.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)

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


class Integration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 integration_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Integration resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] configs: List of Config IDs that are connected with this Integration. If the list is empty, all of the Configs are connected.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: List of Environment IDs that are connected with this Integration. If the list is empty, all of the Environments are
               connected.
        :param pulumi.Input[str] integration_type: The integration type of the Integration. Possible values: `dataDog`, `slack`, `amplitude`, `mixPanel`, `segment`,
               `pubNub`.
        :param pulumi.Input[str] name: The name of the Integration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Parameters of the integration. The Parameters dictionary differs for each IntegrationType. See available options per
               integration type at the Example usage section.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Integration resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param IntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 integration_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationArgs.__new__(IntegrationArgs)

            __props__.__dict__["configs"] = configs
            __props__.__dict__["environments"] = environments
            if integration_type is None and not opts.urn:
                raise TypeError("Missing required property 'integration_type'")
            __props__.__dict__["integration_type"] = integration_type
            __props__.__dict__["name"] = name
            __props__.__dict__["parameters"] = parameters
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
        super(Integration, __self__).__init__(
            'configcat:index/integration:Integration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            configs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            integration_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            product_id: Optional[pulumi.Input[str]] = None) -> 'Integration':
        """
        Get an existing Integration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] configs: List of Config IDs that are connected with this Integration. If the list is empty, all of the Configs are connected.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: List of Environment IDs that are connected with this Integration. If the list is empty, all of the Environments are
               connected.
        :param pulumi.Input[str] integration_type: The integration type of the Integration. Possible values: `dataDog`, `slack`, `amplitude`, `mixPanel`, `segment`,
               `pubNub`.
        :param pulumi.Input[str] name: The name of the Integration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Parameters of the integration. The Parameters dictionary differs for each IntegrationType. See available options per
               integration type at the Example usage section.
        :param pulumi.Input[str] product_id: The ID of the Product.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationState.__new__(_IntegrationState)

        __props__.__dict__["configs"] = configs
        __props__.__dict__["environments"] = environments
        __props__.__dict__["integration_type"] = integration_type
        __props__.__dict__["name"] = name
        __props__.__dict__["parameters"] = parameters
        __props__.__dict__["product_id"] = product_id
        return Integration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def configs(self) -> pulumi.Output[Sequence[str]]:
        """
        List of Config IDs that are connected with this Integration. If the list is empty, all of the Configs are connected.
        """
        return pulumi.get(self, "configs")

    @property
    @pulumi.getter
    def environments(self) -> pulumi.Output[Sequence[str]]:
        """
        List of Environment IDs that are connected with this Integration. If the list is empty, all of the Environments are
        connected.
        """
        return pulumi.get(self, "environments")

    @property
    @pulumi.getter(name="integrationType")
    def integration_type(self) -> pulumi.Output[str]:
        """
        The integration type of the Integration. Possible values: `dataDog`, `slack`, `amplitude`, `mixPanel`, `segment`,
        `pubNub`.
        """
        return pulumi.get(self, "integration_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Integration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Parameters of the integration. The Parameters dictionary differs for each IntegrationType. See available options per
        integration type at the Example usage section.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Output[str]:
        """
        The ID of the Product.
        """
        return pulumi.get(self, "product_id")

