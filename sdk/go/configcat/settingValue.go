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

// ## # SettingValue Resource
//
// Initializes and updates **Feature Flag and Setting** values. [Read more about the anatomy of a Feature Flag or Setting.](https://configcat.com/docs/main-concepts)
//
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
//			myConfigs, err := configcat.GetConfigurations(ctx, &configcat.GetConfigurationsArgs{
//				ProductId:       myProducts.Products[0].ProductId,
//				NameFilterRegex: pulumi.StringRef("Main Config"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			myEnvironments, err := configcat.GetEnvironments(ctx, &configcat.GetEnvironmentsArgs{
//				ProductId:       myProducts.Products[0].ProductId,
//				NameFilterRegex: pulumi.StringRef("Test"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			mySettings, err := configcat.GetSettings(ctx, &configcat.GetSettingsArgs{
//				ConfigId:       myConfigs.Configs[0].ConfigId,
//				KeyFilterRegex: pulumi.StringRef("isAwesomeFeatureEnabled"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = configcat.NewSettingValue(ctx, "my_setting_value", &configcat.SettingValueArgs{
//				EnvironmentId:  pulumi.String(myEnvironments.Environments[0].EnvironmentId),
//				SettingId:      pulumi.String(mySettings.Settings[0].SettingId),
//				MandatoryNotes: pulumi.String("mandatory notes"),
//				Value:          pulumi.String("true"),
//				RolloutRules: configcat.SettingValueRolloutRuleArray{
//					&configcat.SettingValueRolloutRuleArgs{
//						ComparisonAttribute: pulumi.String("Email"),
//						Comparator:          pulumi.String("contains"),
//						ComparisonValue:     pulumi.String("@mycompany.com"),
//						Value:               pulumi.String("true"),
//					},
//					&configcat.SettingValueRolloutRuleArgs{
//						ComparisonAttribute: pulumi.String("custom"),
//						Comparator:          pulumi.String("isOneOf"),
//						ComparisonValue:     pulumi.String("red"),
//						Value:               pulumi.String("false"),
//					},
//				},
//				PercentageItems: configcat.SettingValuePercentageItemArray{
//					&configcat.SettingValuePercentageItemArgs{
//						Percentage: pulumi.String("20"),
//						Value:      pulumi.String("true"),
//					},
//					&configcat.SettingValuePercentageItemArgs{
//						Percentage: pulumi.String("80"),
//						Value:      pulumi.String("false"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Endpoints used
//
// * [Get Value](https://api.configcat.com/docs/#tag/Feature-Flag-and-Setting-values/operation/get-setting-value)
// * [Replace Value](https://api.configcat.com/docs/#tag/Feature-Flag-and-Setting-values/operation/replace-setting-value)
//
// ## Import
//
// Feature Flag/Setting values can be imported using a combined EnvironmentID:SettingId ID.
//
// Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).
//
// Get the EnvironmentId using e.g. the [List Environments API](https://api.configcat.com/docs/#tag/Environments/operation/get-environments).
//
// ```sh
// $ pulumi import configcat:index/settingValue:SettingValue example 08d86d63-2726-47cd-8bfc-59608ecb91e2:1234
// ```
//
// Read more about importing.
type SettingValue struct {
	pulumi.CustomResourceState

	// The ID of the Environment.
	EnvironmentId pulumi.StringOutput `pulumi:"environmentId"`
	// Default: true. Read more below.
	//
	// The Feature Flag/Setting's value
	InitOnly pulumi.BoolPtrOutput `pulumi:"initOnly"`
	// Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
	MandatoryNotes pulumi.StringPtrOutput `pulumi:"mandatoryNotes"`
	// A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
	PercentageItems SettingValuePercentageItemArrayOutput `pulumi:"percentageItems"`
	// A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
	RolloutRules SettingValueRolloutRuleArrayOutput `pulumi:"rolloutRules"`
	// The ID of the Feature Flag/Setting.
	SettingId pulumi.StringOutput `pulumi:"settingId"`
	// The Setting's type.
	SettingType pulumi.StringOutput `pulumi:"settingType"`
	// The Setting's value. Type: `string`. It must be compatible with the `settingType`.
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewSettingValue registers a new resource with the given unique name, arguments, and options.
func NewSettingValue(ctx *pulumi.Context,
	name string, args *SettingValueArgs, opts ...pulumi.ResourceOption) (*SettingValue, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.EnvironmentId == nil {
		return nil, errors.New("invalid value for required argument 'EnvironmentId'")
	}
	if args.SettingId == nil {
		return nil, errors.New("invalid value for required argument 'SettingId'")
	}
	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SettingValue
	err := ctx.RegisterResource("configcat:index/settingValue:SettingValue", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSettingValue gets an existing SettingValue resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSettingValue(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SettingValueState, opts ...pulumi.ResourceOption) (*SettingValue, error) {
	var resource SettingValue
	err := ctx.ReadResource("configcat:index/settingValue:SettingValue", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SettingValue resources.
type settingValueState struct {
	// The ID of the Environment.
	EnvironmentId *string `pulumi:"environmentId"`
	// Default: true. Read more below.
	//
	// The Feature Flag/Setting's value
	InitOnly *bool `pulumi:"initOnly"`
	// Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
	MandatoryNotes *string `pulumi:"mandatoryNotes"`
	// A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
	PercentageItems []SettingValuePercentageItem `pulumi:"percentageItems"`
	// A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
	RolloutRules []SettingValueRolloutRule `pulumi:"rolloutRules"`
	// The ID of the Feature Flag/Setting.
	SettingId *string `pulumi:"settingId"`
	// The Setting's type.
	SettingType *string `pulumi:"settingType"`
	// The Setting's value. Type: `string`. It must be compatible with the `settingType`.
	Value *string `pulumi:"value"`
}

type SettingValueState struct {
	// The ID of the Environment.
	EnvironmentId pulumi.StringPtrInput
	// Default: true. Read more below.
	//
	// The Feature Flag/Setting's value
	InitOnly pulumi.BoolPtrInput
	// Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
	MandatoryNotes pulumi.StringPtrInput
	// A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
	PercentageItems SettingValuePercentageItemArrayInput
	// A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
	RolloutRules SettingValueRolloutRuleArrayInput
	// The ID of the Feature Flag/Setting.
	SettingId pulumi.StringPtrInput
	// The Setting's type.
	SettingType pulumi.StringPtrInput
	// The Setting's value. Type: `string`. It must be compatible with the `settingType`.
	Value pulumi.StringPtrInput
}

func (SettingValueState) ElementType() reflect.Type {
	return reflect.TypeOf((*settingValueState)(nil)).Elem()
}

type settingValueArgs struct {
	// The ID of the Environment.
	EnvironmentId string `pulumi:"environmentId"`
	// Default: true. Read more below.
	//
	// The Feature Flag/Setting's value
	InitOnly *bool `pulumi:"initOnly"`
	// Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
	MandatoryNotes *string `pulumi:"mandatoryNotes"`
	// A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
	PercentageItems []SettingValuePercentageItem `pulumi:"percentageItems"`
	// A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
	RolloutRules []SettingValueRolloutRule `pulumi:"rolloutRules"`
	// The ID of the Feature Flag/Setting.
	SettingId string `pulumi:"settingId"`
	// The Setting's value. Type: `string`. It must be compatible with the `settingType`.
	Value string `pulumi:"value"`
}

// The set of arguments for constructing a SettingValue resource.
type SettingValueArgs struct {
	// The ID of the Environment.
	EnvironmentId pulumi.StringInput
	// Default: true. Read more below.
	//
	// The Feature Flag/Setting's value
	InitOnly pulumi.BoolPtrInput
	// Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
	MandatoryNotes pulumi.StringPtrInput
	// A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
	PercentageItems SettingValuePercentageItemArrayInput
	// A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
	RolloutRules SettingValueRolloutRuleArrayInput
	// The ID of the Feature Flag/Setting.
	SettingId pulumi.StringInput
	// The Setting's value. Type: `string`. It must be compatible with the `settingType`.
	Value pulumi.StringInput
}

func (SettingValueArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*settingValueArgs)(nil)).Elem()
}

type SettingValueInput interface {
	pulumi.Input

	ToSettingValueOutput() SettingValueOutput
	ToSettingValueOutputWithContext(ctx context.Context) SettingValueOutput
}

func (*SettingValue) ElementType() reflect.Type {
	return reflect.TypeOf((**SettingValue)(nil)).Elem()
}

func (i *SettingValue) ToSettingValueOutput() SettingValueOutput {
	return i.ToSettingValueOutputWithContext(context.Background())
}

func (i *SettingValue) ToSettingValueOutputWithContext(ctx context.Context) SettingValueOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SettingValueOutput)
}

// SettingValueArrayInput is an input type that accepts SettingValueArray and SettingValueArrayOutput values.
// You can construct a concrete instance of `SettingValueArrayInput` via:
//
//	SettingValueArray{ SettingValueArgs{...} }
type SettingValueArrayInput interface {
	pulumi.Input

	ToSettingValueArrayOutput() SettingValueArrayOutput
	ToSettingValueArrayOutputWithContext(context.Context) SettingValueArrayOutput
}

type SettingValueArray []SettingValueInput

func (SettingValueArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SettingValue)(nil)).Elem()
}

func (i SettingValueArray) ToSettingValueArrayOutput() SettingValueArrayOutput {
	return i.ToSettingValueArrayOutputWithContext(context.Background())
}

func (i SettingValueArray) ToSettingValueArrayOutputWithContext(ctx context.Context) SettingValueArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SettingValueArrayOutput)
}

// SettingValueMapInput is an input type that accepts SettingValueMap and SettingValueMapOutput values.
// You can construct a concrete instance of `SettingValueMapInput` via:
//
//	SettingValueMap{ "key": SettingValueArgs{...} }
type SettingValueMapInput interface {
	pulumi.Input

	ToSettingValueMapOutput() SettingValueMapOutput
	ToSettingValueMapOutputWithContext(context.Context) SettingValueMapOutput
}

type SettingValueMap map[string]SettingValueInput

func (SettingValueMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SettingValue)(nil)).Elem()
}

func (i SettingValueMap) ToSettingValueMapOutput() SettingValueMapOutput {
	return i.ToSettingValueMapOutputWithContext(context.Background())
}

func (i SettingValueMap) ToSettingValueMapOutputWithContext(ctx context.Context) SettingValueMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SettingValueMapOutput)
}

type SettingValueOutput struct{ *pulumi.OutputState }

func (SettingValueOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SettingValue)(nil)).Elem()
}

func (o SettingValueOutput) ToSettingValueOutput() SettingValueOutput {
	return o
}

func (o SettingValueOutput) ToSettingValueOutputWithContext(ctx context.Context) SettingValueOutput {
	return o
}

// The ID of the Environment.
func (o SettingValueOutput) EnvironmentId() pulumi.StringOutput {
	return o.ApplyT(func(v *SettingValue) pulumi.StringOutput { return v.EnvironmentId }).(pulumi.StringOutput)
}

// Default: true. Read more below.
//
// The Feature Flag/Setting's value
func (o SettingValueOutput) InitOnly() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SettingValue) pulumi.BoolPtrOutput { return v.InitOnly }).(pulumi.BoolPtrOutput)
}

// Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
func (o SettingValueOutput) MandatoryNotes() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SettingValue) pulumi.StringPtrOutput { return v.MandatoryNotes }).(pulumi.StringPtrOutput)
}

// A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
func (o SettingValueOutput) PercentageItems() SettingValuePercentageItemArrayOutput {
	return o.ApplyT(func(v *SettingValue) SettingValuePercentageItemArrayOutput { return v.PercentageItems }).(SettingValuePercentageItemArrayOutput)
}

// A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
func (o SettingValueOutput) RolloutRules() SettingValueRolloutRuleArrayOutput {
	return o.ApplyT(func(v *SettingValue) SettingValueRolloutRuleArrayOutput { return v.RolloutRules }).(SettingValueRolloutRuleArrayOutput)
}

// The ID of the Feature Flag/Setting.
func (o SettingValueOutput) SettingId() pulumi.StringOutput {
	return o.ApplyT(func(v *SettingValue) pulumi.StringOutput { return v.SettingId }).(pulumi.StringOutput)
}

// The Setting's type.
func (o SettingValueOutput) SettingType() pulumi.StringOutput {
	return o.ApplyT(func(v *SettingValue) pulumi.StringOutput { return v.SettingType }).(pulumi.StringOutput)
}

// The Setting's value. Type: `string`. It must be compatible with the `settingType`.
func (o SettingValueOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v *SettingValue) pulumi.StringOutput { return v.Value }).(pulumi.StringOutput)
}

type SettingValueArrayOutput struct{ *pulumi.OutputState }

func (SettingValueArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SettingValue)(nil)).Elem()
}

func (o SettingValueArrayOutput) ToSettingValueArrayOutput() SettingValueArrayOutput {
	return o
}

func (o SettingValueArrayOutput) ToSettingValueArrayOutputWithContext(ctx context.Context) SettingValueArrayOutput {
	return o
}

func (o SettingValueArrayOutput) Index(i pulumi.IntInput) SettingValueOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SettingValue {
		return vs[0].([]*SettingValue)[vs[1].(int)]
	}).(SettingValueOutput)
}

type SettingValueMapOutput struct{ *pulumi.OutputState }

func (SettingValueMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SettingValue)(nil)).Elem()
}

func (o SettingValueMapOutput) ToSettingValueMapOutput() SettingValueMapOutput {
	return o
}

func (o SettingValueMapOutput) ToSettingValueMapOutputWithContext(ctx context.Context) SettingValueMapOutput {
	return o
}

func (o SettingValueMapOutput) MapIndex(k pulumi.StringInput) SettingValueOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SettingValue {
		return vs[0].(map[string]*SettingValue)[vs[1].(string)]
	}).(SettingValueOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SettingValueInput)(nil)).Elem(), &SettingValue{})
	pulumi.RegisterInputType(reflect.TypeOf((*SettingValueArrayInput)(nil)).Elem(), SettingValueArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SettingValueMapInput)(nil)).Elem(), SettingValueMap{})
	pulumi.RegisterOutputType(SettingValueOutput{})
	pulumi.RegisterOutputType(SettingValueArrayOutput{})
	pulumi.RegisterOutputType(SettingValueMapOutput{})
}
