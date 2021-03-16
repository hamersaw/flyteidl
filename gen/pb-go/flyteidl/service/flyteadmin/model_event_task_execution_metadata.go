/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

type EventTaskExecutionMetadata struct {
	InstanceClass *TaskExecutionMetadataInstanceClass `json:"instance_class,omitempty"`
	// Generated unique name for this task execution used by the backend.
	GeneratedName string `json:"generated_name,omitempty"`
	// Includes information about how resource token allocation (if applicable).
	ManagedResourceInfo *EventManagedResourceInfo `json:"managed_resource_info,omitempty"`
}
