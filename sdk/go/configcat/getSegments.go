// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/go/configcat/internal"
)

// ## # getSegments Resource
//
// Use this data source to access information about existing **Segments**. [What is a Segment in ConfigCat?](https://configcat.com/docs/advanced/segments)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-configcat/sdk/go/configcat"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			myProducts, err := configcat.GetProducts(ctx, &configcat.GetProductsArgs{
//				NameFilterRegex: pulumi.StringRef("ConfigCat's product"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			mySegments, err := configcat.GetSegments(ctx, &configcat.GetSegmentsArgs{
//				ProductId:       myProducts.Products[0].ProductId,
//				NameFilterRegex: pulumi.StringRef("Test"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("segmentId", mySegments.Segments[0].SegmentId)
//			return nil
//		})
//	}
//
// ```
//
// ## Endpoints used
//
// - [List Segments](https://api.configcat.com/docs/#tag/Segments/operation/get-segments)
func GetSegments(ctx *pulumi.Context, args *GetSegmentsArgs, opts ...pulumi.InvokeOption) (*GetSegmentsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetSegmentsResult
	err := ctx.Invoke("configcat:index/getSegments:getSegments", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSegments.
type GetSegmentsArgs struct {
	// Filter the Segments by name.
	NameFilterRegex *string `pulumi:"nameFilterRegex"`
	// The ID of the Product.
	ProductId string `pulumi:"productId"`
}

// A collection of values returned by getSegments.
type GetSegmentsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id              string  `pulumi:"id"`
	NameFilterRegex *string `pulumi:"nameFilterRegex"`
	ProductId       string  `pulumi:"productId"`
	// A segment list block defined as below.
	Segments []GetSegmentsSegment `pulumi:"segments"`
}

func GetSegmentsOutput(ctx *pulumi.Context, args GetSegmentsOutputArgs, opts ...pulumi.InvokeOption) GetSegmentsResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetSegmentsResultOutput, error) {
			args := v.(GetSegmentsArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("configcat:index/getSegments:getSegments", args, GetSegmentsResultOutput{}, options).(GetSegmentsResultOutput), nil
		}).(GetSegmentsResultOutput)
}

// A collection of arguments for invoking getSegments.
type GetSegmentsOutputArgs struct {
	// Filter the Segments by name.
	NameFilterRegex pulumi.StringPtrInput `pulumi:"nameFilterRegex"`
	// The ID of the Product.
	ProductId pulumi.StringInput `pulumi:"productId"`
}

func (GetSegmentsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSegmentsArgs)(nil)).Elem()
}

// A collection of values returned by getSegments.
type GetSegmentsResultOutput struct{ *pulumi.OutputState }

func (GetSegmentsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSegmentsResult)(nil)).Elem()
}

func (o GetSegmentsResultOutput) ToGetSegmentsResultOutput() GetSegmentsResultOutput {
	return o
}

func (o GetSegmentsResultOutput) ToGetSegmentsResultOutputWithContext(ctx context.Context) GetSegmentsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetSegmentsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetSegmentsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetSegmentsResultOutput) NameFilterRegex() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSegmentsResult) *string { return v.NameFilterRegex }).(pulumi.StringPtrOutput)
}

func (o GetSegmentsResultOutput) ProductId() pulumi.StringOutput {
	return o.ApplyT(func(v GetSegmentsResult) string { return v.ProductId }).(pulumi.StringOutput)
}

// A segment list block defined as below.
func (o GetSegmentsResultOutput) Segments() GetSegmentsSegmentArrayOutput {
	return o.ApplyT(func(v GetSegmentsResult) []GetSegmentsSegment { return v.Segments }).(GetSegmentsSegmentArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetSegmentsResultOutput{})
}
