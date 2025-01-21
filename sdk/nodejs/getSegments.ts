// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

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
    nameFilterRegex?: string;
    productId: string;
}

/**
 * A collection of values returned by getSegments.
 */
export interface GetSegmentsResult {
    readonly id: string;
    readonly nameFilterRegex?: string;
    readonly productId: string;
    readonly segments: outputs.GetSegmentsSegment[];
}
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
    nameFilterRegex?: pulumi.Input<string>;
    productId: pulumi.Input<string>;
}
