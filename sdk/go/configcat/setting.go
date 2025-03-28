// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/v5/go/configcat/internal"
)

// Creates and manages a **Feature Flag or Setting**. [What is a Feature Flag or Setting in ConfigCat?](https://configcat.com/docs/main-concepts)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
//	"github.com/pulumiverse/pulumi-configcat/sdk/v5/go/configcat"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			cfg := config.New(ctx, "")
//			configId := cfg.Require("configId")
//			mySetting, err := configcat.NewSetting(ctx, "my_setting", &configcat.SettingArgs{
//				ConfigId:    pulumi.String(configId),
//				Key:         pulumi.String("isAwesomeFeatureEnabled"),
//				Name:        pulumi.String("My awesome feature flag"),
//				Hint:        pulumi.String("This is the hint for my awesome feature flag"),
//				SettingType: pulumi.String("boolean"),
//				Order:       pulumi.Int(0),
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("settingId", mySetting.ID())
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Feature Flags/Settings can be imported using the SettingId. Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).
//
// ```sh
// $ pulumi import configcat:index/setting:Setting example 1234
// ```
type Setting struct {
	pulumi.CustomResourceState

	// The ID of the Config.
	ConfigId pulumi.StringOutput `pulumi:"configId"`
	// The hint of the Feature Flag or Setting.
	Hint pulumi.StringOutput `pulumi:"hint"`
	// The key of the Feature Flag or Setting.
	Key pulumi.StringOutput `pulumi:"key"`
	// The name of the Feature Flag or Setting.
	Name pulumi.StringOutput `pulumi:"name"`
	// The order of the Feature Flag or Setting within a Product (zero-based). If multiple Feature Flags or Settings has the same order, they are displayed in alphabetical order.
	Order pulumi.IntOutput `pulumi:"order"`
	// The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`. Default: `boolean`.
	SettingType pulumi.StringOutput `pulumi:"settingType"`
}

// NewSetting registers a new resource with the given unique name, arguments, and options.
func NewSetting(ctx *pulumi.Context,
	name string, args *SettingArgs, opts ...pulumi.ResourceOption) (*Setting, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConfigId == nil {
		return nil, errors.New("invalid value for required argument 'ConfigId'")
	}
	if args.Key == nil {
		return nil, errors.New("invalid value for required argument 'Key'")
	}
	if args.Order == nil {
		return nil, errors.New("invalid value for required argument 'Order'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Setting
	err := ctx.RegisterResource("configcat:index/setting:Setting", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSetting gets an existing Setting resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSetting(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SettingState, opts ...pulumi.ResourceOption) (*Setting, error) {
	var resource Setting
	err := ctx.ReadResource("configcat:index/setting:Setting", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Setting resources.
type settingState struct {
	// The ID of the Config.
	ConfigId *string `pulumi:"configId"`
	// The hint of the Feature Flag or Setting.
	Hint *string `pulumi:"hint"`
	// The key of the Feature Flag or Setting.
	Key *string `pulumi:"key"`
	// The name of the Feature Flag or Setting.
	Name *string `pulumi:"name"`
	// The order of the Feature Flag or Setting within a Product (zero-based). If multiple Feature Flags or Settings has the same order, they are displayed in alphabetical order.
	Order *int `pulumi:"order"`
	// The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`. Default: `boolean`.
	SettingType *string `pulumi:"settingType"`
}

type SettingState struct {
	// The ID of the Config.
	ConfigId pulumi.StringPtrInput
	// The hint of the Feature Flag or Setting.
	Hint pulumi.StringPtrInput
	// The key of the Feature Flag or Setting.
	Key pulumi.StringPtrInput
	// The name of the Feature Flag or Setting.
	Name pulumi.StringPtrInput
	// The order of the Feature Flag or Setting within a Product (zero-based). If multiple Feature Flags or Settings has the same order, they are displayed in alphabetical order.
	Order pulumi.IntPtrInput
	// The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`. Default: `boolean`.
	SettingType pulumi.StringPtrInput
}

func (SettingState) ElementType() reflect.Type {
	return reflect.TypeOf((*settingState)(nil)).Elem()
}

type settingArgs struct {
	// The ID of the Config.
	ConfigId string `pulumi:"configId"`
	// The hint of the Feature Flag or Setting.
	Hint *string `pulumi:"hint"`
	// The key of the Feature Flag or Setting.
	Key string `pulumi:"key"`
	// The name of the Feature Flag or Setting.
	Name *string `pulumi:"name"`
	// The order of the Feature Flag or Setting within a Product (zero-based). If multiple Feature Flags or Settings has the same order, they are displayed in alphabetical order.
	Order int `pulumi:"order"`
	// The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`. Default: `boolean`.
	SettingType *string `pulumi:"settingType"`
}

// The set of arguments for constructing a Setting resource.
type SettingArgs struct {
	// The ID of the Config.
	ConfigId pulumi.StringInput
	// The hint of the Feature Flag or Setting.
	Hint pulumi.StringPtrInput
	// The key of the Feature Flag or Setting.
	Key pulumi.StringInput
	// The name of the Feature Flag or Setting.
	Name pulumi.StringPtrInput
	// The order of the Feature Flag or Setting within a Product (zero-based). If multiple Feature Flags or Settings has the same order, they are displayed in alphabetical order.
	Order pulumi.IntInput
	// The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`. Default: `boolean`.
	SettingType pulumi.StringPtrInput
}

func (SettingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*settingArgs)(nil)).Elem()
}

type SettingInput interface {
	pulumi.Input

	ToSettingOutput() SettingOutput
	ToSettingOutputWithContext(ctx context.Context) SettingOutput
}

func (*Setting) ElementType() reflect.Type {
	return reflect.TypeOf((**Setting)(nil)).Elem()
}

func (i *Setting) ToSettingOutput() SettingOutput {
	return i.ToSettingOutputWithContext(context.Background())
}

func (i *Setting) ToSettingOutputWithContext(ctx context.Context) SettingOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SettingOutput)
}

// SettingArrayInput is an input type that accepts SettingArray and SettingArrayOutput values.
// You can construct a concrete instance of `SettingArrayInput` via:
//
//	SettingArray{ SettingArgs{...} }
type SettingArrayInput interface {
	pulumi.Input

	ToSettingArrayOutput() SettingArrayOutput
	ToSettingArrayOutputWithContext(context.Context) SettingArrayOutput
}

type SettingArray []SettingInput

func (SettingArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Setting)(nil)).Elem()
}

func (i SettingArray) ToSettingArrayOutput() SettingArrayOutput {
	return i.ToSettingArrayOutputWithContext(context.Background())
}

func (i SettingArray) ToSettingArrayOutputWithContext(ctx context.Context) SettingArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SettingArrayOutput)
}

// SettingMapInput is an input type that accepts SettingMap and SettingMapOutput values.
// You can construct a concrete instance of `SettingMapInput` via:
//
//	SettingMap{ "key": SettingArgs{...} }
type SettingMapInput interface {
	pulumi.Input

	ToSettingMapOutput() SettingMapOutput
	ToSettingMapOutputWithContext(context.Context) SettingMapOutput
}

type SettingMap map[string]SettingInput

func (SettingMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Setting)(nil)).Elem()
}

func (i SettingMap) ToSettingMapOutput() SettingMapOutput {
	return i.ToSettingMapOutputWithContext(context.Background())
}

func (i SettingMap) ToSettingMapOutputWithContext(ctx context.Context) SettingMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SettingMapOutput)
}

type SettingOutput struct{ *pulumi.OutputState }

func (SettingOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Setting)(nil)).Elem()
}

func (o SettingOutput) ToSettingOutput() SettingOutput {
	return o
}

func (o SettingOutput) ToSettingOutputWithContext(ctx context.Context) SettingOutput {
	return o
}

// The ID of the Config.
func (o SettingOutput) ConfigId() pulumi.StringOutput {
	return o.ApplyT(func(v *Setting) pulumi.StringOutput { return v.ConfigId }).(pulumi.StringOutput)
}

// The hint of the Feature Flag or Setting.
func (o SettingOutput) Hint() pulumi.StringOutput {
	return o.ApplyT(func(v *Setting) pulumi.StringOutput { return v.Hint }).(pulumi.StringOutput)
}

// The key of the Feature Flag or Setting.
func (o SettingOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *Setting) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

// The name of the Feature Flag or Setting.
func (o SettingOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Setting) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The order of the Feature Flag or Setting within a Product (zero-based). If multiple Feature Flags or Settings has the same order, they are displayed in alphabetical order.
func (o SettingOutput) Order() pulumi.IntOutput {
	return o.ApplyT(func(v *Setting) pulumi.IntOutput { return v.Order }).(pulumi.IntOutput)
}

// The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`. Default: `boolean`.
func (o SettingOutput) SettingType() pulumi.StringOutput {
	return o.ApplyT(func(v *Setting) pulumi.StringOutput { return v.SettingType }).(pulumi.StringOutput)
}

type SettingArrayOutput struct{ *pulumi.OutputState }

func (SettingArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Setting)(nil)).Elem()
}

func (o SettingArrayOutput) ToSettingArrayOutput() SettingArrayOutput {
	return o
}

func (o SettingArrayOutput) ToSettingArrayOutputWithContext(ctx context.Context) SettingArrayOutput {
	return o
}

func (o SettingArrayOutput) Index(i pulumi.IntInput) SettingOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Setting {
		return vs[0].([]*Setting)[vs[1].(int)]
	}).(SettingOutput)
}

type SettingMapOutput struct{ *pulumi.OutputState }

func (SettingMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Setting)(nil)).Elem()
}

func (o SettingMapOutput) ToSettingMapOutput() SettingMapOutput {
	return o
}

func (o SettingMapOutput) ToSettingMapOutputWithContext(ctx context.Context) SettingMapOutput {
	return o
}

func (o SettingMapOutput) MapIndex(k pulumi.StringInput) SettingOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Setting {
		return vs[0].(map[string]*Setting)[vs[1].(string)]
	}).(SettingOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SettingInput)(nil)).Elem(), &Setting{})
	pulumi.RegisterInputType(reflect.TypeOf((*SettingArrayInput)(nil)).Elem(), SettingArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SettingMapInput)(nil)).Elem(), SettingMap{})
	pulumi.RegisterOutputType(SettingOutput{})
	pulumi.RegisterOutputType(SettingArrayOutput{})
	pulumi.RegisterOutputType(SettingMapOutput{})
}
