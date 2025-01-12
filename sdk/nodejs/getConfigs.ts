// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * ## # configcat.getConfigs Resource
 *
 * Use this data source to access information about existing **Configs**. [What is a Config in ConfigCat?](https://configcat.com/docs/main-concepts)
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
 * export const configId = myConfigs.then(myConfigs => myConfigs.configs?.[0]?.configId);
 * ```
 *
 * ## Endpoints used
 *
 * [List Configs](https://api.configcat.com/docs/#tag/Configs/operation/get-configs)
 */
export function getConfigs(args: GetConfigsArgs, opts?: pulumi.InvokeOptions): Promise<GetConfigsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("configcat:index/getConfigs:getConfigs", {
        "nameFilterRegex": args.nameFilterRegex,
        "productId": args.productId,
    }, opts);
}

/**
 * A collection of arguments for invoking getConfigs.
 */
export interface GetConfigsArgs {
    /**
     * Filter the Configs by name.
     */
    nameFilterRegex?: string;
    /**
     * The ID of the Product.
     */
    productId: string;
}

/**
 * A collection of values returned by getConfigs.
 */
export interface GetConfigsResult {
    /**
     * A config list block defined as below.
     */
    readonly configs: outputs.GetConfigsConfig[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly nameFilterRegex?: string;
    readonly productId: string;
}
/**
 * ## # configcat.getConfigs Resource
 *
 * Use this data source to access information about existing **Configs**. [What is a Config in ConfigCat?](https://configcat.com/docs/main-concepts)
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
 * export const configId = myConfigs.then(myConfigs => myConfigs.configs?.[0]?.configId);
 * ```
 *
 * ## Endpoints used
 *
 * [List Configs](https://api.configcat.com/docs/#tag/Configs/operation/get-configs)
 */
export function getConfigsOutput(args: GetConfigsOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetConfigsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("configcat:index/getConfigs:getConfigs", {
        "nameFilterRegex": args.nameFilterRegex,
        "productId": args.productId,
    }, opts);
}

/**
 * A collection of arguments for invoking getConfigs.
 */
export interface GetConfigsOutputArgs {
    /**
     * Filter the Configs by name.
     */
    nameFilterRegex?: pulumi.Input<string>;
    /**
     * The ID of the Product.
     */
    productId: pulumi.Input<string>;
}
