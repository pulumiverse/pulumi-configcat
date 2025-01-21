// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getTags(args: GetTagsArgs, opts?: pulumi.InvokeOptions): Promise<GetTagsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("configcat:index/getTags:getTags", {
        "nameFilterRegex": args.nameFilterRegex,
        "productId": args.productId,
    }, opts);
}

/**
 * A collection of arguments for invoking getTags.
 */
export interface GetTagsArgs {
    nameFilterRegex?: string;
    productId: string;
}

/**
 * A collection of values returned by getTags.
 */
export interface GetTagsResult {
    readonly id: string;
    readonly nameFilterRegex?: string;
    readonly productId: string;
    readonly tags: outputs.GetTagsTag[];
}
export function getTagsOutput(args: GetTagsOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetTagsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("configcat:index/getTags:getTags", {
        "nameFilterRegex": args.nameFilterRegex,
        "productId": args.productId,
    }, opts);
}

/**
 * A collection of arguments for invoking getTags.
 */
export interface GetTagsOutputArgs {
    nameFilterRegex?: pulumi.Input<string>;
    productId: pulumi.Input<string>;
}
