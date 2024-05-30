// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * ## # configcat.getSettings Resource
 *
 * Use this data source to access information about existing **Feature Flags or Settings**. [Read more about the anatomy of a Feature Flag or Setting.](https://configcat.com/docs/main-concepts)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as configcat from "@pulumi/configcat";
 *
 * const myProducts = configcat.getProducts({
 *     nameFilterRegex: "ConfigCat's product",
 * });
 * const myConfigs = myProducts.then(myProducts => configcat.getConfigs({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Main Config",
 * }));
 * const settings = myConfigs.then(myConfigs => configcat.getSettings({
 *     configId: myConfigs.configs?.[0]?.configId,
 *     keyFilterRegex: "isAwesomeFeatureEnabled",
 * }));
 * export const settingId = settings.then(settings => settings.settings?.[0]?.settingId);
 * ```
 *
 * ## Endpoints used
 *
 * - [List Flags](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings)
 */
export function getSettings(args: GetSettingsArgs, opts?: pulumi.InvokeOptions): Promise<GetSettingsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("configcat:index/getSettings:getSettings", {
        "configId": args.configId,
        "keyFilterRegex": args.keyFilterRegex,
    }, opts);
}

/**
 * A collection of arguments for invoking getSettings.
 */
export interface GetSettingsArgs {
    /**
     * The ID of the Config.
     */
    configId: string;
    /**
     * Filter the Settings by key.
     */
    keyFilterRegex?: string;
}

/**
 * A collection of values returned by getSettings.
 */
export interface GetSettingsResult {
    readonly configId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly keyFilterRegex?: string;
    /**
     * A setting list block defined as below.
     */
    readonly settings: outputs.GetSettingsSetting[];
}
/**
 * ## # configcat.getSettings Resource
 *
 * Use this data source to access information about existing **Feature Flags or Settings**. [Read more about the anatomy of a Feature Flag or Setting.](https://configcat.com/docs/main-concepts)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as configcat from "@pulumi/configcat";
 *
 * const myProducts = configcat.getProducts({
 *     nameFilterRegex: "ConfigCat's product",
 * });
 * const myConfigs = myProducts.then(myProducts => configcat.getConfigs({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Main Config",
 * }));
 * const settings = myConfigs.then(myConfigs => configcat.getSettings({
 *     configId: myConfigs.configs?.[0]?.configId,
 *     keyFilterRegex: "isAwesomeFeatureEnabled",
 * }));
 * export const settingId = settings.then(settings => settings.settings?.[0]?.settingId);
 * ```
 *
 * ## Endpoints used
 *
 * - [List Flags](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings)
 */
export function getSettingsOutput(args: GetSettingsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSettingsResult> {
    return pulumi.output(args).apply((a: any) => getSettings(a, opts))
}

/**
 * A collection of arguments for invoking getSettings.
 */
export interface GetSettingsOutputArgs {
    /**
     * The ID of the Config.
     */
    configId: pulumi.Input<string>;
    /**
     * Filter the Settings by key.
     */
    keyFilterRegex?: pulumi.Input<string>;
}
