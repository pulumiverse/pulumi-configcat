// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/v5/go/configcat/internal"
)

func GetSdkKeys(ctx *pulumi.Context, args *GetSdkKeysArgs, opts ...pulumi.InvokeOption) (*GetSdkKeysResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetSdkKeysResult
	err := ctx.Invoke("configcat:index/getSdkKeys:getSdkKeys", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSdkKeys.
type GetSdkKeysArgs struct {
	ConfigId      string `pulumi:"configId"`
	EnvironmentId string `pulumi:"environmentId"`
}

// A collection of values returned by getSdkKeys.
type GetSdkKeysResult struct {
	ConfigId      string `pulumi:"configId"`
	EnvironmentId string `pulumi:"environmentId"`
	Id            string `pulumi:"id"`
	Primary       string `pulumi:"primary"`
	Secondary     string `pulumi:"secondary"`
}

func GetSdkKeysOutput(ctx *pulumi.Context, args GetSdkKeysOutputArgs, opts ...pulumi.InvokeOption) GetSdkKeysResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetSdkKeysResultOutput, error) {
			args := v.(GetSdkKeysArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("configcat:index/getSdkKeys:getSdkKeys", args, GetSdkKeysResultOutput{}, options).(GetSdkKeysResultOutput), nil
		}).(GetSdkKeysResultOutput)
}

// A collection of arguments for invoking getSdkKeys.
type GetSdkKeysOutputArgs struct {
	ConfigId      pulumi.StringInput `pulumi:"configId"`
	EnvironmentId pulumi.StringInput `pulumi:"environmentId"`
}

func (GetSdkKeysOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSdkKeysArgs)(nil)).Elem()
}

// A collection of values returned by getSdkKeys.
type GetSdkKeysResultOutput struct{ *pulumi.OutputState }

func (GetSdkKeysResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSdkKeysResult)(nil)).Elem()
}

func (o GetSdkKeysResultOutput) ToGetSdkKeysResultOutput() GetSdkKeysResultOutput {
	return o
}

func (o GetSdkKeysResultOutput) ToGetSdkKeysResultOutputWithContext(ctx context.Context) GetSdkKeysResultOutput {
	return o
}

func (o GetSdkKeysResultOutput) ConfigId() pulumi.StringOutput {
	return o.ApplyT(func(v GetSdkKeysResult) string { return v.ConfigId }).(pulumi.StringOutput)
}

func (o GetSdkKeysResultOutput) EnvironmentId() pulumi.StringOutput {
	return o.ApplyT(func(v GetSdkKeysResult) string { return v.EnvironmentId }).(pulumi.StringOutput)
}

func (o GetSdkKeysResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetSdkKeysResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetSdkKeysResultOutput) Primary() pulumi.StringOutput {
	return o.ApplyT(func(v GetSdkKeysResult) string { return v.Primary }).(pulumi.StringOutput)
}

func (o GetSdkKeysResultOutput) Secondary() pulumi.StringOutput {
	return o.ApplyT(func(v GetSdkKeysResult) string { return v.Secondary }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetSdkKeysResultOutput{})
}
