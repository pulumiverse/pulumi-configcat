// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Configcat.Outputs
{

    [OutputType]
    public sealed class GetPermissionGroupsPermissionGroupResult
    {
        /// <summary>
        /// Represent the Feature Management permission. Possible values: readOnly, full, custom
        /// </summary>
        public readonly string Accesstype;
        /// <summary>
        /// Group members can create/update Configs.
        /// </summary>
        public readonly bool CanCreateorupdateConfig;
        /// <summary>
        /// Group members can create/update Environments.
        /// </summary>
        public readonly bool CanCreateorupdateEnvironment;
        /// <summary>
        /// Group members can create/update Segments.
        /// </summary>
        public readonly bool CanCreateorupdateSegment;
        /// <summary>
        /// Group members can create/update Feature Flags and Settings.
        /// </summary>
        public readonly bool CanCreateorupdateSetting;
        /// <summary>
        /// Group members can create/update Tags.
        /// </summary>
        public readonly bool CanCreateorupdateTag;
        /// <summary>
        /// Group members can delete Configs.
        /// </summary>
        public readonly bool CanDeleteConfig;
        /// <summary>
        /// Group members can delete Environments.
        /// </summary>
        public readonly bool CanDeleteEnvironment;
        /// <summary>
        /// Group members can delete Segments.
        /// </summary>
        public readonly bool CanDeleteSegment;
        /// <summary>
        /// Group members can delete Feature Flags and Settings.
        /// </summary>
        public readonly bool CanDeleteSetting;
        /// <summary>
        /// Group members can delete Tags.
        /// </summary>
        public readonly bool CanDeleteTag;
        /// <summary>
        /// Group members can disable two-factor authentication for other members.
        /// </summary>
        public readonly bool CanDisable2fa;
        /// <summary>
        /// Group members can add and configure integrations.
        /// </summary>
        public readonly bool CanManageIntegrations;
        /// <summary>
        /// Group members can manage team members.
        /// </summary>
        public readonly bool CanManageMembers;
        /// <summary>
        /// Group members can update Product preferences.
        /// </summary>
        public readonly bool CanManageProductPreferences;
        /// <summary>
        /// Group members can create/update/delete Webhooks.
        /// </summary>
        public readonly bool CanManageWebhook;
        /// <summary>
        /// Group members can rotate SDK keys.
        /// </summary>
        public readonly bool CanRotateSdkkey;
        /// <summary>
        /// Group members can attach/detach Tags to Feature Flags and Settings.
        /// </summary>
        public readonly bool CanTagSetting;
        /// <summary>
        /// Group members can use the export/import feature.
        /// </summary>
        public readonly bool CanUseExportimport;
        /// <summary>
        /// Group members has access to audit logs.
        /// </summary>
        public readonly bool CanViewProductAuditlog;
        /// <summary>
        /// Group members has access to product statistics.
        /// </summary>
        public readonly bool CanViewProductStatistics;
        /// <summary>
        /// Group members has access to SDK keys.
        /// </summary>
        public readonly bool CanViewSdkkey;
        /// <summary>
        /// The environment specific permissions map block. Keys are the Environment IDs and the values represent the environment specific Feature Management permission. Possible values: full, readOnly
        /// </summary>
        public readonly ImmutableDictionary<string, string> EnvironmentAccesses;
        /// <summary>
        /// The name of the Permission Group.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Represent the environment specific Feature Management permission for new Environments. Possible values: full, readOnly, none
        /// </summary>
        public readonly string NewEnvironmentAccesstype;
        /// <summary>
        /// The unique Permission Group ID.
        /// </summary>
        public readonly int PermissionGroupId;

        [OutputConstructor]
        private GetPermissionGroupsPermissionGroupResult(
            string accesstype,

            bool canCreateorupdateConfig,

            bool canCreateorupdateEnvironment,

            bool canCreateorupdateSegment,

            bool canCreateorupdateSetting,

            bool canCreateorupdateTag,

            bool canDeleteConfig,

            bool canDeleteEnvironment,

            bool canDeleteSegment,

            bool canDeleteSetting,

            bool canDeleteTag,

            bool canDisable2fa,

            bool canManageIntegrations,

            bool canManageMembers,

            bool canManageProductPreferences,

            bool canManageWebhook,

            bool canRotateSdkkey,

            bool canTagSetting,

            bool canUseExportimport,

            bool canViewProductAuditlog,

            bool canViewProductStatistics,

            bool canViewSdkkey,

            ImmutableDictionary<string, string> environmentAccesses,

            string name,

            string newEnvironmentAccesstype,

            int permissionGroupId)
        {
            Accesstype = accesstype;
            CanCreateorupdateConfig = canCreateorupdateConfig;
            CanCreateorupdateEnvironment = canCreateorupdateEnvironment;
            CanCreateorupdateSegment = canCreateorupdateSegment;
            CanCreateorupdateSetting = canCreateorupdateSetting;
            CanCreateorupdateTag = canCreateorupdateTag;
            CanDeleteConfig = canDeleteConfig;
            CanDeleteEnvironment = canDeleteEnvironment;
            CanDeleteSegment = canDeleteSegment;
            CanDeleteSetting = canDeleteSetting;
            CanDeleteTag = canDeleteTag;
            CanDisable2fa = canDisable2fa;
            CanManageIntegrations = canManageIntegrations;
            CanManageMembers = canManageMembers;
            CanManageProductPreferences = canManageProductPreferences;
            CanManageWebhook = canManageWebhook;
            CanRotateSdkkey = canRotateSdkkey;
            CanTagSetting = canTagSetting;
            CanUseExportimport = canUseExportimport;
            CanViewProductAuditlog = canViewProductAuditlog;
            CanViewProductStatistics = canViewProductStatistics;
            CanViewSdkkey = canViewSdkkey;
            EnvironmentAccesses = environmentAccesses;
            Name = name;
            NewEnvironmentAccesstype = newEnvironmentAccesstype;
            PermissionGroupId = permissionGroupId;
        }
    }
}
