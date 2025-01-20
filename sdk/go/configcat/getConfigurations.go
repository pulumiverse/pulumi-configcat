// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/v3/go/configcat/internal"
)

// ## # getConfigurations Resource
//
// Use this data source to access information about existing **Configs**. [What is a Config in ConfigCat?](https://configcat.com/docs/main-concepts)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-configcat/sdk/v3/go/configcat"
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
//			myConfigs, err := configcat.GetConfigurations(ctx, &configcat.GetConfigurationsArgs{
//				ProductId:       myProducts.Products[0].ProductId,
//				NameFilterRegex: pulumi.StringRef("Main Config"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("configId", myConfigs.Configs[0].ConfigId)
//			return nil
//		})
//	}
//
// ```
//
// ## Endpoints used
//
// [List Configs](https://api.configcat.com/docs/#tag/Configs/operation/get-configs)
func GetConfigurations(ctx *pulumi.Context, args *GetConfigurationsArgs, opts ...pulumi.InvokeOption) (*GetConfigurationsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetConfigurationsResult
	err := ctx.Invoke("configcat:index/getConfigurations:getConfigurations", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getConfigurations.
type GetConfigurationsArgs struct {
	// Filter the Configs by name.
	NameFilterRegex *string `pulumi:"nameFilterRegex"`
	// The ID of the Product.
	ProductId string `pulumi:"productId"`
}

// A collection of values returned by getConfigurations.
type GetConfigurationsResult struct {
	// A config list block defined as below.
	Configs []GetConfigurationsConfig `pulumi:"configs"`
	// The provider-assigned unique ID for this managed resource.
	Id              string  `pulumi:"id"`
	NameFilterRegex *string `pulumi:"nameFilterRegex"`
	ProductId       string  `pulumi:"productId"`
}

func GetConfigurationsOutput(ctx *pulumi.Context, args GetConfigurationsOutputArgs, opts ...pulumi.InvokeOption) GetConfigurationsResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetConfigurationsResultOutput, error) {
			args := v.(GetConfigurationsArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("configcat:index/getConfigurations:getConfigurations", args, GetConfigurationsResultOutput{}, options).(GetConfigurationsResultOutput), nil
		}).(GetConfigurationsResultOutput)
}

// A collection of arguments for invoking getConfigurations.
type GetConfigurationsOutputArgs struct {
	// Filter the Configs by name.
	NameFilterRegex pulumi.StringPtrInput `pulumi:"nameFilterRegex"`
	// The ID of the Product.
	ProductId pulumi.StringInput `pulumi:"productId"`
}

func (GetConfigurationsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetConfigurationsArgs)(nil)).Elem()
}

// A collection of values returned by getConfigurations.
type GetConfigurationsResultOutput struct{ *pulumi.OutputState }

func (GetConfigurationsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetConfigurationsResult)(nil)).Elem()
}

func (o GetConfigurationsResultOutput) ToGetConfigurationsResultOutput() GetConfigurationsResultOutput {
	return o
}

func (o GetConfigurationsResultOutput) ToGetConfigurationsResultOutputWithContext(ctx context.Context) GetConfigurationsResultOutput {
	return o
}

// A config list block defined as below.
func (o GetConfigurationsResultOutput) Configs() GetConfigurationsConfigArrayOutput {
	return o.ApplyT(func(v GetConfigurationsResult) []GetConfigurationsConfig { return v.Configs }).(GetConfigurationsConfigArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetConfigurationsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetConfigurationsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetConfigurationsResultOutput) NameFilterRegex() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetConfigurationsResult) *string { return v.NameFilterRegex }).(pulumi.StringPtrOutput)
}

func (o GetConfigurationsResultOutput) ProductId() pulumi.StringOutput {
	return o.ApplyT(func(v GetConfigurationsResult) string { return v.ProductId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetConfigurationsResultOutput{})
}
