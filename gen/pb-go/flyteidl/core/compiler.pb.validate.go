// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: flyteidl/core/compiler.proto

package core

import (
	"bytes"
	"errors"
	"fmt"
	"net"
	"net/mail"
	"net/url"
	"regexp"
	"strings"
	"time"
	"unicode/utf8"

	"github.com/golang/protobuf/ptypes"
)

// ensure the imports are used
var (
	_ = bytes.MinRead
	_ = errors.New("")
	_ = fmt.Print
	_ = utf8.UTFMax
	_ = (*regexp.Regexp)(nil)
	_ = (*strings.Reader)(nil)
	_ = net.IPv4len
	_ = time.Duration(0)
	_ = (*url.URL)(nil)
	_ = (*mail.Address)(nil)
	_ = ptypes.DynamicAny{}
)

// define the regex for a UUID once up-front
var _compiler_uuidPattern = regexp.MustCompile("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")

// Validate checks the field values on ConnectionSet with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *ConnectionSet) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Downstream

	// no validation rules for Upstream

	return nil
}

// ConnectionSetValidationError is the validation error returned by
// ConnectionSet.Validate if the designated constraints aren't met.
type ConnectionSetValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ConnectionSetValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ConnectionSetValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ConnectionSetValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ConnectionSetValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ConnectionSetValidationError) ErrorName() string { return "ConnectionSetValidationError" }

// Error satisfies the builtin error interface
func (e ConnectionSetValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sConnectionSet.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ConnectionSetValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ConnectionSetValidationError{}

// Validate checks the field values on CompiledWorkflow with the rules defined
// in the proto definition for this message. If any rules are violated, an
// error is returned.
func (m *CompiledWorkflow) Validate() error {
	if m == nil {
		return nil
	}

	if v, ok := interface{}(m.GetTemplate()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return CompiledWorkflowValidationError{
				field:  "Template",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	if v, ok := interface{}(m.GetConnections()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return CompiledWorkflowValidationError{
				field:  "Connections",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// CompiledWorkflowValidationError is the validation error returned by
// CompiledWorkflow.Validate if the designated constraints aren't met.
type CompiledWorkflowValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e CompiledWorkflowValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e CompiledWorkflowValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e CompiledWorkflowValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e CompiledWorkflowValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e CompiledWorkflowValidationError) ErrorName() string { return "CompiledWorkflowValidationError" }

// Error satisfies the builtin error interface
func (e CompiledWorkflowValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sCompiledWorkflow.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = CompiledWorkflowValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = CompiledWorkflowValidationError{}

// Validate checks the field values on CompiledTask with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *CompiledTask) Validate() error {
	if m == nil {
		return nil
	}

	if v, ok := interface{}(m.GetTemplate()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return CompiledTaskValidationError{
				field:  "Template",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// CompiledTaskValidationError is the validation error returned by
// CompiledTask.Validate if the designated constraints aren't met.
type CompiledTaskValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e CompiledTaskValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e CompiledTaskValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e CompiledTaskValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e CompiledTaskValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e CompiledTaskValidationError) ErrorName() string { return "CompiledTaskValidationError" }

// Error satisfies the builtin error interface
func (e CompiledTaskValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sCompiledTask.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = CompiledTaskValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = CompiledTaskValidationError{}

// Validate checks the field values on CompiledWorkflowClosure with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *CompiledWorkflowClosure) Validate() error {
	if m == nil {
		return nil
	}

	if v, ok := interface{}(m.GetPrimary()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return CompiledWorkflowClosureValidationError{
				field:  "Primary",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	for idx, item := range m.GetSubWorkflows() {
		_, _ = idx, item

		if v, ok := interface{}(item).(interface{ Validate() error }); ok {
			if err := v.Validate(); err != nil {
				return CompiledWorkflowClosureValidationError{
					field:  fmt.Sprintf("SubWorkflows[%v]", idx),
					reason: "embedded message failed validation",
					cause:  err,
				}
			}
		}

	}

	for idx, item := range m.GetTasks() {
		_, _ = idx, item

		if v, ok := interface{}(item).(interface{ Validate() error }); ok {
			if err := v.Validate(); err != nil {
				return CompiledWorkflowClosureValidationError{
					field:  fmt.Sprintf("Tasks[%v]", idx),
					reason: "embedded message failed validation",
					cause:  err,
				}
			}
		}

	}

	return nil
}

// CompiledWorkflowClosureValidationError is the validation error returned by
// CompiledWorkflowClosure.Validate if the designated constraints aren't met.
type CompiledWorkflowClosureValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e CompiledWorkflowClosureValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e CompiledWorkflowClosureValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e CompiledWorkflowClosureValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e CompiledWorkflowClosureValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e CompiledWorkflowClosureValidationError) ErrorName() string {
	return "CompiledWorkflowClosureValidationError"
}

// Error satisfies the builtin error interface
func (e CompiledWorkflowClosureValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sCompiledWorkflowClosure.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = CompiledWorkflowClosureValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = CompiledWorkflowClosureValidationError{}

// Validate checks the field values on ConnectionSet_IdList with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *ConnectionSet_IdList) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// ConnectionSet_IdListValidationError is the validation error returned by
// ConnectionSet_IdList.Validate if the designated constraints aren't met.
type ConnectionSet_IdListValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ConnectionSet_IdListValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ConnectionSet_IdListValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ConnectionSet_IdListValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ConnectionSet_IdListValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ConnectionSet_IdListValidationError) ErrorName() string {
	return "ConnectionSet_IdListValidationError"
}

// Error satisfies the builtin error interface
func (e ConnectionSet_IdListValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sConnectionSet_IdList.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ConnectionSet_IdListValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ConnectionSet_IdListValidationError{}
