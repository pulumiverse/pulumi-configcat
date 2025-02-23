// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/v5/go/configcat/internal"
)

// Use this data source to access information about existing **Organizations**. [What is an Organization in ConfigCat?](https://configcat.com/docs/main-concepts)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-configcat/sdk/v5/go/configcat"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			myOrganizations, err := configcat.GetOrganizations(ctx, &configcat.GetOrganizationsArgs{
//				NameFilterRegex: pulumi.StringRef("ConfigCat"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("organizationId", myOrganizations.Organizations[0].OrganizationId)
//			return nil
//		})
//	}
//
// ```
func GetOrganizations(ctx *pulumi.Context, args *GetOrganizationsArgs, opts ...pulumi.InvokeOption) (*GetOrganizationsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetOrganizationsResult
	err := ctx.Invoke("configcat:index/getOrganizations:getOrganizations", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getOrganizations.
type GetOrganizationsArgs struct {
	// Filter the Organizations by name.
	NameFilterRegex *string `pulumi:"nameFilterRegex"`
}

// A collection of values returned by getOrganizations.
type GetOrganizationsResult struct {
	// Internal ID of the data source. Do not use.
	Id string `pulumi:"id"`
	// Filter the Organizations by name.
	NameFilterRegex *string                        `pulumi:"nameFilterRegex"`
	Organizations   []GetOrganizationsOrganization `pulumi:"organizations"`
}

func GetOrganizationsOutput(ctx *pulumi.Context, args GetOrganizationsOutputArgs, opts ...pulumi.InvokeOption) GetOrganizationsResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetOrganizationsResultOutput, error) {
			args := v.(GetOrganizationsArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("configcat:index/getOrganizations:getOrganizations", args, GetOrganizationsResultOutput{}, options).(GetOrganizationsResultOutput), nil
		}).(GetOrganizationsResultOutput)
}

// A collection of arguments for invoking getOrganizations.
type GetOrganizationsOutputArgs struct {
	// Filter the Organizations by name.
	NameFilterRegex pulumi.StringPtrInput `pulumi:"nameFilterRegex"`
}

func (GetOrganizationsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetOrganizationsArgs)(nil)).Elem()
}

// A collection of values returned by getOrganizations.
type GetOrganizationsResultOutput struct{ *pulumi.OutputState }

func (GetOrganizationsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetOrganizationsResult)(nil)).Elem()
}

func (o GetOrganizationsResultOutput) ToGetOrganizationsResultOutput() GetOrganizationsResultOutput {
	return o
}

func (o GetOrganizationsResultOutput) ToGetOrganizationsResultOutputWithContext(ctx context.Context) GetOrganizationsResultOutput {
	return o
}

// Internal ID of the data source. Do not use.
func (o GetOrganizationsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetOrganizationsResult) string { return v.Id }).(pulumi.StringOutput)
}

// Filter the Organizations by name.
func (o GetOrganizationsResultOutput) NameFilterRegex() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetOrganizationsResult) *string { return v.NameFilterRegex }).(pulumi.StringPtrOutput)
}

func (o GetOrganizationsResultOutput) Organizations() GetOrganizationsOrganizationArrayOutput {
	return o.ApplyT(func(v GetOrganizationsResult) []GetOrganizationsOrganization { return v.Organizations }).(GetOrganizationsOrganizationArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetOrganizationsResultOutput{})
}
