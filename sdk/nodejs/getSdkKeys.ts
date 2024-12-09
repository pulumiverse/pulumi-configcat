// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## # configcat.getSdkKeys Resource
 *
 * Use this data source to access information about **SDK Keys**.
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
 * const myEnvironments = myProducts.then(myProducts => configcat.getEnvironments({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Test",
 * }));
 * const mySdkkey = Promise.all([myConfigs, myEnvironments]).then(([myConfigs, myEnvironments]) => configcat.getSdkKeys({
 *     configId: myConfigs.configs?.[0]?.configId,
 *     environmentId: myEnvironments.environments?.[0]?.environmentId,
 * }));
 * export const primarySdkkey = mySdkkey.then(mySdkkey => mySdkkey.primary);
 * export const secondarySdkkey = mySdkkey.then(mySdkkey => mySdkkey.secondary);
 * ```
 *
 * ## Endpoints used
 *
 * - [Get SDK Key](https://api.configcat.com/docs/#tag/SDK-Keys/operation/get-sdk-keys)
 */
export function getSdkKeys(args: GetSdkKeysArgs, opts?: pulumi.InvokeOptions): Promise<GetSdkKeysResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("configcat:index/getSdkKeys:getSdkKeys", {
        "configId": args.configId,
        "environmentId": args.environmentId,
    }, opts);
}

/**
 * A collection of arguments for invoking getSdkKeys.
 */
export interface GetSdkKeysArgs {
    /**
     * The ID of the Config.
     */
    configId: string;
    /**
     * The ID of the Environment.
     */
    environmentId: string;
}

/**
 * A collection of values returned by getSdkKeys.
 */
export interface GetSdkKeysResult {
    readonly configId: string;
    readonly environmentId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The primary SDK Key associated with your **Config** and **Environment**.
     */
    readonly primary: string;
    /**
     * The secondary SDK Key associated with your **Config** and **Environment**.
     */
    readonly secondary: string;
}
/**
 * ## # configcat.getSdkKeys Resource
 *
 * Use this data source to access information about **SDK Keys**.
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
 * const myEnvironments = myProducts.then(myProducts => configcat.getEnvironments({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Test",
 * }));
 * const mySdkkey = Promise.all([myConfigs, myEnvironments]).then(([myConfigs, myEnvironments]) => configcat.getSdkKeys({
 *     configId: myConfigs.configs?.[0]?.configId,
 *     environmentId: myEnvironments.environments?.[0]?.environmentId,
 * }));
 * export const primarySdkkey = mySdkkey.then(mySdkkey => mySdkkey.primary);
 * export const secondarySdkkey = mySdkkey.then(mySdkkey => mySdkkey.secondary);
 * ```
 *
 * ## Endpoints used
 *
 * - [Get SDK Key](https://api.configcat.com/docs/#tag/SDK-Keys/operation/get-sdk-keys)
 */
export function getSdkKeysOutput(args: GetSdkKeysOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSdkKeysResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("configcat:index/getSdkKeys:getSdkKeys", {
        "configId": args.configId,
        "environmentId": args.environmentId,
    }, opts);
}

/**
 * A collection of arguments for invoking getSdkKeys.
 */
export interface GetSdkKeysOutputArgs {
    /**
     * The ID of the Config.
     */
    configId: pulumi.Input<string>;
    /**
     * The ID of the Environment.
     */
    environmentId: pulumi.Input<string>;
}
