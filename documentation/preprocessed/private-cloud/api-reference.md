---
title: API Reference
---
# API Reference
## Packages
 auth.qdrant.io/v1alpha1
 qdrant.io/v1
## auth.qdrant.io/v1alpha1
Package v1alpha1 contains API Schema definitions for the qdrant.io v1alpha1 API group
### Resource Types
 APIAuthentication
#### APIAuthentication
APIAuthentication is a configuration for authenticating against Qdrant clusters.
_Appears in:_
 APIAuthenticationList
`apiVersion` _string_ — `auth.qdrant.io/v1alpha1`
`kind` _string_ — `APIAuthentication`
`metadata` _ObjectMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`spec` _APIAuthenticationSpec_
#### APIAuthenticationSpec
APIAuthenticationSpec describes the configuration for authenticating against Qdrant clusters.
_Appears in:_
 APIAuthentication
`sha512` _string_ — SHA512 hash of an API key. — MaxLength: 128 MinLength: 128
`clusterIDs` _string array_ — List of cluster IDs for which the API key is valid
## qdrant.io/v1
Package v1 contains API Schema definitions for the qdrant.io v1 API group
### Resource Types
 QdrantCloudRegion
 QdrantCloudRegionList
 QdrantCluster
 QdrantClusterList
 QdrantClusterRestore
 QdrantClusterRestoreList
 QdrantClusterScheduledSnapshot
 QdrantClusterScheduledSnapshotList
 QdrantClusterSnapshot
 QdrantClusterSnapshotList
 QdrantEntity
 QdrantEntityList
 QdrantRelease
 QdrantReleaseList
#### ClusterManagerReponse
_Appears in:_
 QdrantClusterStatus
`lastResponseTime` _Time_ — The last time the cluster-manager responded in UTC
`executed_actions` _RawMessage_ — ExecutedActions are the actions that have been executed by the cluster-manager
`required_actions` _RawMessage_ — RequiredActions are the actions that are required to be executed by the operator as instructed by cluster-manager
`suggested_actions` _RawMessage_ — SuggestedActions are suggested but not required actions to be executed by the operator as instructed by cluster-manager
#### ClusterPhase
_Underlying type:_ _string_
_Appears in:_
 QdrantClusterStatus
`Creating`
`FailedToCreate`
`Updating`
`FailedToUpdate`
`Scaling`
`Upgrading`
`Suspending`
`Suspended`
`FailedToSuspend`
`Resuming`
`FailedToResume`
`Healthy`
`NotReady`
`RecoveryMode`
`ManualMaintenance`
#### ComponentPhase
_Underlying type:_ _string_
_Appears in:_
 ComponentStatus
`Ready`
`NotReady`
`Unknown`
`NotFound`
#### ComponentReference
_Appears in:_
 QdrantCloudRegionSpec
`apiVersion` _string_ — APIVersion is the group and version of the component being referenced.
`kind` _string_ — Kind is the type of component being referenced
`name` _string_ — Name is the name of component being referenced
`namespace` _string_ — Namespace is the namespace of component being referenced.
`markedForDeletion` _boolean_ — MarkedForDeletion specifies whether the component is marked for deletion
#### ComponentStatus
_Appears in:_
 QdrantCloudRegionStatus
`name` _string_ — Name specifies the name of the component
`namespace` _string_ — Namespace specifies the namespace of the component
`version` _string_ — Version specifies the version of the component
`phase` _ComponentPhase_ — Phase specifies the current phase of the component
`message` _string_ — Message specifies the info explaining the current phase of the component
#### EntityPhase
_Underlying type:_ _string_
_Appears in:_
 QdrantEntityStatus
`Creating`
`Ready`
`Updating`
`Failing`
`Deleting`
`Deleted`
#### EntityResult
_Underlying type:_ _string_
EntityResult is the last result from the invocation to a manager
_Appears in:_
 QdrantEntityStatusResult
`Ok`
`Pending`
`Error`
#### GPU
_Appears in:_
 QdrantClusterSpec
`gpuType` _GPUType_ — GPUType specifies the type of the GPU to use. If set, GPU indexing is enabled. — Enum: [nvidia amd]
`forceHalfPrecision` _boolean_ — ForceHalfPrecision for `f32` values while indexing.`f16` conversion will take placeonly inside GPU memory and won't affect storage type. — false
`deviceFilter` _string array_ — DeviceFilter for GPU devices by hardware name. Case-insensitive.List of substrings to match against the gpu device name.Example: [- "nvidia"]If not specified, all devices are accepted. — MinItems: 1
`devices` _string array_ — Devices is a List of explicit GPU devices to use.If host has multiple GPUs, this option allows to select specific devicesby their index in the list of found devices.If `deviceFilter` is set, indexes are applied after filtering.If not specified, all devices are accepted. — MinItems: 1
`parallelIndexes` _integer_ — ParallelIndexes is the number of parallel indexes to run on the GPU. — 1 — Minimum: 1
`groupsCount` _integer_ — GroupsCount is the amount of used vulkan "groups" of GPU.In other words, how many parallel points can be indexed by GPU.Optimal value might depend on the GPU model.Proportional, but doesn't necessary equal to the physical number of warps.Do not change this value unless you know what you are doing. — Minimum: 1
`allowIntegrated` _boolean_ — AllowIntegrated specifies whether to allow integrated GPUs to be used. — false
#### GPUType
_Underlying type:_ _string_
GPUType specifies the type of GPU to use.
_Validation:_
 Enum: [nvidia amd]
_Appears in:_
 GPU
`nvidia`
`amd`
#### HelmRelease
_Appears in:_
 QdrantCloudRegionSpec
`markedForDeletionAt` _string_ — MarkedForDeletionAt specifies the time when the helm release was marked for deletion
`object` _HelmRelease_ — Object specifies the helm release object — EmbeddedResource: \{\}
#### HelmRepository
_Appears in:_
 QdrantCloudRegionSpec
`markedForDeletionAt` _string_ — MarkedForDeletionAt specifies the time when the helm repository was marked for deletion
`object` _HelmRepository_ — Object specifies the helm repository object — EmbeddedResource: \{\}
#### InferenceConfig
_Appears in:_
 QdrantConfiguration
`enabled` _boolean_ — Enabled specifies whether to enable inference for the cluster or not. — false
#### Ingress
_Appears in:_
 QdrantClusterSpec
`enabled` _boolean_ — Enabled specifies whether to enable ingress for the cluster or not.
`annotations` _object (keys:string, values:string)_ — Annotations specifies annotations for the ingress.
`ingressClassName` _string_ — IngressClassName specifies the name of the ingress class
`host` _string_ — Host specifies the host for the ingress.
`tls` _boolean_ — TLS specifies whether to enable tls for the ingress.The default depends on the ingress provider:- KubernetesIngress: False- NginxIngress: False- QdrantCloudTraefik: Depending on the config.tls setting of the operator.
`tlsSecretName` _string_ — TLSSecretName specifies the name of the secret containing the tls certificate.
`nginx` _NGINXConfig_ — NGINX specifies the nginx ingress specific configurations.
`traefik` _TraefikConfig_ — Traefik specifies the traefik ingress specific configurations.
#### KubernetesDistribution
_Underlying type:_ _string_
_Appears in:_
 QdrantCloudRegionStatus
`unknown`
`aws`
`gcp`
`azure`
`do`
`scaleway`
`openshift`
`linode`
`civo`
`oci`
`ovhcloud`
`stackit`
`vultr`
`k3s`
#### KubernetesEventInfo
_Appears in:_
 NodePVCStatus
 NodeStatus
 VolumeSnapshotInfo
`message` _string_ — Event message
`reason` _string_ — Event reason
`count` _integer_ — How many times the event has occurred
`firstTimestamp` _Time_ — The first time the event was seen
`lastTimestamp` _Time_ — The last time the event was seen
#### KubernetesPod
_Appears in:_
 KubernetesStatefulSet
`annotations` _object (keys:string, values:string)_ — Annotations specifies the annotations for the Pods.
`labels` _object (keys:string, values:string)_ — Labels specifies the labels for the Pods.
`extraEnv` _EnvVar array_ — ExtraEnv specifies the extra environment variables for the Pods.
#### KubernetesService
_Appears in:_
 QdrantClusterSpec
`type` _ServiceType_ — Type specifies the type of the Service: "ClusterIP", "NodePort", "LoadBalancer". — ClusterIP
`annotations` _object (keys:string, values:string)_ — Annotations specifies the annotations for the Service.
#### KubernetesStatefulSet
_Appears in:_
 QdrantClusterSpec
`annotations` _object (keys:string, values:string)_ — Annotations specifies the annotations for the StatefulSet.
`pods` _KubernetesPod_ — Pods specifies the configuration of the Pods of the Qdrant StatefulSet.
#### MetricSource
_Underlying type:_ _string_
_Appears in:_
 Monitoring
`kubelet`
`api`
#### Monitoring
_Appears in:_
 QdrantCloudRegionStatus
`cAdvisorMetricSource` _MetricSource_ — CAdvisorMetricSource specifies the cAdvisor metric source
`nodeMetricSource` _MetricSource_ — NodeMetricSource specifies the node metric source
#### NGINXConfig
_Appears in:_
 Ingress
`allowedSourceRanges` _string array_ — AllowedSourceRanges specifies the allowed CIDR source ranges for the ingress.
`grpcHost` _string_ — GRPCHost specifies the host name for the GRPC ingress.
#### NodeInfo
_Appears in:_
 QdrantCloudRegionStatus
`name` _string_ — Name specifies the name of the node
`region` _string_ — Region specifies the region of the node
`zone` _string_ — Zone specifies the zone of the node
`instanceType` _string_ — InstanceType specifies the instance type of the node
`arch` _string_ — Arch specifies the CPU architecture of the node
`capacity` _NodeResourceInfo_ — Capacity specifies the capacity of the node
`allocatable` _NodeResourceInfo_ — Allocatable specifies the allocatable resources of the node
#### NodePVCStatus
_Appears in:_
 NodeStatus
`storageClassName` _string_ — Name of the StorageClass used by the PVC
`phase` _PersistentVolumeClaimPhase_ — Status phase of the PVC
`conditions` _PersistentVolumeClaimCondition array_ — Conditions of the PVC
`events` _KubernetesEventInfo array_ — Recent Kubernetes Events related to the PVCEvents that happened in the last 30 minutes are stored.
`capacity` _ResourceList_ — capacity represents the actual resources of the underlying volume.
`currentVolumeAttributesClassName` _string_ — currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using.When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim
`modifyVolumeStatus` _ModifyVolumeStatus_ — ModifyVolumeStatus represents the status object of ControllerModifyVolume operation.When this is unset, there is no ModifyVolume operation being attempted.
#### NodeResourceInfo
_Appears in:_
 NodeInfo
`cpu` _string_ — CPU specifies the CPU resources of the node
`memory` _string_ — Memory specifies the memory resources of the node
`pods` _string_ — Pods specifies the pods resources of the node
`ephemeralStorage` _string_ — EphemeralStorage specifies the ephemeral storage resources of the node
#### NodeStatus
_Appears in:_
 QdrantClusterStatus
`name` _string_ — Name specifies the name of the node
`started_at` _string_ — StartedAt specifies the time when the node started (in RFC3339 format)
`state` _object (keys:PodConditionType, values:ConditionStatus)_ — States specifies the condition states of the node
`version` _string_ — Version specifies the version of Qdrant running on the node
`liveness` _boolean_ — Reports if qdrant node responded to liveness request (before readiness).This is needed to beter report recovery process to the user.
`podPhase` _PodPhase_ — Status phase of the Pod of the node
`podConditions` _PodCondition array_ — Conditions of the Pod of the node
`podMessage` _string_ — Status message of the Pod of the node
`podReason` _string_ — Status reason of the Pod of the node
`containerStatuses` _ContainerStatus array_ — Details container statuses of the Pod of the node
`events` _KubernetesEventInfo array_ — Recent Kubernetes Events related to the Pod of the nodeEvents that happened in the last 30 minutes are stored.
`restartCount` _integer_ — The number of times the main qdrant container has been restarted.
`databasePVCStatus` _NodePVCStatus_ — Status of the database storage PVC
`snapshotsPVCStatus` _NodePVCStatus_ — Status of the snapshots storage PVC
#### Pause
_Appears in:_
 QdrantClusterSpec
`owner` _string_ — Owner specifies the owner of the pause request.
`reason` _string_ — Reason specifies the reason for the pause request.
`creationTimestamp` _string_ — CreationTimestamp specifies the time when the pause request was created.
#### QdrantCloudRegion
QdrantCloudRegion is the Schema for the qdrantcloudregions API
_Appears in:_
 QdrantCloudRegionList
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantCloudRegion`
`metadata` _ObjectMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`spec` _QdrantCloudRegionSpec_
#### QdrantCloudRegionList
QdrantCloudRegionList contains a list of QdrantCloudRegion
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantCloudRegionList`
`metadata` _ListMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`items` _QdrantCloudRegion array_
#### QdrantCloudRegionSpec
QdrantCloudRegionSpec defines the desired state of QdrantCloudRegion
_Appears in:_
 QdrantCloudRegion
`id` _string_ — Id specifies the unique identifier of the region
`components` _ComponentReference array_ — Components specifies the list of components to be installed in the region
`helmRepositories` _HelmRepository array_ — HelmRepositories specifies the list of helm repositories to be created to the regionDeprecated: Use "Components" instead
`helmReleases` _HelmRelease array_ — HelmReleases specifies the list of helm releases to be created to the regionDeprecated: Use "Components" instead
#### QdrantCluster
QdrantCluster is the Schema for the qdrantclusters API
_Appears in:_
 QdrantClusterList
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantCluster`
`metadata` _ObjectMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`spec` _QdrantClusterSpec_
#### QdrantClusterList
QdrantClusterList contains a list of QdrantCluster
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantClusterList`
`metadata` _ListMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`items` _QdrantCluster array_
#### QdrantClusterRestore
QdrantClusterRestore is the Schema for the qdrantclusterrestores API
_Appears in:_
 QdrantClusterRestoreList
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantClusterRestore`
`metadata` _ObjectMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`spec` _QdrantClusterRestoreSpec_
#### QdrantClusterRestoreList
QdrantClusterRestoreList contains a list of QdrantClusterRestore objects
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantClusterRestoreList`
`metadata` _ListMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`items` _QdrantClusterRestore array_
#### QdrantClusterRestoreSpec
QdrantClusterRestoreSpec defines the desired state of QdrantClusterRestore
_Appears in:_
 QdrantClusterRestore
`source` _RestoreSource_ — Source defines the source snapshot from which the restore will be done
`destination` _RestoreDestination_ — Destination defines the destination cluster where the source data will end up
#### QdrantClusterScheduledSnapshot
QdrantClusterScheduledSnapshot is the Schema for the qdrantclusterscheduledsnapshots API
_Appears in:_
 QdrantClusterScheduledSnapshotList
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantClusterScheduledSnapshot`
`metadata` _ObjectMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`spec` _QdrantClusterScheduledSnapshotSpec_
#### QdrantClusterScheduledSnapshotList
QdrantClusterScheduledSnapshotList contains a list of QdrantCluster
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantClusterScheduledSnapshotList`
`metadata` _ListMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`items` _QdrantClusterScheduledSnapshot array_
#### QdrantClusterScheduledSnapshotSpec
QdrantClusterScheduledSnapshotSpec defines the desired state of QdrantCluster
_Appears in:_
 QdrantClusterScheduledSnapshot
`cluster-id` _string_ — Id specifies the unique identifier of the cluster
`scheduleShortId` _string_ — Specifies short Id which identifies a schedule — MaxLength: 8
`retention` _string_ — Retention of schedule in hours — Pattern: `^[0-9]+h$`
#### QdrantClusterSnapshot
QdrantClusterSnapshot is the Schema for the qdrantclustersnapshots API
_Appears in:_
 QdrantClusterSnapshotList
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantClusterSnapshot`
`metadata` _ObjectMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`spec` _QdrantClusterSnapshotSpec_
#### QdrantClusterSnapshotList
QdrantClusterSnapshotList contains a list of QdrantClusterSnapshot
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantClusterSnapshotList`
`metadata` _ListMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`items` _QdrantClusterSnapshot array_
#### QdrantClusterSnapshotPhase
_Underlying type:_ _string_
_Appears in:_
 QdrantClusterSnapshotStatus
`Running`
`Skipped`
`Failed`
`Succeeded`
#### QdrantClusterSnapshotSpec
_Appears in:_
 QdrantClusterSnapshot
`cluster-id` _string_ — The cluster ID for which a Snapshot need to be takenThe cluster should be in the same namespace as this QdrantClusterSnapshot is located
`creation-timestamp` _integer_ — The CreationTimestamp of the backup (expressed in Unix epoch format)
`scheduleShortId` _string_ — Specifies the short Id which identifies a schedule, if any.This field should not be set if the backup is made manually. — MaxLength: 8
`retention` _string_ — The retention period of this snapshot in hours, if any.If not set, the backup doesn't have a retention period, meaning it will not be removed. — Pattern: `^[0-9]+h$`
#### QdrantClusterSpec
QdrantClusterSpec defines the desired state of QdrantCluster
_Appears in:_
 QdrantCluster
`id` _string_ — Id specifies the unique identifier of the cluster
`version` _string_ — Version specifies the version of Qdrant to deploy
`size` _integer_ — Size specifies the desired number of Qdrant nodes in the cluster — Maximum: 100 Minimum: 1
`servicePerNode` _boolean_ — ServicePerNode specifies whether the cluster should start a dedicated service for each node. — true
`clusterManager` _boolean_ — ClusterManager specifies whether to use the cluster manager for this cluster.The Python-operator will deploy a dedicated cluster manager instance.The Go-operator will use a shared instance.If not set, the default will be taken from the operator config.
`suspend` _boolean_ — Suspend specifies whether to suspend the cluster.If enabled, the cluster will be suspended and all related resources will be removed except the PVCs. — false
`pauses` _Pause array_ — Pauses specifies a list of pause request by developer for manual maintenance.Operator will skip handling any changes in the CR if any pause request is present.
`image` _QdrantImage_ — Image specifies the image to use for each Qdrant node.
`resources` _Resources_ — Resources specifies the resources to allocate for each Qdrant node.
`security` _QdrantSecurityContext_ — Security specifies the security context for each Qdrant node.
`tolerations` _Toleration array_ — Tolerations specifies the tolerations for each Qdrant node.
`nodeSelector` _object (keys:string, values:string)_ — NodeSelector specifies the node selector for each Qdrant node.
`config` _QdrantConfiguration_ — Config specifies the Qdrant configuration setttings for the clusters.
`ingress` _Ingress_ — Ingress specifies the ingress for the cluster.
`service` _KubernetesService_ — Service specifies the configuration of the Qdrant Kubernetes Service.
`gpu` _GPU_ — GPU specifies GPU configuration for the cluster. If this field is not set, no GPU will be used.
`statefulSet` _KubernetesStatefulSet_ — StatefulSet specifies the configuration of the Qdrant Kubernetes StatefulSet.
`storageClassNames` _StorageClassNames_ — StorageClassNames specifies the storage class names for db and snapshots.
`storage` _Storage_ — Storage specifies the storage specification for the PVCs of the cluster. If the field is not set, no configuration will be applied.
`topologySpreadConstraints` _TopologySpreadConstraint_ — TopologySpreadConstraints specifies the topology spread constraints for the cluster.
`podDisruptionBudget` _PodDisruptionBudgetSpec_ — PodDisruptionBudget specifies the pod disruption budget for the cluster.
`restartAllPodsConcurrently` _boolean_ — RestartAllPodsConcurrently specifies whether to restart all pods concurrently (also called one-shot-restart).If enabled, all the pods in the cluster will be restarted concurrently in situations where multiple podsneed to be restarted, like when RestartedAtAnnotationKey is added/updated or the Qdrant version needs to be upgraded.This helps sharded but not replicated clusters to reduce downtime to a possible minimum during restart.If unset, the operator is going to restart nodes concurrently if none of the collections if replicated.
`startupDelaySeconds` _integer_ — If StartupDelaySeconds is set (> 0), an additional 'sleep ' will be emitted to the pod startup.The sleep will be added when a pod is restarted, it will not force any pod to restart.This feature can be used for debugging the core, e.g. if a pod is in crash loop, it provided a wayto inspect the attached storage.
`rebalanceStrategy` _RebalanceStrategy_ — RebalanceStrategy specifies the strategy to use for automaticially rebalancing shards the cluster.Cluster-manager needs to be enabled for this feature to work. — Enum: [by_count by_size by_count_and_size]
`readClusters` _ReadCluster array_ — ReadClusters specifies the read clusters for this cluster to synchronize.Cluster-manager needs to be enabled for this feature to work.
`writeCluster` _WriteCluster_ — WriteCluster specifies the write cluster for this cluster. This configures the NetworkPolicy to allow egress to the write cluster.
#### QdrantConfiguration
_Appears in:_
 QdrantClusterSpec
`collection` _QdrantConfigurationCollection_ — Collection specifies the default collection configuration for Qdrant.
`log_level` _string_ — LogLevel specifies the log level for Qdrant.
`service` _QdrantConfigurationService_ — Service specifies the service level configuration for Qdrant.
`tls` _QdrantConfigurationTLS_ — TLS specifies the TLS configuration for Qdrant.
`storage` _StorageConfig_ — Storage specifies the storage configuration for Qdrant.
`inference` _InferenceConfig_ — Inference configuration. This is used in Qdrant Managed Cloud only. If not set Inference is not available to this cluster.
#### QdrantConfigurationCollection
_Appears in:_
 QdrantConfiguration
`replication_factor` _integer_ — ReplicationFactor specifies the default number of replicas of each shard
`write_consistency_factor` _integer_ — WriteConsistencyFactor specifies how many replicas should apply the operation to consider it successful
`vectors` _QdrantConfigurationCollectionVectors_ — Vectors specifies the default parameters for vectors
`strict_mode` _QdrantConfigurationCollectionStrictMode_ — StrictMode specifies the strict mode configuration for the collection
#### QdrantConfigurationCollectionStrictMode
_Appears in:_
 QdrantConfigurationCollection
`max_payload_index_count` _integer_ — MaxPayloadIndexCount represents the maximal number of payload indexes allowed to be created.It can be set for Qdrant version >= 1.16.0Default to 100 if omitted and Qdrant version >= 1.16.0 — Minimum: 1
#### QdrantConfigurationCollectionVectors
_Appears in:_
 QdrantConfigurationCollection
`on_disk` _boolean_ — OnDisk specifies whether vectors should be stored in memory or on disk.
#### QdrantConfigurationService
_Appears in:_
 QdrantConfiguration
`api_key` _QdrantSecretKeyRef_ — ApiKey for the qdrant instance
`read_only_api_key` _QdrantSecretKeyRef_ — ReadOnlyApiKey for the qdrant instance
`jwt_rbac` _boolean_ — JwtRbac specifies whether to enable jwt rbac for the qdrant instanceDefault is false
`hide_jwt_dashboard` _boolean_ — HideJwtDashboard specifies whether to hide the JWT dashboard of the embedded UIDefault is false
`enable_tls` _boolean_ — EnableTLS specifies whether to enable tls for the qdrant instanceDefault is false
`max_request_size_mb` _integer_ — MaxRequestSizeMb specifies them maximum size of POST data in a single request in megabytesDefault, if not set is 32 (MB)
#### QdrantConfigurationTLS
_Appears in:_
 QdrantConfiguration
`cert` _QdrantSecretKeyRef_ — Reference to the secret containing the server certificate chain file
`key` _QdrantSecretKeyRef_ — Reference to the secret containing the server private key file
`caCert` _QdrantSecretKeyRef_ — Reference to the secret containing the CA certificate file
#### QdrantEntity
QdrantEntity is the Schema for the qdrantentities API
_Appears in:_
 QdrantEntityList
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantEntity`
`metadata` _ObjectMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`spec` _QdrantEntitySpec_
#### QdrantEntityList
QdrantEntityList contains a list of QdrantEntity objects
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantEntityList`
`metadata` _ListMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`items` _QdrantEntity array_
#### QdrantEntitySpec
QdrantEntitySpec defines the desired state of QdrantEntity
_Appears in:_
 QdrantEntity
`id` _string_ — The unique identifier of the entity (in UUID format).
`entityType` _string_ — The type of the entity.
`clusterId` _string_ — The optional cluster identifier
`createdAt` _MicroTime_ — Timestamp when the entity was created.
`lastUpdatedAt` _MicroTime_ — Timestamp when the entity was last updated.
`deletedAt` _MicroTime_ — Timestamp when the entity was deleted (or is started to be deleting).If not set the entity is not deleted
`payload` _JSON_ — Generic payload for this entity
#### QdrantEntityStatusResult
QdrantEntityStatusResult is the last result from the invocation to a manager
_Appears in:_
 QdrantEntityStatus
`result` _EntityResult_ — The result of last reconcile of the entity — Enum: [Ok Pending Error]
`reason` _string_ — The reason of the result (e.g. in case of an error)
`payload` _JSON_ — The optional payload of the status.
#### QdrantImage
_Appears in:_
 QdrantClusterSpec
`repository` _string_ — Repository specifies the repository of the Qdrant image.If not specified defaults the config of the operator (or qdrant/qdrant if not specified in operator).
`pullPolicy` _PullPolicy_ — PullPolicy specifies the image pull policy for the Qdrant image.If not specified defaults the config of the operator (or IfNotPresent if not specified in operator).
`pullSecretName` _string_ — PullSecretName specifies the pull secret for the Qdrant image.
#### QdrantRelease
QdrantRelease describes an available Qdrant release
_Appears in:_
 QdrantReleaseList
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantRelease`
`metadata` _ObjectMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`spec` _QdrantReleaseSpec_
#### QdrantReleaseList
QdrantReleaseList contains a list of QdrantRelease
`apiVersion` _string_ — `qdrant.io/v1`
`kind` _string_ — `QdrantReleaseList`
`metadata` _ListMeta_ — Refer to Kubernetes API documentation for fields of `metadata`.
`items` _QdrantRelease array_
#### QdrantReleaseSpec
QdrantReleaseSpec defines the desired state of QdrantRelease
_Appears in:_
 QdrantRelease
`version` _string_ — Version number (should be semver compliant).E.g. "v1.10.1"
`default` _boolean_ — If set, this version is default for new clusters on Cloud.There should be only 1 Qdrant version in the platform set as default. — false
`image` _string_ — Full docker image to use for this version.If empty, a default image will be derived from Version (and qdrant/qdrant is assumed).
`unavailable` _boolean_ — If set, this version cannot be used for new clusters. — false
`endOfLife` _boolean_ — If set, this version is no longer actively supported. — false
`accountIds` _string array_ — If set, this version can only be used by accounts with given IDs.
`accountPrivileges` _string array_ — If set, this version can only be used by accounts that have been given the listed privileges.
`remarks` _string_ — General remarks for human reading
`releaseNotesURL` _string_ — Release Notes URL for the specified version
#### QdrantSecretKeyRef
_Appears in:_
 QdrantConfigurationService
 QdrantConfigurationTLS
`secretKeyRef` _SecretKeySelector_ — SecretKeyRef to the secret containing data to configure the qdrant instance
#### QdrantSecurityContext
_Appears in:_
 QdrantClusterSpec
`user` _integer_ — User specifies the user to run the Qdrant process as.
`group` _integer_ — Group specifies the group to run the Qdrant process as.
`fsGroup` _integer_ — FsGroup specifies file system group to run the Qdrant process as.
#### ReadCluster
_Appears in:_
 QdrantClusterSpec
`id` _string_ — Id specifies the unique identifier of the read cluster
#### RebalanceStrategy
_Underlying type:_ _string_
RebalanceStrategy specifies the strategy to use for automaticially rebalancing shards the cluster.
_Validation:_
 Enum: [by_count by_size by_count_and_size]
_Appears in:_
 QdrantClusterSpec
`by_count`
`by_size`
`by_count_and_size`
#### RegionCapabilities
_Appears in:_
 QdrantCloudRegionStatus
`volumeSnapshot` _boolean_ — VolumeSnapshot specifies whether the Kubernetes cluster supports volume snapshot
`volumeExpansion` _boolean_ — VolumeExpansion specifies whether the Kubernetes cluster supports volume expansion
#### RegionPhase
_Underlying type:_ _string_
_Appears in:_
 QdrantCloudRegionStatus
`Ready`
`NotReady`
`FailedToSync`
#### ResourceRequests
_Appears in:_
 Resources
`cpu` _string_ — CPU specifies the CPU request for each Qdrant node.
`memory` _string_ — Memory specifies the memory request for each Qdrant node.
#### Resources
_Appears in:_
 QdrantClusterSpec
`cpu` _string_ — CPU specifies the CPU limit for each Qdrant node.
`memory` _string_ — Memory specifies the memory limit for each Qdrant node.
`storage` _string_ — Storage specifies the storage amount for each Qdrant node.
`requests` _ResourceRequests_ — Requests specifies the resource requests for each Qdrant node.
#### RestoreDestination
_Appears in:_
 QdrantClusterRestoreSpec
`name` _string_ — Name of the destination cluster
`namespace` _string_ — Namespace of the destination cluster
`create` _boolean_ — Create when set to true indicates thata new cluster with the specified name should be created.Otherwise, if set to false, the existing cluster is going to be restoredto the specified state.
#### RestorePhase
_Underlying type:_ _string_
_Appears in:_
 QdrantClusterRestoreStatus
`Running`
`Skipped`
`Failed`
`Succeeded`
`Pending`
#### RestoreSource
_Appears in:_
 QdrantClusterRestoreSpec
`snapshotName` _string_ — SnapshotName is the name of the snapshot from which we wish to restore
`namespace` _string_ — Namespace of the snapshot
#### ScheduledSnapshotPhase
_Underlying type:_ _string_
_Appears in:_
 QdrantClusterScheduledSnapshotStatus
`Active`
`Disabled`
#### Storage
_Appears in:_
 QdrantClusterSpec
`volumeAttributesClassName` _string_ — VolumeAttributesClassName specifies VolumeAttributeClass name to use for the storage PVCs
`iops` _integer_ — IOPS defines the IOPS number to configure for the storage PVCs
`throughput` _integer_ — Throughput defines the throughput number in MB/s for the storage PVCs
#### StorageClass
_Appears in:_
 QdrantCloudRegionStatus
`name` _string_ — Name specifies the name of the storage class
`default` _boolean_ — Default specifies whether the storage class is the default storage class
`provisioner` _string_ — Provisioner specifies the provisioner of the storage class
`allowVolumeExpansion` _boolean_ — AllowVolumeExpansion specifies whether the storage class allows volume expansion
`reclaimPolicy` _string_ — ReclaimPolicy specifies the reclaim policy of the storage class
`parameters` _object (keys:string, values:string)_ — Parameters specifies the parameters of the storage class
#### StorageClassNames
_Appears in:_
 QdrantClusterSpec
`db` _string_ — DB specifies the storage class name for db volume.
`snapshots` _string_ — Snapshots specifies the storage class name for snapshots volume.
#### StorageConfig
_Appears in:_
 QdrantConfiguration
`performance` _StoragePerformanceConfig_ — Performance configuration
`maxCollections` _integer_ — MaxCollections represents the maximal number of collections allowed to be created.It can be set for Qdrant version >= 1.14.1Default to 1000 if omitted and Qdrant version >= 1.15.0 — Minimum: 1
#### StoragePerformanceConfig
_Appears in:_
 StorageConfig
`optimizer_cpu_budget` _integer_ — OptimizerCPUBudget defines the number of CPU allocation.If 0 auto selection, keep 1 or more CPUs unallocated depending on CPU sizeIf negative subtract this number of CPUs from the available CPUs.If positive use this exact number of CPUs.
`async_scorer` _boolean_ — AsyncScorer enables io_uring when rescoring
#### TraefikConfig
_Appears in:_
 Ingress
`allowedSourceRanges` _string array_ — AllowedSourceRanges specifies the allowed CIDR source ranges for the ingress.
`entryPoints` _string array_ — EntryPoints is the list of traefik entry points to use for the ingress route.If nothing is set, it will take the entryPoints configured in the operator config.
#### VolumeSnapshotClass
_Appears in:_
 QdrantCloudRegionStatus
`name` _string_ — Name specifies the name of the volume snapshot class
`driver` _string_ — Driver specifies the driver of the volume snapshot class
#### VolumeSnapshotInfo
_Appears in:_
 QdrantClusterSnapshotStatus
`volumeSnapshotName` _string_ — VolumeSnapshotName is the name of the volume snapshot
`volumeName` _string_ — VolumeName is the name of the volume that was backed up
`readyToUse` _boolean_ — ReadyToUse indicates if the volume snapshot is ready to use
`snapshotHandle` _string_ — SnapshotHandle is the identifier of the volume snapshot in the respective cloud provider
`error` _VolumeSnapshotError_ — Error contains the error details if the snapshot creation failed
`events` _KubernetesEventInfo array_ — Recent Kubernetes Events related to the VolumeSnapshotEvents that happened in the last 30 minutes are stored.
#### WriteCluster
_Appears in:_
 QdrantClusterSpec
`id` _string_ — Id specifies the unique identifier of the write cluster
