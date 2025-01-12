// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/go/configcat/internal"
)

// ## # getTags Resource
//
// Use this data source to access information about existing **Tags**.
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
//			myTags, err := configcat.GetTags(ctx, &configcat.GetTagsArgs{
//				ProductId:       myProducts.Products[0].ProductId,
//				NameFilterRegex: pulumi.StringRef("Test"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("tagId", myTags.Tags[0].TagId)
//			return nil
//		})
//	}
//
// ```
//
// ## Endpoints used
//
// - [List Tags](https://api.configcat.com/docs/#tag/Tags/operation/get-tags)
func GetTags(ctx *pulumi.Context, args *GetTagsArgs, opts ...pulumi.InvokeOption) (*GetTagsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetTagsResult
	err := ctx.Invoke("configcat:index/getTags:getTags", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTags.
type GetTagsArgs struct {
	// Filter the Tags by name.
	NameFilterRegex *string `pulumi:"nameFilterRegex"`
	// The ID of the Product.
	ProductId string `pulumi:"productId"`
}

// A collection of values returned by getTags.
type GetTagsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id              string  `pulumi:"id"`
	NameFilterRegex *string `pulumi:"nameFilterRegex"`
	ProductId       string  `pulumi:"productId"`
	// A tag list block defined as below.
	Tags []GetTagsTag `pulumi:"tags"`
}

func GetTagsOutput(ctx *pulumi.Context, args GetTagsOutputArgs, opts ...pulumi.InvokeOption) GetTagsResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetTagsResultOutput, error) {
			args := v.(GetTagsArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("configcat:index/getTags:getTags", args, GetTagsResultOutput{}, options).(GetTagsResultOutput), nil
		}).(GetTagsResultOutput)
}

// A collection of arguments for invoking getTags.
type GetTagsOutputArgs struct {
	// Filter the Tags by name.
	NameFilterRegex pulumi.StringPtrInput `pulumi:"nameFilterRegex"`
	// The ID of the Product.
	ProductId pulumi.StringInput `pulumi:"productId"`
}

func (GetTagsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTagsArgs)(nil)).Elem()
}

// A collection of values returned by getTags.
type GetTagsResultOutput struct{ *pulumi.OutputState }

func (GetTagsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTagsResult)(nil)).Elem()
}

func (o GetTagsResultOutput) ToGetTagsResultOutput() GetTagsResultOutput {
	return o
}

func (o GetTagsResultOutput) ToGetTagsResultOutputWithContext(ctx context.Context) GetTagsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetTagsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetTagsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetTagsResultOutput) NameFilterRegex() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTagsResult) *string { return v.NameFilterRegex }).(pulumi.StringPtrOutput)
}

func (o GetTagsResultOutput) ProductId() pulumi.StringOutput {
	return o.ApplyT(func(v GetTagsResult) string { return v.ProductId }).(pulumi.StringOutput)
}

// A tag list block defined as below.
func (o GetTagsResultOutput) Tags() GetTagsTagArrayOutput {
	return o.ApplyT(func(v GetTagsResult) []GetTagsTag { return v.Tags }).(GetTagsTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetTagsResultOutput{})
}
