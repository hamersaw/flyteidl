// Code generated by "enumer --type=AuthType -json -yaml -trimprefix=AuthType"; DO NOT EDIT.

//
package admin

import (
	"encoding/json"
	"fmt"
)

const _AuthTypeName = "CLIENTSECRETTHREELEGGEDAUTH"

var _AuthTypeIndex = [...]uint8{0, 12, 27}

func (i AuthType) String() string {
	if i >= AuthType(len(_AuthTypeIndex)-1) {
		return fmt.Sprintf("AuthType(%d)", i)
	}
	return _AuthTypeName[_AuthTypeIndex[i]:_AuthTypeIndex[i+1]]
}

var _AuthTypeValues = []AuthType{0, 1}

var _AuthTypeNameToValueMap = map[string]AuthType{
	_AuthTypeName[0:12]:  0,
	_AuthTypeName[12:27]: 1,
}

// AuthTypeString retrieves an enum value from the enum constants string name.
// Throws an error if the param is not part of the enum.
func AuthTypeString(s string) (AuthType, error) {
	if val, ok := _AuthTypeNameToValueMap[s]; ok {
		return val, nil
	}
	return 0, fmt.Errorf("%s does not belong to AuthType values", s)
}

// AuthTypeValues returns all values of the enum
func AuthTypeValues() []AuthType {
	return _AuthTypeValues
}

// IsAAuthType returns "true" if the value is listed in the enum definition. "false" otherwise
func (i AuthType) IsAAuthType() bool {
	for _, v := range _AuthTypeValues {
		if i == v {
			return true
		}
	}
	return false
}

// MarshalJSON implements the json.Marshaler interface for AuthType
func (i AuthType) MarshalJSON() ([]byte, error) {
	return json.Marshal(i.String())
}

// UnmarshalJSON implements the json.Unmarshaler interface for AuthType
func (i *AuthType) UnmarshalJSON(data []byte) error {
	var s string
	if err := json.Unmarshal(data, &s); err != nil {
		return fmt.Errorf("AuthType should be a string, got %s", data)
	}

	var err error
	*i, err = AuthTypeString(s)
	return err
}

// MarshalYAML implements a YAML Marshaler for AuthType
func (i AuthType) MarshalYAML() (interface{}, error) {
	return i.String(), nil
}

// UnmarshalYAML implements a YAML Unmarshaler for AuthType
func (i *AuthType) UnmarshalYAML(unmarshal func(interface{}) error) error {
	var s string
	if err := unmarshal(&s); err != nil {
		return err
	}

	var err error
	*i, err = AuthTypeString(s)
	return err
}
