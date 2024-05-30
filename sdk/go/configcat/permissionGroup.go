// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/go/configcat/internal"
)

// ## # PermissionGroup Resource
//
// Creates and manages a **Permission Group**. [What is a Permission Group in ConfigCat?](https://configcat.com/docs/advanced/team-management/team-management-basics/#permissions--permission-groups-product-level)
//
// ## Example Usage
//
// ### S
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
//			myPermissionGroup, err := configcat.NewPermissionGroup(ctx, "myPermissionGroup", &configcat.PermissionGroupArgs{
//				ProductId:                    pulumi.String(myProducts.Products[0].ProductId),
//				Accesstype:                   pulumi.String("full"),
//				CanManageMembers:             pulumi.Bool(true),
//				CanCreateorupdateConfig:      pulumi.Bool(true),
//				CanDeleteConfig:              pulumi.Bool(true),
//				CanCreateorupdateEnvironment: pulumi.Bool(true),
//				CanDeleteEnvironment:         pulumi.Bool(true),
//				CanCreateorupdateSetting:     pulumi.Bool(true),
//				CanTagSetting:                pulumi.Bool(true),
//				CanDeleteSetting:             pulumi.Bool(true),
//				CanCreateorupdateTag:         pulumi.Bool(true),
//				CanDeleteTag:                 pulumi.Bool(true),
//				CanManageWebhook:             pulumi.Bool(true),
//				CanUseExportimport:           pulumi.Bool(true),
//				CanManageProductPreferences:  pulumi.Bool(true),
//				CanManageIntegrations:        pulumi.Bool(true),
//				CanViewSdkkey:                pulumi.Bool(true),
//				CanRotateSdkkey:              pulumi.Bool(true),
//				CanCreateorupdateSegment:     pulumi.Bool(true),
//				CanDeleteSegment:             pulumi.Bool(true),
//				CanViewProductAuditlog:       pulumi.Bool(true),
//				CanViewProductStatistics:     pulumi.Bool(true),
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("permissionGroupId", myPermissionGroup.ID())
//			return nil
//		})
//	}
//
// ```
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
//			myTestEnvironments, err := configcat.GetEnvironments(ctx, &configcat.GetEnvironmentsArgs{
//				NameFilterRegex: pulumi.StringRef("Test"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			myProductionEnvironments, err := configcat.GetEnvironments(ctx, &configcat.GetEnvironmentsArgs{
//				NameFilterRegex: pulumi.StringRef("Production"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			myPermissionGroup, err := configcat.NewPermissionGroup(ctx, "myPermissionGroup", &configcat.PermissionGroupArgs{
//				ProductId:  pulumi.String(myProducts.Products[0].ProductId),
//				Accesstype: pulumi.String("custom"),
//				EnvironmentAccesses: configcat.PermissionGroupEnvironmentAccessArray{
//					&configcat.PermissionGroupEnvironmentAccessArgs{
//						EnvironmentId:         pulumi.String(myTestEnvironments.Environments[0].EnvironmentId),
//						EnvironmentAccesstype: pulumi.String("full"),
//					},
//					&configcat.PermissionGroupEnvironmentAccessArgs{
//						EnvironmentId:         pulumi.String(myProductionEnvironments.Environments[0].EnvironmentId),
//						EnvironmentAccesstype: pulumi.String("none"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("permissionGroupId", myPermissionGroup.ID())
//			return nil
//		})
//	}
//
// ```
//
// ## Endpoints used
//
// * [Get Permission Group](https://api.configcat.com/docs/#tag/Permission-Groups/operation/get-permission-group)
// * [Create Permission Group](https://api.configcat.com/docs/#tag/Permission-Groups/operation/create-permission-group)
// * [Update Permission Group](https://api.configcat.com/docs/#tag/Permission-Groups/operation/update-permission-group)
// * [Delete Permission Group](https://api.configcat.com/docs/#tag/Permission-Groups/operation/delete-permission-group)
//
// ## Import
//
// Permission Groups can be imported using the PermissionGroupId. Get the PermissionGroupId using the [List Permission Groups API](https://api.configcat.com/docs/#tag/Permission-Groups/operation/get-permission-groups) for example.
//
// ```sh
// $ pulumi import configcat:index/permissionGroup:PermissionGroup example 123
// ```
// Read more about importing.
type PermissionGroup struct {
	pulumi.CustomResourceState

	// Represent the Feature Management permission. Possible values: readOnly, full, custom. Default: custom
	Accesstype pulumi.StringPtrOutput `pulumi:"accesstype"`
	// Group members can create/update Configs. Default: false.
	CanCreateorupdateConfig pulumi.BoolPtrOutput `pulumi:"canCreateorupdateConfig"`
	// Group members can create/update Environments. Default: false.
	CanCreateorupdateEnvironment pulumi.BoolPtrOutput `pulumi:"canCreateorupdateEnvironment"`
	CanCreateorupdateSegment     pulumi.BoolPtrOutput `pulumi:"canCreateorupdateSegment"`
	// Group members can create/update Feature Flags and Settings. Default: false.
	CanCreateorupdateSetting pulumi.BoolPtrOutput `pulumi:"canCreateorupdateSetting"`
	// Group members can create/update Tags. Default: false.
	CanCreateorupdateTag pulumi.BoolPtrOutput `pulumi:"canCreateorupdateTag"`
	// Group members can delete Configs. Default: false.
	CanDeleteConfig pulumi.BoolPtrOutput `pulumi:"canDeleteConfig"`
	// Group members can delete Environments. Default: false.
	CanDeleteEnvironment pulumi.BoolPtrOutput `pulumi:"canDeleteEnvironment"`
	CanDeleteSegment     pulumi.BoolPtrOutput `pulumi:"canDeleteSegment"`
	// Group members can delete Feature Flags and Settings. Default: false.
	CanDeleteSetting pulumi.BoolPtrOutput `pulumi:"canDeleteSetting"`
	// Group members can delete Tags. Default: false.
	CanDeleteTag pulumi.BoolPtrOutput `pulumi:"canDeleteTag"`
	// Group members can add and configure integrations. Default: false.
	CanManageIntegrations pulumi.BoolPtrOutput `pulumi:"canManageIntegrations"`
	// Group members can manage team members. Default: false.
	CanManageMembers pulumi.BoolPtrOutput `pulumi:"canManageMembers"`
	// Group members can update Product preferences. Default: false.
	CanManageProductPreferences pulumi.BoolPtrOutput `pulumi:"canManageProductPreferences"`
	// Group members can create/update/delete Webhooks. Default: false.
	CanManageWebhook pulumi.BoolPtrOutput `pulumi:"canManageWebhook"`
	// Group members can rotate SDK keys. Default: false.
	CanRotateSdkkey pulumi.BoolPtrOutput `pulumi:"canRotateSdkkey"`
	// Group members can attach/detach Tags to Feature Flags and Settings. Default: false.
	CanTagSetting pulumi.BoolPtrOutput `pulumi:"canTagSetting"`
	// Group members can use the export/import feature. Default: false.
	CanUseExportimport pulumi.BoolPtrOutput `pulumi:"canUseExportimport"`
	// Group members has access to audit logs. Default: false.
	CanViewProductAuditlog pulumi.BoolPtrOutput `pulumi:"canViewProductAuditlog"`
	// Group members has access to product statistics. Default: false.
	CanViewProductStatistics pulumi.BoolPtrOutput `pulumi:"canViewProductStatistics"`
	// Group members has access to SDK keys. Default: false.
	CanViewSdkkey pulumi.BoolPtrOutput `pulumi:"canViewSdkkey"`
	// The environment specific permissions list block defined as below.
	EnvironmentAccesses PermissionGroupEnvironmentAccessArrayOutput `pulumi:"environmentAccesses"`
	// The name of the Permission Group.
	Name pulumi.StringOutput `pulumi:"name"`
	// Represent the environment specific Feature Management permission for new Environments and for those that are not specified in the environmentAccess list. Possible values: full, readOnly, none. Default: none.
	NewEnvironmentAccesstype pulumi.StringPtrOutput `pulumi:"newEnvironmentAccesstype"`
	// The ID of the Product.
	ProductId pulumi.StringOutput `pulumi:"productId"`
}

// NewPermissionGroup registers a new resource with the given unique name, arguments, and options.
func NewPermissionGroup(ctx *pulumi.Context,
	name string, args *PermissionGroupArgs, opts ...pulumi.ResourceOption) (*PermissionGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ProductId == nil {
		return nil, errors.New("invalid value for required argument 'ProductId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource PermissionGroup
	err := ctx.RegisterResource("configcat:index/permissionGroup:PermissionGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPermissionGroup gets an existing PermissionGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPermissionGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PermissionGroupState, opts ...pulumi.ResourceOption) (*PermissionGroup, error) {
	var resource PermissionGroup
	err := ctx.ReadResource("configcat:index/permissionGroup:PermissionGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PermissionGroup resources.
type permissionGroupState struct {
	// Represent the Feature Management permission. Possible values: readOnly, full, custom. Default: custom
	Accesstype *string `pulumi:"accesstype"`
	// Group members can create/update Configs. Default: false.
	CanCreateorupdateConfig *bool `pulumi:"canCreateorupdateConfig"`
	// Group members can create/update Environments. Default: false.
	CanCreateorupdateEnvironment *bool `pulumi:"canCreateorupdateEnvironment"`
	CanCreateorupdateSegment     *bool `pulumi:"canCreateorupdateSegment"`
	// Group members can create/update Feature Flags and Settings. Default: false.
	CanCreateorupdateSetting *bool `pulumi:"canCreateorupdateSetting"`
	// Group members can create/update Tags. Default: false.
	CanCreateorupdateTag *bool `pulumi:"canCreateorupdateTag"`
	// Group members can delete Configs. Default: false.
	CanDeleteConfig *bool `pulumi:"canDeleteConfig"`
	// Group members can delete Environments. Default: false.
	CanDeleteEnvironment *bool `pulumi:"canDeleteEnvironment"`
	CanDeleteSegment     *bool `pulumi:"canDeleteSegment"`
	// Group members can delete Feature Flags and Settings. Default: false.
	CanDeleteSetting *bool `pulumi:"canDeleteSetting"`
	// Group members can delete Tags. Default: false.
	CanDeleteTag *bool `pulumi:"canDeleteTag"`
	// Group members can add and configure integrations. Default: false.
	CanManageIntegrations *bool `pulumi:"canManageIntegrations"`
	// Group members can manage team members. Default: false.
	CanManageMembers *bool `pulumi:"canManageMembers"`
	// Group members can update Product preferences. Default: false.
	CanManageProductPreferences *bool `pulumi:"canManageProductPreferences"`
	// Group members can create/update/delete Webhooks. Default: false.
	CanManageWebhook *bool `pulumi:"canManageWebhook"`
	// Group members can rotate SDK keys. Default: false.
	CanRotateSdkkey *bool `pulumi:"canRotateSdkkey"`
	// Group members can attach/detach Tags to Feature Flags and Settings. Default: false.
	CanTagSetting *bool `pulumi:"canTagSetting"`
	// Group members can use the export/import feature. Default: false.
	CanUseExportimport *bool `pulumi:"canUseExportimport"`
	// Group members has access to audit logs. Default: false.
	CanViewProductAuditlog *bool `pulumi:"canViewProductAuditlog"`
	// Group members has access to product statistics. Default: false.
	CanViewProductStatistics *bool `pulumi:"canViewProductStatistics"`
	// Group members has access to SDK keys. Default: false.
	CanViewSdkkey *bool `pulumi:"canViewSdkkey"`
	// The environment specific permissions list block defined as below.
	EnvironmentAccesses []PermissionGroupEnvironmentAccess `pulumi:"environmentAccesses"`
	// The name of the Permission Group.
	Name *string `pulumi:"name"`
	// Represent the environment specific Feature Management permission for new Environments and for those that are not specified in the environmentAccess list. Possible values: full, readOnly, none. Default: none.
	NewEnvironmentAccesstype *string `pulumi:"newEnvironmentAccesstype"`
	// The ID of the Product.
	ProductId *string `pulumi:"productId"`
}

type PermissionGroupState struct {
	// Represent the Feature Management permission. Possible values: readOnly, full, custom. Default: custom
	Accesstype pulumi.StringPtrInput
	// Group members can create/update Configs. Default: false.
	CanCreateorupdateConfig pulumi.BoolPtrInput
	// Group members can create/update Environments. Default: false.
	CanCreateorupdateEnvironment pulumi.BoolPtrInput
	CanCreateorupdateSegment     pulumi.BoolPtrInput
	// Group members can create/update Feature Flags and Settings. Default: false.
	CanCreateorupdateSetting pulumi.BoolPtrInput
	// Group members can create/update Tags. Default: false.
	CanCreateorupdateTag pulumi.BoolPtrInput
	// Group members can delete Configs. Default: false.
	CanDeleteConfig pulumi.BoolPtrInput
	// Group members can delete Environments. Default: false.
	CanDeleteEnvironment pulumi.BoolPtrInput
	CanDeleteSegment     pulumi.BoolPtrInput
	// Group members can delete Feature Flags and Settings. Default: false.
	CanDeleteSetting pulumi.BoolPtrInput
	// Group members can delete Tags. Default: false.
	CanDeleteTag pulumi.BoolPtrInput
	// Group members can add and configure integrations. Default: false.
	CanManageIntegrations pulumi.BoolPtrInput
	// Group members can manage team members. Default: false.
	CanManageMembers pulumi.BoolPtrInput
	// Group members can update Product preferences. Default: false.
	CanManageProductPreferences pulumi.BoolPtrInput
	// Group members can create/update/delete Webhooks. Default: false.
	CanManageWebhook pulumi.BoolPtrInput
	// Group members can rotate SDK keys. Default: false.
	CanRotateSdkkey pulumi.BoolPtrInput
	// Group members can attach/detach Tags to Feature Flags and Settings. Default: false.
	CanTagSetting pulumi.BoolPtrInput
	// Group members can use the export/import feature. Default: false.
	CanUseExportimport pulumi.BoolPtrInput
	// Group members has access to audit logs. Default: false.
	CanViewProductAuditlog pulumi.BoolPtrInput
	// Group members has access to product statistics. Default: false.
	CanViewProductStatistics pulumi.BoolPtrInput
	// Group members has access to SDK keys. Default: false.
	CanViewSdkkey pulumi.BoolPtrInput
	// The environment specific permissions list block defined as below.
	EnvironmentAccesses PermissionGroupEnvironmentAccessArrayInput
	// The name of the Permission Group.
	Name pulumi.StringPtrInput
	// Represent the environment specific Feature Management permission for new Environments and for those that are not specified in the environmentAccess list. Possible values: full, readOnly, none. Default: none.
	NewEnvironmentAccesstype pulumi.StringPtrInput
	// The ID of the Product.
	ProductId pulumi.StringPtrInput
}

func (PermissionGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*permissionGroupState)(nil)).Elem()
}

type permissionGroupArgs struct {
	// Represent the Feature Management permission. Possible values: readOnly, full, custom. Default: custom
	Accesstype *string `pulumi:"accesstype"`
	// Group members can create/update Configs. Default: false.
	CanCreateorupdateConfig *bool `pulumi:"canCreateorupdateConfig"`
	// Group members can create/update Environments. Default: false.
	CanCreateorupdateEnvironment *bool `pulumi:"canCreateorupdateEnvironment"`
	CanCreateorupdateSegment     *bool `pulumi:"canCreateorupdateSegment"`
	// Group members can create/update Feature Flags and Settings. Default: false.
	CanCreateorupdateSetting *bool `pulumi:"canCreateorupdateSetting"`
	// Group members can create/update Tags. Default: false.
	CanCreateorupdateTag *bool `pulumi:"canCreateorupdateTag"`
	// Group members can delete Configs. Default: false.
	CanDeleteConfig *bool `pulumi:"canDeleteConfig"`
	// Group members can delete Environments. Default: false.
	CanDeleteEnvironment *bool `pulumi:"canDeleteEnvironment"`
	CanDeleteSegment     *bool `pulumi:"canDeleteSegment"`
	// Group members can delete Feature Flags and Settings. Default: false.
	CanDeleteSetting *bool `pulumi:"canDeleteSetting"`
	// Group members can delete Tags. Default: false.
	CanDeleteTag *bool `pulumi:"canDeleteTag"`
	// Group members can add and configure integrations. Default: false.
	CanManageIntegrations *bool `pulumi:"canManageIntegrations"`
	// Group members can manage team members. Default: false.
	CanManageMembers *bool `pulumi:"canManageMembers"`
	// Group members can update Product preferences. Default: false.
	CanManageProductPreferences *bool `pulumi:"canManageProductPreferences"`
	// Group members can create/update/delete Webhooks. Default: false.
	CanManageWebhook *bool `pulumi:"canManageWebhook"`
	// Group members can rotate SDK keys. Default: false.
	CanRotateSdkkey *bool `pulumi:"canRotateSdkkey"`
	// Group members can attach/detach Tags to Feature Flags and Settings. Default: false.
	CanTagSetting *bool `pulumi:"canTagSetting"`
	// Group members can use the export/import feature. Default: false.
	CanUseExportimport *bool `pulumi:"canUseExportimport"`
	// Group members has access to audit logs. Default: false.
	CanViewProductAuditlog *bool `pulumi:"canViewProductAuditlog"`
	// Group members has access to product statistics. Default: false.
	CanViewProductStatistics *bool `pulumi:"canViewProductStatistics"`
	// Group members has access to SDK keys. Default: false.
	CanViewSdkkey *bool `pulumi:"canViewSdkkey"`
	// The environment specific permissions list block defined as below.
	EnvironmentAccesses []PermissionGroupEnvironmentAccess `pulumi:"environmentAccesses"`
	// The name of the Permission Group.
	Name *string `pulumi:"name"`
	// Represent the environment specific Feature Management permission for new Environments and for those that are not specified in the environmentAccess list. Possible values: full, readOnly, none. Default: none.
	NewEnvironmentAccesstype *string `pulumi:"newEnvironmentAccesstype"`
	// The ID of the Product.
	ProductId string `pulumi:"productId"`
}

// The set of arguments for constructing a PermissionGroup resource.
type PermissionGroupArgs struct {
	// Represent the Feature Management permission. Possible values: readOnly, full, custom. Default: custom
	Accesstype pulumi.StringPtrInput
	// Group members can create/update Configs. Default: false.
	CanCreateorupdateConfig pulumi.BoolPtrInput
	// Group members can create/update Environments. Default: false.
	CanCreateorupdateEnvironment pulumi.BoolPtrInput
	CanCreateorupdateSegment     pulumi.BoolPtrInput
	// Group members can create/update Feature Flags and Settings. Default: false.
	CanCreateorupdateSetting pulumi.BoolPtrInput
	// Group members can create/update Tags. Default: false.
	CanCreateorupdateTag pulumi.BoolPtrInput
	// Group members can delete Configs. Default: false.
	CanDeleteConfig pulumi.BoolPtrInput
	// Group members can delete Environments. Default: false.
	CanDeleteEnvironment pulumi.BoolPtrInput
	CanDeleteSegment     pulumi.BoolPtrInput
	// Group members can delete Feature Flags and Settings. Default: false.
	CanDeleteSetting pulumi.BoolPtrInput
	// Group members can delete Tags. Default: false.
	CanDeleteTag pulumi.BoolPtrInput
	// Group members can add and configure integrations. Default: false.
	CanManageIntegrations pulumi.BoolPtrInput
	// Group members can manage team members. Default: false.
	CanManageMembers pulumi.BoolPtrInput
	// Group members can update Product preferences. Default: false.
	CanManageProductPreferences pulumi.BoolPtrInput
	// Group members can create/update/delete Webhooks. Default: false.
	CanManageWebhook pulumi.BoolPtrInput
	// Group members can rotate SDK keys. Default: false.
	CanRotateSdkkey pulumi.BoolPtrInput
	// Group members can attach/detach Tags to Feature Flags and Settings. Default: false.
	CanTagSetting pulumi.BoolPtrInput
	// Group members can use the export/import feature. Default: false.
	CanUseExportimport pulumi.BoolPtrInput
	// Group members has access to audit logs. Default: false.
	CanViewProductAuditlog pulumi.BoolPtrInput
	// Group members has access to product statistics. Default: false.
	CanViewProductStatistics pulumi.BoolPtrInput
	// Group members has access to SDK keys. Default: false.
	CanViewSdkkey pulumi.BoolPtrInput
	// The environment specific permissions list block defined as below.
	EnvironmentAccesses PermissionGroupEnvironmentAccessArrayInput
	// The name of the Permission Group.
	Name pulumi.StringPtrInput
	// Represent the environment specific Feature Management permission for new Environments and for those that are not specified in the environmentAccess list. Possible values: full, readOnly, none. Default: none.
	NewEnvironmentAccesstype pulumi.StringPtrInput
	// The ID of the Product.
	ProductId pulumi.StringInput
}

func (PermissionGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*permissionGroupArgs)(nil)).Elem()
}

type PermissionGroupInput interface {
	pulumi.Input

	ToPermissionGroupOutput() PermissionGroupOutput
	ToPermissionGroupOutputWithContext(ctx context.Context) PermissionGroupOutput
}

func (*PermissionGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**PermissionGroup)(nil)).Elem()
}

func (i *PermissionGroup) ToPermissionGroupOutput() PermissionGroupOutput {
	return i.ToPermissionGroupOutputWithContext(context.Background())
}

func (i *PermissionGroup) ToPermissionGroupOutputWithContext(ctx context.Context) PermissionGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionGroupOutput)
}

// PermissionGroupArrayInput is an input type that accepts PermissionGroupArray and PermissionGroupArrayOutput values.
// You can construct a concrete instance of `PermissionGroupArrayInput` via:
//
//	PermissionGroupArray{ PermissionGroupArgs{...} }
type PermissionGroupArrayInput interface {
	pulumi.Input

	ToPermissionGroupArrayOutput() PermissionGroupArrayOutput
	ToPermissionGroupArrayOutputWithContext(context.Context) PermissionGroupArrayOutput
}

type PermissionGroupArray []PermissionGroupInput

func (PermissionGroupArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PermissionGroup)(nil)).Elem()
}

func (i PermissionGroupArray) ToPermissionGroupArrayOutput() PermissionGroupArrayOutput {
	return i.ToPermissionGroupArrayOutputWithContext(context.Background())
}

func (i PermissionGroupArray) ToPermissionGroupArrayOutputWithContext(ctx context.Context) PermissionGroupArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionGroupArrayOutput)
}

// PermissionGroupMapInput is an input type that accepts PermissionGroupMap and PermissionGroupMapOutput values.
// You can construct a concrete instance of `PermissionGroupMapInput` via:
//
//	PermissionGroupMap{ "key": PermissionGroupArgs{...} }
type PermissionGroupMapInput interface {
	pulumi.Input

	ToPermissionGroupMapOutput() PermissionGroupMapOutput
	ToPermissionGroupMapOutputWithContext(context.Context) PermissionGroupMapOutput
}

type PermissionGroupMap map[string]PermissionGroupInput

func (PermissionGroupMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PermissionGroup)(nil)).Elem()
}

func (i PermissionGroupMap) ToPermissionGroupMapOutput() PermissionGroupMapOutput {
	return i.ToPermissionGroupMapOutputWithContext(context.Background())
}

func (i PermissionGroupMap) ToPermissionGroupMapOutputWithContext(ctx context.Context) PermissionGroupMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PermissionGroupMapOutput)
}

type PermissionGroupOutput struct{ *pulumi.OutputState }

func (PermissionGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PermissionGroup)(nil)).Elem()
}

func (o PermissionGroupOutput) ToPermissionGroupOutput() PermissionGroupOutput {
	return o
}

func (o PermissionGroupOutput) ToPermissionGroupOutputWithContext(ctx context.Context) PermissionGroupOutput {
	return o
}

// Represent the Feature Management permission. Possible values: readOnly, full, custom. Default: custom
func (o PermissionGroupOutput) Accesstype() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.StringPtrOutput { return v.Accesstype }).(pulumi.StringPtrOutput)
}

// Group members can create/update Configs. Default: false.
func (o PermissionGroupOutput) CanCreateorupdateConfig() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanCreateorupdateConfig }).(pulumi.BoolPtrOutput)
}

// Group members can create/update Environments. Default: false.
func (o PermissionGroupOutput) CanCreateorupdateEnvironment() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanCreateorupdateEnvironment }).(pulumi.BoolPtrOutput)
}

func (o PermissionGroupOutput) CanCreateorupdateSegment() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanCreateorupdateSegment }).(pulumi.BoolPtrOutput)
}

// Group members can create/update Feature Flags and Settings. Default: false.
func (o PermissionGroupOutput) CanCreateorupdateSetting() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanCreateorupdateSetting }).(pulumi.BoolPtrOutput)
}

// Group members can create/update Tags. Default: false.
func (o PermissionGroupOutput) CanCreateorupdateTag() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanCreateorupdateTag }).(pulumi.BoolPtrOutput)
}

// Group members can delete Configs. Default: false.
func (o PermissionGroupOutput) CanDeleteConfig() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanDeleteConfig }).(pulumi.BoolPtrOutput)
}

// Group members can delete Environments. Default: false.
func (o PermissionGroupOutput) CanDeleteEnvironment() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanDeleteEnvironment }).(pulumi.BoolPtrOutput)
}

func (o PermissionGroupOutput) CanDeleteSegment() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanDeleteSegment }).(pulumi.BoolPtrOutput)
}

// Group members can delete Feature Flags and Settings. Default: false.
func (o PermissionGroupOutput) CanDeleteSetting() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanDeleteSetting }).(pulumi.BoolPtrOutput)
}

// Group members can delete Tags. Default: false.
func (o PermissionGroupOutput) CanDeleteTag() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanDeleteTag }).(pulumi.BoolPtrOutput)
}

// Group members can add and configure integrations. Default: false.
func (o PermissionGroupOutput) CanManageIntegrations() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanManageIntegrations }).(pulumi.BoolPtrOutput)
}

// Group members can manage team members. Default: false.
func (o PermissionGroupOutput) CanManageMembers() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanManageMembers }).(pulumi.BoolPtrOutput)
}

// Group members can update Product preferences. Default: false.
func (o PermissionGroupOutput) CanManageProductPreferences() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanManageProductPreferences }).(pulumi.BoolPtrOutput)
}

// Group members can create/update/delete Webhooks. Default: false.
func (o PermissionGroupOutput) CanManageWebhook() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanManageWebhook }).(pulumi.BoolPtrOutput)
}

// Group members can rotate SDK keys. Default: false.
func (o PermissionGroupOutput) CanRotateSdkkey() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanRotateSdkkey }).(pulumi.BoolPtrOutput)
}

// Group members can attach/detach Tags to Feature Flags and Settings. Default: false.
func (o PermissionGroupOutput) CanTagSetting() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanTagSetting }).(pulumi.BoolPtrOutput)
}

// Group members can use the export/import feature. Default: false.
func (o PermissionGroupOutput) CanUseExportimport() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanUseExportimport }).(pulumi.BoolPtrOutput)
}

// Group members has access to audit logs. Default: false.
func (o PermissionGroupOutput) CanViewProductAuditlog() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanViewProductAuditlog }).(pulumi.BoolPtrOutput)
}

// Group members has access to product statistics. Default: false.
func (o PermissionGroupOutput) CanViewProductStatistics() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanViewProductStatistics }).(pulumi.BoolPtrOutput)
}

// Group members has access to SDK keys. Default: false.
func (o PermissionGroupOutput) CanViewSdkkey() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.BoolPtrOutput { return v.CanViewSdkkey }).(pulumi.BoolPtrOutput)
}

// The environment specific permissions list block defined as below.
func (o PermissionGroupOutput) EnvironmentAccesses() PermissionGroupEnvironmentAccessArrayOutput {
	return o.ApplyT(func(v *PermissionGroup) PermissionGroupEnvironmentAccessArrayOutput { return v.EnvironmentAccesses }).(PermissionGroupEnvironmentAccessArrayOutput)
}

// The name of the Permission Group.
func (o PermissionGroupOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Represent the environment specific Feature Management permission for new Environments and for those that are not specified in the environmentAccess list. Possible values: full, readOnly, none. Default: none.
func (o PermissionGroupOutput) NewEnvironmentAccesstype() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.StringPtrOutput { return v.NewEnvironmentAccesstype }).(pulumi.StringPtrOutput)
}

// The ID of the Product.
func (o PermissionGroupOutput) ProductId() pulumi.StringOutput {
	return o.ApplyT(func(v *PermissionGroup) pulumi.StringOutput { return v.ProductId }).(pulumi.StringOutput)
}

type PermissionGroupArrayOutput struct{ *pulumi.OutputState }

func (PermissionGroupArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PermissionGroup)(nil)).Elem()
}

func (o PermissionGroupArrayOutput) ToPermissionGroupArrayOutput() PermissionGroupArrayOutput {
	return o
}

func (o PermissionGroupArrayOutput) ToPermissionGroupArrayOutputWithContext(ctx context.Context) PermissionGroupArrayOutput {
	return o
}

func (o PermissionGroupArrayOutput) Index(i pulumi.IntInput) PermissionGroupOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *PermissionGroup {
		return vs[0].([]*PermissionGroup)[vs[1].(int)]
	}).(PermissionGroupOutput)
}

type PermissionGroupMapOutput struct{ *pulumi.OutputState }

func (PermissionGroupMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PermissionGroup)(nil)).Elem()
}

func (o PermissionGroupMapOutput) ToPermissionGroupMapOutput() PermissionGroupMapOutput {
	return o
}

func (o PermissionGroupMapOutput) ToPermissionGroupMapOutputWithContext(ctx context.Context) PermissionGroupMapOutput {
	return o
}

func (o PermissionGroupMapOutput) MapIndex(k pulumi.StringInput) PermissionGroupOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *PermissionGroup {
		return vs[0].(map[string]*PermissionGroup)[vs[1].(string)]
	}).(PermissionGroupOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PermissionGroupInput)(nil)).Elem(), &PermissionGroup{})
	pulumi.RegisterInputType(reflect.TypeOf((*PermissionGroupArrayInput)(nil)).Elem(), PermissionGroupArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PermissionGroupMapInput)(nil)).Elem(), PermissionGroupMap{})
	pulumi.RegisterOutputType(PermissionGroupOutput{})
	pulumi.RegisterOutputType(PermissionGroupArrayOutput{})
	pulumi.RegisterOutputType(PermissionGroupMapOutput{})
}
