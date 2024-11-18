// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * ## # configcat.getEnvironments Resource
 *
 * Use this data source to access information about existing **Environments**. [What is an Environment in ConfigCat?](https://configcat.com/docs/main-concepts)
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
 * const myEnvironments = myProducts.then(myProducts => configcat.getEnvironments({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Test",
 * }));
 * export const environmentId = myEnvironments.then(myEnvironments => myEnvironments.environments?.[0]?.environmentId);
 * ```
 *
 * ## Endpoints used
 *
 * - [List Environments](https://api.configcat.com/docs/#tag/Environments/operation/get-environments)
 */
export function getEnvironments(args: GetEnvironmentsArgs, opts?: pulumi.InvokeOptions): Promise<GetEnvironmentsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("configcat:index/getEnvironments:getEnvironments", {
        "nameFilterRegex": args.nameFilterRegex,
        "productId": args.productId,
    }, opts);
}

/**
 * A collection of arguments for invoking getEnvironments.
 */
export interface GetEnvironmentsArgs {
    /**
     * Filter the Environments by name.
     */
    nameFilterRegex?: string;
    /**
     * The ID of the Product.
     */
    productId: string;
}

/**
 * A collection of values returned by getEnvironments.
 */
export interface GetEnvironmentsResult {
    /**
     * An environment list block defined as below.
     */
    readonly environments: outputs.GetEnvironmentsEnvironment[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly nameFilterRegex?: string;
    readonly productId: string;
}
/**
 * ## # configcat.getEnvironments Resource
 *
 * Use this data source to access information about existing **Environments**. [What is an Environment in ConfigCat?](https://configcat.com/docs/main-concepts)
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
 * const myEnvironments = myProducts.then(myProducts => configcat.getEnvironments({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Test",
 * }));
 * export const environmentId = myEnvironments.then(myEnvironments => myEnvironments.environments?.[0]?.environmentId);
 * ```
 *
 * ## Endpoints used
 *
 * - [List Environments](https://api.configcat.com/docs/#tag/Environments/operation/get-environments)
 */
export function getEnvironmentsOutput(args: GetEnvironmentsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEnvironmentsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("configcat:index/getEnvironments:getEnvironments", {
        "nameFilterRegex": args.nameFilterRegex,
        "productId": args.productId,
    }, opts);
}

/**
 * A collection of arguments for invoking getEnvironments.
 */
export interface GetEnvironmentsOutputArgs {
    /**
     * Filter the Environments by name.
     */
    nameFilterRegex?: pulumi.Input<string>;
    /**
     * The ID of the Product.
     */
    productId: pulumi.Input<string>;
}
