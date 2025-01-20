// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package configcat

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-configcat/sdk/v3/go/configcat/internal"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "configcat:index/configuration:Configuration":
		r = &Configuration{}
	case "configcat:index/environment:Environment":
		r = &Environment{}
	case "configcat:index/permissionGroup:PermissionGroup":
		r = &PermissionGroup{}
	case "configcat:index/product:Product":
		r = &Product{}
	case "configcat:index/segment:Segment":
		r = &Segment{}
	case "configcat:index/setting:Setting":
		r = &Setting{}
	case "configcat:index/settingTag:SettingTag":
		r = &SettingTag{}
	case "configcat:index/settingValue:SettingValue":
		r = &SettingValue{}
	case "configcat:index/tag:Tag":
		r = &Tag{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:configcat" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"configcat",
		"index/configuration",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"configcat",
		"index/environment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"configcat",
		"index/permissionGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"configcat",
		"index/product",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"configcat",
		"index/segment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"configcat",
		"index/setting",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"configcat",
		"index/settingTag",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"configcat",
		"index/settingValue",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"configcat",
		"index/tag",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"configcat",
		&pkg{version},
	)
}
