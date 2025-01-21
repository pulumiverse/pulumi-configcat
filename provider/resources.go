// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package configcat

import (
	"fmt"
	"path/filepath"

	// The linter requires unnamed imports to have a doc comment
	_ "embed"

	configcat "github.com/configcat/terraform-provider-configcat/v5/providerlink"

	pf "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	tks "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"

	"github.com/pulumiverse/pulumi-configcat/provider/v5/pkg/version"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "configcat"
	// modules:
	mainMod = "index" // the configcat module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(_ resource.PropertyMap, _ shim.ResourceConfig) error {
	return nil
}

//go:embed cmd/pulumi-resource-configcat/bridge-metadata.json
var metadata []byte

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := pf.ShimProvider(configcat.New(version.Version)())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:    p,
		Name: "configcat",
		// DisplayName is a way to be able to change the casing of the provider
		// name when being displayed on the Pulumi registry
		DisplayName: "ConfigCat",
		// The default publisher for all packages is Pulumi.
		// Change this to your personal name (or a company name) that you
		// would like to be shown in the Pulumi Registry if this package is published
		// there.
		Publisher: "Pulumiverse",
		// LogoURL is optional but useful to help identify your package in the Pulumi Registry
		// if this package is published there.
		//
		// You may host a logo on a domain you control or add an SVG logo for your package
		// in your repository and use the raw content URL for that file as your logo URL.
		LogoURL: "https://raw.githubusercontent.com/pulumiverse/pulumi-configcat/refs/heads/main/docs/configcat-logo.png",
		// PluginDownloadURL is an optional URL used to download the Provider
		// for use in Pulumi programs
		// e.g https://github.com/org/pulumi-provider-name/releases/
		PluginDownloadURL: "api://github.com/pulumiverse",
		Description:       "A Pulumi package for creating and managing configcat cloud resources.",
		// category/cloud tag helps with categorizing the package in the Pulumi Registry.
		// For all available categories, see `Keywords` in
		// https://www.pulumi.com/docs/guides/pulumi-packages/schema/#package.
		Keywords:   []string{"pulumi", "configcat", "category/cloud"},
		License:    "Apache-2.0",
		Homepage:   "https://www.pulumi.com",
		Repository: "https://github.com/pulumiverse/pulumi-configcat",
		// The GitHub Org for the provider - defaults to `terraform-providers`
		GitHubOrg:    "configcat",
		MetadataInfo: tfbridge.NewProviderMetadata(metadata),
		Config: map[string]*tfbridge.SchemaInfo{
			"basic_auth_username": {
				Type: "string",
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"CONFIGCAT_BASIC_AUTH_USERNAME"},
				},
			},
			"basic_auth_password": {
				Type:   "string",
				Secret: tfbridge.True(),
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"CONFIGCAT_BASIC_AUTH_PASSWORD"},
				},
			},
			"base_path": {
				Type:           "string",
				MarkAsOptional: tfbridge.True(),
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"CONFIGCAT_BASE_PATH"},
				},
			},
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"configcat_config": {
				// Changed from Config to Configuration to not conflict with Pulumi's generated provider `Config` type.
				Tok: tfbridge.MakeResource(mainPkg, mainMod, "Configuration"),
			},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Changed from getConfig to getConfiguration to align with the similarly named resource type.
			"configcat_configs": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getConfigurations")},
			"configcat_sdkkeys": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getSdkKeys")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@pulumiverse/configcat",
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			RespectSchemaVersion: true,
		},
		Python: &tfbridge.PythonInfo{
			PackageName:          "pulumiverse_configcat",
			PyProject:            struct{ Enabled bool }{true},
			RespectSchemaVersion: true,
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumiverse/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
			RespectSchemaVersion:           true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace:        "Pulumiverse",
			RespectSchemaVersion: true,
		},
	}

	prov.MustComputeTokens(
		tks.SingleModule(
			"configcat_",
			"index",
			tks.MakeStandard(mainPkg),
		),
	)

	prov.SetAutonaming(255, "-")
	prov.MustApplyAutoAliases()

	return prov
}
