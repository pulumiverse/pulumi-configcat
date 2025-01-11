// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * ## # configcat.getSegments Resource
 *
 * Use this data source to access information about existing **Segments**. [What is a Segment in ConfigCat?](https://configcat.com/docs/advanced/segments)
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
 * const mySegments = myProducts.then(myProducts => configcat.getSegments({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Test",
 * }));
 * export const segmentId = mySegments.then(mySegments => mySegments.segments?.[0]?.segmentId);
 * ```
 *
 * ## Endpoints used
 *
 * - [List Segments](https://api.configcat.com/docs/#tag/Segments/operation/get-segments)
 */
export function getSegments(args: GetSegmentsArgs, opts?: pulumi.InvokeOptions): Promise<GetSegmentsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("configcat:index/getSegments:getSegments", {
        "nameFilterRegex": args.nameFilterRegex,
        "productId": args.productId,
    }, opts);
}

/**
 * A collection of arguments for invoking getSegments.
 */
export interface GetSegmentsArgs {
    /**
     * Filter the Segments by name.
     */
    nameFilterRegex?: string;
    /**
     * The ID of the Product.
     */
    productId: string;
}

/**
 * A collection of values returned by getSegments.
 */
export interface GetSegmentsResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly nameFilterRegex?: string;
    readonly productId: string;
    /**
     * A segment list block defined as below.
     */
    readonly segments: outputs.GetSegmentsSegment[];
}
/**
 * ## # configcat.getSegments Resource
 *
 * Use this data source to access information about existing **Segments**. [What is a Segment in ConfigCat?](https://configcat.com/docs/advanced/segments)
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
 * const mySegments = myProducts.then(myProducts => configcat.getSegments({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Test",
 * }));
 * export const segmentId = mySegments.then(mySegments => mySegments.segments?.[0]?.segmentId);
 * ```
 *
 * ## Endpoints used
 *
 * - [List Segments](https://api.configcat.com/docs/#tag/Segments/operation/get-segments)
 */
export function getSegmentsOutput(args: GetSegmentsOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetSegmentsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("configcat:index/getSegments:getSegments", {
        "nameFilterRegex": args.nameFilterRegex,
        "productId": args.productId,
    }, opts);
}

/**
 * A collection of arguments for invoking getSegments.
 */
export interface GetSegmentsOutputArgs {
    /**
     * Filter the Segments by name.
     */
    nameFilterRegex?: pulumi.Input<string>;
    /**
     * The ID of the Product.
     */
    productId: pulumi.Input<string>;
}
