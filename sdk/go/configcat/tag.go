// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/v3/go/configcat/internal"
)

// ## # Tag Resource
//
// Creates and manages a **Tag**.
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
//			myTag, err := configcat.NewTag(ctx, "my_tag", &configcat.TagArgs{
//				ProductId: pulumi.String(myProducts.Products[0].ProductId),
//				Name:      pulumi.String("Created by Terraform"),
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("tagId", myTag.ID())
//			return nil
//		})
//	}
//
// ```
//
// ## Endpoints used
//
// * [Get Tag](https://api.configcat.com/docs/#tag/Tags/operation/get-tag)
// * [Create Tag](https://api.configcat.com/docs/#tag/Tags/operation/create-tag)
// * [Update Tag](https://api.configcat.com/docs/#tag/Tags/operation/update-tag)
// * [Delete Tag](https://api.configcat.com/docs/#tag/Tags/operation/delete-tag)
//
// ## Import
//
// Tags can be imported using the TagId. Get the TagId using e.g. the [List Tags API](https://api.configcat.com/docs/#tag/Tags/operation/get-tags).
//
// ```sh
// $ pulumi import configcat:index/tag:Tag example 1234
// ```
// Read more about importing.
type Tag struct {
	pulumi.CustomResourceState

	// Default: `panther`. The color of the Tag. Valid values: `panther`, `whale`, `salmon`, `lizard`, `canary`, `koala`.
	Color pulumi.StringPtrOutput `pulumi:"color"`
	// The name of the Tag.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the Product.
	ProductId pulumi.StringOutput `pulumi:"productId"`
}

// NewTag registers a new resource with the given unique name, arguments, and options.
func NewTag(ctx *pulumi.Context,
	name string, args *TagArgs, opts ...pulumi.ResourceOption) (*Tag, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ProductId == nil {
		return nil, errors.New("invalid value for required argument 'ProductId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Tag
	err := ctx.RegisterResource("configcat:index/tag:Tag", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTag gets an existing Tag resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTag(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TagState, opts ...pulumi.ResourceOption) (*Tag, error) {
	var resource Tag
	err := ctx.ReadResource("configcat:index/tag:Tag", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Tag resources.
type tagState struct {
	// Default: `panther`. The color of the Tag. Valid values: `panther`, `whale`, `salmon`, `lizard`, `canary`, `koala`.
	Color *string `pulumi:"color"`
	// The name of the Tag.
	Name *string `pulumi:"name"`
	// The ID of the Product.
	ProductId *string `pulumi:"productId"`
}

type TagState struct {
	// Default: `panther`. The color of the Tag. Valid values: `panther`, `whale`, `salmon`, `lizard`, `canary`, `koala`.
	Color pulumi.StringPtrInput
	// The name of the Tag.
	Name pulumi.StringPtrInput
	// The ID of the Product.
	ProductId pulumi.StringPtrInput
}

func (TagState) ElementType() reflect.Type {
	return reflect.TypeOf((*tagState)(nil)).Elem()
}

type tagArgs struct {
	// Default: `panther`. The color of the Tag. Valid values: `panther`, `whale`, `salmon`, `lizard`, `canary`, `koala`.
	Color *string `pulumi:"color"`
	// The name of the Tag.
	Name *string `pulumi:"name"`
	// The ID of the Product.
	ProductId string `pulumi:"productId"`
}

// The set of arguments for constructing a Tag resource.
type TagArgs struct {
	// Default: `panther`. The color of the Tag. Valid values: `panther`, `whale`, `salmon`, `lizard`, `canary`, `koala`.
	Color pulumi.StringPtrInput
	// The name of the Tag.
	Name pulumi.StringPtrInput
	// The ID of the Product.
	ProductId pulumi.StringInput
}

func (TagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tagArgs)(nil)).Elem()
}

type TagInput interface {
	pulumi.Input

	ToTagOutput() TagOutput
	ToTagOutputWithContext(ctx context.Context) TagOutput
}

func (*Tag) ElementType() reflect.Type {
	return reflect.TypeOf((**Tag)(nil)).Elem()
}

func (i *Tag) ToTagOutput() TagOutput {
	return i.ToTagOutputWithContext(context.Background())
}

func (i *Tag) ToTagOutputWithContext(ctx context.Context) TagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TagOutput)
}

// TagArrayInput is an input type that accepts TagArray and TagArrayOutput values.
// You can construct a concrete instance of `TagArrayInput` via:
//
//	TagArray{ TagArgs{...} }
type TagArrayInput interface {
	pulumi.Input

	ToTagArrayOutput() TagArrayOutput
	ToTagArrayOutputWithContext(context.Context) TagArrayOutput
}

type TagArray []TagInput

func (TagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Tag)(nil)).Elem()
}

func (i TagArray) ToTagArrayOutput() TagArrayOutput {
	return i.ToTagArrayOutputWithContext(context.Background())
}

func (i TagArray) ToTagArrayOutputWithContext(ctx context.Context) TagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TagArrayOutput)
}

// TagMapInput is an input type that accepts TagMap and TagMapOutput values.
// You can construct a concrete instance of `TagMapInput` via:
//
//	TagMap{ "key": TagArgs{...} }
type TagMapInput interface {
	pulumi.Input

	ToTagMapOutput() TagMapOutput
	ToTagMapOutputWithContext(context.Context) TagMapOutput
}

type TagMap map[string]TagInput

func (TagMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Tag)(nil)).Elem()
}

func (i TagMap) ToTagMapOutput() TagMapOutput {
	return i.ToTagMapOutputWithContext(context.Background())
}

func (i TagMap) ToTagMapOutputWithContext(ctx context.Context) TagMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TagMapOutput)
}

type TagOutput struct{ *pulumi.OutputState }

func (TagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Tag)(nil)).Elem()
}

func (o TagOutput) ToTagOutput() TagOutput {
	return o
}

func (o TagOutput) ToTagOutputWithContext(ctx context.Context) TagOutput {
	return o
}

// Default: `panther`. The color of the Tag. Valid values: `panther`, `whale`, `salmon`, `lizard`, `canary`, `koala`.
func (o TagOutput) Color() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Tag) pulumi.StringPtrOutput { return v.Color }).(pulumi.StringPtrOutput)
}

// The name of the Tag.
func (o TagOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Tag) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The ID of the Product.
func (o TagOutput) ProductId() pulumi.StringOutput {
	return o.ApplyT(func(v *Tag) pulumi.StringOutput { return v.ProductId }).(pulumi.StringOutput)
}

type TagArrayOutput struct{ *pulumi.OutputState }

func (TagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Tag)(nil)).Elem()
}

func (o TagArrayOutput) ToTagArrayOutput() TagArrayOutput {
	return o
}

func (o TagArrayOutput) ToTagArrayOutputWithContext(ctx context.Context) TagArrayOutput {
	return o
}

func (o TagArrayOutput) Index(i pulumi.IntInput) TagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Tag {
		return vs[0].([]*Tag)[vs[1].(int)]
	}).(TagOutput)
}

type TagMapOutput struct{ *pulumi.OutputState }

func (TagMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Tag)(nil)).Elem()
}

func (o TagMapOutput) ToTagMapOutput() TagMapOutput {
	return o
}

func (o TagMapOutput) ToTagMapOutputWithContext(ctx context.Context) TagMapOutput {
	return o
}

func (o TagMapOutput) MapIndex(k pulumi.StringInput) TagOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Tag {
		return vs[0].(map[string]*Tag)[vs[1].(string)]
	}).(TagOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TagInput)(nil)).Elem(), &Tag{})
	pulumi.RegisterInputType(reflect.TypeOf((*TagArrayInput)(nil)).Elem(), TagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TagMapInput)(nil)).Elem(), TagMap{})
	pulumi.RegisterOutputType(TagOutput{})
	pulumi.RegisterOutputType(TagArrayOutput{})
	pulumi.RegisterOutputType(TagMapOutput{})
}
