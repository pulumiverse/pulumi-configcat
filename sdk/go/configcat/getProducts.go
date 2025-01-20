// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/v3/go/configcat/internal"
)

// ## # getProducts Resource
//
// Use this data source to access information about existing **Products**. [What is a Product in ConfigCat?](https://configcat.com/docs/main-concepts)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-configcat/sdk/v2/go/configcat"
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
//			ctx.Export("productId", myProducts.Products[0].ProductId)
//			return nil
//		})
//	}
//
// ```
//
// ## Endpoints used
//
// - [List Products](https://api.configcat.com/docs/#tag/Products/operation/get-products)
func GetProducts(ctx *pulumi.Context, args *GetProductsArgs, opts ...pulumi.InvokeOption) (*GetProductsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetProductsResult
	err := ctx.Invoke("configcat:index/getProducts:getProducts", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getProducts.
type GetProductsArgs struct {
	// Filter the Products by name.
	NameFilterRegex *string `pulumi:"nameFilterRegex"`
}

// A collection of values returned by getProducts.
type GetProductsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id              string  `pulumi:"id"`
	NameFilterRegex *string `pulumi:"nameFilterRegex"`
	// A product list block defined as below.
	Products []GetProductsProduct `pulumi:"products"`
}

func GetProductsOutput(ctx *pulumi.Context, args GetProductsOutputArgs, opts ...pulumi.InvokeOption) GetProductsResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetProductsResultOutput, error) {
			args := v.(GetProductsArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("configcat:index/getProducts:getProducts", args, GetProductsResultOutput{}, options).(GetProductsResultOutput), nil
		}).(GetProductsResultOutput)
}

// A collection of arguments for invoking getProducts.
type GetProductsOutputArgs struct {
	// Filter the Products by name.
	NameFilterRegex pulumi.StringPtrInput `pulumi:"nameFilterRegex"`
}

func (GetProductsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetProductsArgs)(nil)).Elem()
}

// A collection of values returned by getProducts.
type GetProductsResultOutput struct{ *pulumi.OutputState }

func (GetProductsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetProductsResult)(nil)).Elem()
}

func (o GetProductsResultOutput) ToGetProductsResultOutput() GetProductsResultOutput {
	return o
}

func (o GetProductsResultOutput) ToGetProductsResultOutputWithContext(ctx context.Context) GetProductsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetProductsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetProductsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetProductsResultOutput) NameFilterRegex() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetProductsResult) *string { return v.NameFilterRegex }).(pulumi.StringPtrOutput)
}

// A product list block defined as below.
func (o GetProductsResultOutput) Products() GetProductsProductArrayOutput {
	return o.ApplyT(func(v GetProductsResult) []GetProductsProduct { return v.Products }).(GetProductsProductArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetProductsResultOutput{})
}
