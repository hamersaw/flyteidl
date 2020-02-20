/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

// Defines extra information about the Node.
type CoreNodeMetadata struct {
	Name string `json:"name,omitempty"`
	// The overall timeout of a task.
	Timeout string `json:"timeout,omitempty"`
	// Number of retries per task.
	Retries *CoreRetryStrategy `json:"retries,omitempty"`
}
