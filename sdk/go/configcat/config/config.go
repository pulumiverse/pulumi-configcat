// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

// ConfigCat Public Management API Base Path (defaults to production).
func GetBasePath(ctx *pulumi.Context) string {
	return config.Get(ctx, "configcat:basePath")
}

// ConfigCat Public API credential - Basic Auth Password
func GetBasicAuthPassword(ctx *pulumi.Context) string {
	return config.Get(ctx, "configcat:basicAuthPassword")
}

// ConfigCat Public API credential - Basic Auth Username.
func GetBasicAuthUsername(ctx *pulumi.Context) string {
	return config.Get(ctx, "configcat:basicAuthUsername")
}
