/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

// A map of Parameters in the form of repeated map entries.
type CoreParameterMap struct {
	// Defines a map of parameter names to parameters.
	Parameters []CoreParameterMapEntry `json:"parameters,omitempty"`
}
