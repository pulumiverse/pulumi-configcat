// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * ## # configcat.getProducts Resource
 *
 * Use this data source to access information about existing **Products**. [What is a Product in ConfigCat?](https://configcat.com/docs/main-concepts)
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
 * export const productId = myProducts.then(myProducts => myProducts.products?.[0]?.productId);
 * ```
 *
 * ## Endpoints used
 *
 * - [List Products](https://api.configcat.com/docs/#tag/Products/operation/get-products)
 */
export function getProducts(args?: GetProductsArgs, opts?: pulumi.InvokeOptions): Promise<GetProductsResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("configcat:index/getProducts:getProducts", {
        "nameFilterRegex": args.nameFilterRegex,
    }, opts);
}

/**
 * A collection of arguments for invoking getProducts.
 */
export interface GetProductsArgs {
    /**
     * Filter the Products by name.
     */
    nameFilterRegex?: string;
}

/**
 * A collection of values returned by getProducts.
 */
export interface GetProductsResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly nameFilterRegex?: string;
    /**
     * A product list block defined as below.
     */
    readonly products: outputs.GetProductsProduct[];
}
/**
 * ## # configcat.getProducts Resource
 *
 * Use this data source to access information about existing **Products**. [What is a Product in ConfigCat?](https://configcat.com/docs/main-concepts)
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
 * export const productId = myProducts.then(myProducts => myProducts.products?.[0]?.productId);
 * ```
 *
 * ## Endpoints used
 *
 * - [List Products](https://api.configcat.com/docs/#tag/Products/operation/get-products)
 */
export function getProductsOutput(args?: GetProductsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetProductsResult> {
    return pulumi.output(args).apply((a: any) => getProducts(a, opts))
}

/**
 * A collection of arguments for invoking getProducts.
 */
export interface GetProductsOutputArgs {
    /**
     * Filter the Products by name.
     */
    nameFilterRegex?: pulumi.Input<string>;
}