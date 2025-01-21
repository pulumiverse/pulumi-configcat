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

// Creates and manages a **Config**. [What is a Config in ConfigCat?](https://configcat.com/docs/main-concepts)
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
//			productId := cfg.Require("productId")
//			myConfig, err := configcat.NewConfiguration(ctx, "my_config", &configcat.ConfigurationArgs{
//				ProductId:         pulumi.String(productId),
//				Name:              pulumi.String("My config"),
//				Description:       pulumi.String("My config description"),
//				Order:             pulumi.Int(0),
//				EvaluationVersion: pulumi.String("v1"),
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("configId", myConfig.ID())
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Configs can be imported using the ConfigId. Get the ConfigId using the [List Configs API](https://api.configcat.com/docs/#tag/Configs/operation/get-configs) for example.
//
// ```sh
// $ pulumi import configcat:index/configuration:Configuration example 08d86d63-2726-47cd-8bfc-59608ecb91e2
// ```
type Configuration struct {
	pulumi.CustomResourceState

	// The description of the Config.
	Description pulumi.StringOutput `pulumi:"description"`
	// The evaluation version of the Config. Possible values: `v1`, `v2`. Default value: `v1`. Using `v2` enables the new features of [Config V2](https://configcat.com/docs/advanced/config-v2).
	EvaluationVersion pulumi.StringOutput `pulumi:"evaluationVersion"`
	// The name of the Config.
	Name pulumi.StringOutput `pulumi:"name"`
	// The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
	Order pulumi.IntOutput `pulumi:"order"`
	// The ID of the Product.
	ProductId pulumi.StringOutput `pulumi:"productId"`
}

// NewConfiguration registers a new resource with the given unique name, arguments, and options.
func NewConfiguration(ctx *pulumi.Context,
	name string, args *ConfigurationArgs, opts ...pulumi.ResourceOption) (*Configuration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Order == nil {
		return nil, errors.New("invalid value for required argument 'Order'")
	}
	if args.ProductId == nil {
		return nil, errors.New("invalid value for required argument 'ProductId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Configuration
	err := ctx.RegisterResource("configcat:index/configuration:Configuration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfiguration gets an existing Configuration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigurationState, opts ...pulumi.ResourceOption) (*Configuration, error) {
	var resource Configuration
	err := ctx.ReadResource("configcat:index/configuration:Configuration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Configuration resources.
type configurationState struct {
	// The description of the Config.
	Description *string `pulumi:"description"`
	// The evaluation version of the Config. Possible values: `v1`, `v2`. Default value: `v1`. Using `v2` enables the new features of [Config V2](https://configcat.com/docs/advanced/config-v2).
	EvaluationVersion *string `pulumi:"evaluationVersion"`
	// The name of the Config.
	Name *string `pulumi:"name"`
	// The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
	Order *int `pulumi:"order"`
	// The ID of the Product.
	ProductId *string `pulumi:"productId"`
}

type ConfigurationState struct {
	// The description of the Config.
	Description pulumi.StringPtrInput
	// The evaluation version of the Config. Possible values: `v1`, `v2`. Default value: `v1`. Using `v2` enables the new features of [Config V2](https://configcat.com/docs/advanced/config-v2).
	EvaluationVersion pulumi.StringPtrInput
	// The name of the Config.
	Name pulumi.StringPtrInput
	// The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
	Order pulumi.IntPtrInput
	// The ID of the Product.
	ProductId pulumi.StringPtrInput
}

func (ConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationState)(nil)).Elem()
}

type configurationArgs struct {
	// The description of the Config.
	Description *string `pulumi:"description"`
	// The evaluation version of the Config. Possible values: `v1`, `v2`. Default value: `v1`. Using `v2` enables the new features of [Config V2](https://configcat.com/docs/advanced/config-v2).
	EvaluationVersion *string `pulumi:"evaluationVersion"`
	// The name of the Config.
	Name *string `pulumi:"name"`
	// The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
	Order int `pulumi:"order"`
	// The ID of the Product.
	ProductId string `pulumi:"productId"`
}

// The set of arguments for constructing a Configuration resource.
type ConfigurationArgs struct {
	// The description of the Config.
	Description pulumi.StringPtrInput
	// The evaluation version of the Config. Possible values: `v1`, `v2`. Default value: `v1`. Using `v2` enables the new features of [Config V2](https://configcat.com/docs/advanced/config-v2).
	EvaluationVersion pulumi.StringPtrInput
	// The name of the Config.
	Name pulumi.StringPtrInput
	// The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
	Order pulumi.IntInput
	// The ID of the Product.
	ProductId pulumi.StringInput
}

func (ConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationArgs)(nil)).Elem()
}

type ConfigurationInput interface {
	pulumi.Input

	ToConfigurationOutput() ConfigurationOutput
	ToConfigurationOutputWithContext(ctx context.Context) ConfigurationOutput
}

func (*Configuration) ElementType() reflect.Type {
	return reflect.TypeOf((**Configuration)(nil)).Elem()
}

func (i *Configuration) ToConfigurationOutput() ConfigurationOutput {
	return i.ToConfigurationOutputWithContext(context.Background())
}

func (i *Configuration) ToConfigurationOutputWithContext(ctx context.Context) ConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigurationOutput)
}

// ConfigurationArrayInput is an input type that accepts ConfigurationArray and ConfigurationArrayOutput values.
// You can construct a concrete instance of `ConfigurationArrayInput` via:
//
//	ConfigurationArray{ ConfigurationArgs{...} }
type ConfigurationArrayInput interface {
	pulumi.Input

	ToConfigurationArrayOutput() ConfigurationArrayOutput
	ToConfigurationArrayOutputWithContext(context.Context) ConfigurationArrayOutput
}

type ConfigurationArray []ConfigurationInput

func (ConfigurationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Configuration)(nil)).Elem()
}

func (i ConfigurationArray) ToConfigurationArrayOutput() ConfigurationArrayOutput {
	return i.ToConfigurationArrayOutputWithContext(context.Background())
}

func (i ConfigurationArray) ToConfigurationArrayOutputWithContext(ctx context.Context) ConfigurationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigurationArrayOutput)
}

// ConfigurationMapInput is an input type that accepts ConfigurationMap and ConfigurationMapOutput values.
// You can construct a concrete instance of `ConfigurationMapInput` via:
//
//	ConfigurationMap{ "key": ConfigurationArgs{...} }
type ConfigurationMapInput interface {
	pulumi.Input

	ToConfigurationMapOutput() ConfigurationMapOutput
	ToConfigurationMapOutputWithContext(context.Context) ConfigurationMapOutput
}

type ConfigurationMap map[string]ConfigurationInput

func (ConfigurationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Configuration)(nil)).Elem()
}

func (i ConfigurationMap) ToConfigurationMapOutput() ConfigurationMapOutput {
	return i.ToConfigurationMapOutputWithContext(context.Background())
}

func (i ConfigurationMap) ToConfigurationMapOutputWithContext(ctx context.Context) ConfigurationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigurationMapOutput)
}

type ConfigurationOutput struct{ *pulumi.OutputState }

func (ConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Configuration)(nil)).Elem()
}

func (o ConfigurationOutput) ToConfigurationOutput() ConfigurationOutput {
	return o
}

func (o ConfigurationOutput) ToConfigurationOutputWithContext(ctx context.Context) ConfigurationOutput {
	return o
}

// The description of the Config.
func (o ConfigurationOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Configuration) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// The evaluation version of the Config. Possible values: `v1`, `v2`. Default value: `v1`. Using `v2` enables the new features of [Config V2](https://configcat.com/docs/advanced/config-v2).
func (o ConfigurationOutput) EvaluationVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *Configuration) pulumi.StringOutput { return v.EvaluationVersion }).(pulumi.StringOutput)
}

// The name of the Config.
func (o ConfigurationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Configuration) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in alphabetical order.
func (o ConfigurationOutput) Order() pulumi.IntOutput {
	return o.ApplyT(func(v *Configuration) pulumi.IntOutput { return v.Order }).(pulumi.IntOutput)
}

// The ID of the Product.
func (o ConfigurationOutput) ProductId() pulumi.StringOutput {
	return o.ApplyT(func(v *Configuration) pulumi.StringOutput { return v.ProductId }).(pulumi.StringOutput)
}

type ConfigurationArrayOutput struct{ *pulumi.OutputState }

func (ConfigurationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Configuration)(nil)).Elem()
}

func (o ConfigurationArrayOutput) ToConfigurationArrayOutput() ConfigurationArrayOutput {
	return o
}

func (o ConfigurationArrayOutput) ToConfigurationArrayOutputWithContext(ctx context.Context) ConfigurationArrayOutput {
	return o
}

func (o ConfigurationArrayOutput) Index(i pulumi.IntInput) ConfigurationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Configuration {
		return vs[0].([]*Configuration)[vs[1].(int)]
	}).(ConfigurationOutput)
}

type ConfigurationMapOutput struct{ *pulumi.OutputState }

func (ConfigurationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Configuration)(nil)).Elem()
}

func (o ConfigurationMapOutput) ToConfigurationMapOutput() ConfigurationMapOutput {
	return o
}

func (o ConfigurationMapOutput) ToConfigurationMapOutputWithContext(ctx context.Context) ConfigurationMapOutput {
	return o
}

func (o ConfigurationMapOutput) MapIndex(k pulumi.StringInput) ConfigurationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Configuration {
		return vs[0].(map[string]*Configuration)[vs[1].(string)]
	}).(ConfigurationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigurationInput)(nil)).Elem(), &Configuration{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigurationArrayInput)(nil)).Elem(), ConfigurationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigurationMapInput)(nil)).Elem(), ConfigurationMap{})
	pulumi.RegisterOutputType(ConfigurationOutput{})
	pulumi.RegisterOutputType(ConfigurationArrayOutput{})
	pulumi.RegisterOutputType(ConfigurationMapOutput{})
}
