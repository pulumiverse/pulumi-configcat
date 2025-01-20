// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/v2/go/configcat/internal"
)

// ## # Environment Resource
//
// Creates and manages an **Environment**. [What is an Environment in ConfigCat?](https://configcat.com/docs/main-concepts)
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
//			myEnvironment, err := configcat.NewEnvironment(ctx, "my_environment", &configcat.EnvironmentArgs{
//				ProductId:   pulumi.String(myProducts.Products[0].ProductId),
//				Name:        pulumi.String("Staging"),
//				Description: pulumi.String("Staging description"),
//				Color:       pulumi.String("blue"),
//				Order:       pulumi.Int(0),
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("environmentId", myEnvironment.ID())
//			return nil
//		})
//	}
//
// ```
//
// ## Endpoints used
//
// * [Get Environment](https://api.configcat.com/docs/#tag/Environments/operation/get-environment)
// * [Create Environment](https://api.configcat.com/docs/#tag/Environments/operation/create-environment)
// * [Update Environment](https://api.configcat.com/docs/#tag/Environments/operation/update-environment)
// * [Delete Environment](https://api.configcat.com/docs/#tag/Environments/operation/delete-environment)
//
// ## Import
//
// Environments can be imported using the EnvironmentId. Get the EnvironmentId using the [List Environments API](https://api.configcat.com/docs/#tag/Environments/operation/get-environments) for example.
//
// ```sh
// $ pulumi import configcat:index/environment:Environment example 08d86d63-2726-47cd-8bfc-59608ecb91e2
// ```
// Read more about importing.
type Environment struct {
	pulumi.CustomResourceState

	// The color (HTML color code) of the Environment.
	Color pulumi.StringPtrOutput `pulumi:"color"`
	// The description of the Environment.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The name of the Environment.
	Name pulumi.StringOutput `pulumi:"name"`
	// The order of the Environment within a Product (zero-based). If multiple Environments has the same order, they are displayed in alphabetical order.
	Order pulumi.IntOutput `pulumi:"order"`
	// The ID of the Product.
	ProductId pulumi.StringOutput `pulumi:"productId"`
}

// NewEnvironment registers a new resource with the given unique name, arguments, and options.
func NewEnvironment(ctx *pulumi.Context,
	name string, args *EnvironmentArgs, opts ...pulumi.ResourceOption) (*Environment, error) {
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
	var resource Environment
	err := ctx.RegisterResource("configcat:index/environment:Environment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEnvironment gets an existing Environment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEnvironment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EnvironmentState, opts ...pulumi.ResourceOption) (*Environment, error) {
	var resource Environment
	err := ctx.ReadResource("configcat:index/environment:Environment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Environment resources.
type environmentState struct {
	// The color (HTML color code) of the Environment.
	Color *string `pulumi:"color"`
	// The description of the Environment.
	Description *string `pulumi:"description"`
	// The name of the Environment.
	Name *string `pulumi:"name"`
	// The order of the Environment within a Product (zero-based). If multiple Environments has the same order, they are displayed in alphabetical order.
	Order *int `pulumi:"order"`
	// The ID of the Product.
	ProductId *string `pulumi:"productId"`
}

type EnvironmentState struct {
	// The color (HTML color code) of the Environment.
	Color pulumi.StringPtrInput
	// The description of the Environment.
	Description pulumi.StringPtrInput
	// The name of the Environment.
	Name pulumi.StringPtrInput
	// The order of the Environment within a Product (zero-based). If multiple Environments has the same order, they are displayed in alphabetical order.
	Order pulumi.IntPtrInput
	// The ID of the Product.
	ProductId pulumi.StringPtrInput
}

func (EnvironmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*environmentState)(nil)).Elem()
}

type environmentArgs struct {
	// The color (HTML color code) of the Environment.
	Color *string `pulumi:"color"`
	// The description of the Environment.
	Description *string `pulumi:"description"`
	// The name of the Environment.
	Name *string `pulumi:"name"`
	// The order of the Environment within a Product (zero-based). If multiple Environments has the same order, they are displayed in alphabetical order.
	Order int `pulumi:"order"`
	// The ID of the Product.
	ProductId string `pulumi:"productId"`
}

// The set of arguments for constructing a Environment resource.
type EnvironmentArgs struct {
	// The color (HTML color code) of the Environment.
	Color pulumi.StringPtrInput
	// The description of the Environment.
	Description pulumi.StringPtrInput
	// The name of the Environment.
	Name pulumi.StringPtrInput
	// The order of the Environment within a Product (zero-based). If multiple Environments has the same order, they are displayed in alphabetical order.
	Order pulumi.IntInput
	// The ID of the Product.
	ProductId pulumi.StringInput
}

func (EnvironmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*environmentArgs)(nil)).Elem()
}

type EnvironmentInput interface {
	pulumi.Input

	ToEnvironmentOutput() EnvironmentOutput
	ToEnvironmentOutputWithContext(ctx context.Context) EnvironmentOutput
}

func (*Environment) ElementType() reflect.Type {
	return reflect.TypeOf((**Environment)(nil)).Elem()
}

func (i *Environment) ToEnvironmentOutput() EnvironmentOutput {
	return i.ToEnvironmentOutputWithContext(context.Background())
}

func (i *Environment) ToEnvironmentOutputWithContext(ctx context.Context) EnvironmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnvironmentOutput)
}

// EnvironmentArrayInput is an input type that accepts EnvironmentArray and EnvironmentArrayOutput values.
// You can construct a concrete instance of `EnvironmentArrayInput` via:
//
//	EnvironmentArray{ EnvironmentArgs{...} }
type EnvironmentArrayInput interface {
	pulumi.Input

	ToEnvironmentArrayOutput() EnvironmentArrayOutput
	ToEnvironmentArrayOutputWithContext(context.Context) EnvironmentArrayOutput
}

type EnvironmentArray []EnvironmentInput

func (EnvironmentArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Environment)(nil)).Elem()
}

func (i EnvironmentArray) ToEnvironmentArrayOutput() EnvironmentArrayOutput {
	return i.ToEnvironmentArrayOutputWithContext(context.Background())
}

func (i EnvironmentArray) ToEnvironmentArrayOutputWithContext(ctx context.Context) EnvironmentArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnvironmentArrayOutput)
}

// EnvironmentMapInput is an input type that accepts EnvironmentMap and EnvironmentMapOutput values.
// You can construct a concrete instance of `EnvironmentMapInput` via:
//
//	EnvironmentMap{ "key": EnvironmentArgs{...} }
type EnvironmentMapInput interface {
	pulumi.Input

	ToEnvironmentMapOutput() EnvironmentMapOutput
	ToEnvironmentMapOutputWithContext(context.Context) EnvironmentMapOutput
}

type EnvironmentMap map[string]EnvironmentInput

func (EnvironmentMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Environment)(nil)).Elem()
}

func (i EnvironmentMap) ToEnvironmentMapOutput() EnvironmentMapOutput {
	return i.ToEnvironmentMapOutputWithContext(context.Background())
}

func (i EnvironmentMap) ToEnvironmentMapOutputWithContext(ctx context.Context) EnvironmentMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnvironmentMapOutput)
}

type EnvironmentOutput struct{ *pulumi.OutputState }

func (EnvironmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Environment)(nil)).Elem()
}

func (o EnvironmentOutput) ToEnvironmentOutput() EnvironmentOutput {
	return o
}

func (o EnvironmentOutput) ToEnvironmentOutputWithContext(ctx context.Context) EnvironmentOutput {
	return o
}

// The color (HTML color code) of the Environment.
func (o EnvironmentOutput) Color() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Environment) pulumi.StringPtrOutput { return v.Color }).(pulumi.StringPtrOutput)
}

// The description of the Environment.
func (o EnvironmentOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Environment) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The name of the Environment.
func (o EnvironmentOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Environment) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The order of the Environment within a Product (zero-based). If multiple Environments has the same order, they are displayed in alphabetical order.
func (o EnvironmentOutput) Order() pulumi.IntOutput {
	return o.ApplyT(func(v *Environment) pulumi.IntOutput { return v.Order }).(pulumi.IntOutput)
}

// The ID of the Product.
func (o EnvironmentOutput) ProductId() pulumi.StringOutput {
	return o.ApplyT(func(v *Environment) pulumi.StringOutput { return v.ProductId }).(pulumi.StringOutput)
}

type EnvironmentArrayOutput struct{ *pulumi.OutputState }

func (EnvironmentArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Environment)(nil)).Elem()
}

func (o EnvironmentArrayOutput) ToEnvironmentArrayOutput() EnvironmentArrayOutput {
	return o
}

func (o EnvironmentArrayOutput) ToEnvironmentArrayOutputWithContext(ctx context.Context) EnvironmentArrayOutput {
	return o
}

func (o EnvironmentArrayOutput) Index(i pulumi.IntInput) EnvironmentOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Environment {
		return vs[0].([]*Environment)[vs[1].(int)]
	}).(EnvironmentOutput)
}

type EnvironmentMapOutput struct{ *pulumi.OutputState }

func (EnvironmentMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Environment)(nil)).Elem()
}

func (o EnvironmentMapOutput) ToEnvironmentMapOutput() EnvironmentMapOutput {
	return o
}

func (o EnvironmentMapOutput) ToEnvironmentMapOutputWithContext(ctx context.Context) EnvironmentMapOutput {
	return o
}

func (o EnvironmentMapOutput) MapIndex(k pulumi.StringInput) EnvironmentOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Environment {
		return vs[0].(map[string]*Environment)[vs[1].(string)]
	}).(EnvironmentOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentInput)(nil)).Elem(), &Environment{})
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentArrayInput)(nil)).Elem(), EnvironmentArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*EnvironmentMapInput)(nil)).Elem(), EnvironmentMap{})
	pulumi.RegisterOutputType(EnvironmentOutput{})
	pulumi.RegisterOutputType(EnvironmentArrayOutput{})
	pulumi.RegisterOutputType(EnvironmentMapOutput{})
}
