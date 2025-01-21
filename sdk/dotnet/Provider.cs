// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Configcat
{
    /// <summary>
    /// The provider type for the configcat package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [ConfigcatResourceType("pulumi:providers:configcat")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// ConfigCat Public Management API's `base_path`. Defaults to [https://api.configcat.com](https://api.configcat.com). This
        /// can also be sourced from the `CONFIGCAT_BASE_PATH` Environment Variable.
        /// </summary>
        [Output("basePath")]
        public Output<string?> BasePath { get; private set; } = null!;

        /// <summary>
        /// Get your `basic_auth_password` at [ConfigCat Public API
        /// credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
        /// `CONFIGCAT_BASIC_AUTH_PASSWORD` Environment Variable.
        /// </summary>
        [Output("basicAuthPassword")]
        public Output<string?> BasicAuthPassword { get; private set; } = null!;

        /// <summary>
        /// Get your `basic_auth_username` at [ConfigCat Public API
        /// credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
        /// `CONFIGCAT_BASIC_AUTH_USERNAME` Environment Variable.
        /// </summary>
        [Output("basicAuthUsername")]
        public Output<string?> BasicAuthUsername { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("configcat", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "api://github.com/pulumiverse",
                AdditionalSecretOutputs =
                {
                    "basicAuthPassword",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// ConfigCat Public Management API's `base_path`. Defaults to [https://api.configcat.com](https://api.configcat.com). This
        /// can also be sourced from the `CONFIGCAT_BASE_PATH` Environment Variable.
        /// </summary>
        [Input("basePath")]
        public Input<string>? BasePath { get; set; }

        [Input("basicAuthPassword")]
        private Input<string>? _basicAuthPassword;

        /// <summary>
        /// Get your `basic_auth_password` at [ConfigCat Public API
        /// credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
        /// `CONFIGCAT_BASIC_AUTH_PASSWORD` Environment Variable.
        /// </summary>
        public Input<string>? BasicAuthPassword
        {
            get => _basicAuthPassword;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _basicAuthPassword = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Get your `basic_auth_username` at [ConfigCat Public API
        /// credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
        /// `CONFIGCAT_BASIC_AUTH_USERNAME` Environment Variable.
        /// </summary>
        [Input("basicAuthUsername")]
        public Input<string>? BasicAuthUsername { get; set; }

        public ProviderArgs()
        {
            BasePath = Utilities.GetEnv("CONFIGCAT_BASE_PATH");
            BasicAuthPassword = Utilities.GetEnv("CONFIGCAT_BASIC_AUTH_PASSWORD");
            BasicAuthUsername = Utilities.GetEnv("CONFIGCAT_BASIC_AUTH_USERNAME");
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
