// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { ConfigurationArgs, ConfigurationState } from "./configuration";
export type Configuration = import("./configuration").Configuration;
export const Configuration: typeof import("./configuration").Configuration = null as any;
utilities.lazyLoad(exports, ["Configuration"], () => require("./configuration"));

export { EnvironmentArgs, EnvironmentState } from "./environment";
export type Environment = import("./environment").Environment;
export const Environment: typeof import("./environment").Environment = null as any;
utilities.lazyLoad(exports, ["Environment"], () => require("./environment"));

export { GetConfigurationsArgs, GetConfigurationsResult, GetConfigurationsOutputArgs } from "./getConfigurations";
export const getConfigurations: typeof import("./getConfigurations").getConfigurations = null as any;
export const getConfigurationsOutput: typeof import("./getConfigurations").getConfigurationsOutput = null as any;
utilities.lazyLoad(exports, ["getConfigurations","getConfigurationsOutput"], () => require("./getConfigurations"));

export { GetEnvironmentsArgs, GetEnvironmentsResult, GetEnvironmentsOutputArgs } from "./getEnvironments";
export const getEnvironments: typeof import("./getEnvironments").getEnvironments = null as any;
export const getEnvironmentsOutput: typeof import("./getEnvironments").getEnvironmentsOutput = null as any;
utilities.lazyLoad(exports, ["getEnvironments","getEnvironmentsOutput"], () => require("./getEnvironments"));

export { GetOrganizationsArgs, GetOrganizationsResult, GetOrganizationsOutputArgs } from "./getOrganizations";
export const getOrganizations: typeof import("./getOrganizations").getOrganizations = null as any;
export const getOrganizationsOutput: typeof import("./getOrganizations").getOrganizationsOutput = null as any;
utilities.lazyLoad(exports, ["getOrganizations","getOrganizationsOutput"], () => require("./getOrganizations"));

export { GetPermissionGroupsArgs, GetPermissionGroupsResult, GetPermissionGroupsOutputArgs } from "./getPermissionGroups";
export const getPermissionGroups: typeof import("./getPermissionGroups").getPermissionGroups = null as any;
export const getPermissionGroupsOutput: typeof import("./getPermissionGroups").getPermissionGroupsOutput = null as any;
utilities.lazyLoad(exports, ["getPermissionGroups","getPermissionGroupsOutput"], () => require("./getPermissionGroups"));

export { GetProductsArgs, GetProductsResult, GetProductsOutputArgs } from "./getProducts";
export const getProducts: typeof import("./getProducts").getProducts = null as any;
export const getProductsOutput: typeof import("./getProducts").getProductsOutput = null as any;
utilities.lazyLoad(exports, ["getProducts","getProductsOutput"], () => require("./getProducts"));

export { GetSdkKeysArgs, GetSdkKeysResult, GetSdkKeysOutputArgs } from "./getSdkKeys";
export const getSdkKeys: typeof import("./getSdkKeys").getSdkKeys = null as any;
export const getSdkKeysOutput: typeof import("./getSdkKeys").getSdkKeysOutput = null as any;
utilities.lazyLoad(exports, ["getSdkKeys","getSdkKeysOutput"], () => require("./getSdkKeys"));

export { GetSegmentsArgs, GetSegmentsResult, GetSegmentsOutputArgs } from "./getSegments";
export const getSegments: typeof import("./getSegments").getSegments = null as any;
export const getSegmentsOutput: typeof import("./getSegments").getSegmentsOutput = null as any;
utilities.lazyLoad(exports, ["getSegments","getSegmentsOutput"], () => require("./getSegments"));

export { GetSettingsArgs, GetSettingsResult, GetSettingsOutputArgs } from "./getSettings";
export const getSettings: typeof import("./getSettings").getSettings = null as any;
export const getSettingsOutput: typeof import("./getSettings").getSettingsOutput = null as any;
utilities.lazyLoad(exports, ["getSettings","getSettingsOutput"], () => require("./getSettings"));

export { GetTagsArgs, GetTagsResult, GetTagsOutputArgs } from "./getTags";
export const getTags: typeof import("./getTags").getTags = null as any;
export const getTagsOutput: typeof import("./getTags").getTagsOutput = null as any;
utilities.lazyLoad(exports, ["getTags","getTagsOutput"], () => require("./getTags"));

export { GetWebhookSigningKeysArgs, GetWebhookSigningKeysResult, GetWebhookSigningKeysOutputArgs } from "./getWebhookSigningKeys";
export const getWebhookSigningKeys: typeof import("./getWebhookSigningKeys").getWebhookSigningKeys = null as any;
export const getWebhookSigningKeysOutput: typeof import("./getWebhookSigningKeys").getWebhookSigningKeysOutput = null as any;
utilities.lazyLoad(exports, ["getWebhookSigningKeys","getWebhookSigningKeysOutput"], () => require("./getWebhookSigningKeys"));

export { IntegrationArgs, IntegrationState } from "./integration";
export type Integration = import("./integration").Integration;
export const Integration: typeof import("./integration").Integration = null as any;
utilities.lazyLoad(exports, ["Integration"], () => require("./integration"));

export { PermissionGroupArgs, PermissionGroupState } from "./permissionGroup";
export type PermissionGroup = import("./permissionGroup").PermissionGroup;
export const PermissionGroup: typeof import("./permissionGroup").PermissionGroup = null as any;
utilities.lazyLoad(exports, ["PermissionGroup"], () => require("./permissionGroup"));

export { ProductArgs, ProductState } from "./product";
export type Product = import("./product").Product;
export const Product: typeof import("./product").Product = null as any;
utilities.lazyLoad(exports, ["Product"], () => require("./product"));

export { ProductPreferencesArgs, ProductPreferencesState } from "./productPreferences";
export type ProductPreferences = import("./productPreferences").ProductPreferences;
export const ProductPreferences: typeof import("./productPreferences").ProductPreferences = null as any;
utilities.lazyLoad(exports, ["ProductPreferences"], () => require("./productPreferences"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { SegmentArgs, SegmentState } from "./segment";
export type Segment = import("./segment").Segment;
export const Segment: typeof import("./segment").Segment = null as any;
utilities.lazyLoad(exports, ["Segment"], () => require("./segment"));

export { SettingArgs, SettingState } from "./setting";
export type Setting = import("./setting").Setting;
export const Setting: typeof import("./setting").Setting = null as any;
utilities.lazyLoad(exports, ["Setting"], () => require("./setting"));

export { SettingTagArgs, SettingTagState } from "./settingTag";
export type SettingTag = import("./settingTag").SettingTag;
export const SettingTag: typeof import("./settingTag").SettingTag = null as any;
utilities.lazyLoad(exports, ["SettingTag"], () => require("./settingTag"));

export { SettingValueArgs, SettingValueState } from "./settingValue";
export type SettingValue = import("./settingValue").SettingValue;
export const SettingValue: typeof import("./settingValue").SettingValue = null as any;
utilities.lazyLoad(exports, ["SettingValue"], () => require("./settingValue"));

export { SettingValueV2Args, SettingValueV2State } from "./settingValueV2";
export type SettingValueV2 = import("./settingValueV2").SettingValueV2;
export const SettingValueV2: typeof import("./settingValueV2").SettingValueV2 = null as any;
utilities.lazyLoad(exports, ["SettingValueV2"], () => require("./settingValueV2"));

export { TagArgs, TagState } from "./tag";
export type Tag = import("./tag").Tag;
export const Tag: typeof import("./tag").Tag = null as any;
utilities.lazyLoad(exports, ["Tag"], () => require("./tag"));

export { WebhookArgs, WebhookState } from "./webhook";
export type Webhook = import("./webhook").Webhook;
export const Webhook: typeof import("./webhook").Webhook = null as any;
utilities.lazyLoad(exports, ["Webhook"], () => require("./webhook"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "configcat:index/configuration:Configuration":
                return new Configuration(name, <any>undefined, { urn })
            case "configcat:index/environment:Environment":
                return new Environment(name, <any>undefined, { urn })
            case "configcat:index/integration:Integration":
                return new Integration(name, <any>undefined, { urn })
            case "configcat:index/permissionGroup:PermissionGroup":
                return new PermissionGroup(name, <any>undefined, { urn })
            case "configcat:index/product:Product":
                return new Product(name, <any>undefined, { urn })
            case "configcat:index/productPreferences:ProductPreferences":
                return new ProductPreferences(name, <any>undefined, { urn })
            case "configcat:index/segment:Segment":
                return new Segment(name, <any>undefined, { urn })
            case "configcat:index/setting:Setting":
                return new Setting(name, <any>undefined, { urn })
            case "configcat:index/settingTag:SettingTag":
                return new SettingTag(name, <any>undefined, { urn })
            case "configcat:index/settingValue:SettingValue":
                return new SettingValue(name, <any>undefined, { urn })
            case "configcat:index/settingValueV2:SettingValueV2":
                return new SettingValueV2(name, <any>undefined, { urn })
            case "configcat:index/tag:Tag":
                return new Tag(name, <any>undefined, { urn })
            case "configcat:index/webhook:Webhook":
                return new Webhook(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("configcat", "index/configuration", _module)
pulumi.runtime.registerResourceModule("configcat", "index/environment", _module)
pulumi.runtime.registerResourceModule("configcat", "index/integration", _module)
pulumi.runtime.registerResourceModule("configcat", "index/permissionGroup", _module)
pulumi.runtime.registerResourceModule("configcat", "index/product", _module)
pulumi.runtime.registerResourceModule("configcat", "index/productPreferences", _module)
pulumi.runtime.registerResourceModule("configcat", "index/segment", _module)
pulumi.runtime.registerResourceModule("configcat", "index/setting", _module)
pulumi.runtime.registerResourceModule("configcat", "index/settingTag", _module)
pulumi.runtime.registerResourceModule("configcat", "index/settingValue", _module)
pulumi.runtime.registerResourceModule("configcat", "index/settingValueV2", _module)
pulumi.runtime.registerResourceModule("configcat", "index/tag", _module)
pulumi.runtime.registerResourceModule("configcat", "index/webhook", _module)
pulumi.runtime.registerResourcePackage("configcat", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:configcat") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
