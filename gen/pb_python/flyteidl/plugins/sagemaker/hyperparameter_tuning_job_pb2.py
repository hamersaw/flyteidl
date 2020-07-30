# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/plugins/sagemaker/hyperparameter_tuning_job.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.plugins.sagemaker import parameter_ranges_pb2 as flyteidl_dot_plugins_dot_sagemaker_dot_parameter__ranges__pb2
from flyteidl.plugins.sagemaker import training_job_pb2 as flyteidl_dot_plugins_dot_sagemaker_dot_training__job__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/plugins/sagemaker/hyperparameter_tuning_job.proto',
  package='flyteidl.plugins.sagemaker',
  syntax='proto3',
  serialized_options=_b('Z3github.com/lyft/flyteidl/gen/pb-go/flyteidl/plugins'),
  serialized_pb=_b('\n:flyteidl/plugins/sagemaker/hyperparameter_tuning_job.proto\x12\x1a\x66lyteidl.plugins.sagemaker\x1a\x31\x66lyteidl/plugins/sagemaker/parameter_ranges.proto\x1a-flyteidl/plugins/sagemaker/training_job.proto\"\xa1\x01\n\x17HyperparameterTuningJob\x12=\n\x0ctraining_job\x18\x01 \x01(\x0b\x32\'.flyteidl.plugins.sagemaker.TrainingJob\x12#\n\x1bmax_number_of_training_jobs\x18\x02 \x01(\x03\x12\"\n\x1amax_parallel_training_jobs\x18\x03 \x01(\x03\"H\n!HyperparameterTuningObjectiveType\"#\n\x05Value\x12\x0c\n\x08MINIMIZE\x10\x00\x12\x0c\n\x08MAXIMIZE\x10\x01\"\x91\x01\n\x1dHyperparameterTuningObjective\x12[\n\x0eobjective_type\x18\x01 \x01(\x0e\x32\x43.flyteidl.plugins.sagemaker.HyperparameterTuningObjectiveType.Value\x12\x13\n\x0bmetric_name\x18\x02 \x01(\t\"A\n\x1cHyperparameterTuningStrategy\"!\n\x05Value\x12\x0c\n\x08\x42\x41YESIAN\x10\x00\x12\n\n\x06RANDOM\x10\x01\":\n\x1cTrainingJobEarlyStoppingType\"\x1a\n\x05Value\x12\x07\n\x03OFF\x10\x00\x12\x08\n\x04\x41UTO\x10\x01\"\x83\x03\n\x1dHyperparameterTuningJobConfig\x12J\n\x15hyperparameter_ranges\x18\x01 \x01(\x0b\x32+.flyteidl.plugins.sagemaker.ParameterRanges\x12W\n\x0ftuning_strategy\x18\x02 \x01(\x0e\x32>.flyteidl.plugins.sagemaker.HyperparameterTuningStrategy.Value\x12S\n\x10tuning_objective\x18\x03 \x01(\x0b\x32\x39.flyteidl.plugins.sagemaker.HyperparameterTuningObjective\x12h\n training_job_early_stopping_type\x18\x04 \x01(\x0e\x32>.flyteidl.plugins.sagemaker.TrainingJobEarlyStoppingType.ValueB5Z3github.com/lyft/flyteidl/gen/pb-go/flyteidl/pluginsb\x06proto3')
  ,
  dependencies=[flyteidl_dot_plugins_dot_sagemaker_dot_parameter__ranges__pb2.DESCRIPTOR,flyteidl_dot_plugins_dot_sagemaker_dot_training__job__pb2.DESCRIPTOR,])



_HYPERPARAMETERTUNINGOBJECTIVETYPE_VALUE = _descriptor.EnumDescriptor(
  name='Value',
  full_name='flyteidl.plugins.sagemaker.HyperparameterTuningObjectiveType.Value',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MINIMIZE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=389,
  serialized_end=424,
)
_sym_db.RegisterEnumDescriptor(_HYPERPARAMETERTUNINGOBJECTIVETYPE_VALUE)

_HYPERPARAMETERTUNINGSTRATEGY_VALUE = _descriptor.EnumDescriptor(
  name='Value',
  full_name='flyteidl.plugins.sagemaker.HyperparameterTuningStrategy.Value',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BAYESIAN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANDOM', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=606,
  serialized_end=639,
)
_sym_db.RegisterEnumDescriptor(_HYPERPARAMETERTUNINGSTRATEGY_VALUE)

_TRAININGJOBEARLYSTOPPINGTYPE_VALUE = _descriptor.EnumDescriptor(
  name='Value',
  full_name='flyteidl.plugins.sagemaker.TrainingJobEarlyStoppingType.Value',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OFF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=673,
  serialized_end=699,
)
_sym_db.RegisterEnumDescriptor(_TRAININGJOBEARLYSTOPPINGTYPE_VALUE)


_HYPERPARAMETERTUNINGJOB = _descriptor.Descriptor(
  name='HyperparameterTuningJob',
  full_name='flyteidl.plugins.sagemaker.HyperparameterTuningJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='training_job', full_name='flyteidl.plugins.sagemaker.HyperparameterTuningJob.training_job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_number_of_training_jobs', full_name='flyteidl.plugins.sagemaker.HyperparameterTuningJob.max_number_of_training_jobs', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_parallel_training_jobs', full_name='flyteidl.plugins.sagemaker.HyperparameterTuningJob.max_parallel_training_jobs', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=350,
)


_HYPERPARAMETERTUNINGOBJECTIVETYPE = _descriptor.Descriptor(
  name='HyperparameterTuningObjectiveType',
  full_name='flyteidl.plugins.sagemaker.HyperparameterTuningObjectiveType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HYPERPARAMETERTUNINGOBJECTIVETYPE_VALUE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=424,
)


_HYPERPARAMETERTUNINGOBJECTIVE = _descriptor.Descriptor(
  name='HyperparameterTuningObjective',
  full_name='flyteidl.plugins.sagemaker.HyperparameterTuningObjective',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objective_type', full_name='flyteidl.plugins.sagemaker.HyperparameterTuningObjective.objective_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric_name', full_name='flyteidl.plugins.sagemaker.HyperparameterTuningObjective.metric_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=572,
)


_HYPERPARAMETERTUNINGSTRATEGY = _descriptor.Descriptor(
  name='HyperparameterTuningStrategy',
  full_name='flyteidl.plugins.sagemaker.HyperparameterTuningStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HYPERPARAMETERTUNINGSTRATEGY_VALUE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=574,
  serialized_end=639,
)


_TRAININGJOBEARLYSTOPPINGTYPE = _descriptor.Descriptor(
  name='TrainingJobEarlyStoppingType',
  full_name='flyteidl.plugins.sagemaker.TrainingJobEarlyStoppingType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRAININGJOBEARLYSTOPPINGTYPE_VALUE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=641,
  serialized_end=699,
)


_HYPERPARAMETERTUNINGJOBCONFIG = _descriptor.Descriptor(
  name='HyperparameterTuningJobConfig',
  full_name='flyteidl.plugins.sagemaker.HyperparameterTuningJobConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hyperparameter_ranges', full_name='flyteidl.plugins.sagemaker.HyperparameterTuningJobConfig.hyperparameter_ranges', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tuning_strategy', full_name='flyteidl.plugins.sagemaker.HyperparameterTuningJobConfig.tuning_strategy', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tuning_objective', full_name='flyteidl.plugins.sagemaker.HyperparameterTuningJobConfig.tuning_objective', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_job_early_stopping_type', full_name='flyteidl.plugins.sagemaker.HyperparameterTuningJobConfig.training_job_early_stopping_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=1089,
)

_HYPERPARAMETERTUNINGJOB.fields_by_name['training_job'].message_type = flyteidl_dot_plugins_dot_sagemaker_dot_training__job__pb2._TRAININGJOB
_HYPERPARAMETERTUNINGOBJECTIVETYPE_VALUE.containing_type = _HYPERPARAMETERTUNINGOBJECTIVETYPE
_HYPERPARAMETERTUNINGOBJECTIVE.fields_by_name['objective_type'].enum_type = _HYPERPARAMETERTUNINGOBJECTIVETYPE_VALUE
_HYPERPARAMETERTUNINGSTRATEGY_VALUE.containing_type = _HYPERPARAMETERTUNINGSTRATEGY
_TRAININGJOBEARLYSTOPPINGTYPE_VALUE.containing_type = _TRAININGJOBEARLYSTOPPINGTYPE
_HYPERPARAMETERTUNINGJOBCONFIG.fields_by_name['hyperparameter_ranges'].message_type = flyteidl_dot_plugins_dot_sagemaker_dot_parameter__ranges__pb2._PARAMETERRANGES
_HYPERPARAMETERTUNINGJOBCONFIG.fields_by_name['tuning_strategy'].enum_type = _HYPERPARAMETERTUNINGSTRATEGY_VALUE
_HYPERPARAMETERTUNINGJOBCONFIG.fields_by_name['tuning_objective'].message_type = _HYPERPARAMETERTUNINGOBJECTIVE
_HYPERPARAMETERTUNINGJOBCONFIG.fields_by_name['training_job_early_stopping_type'].enum_type = _TRAININGJOBEARLYSTOPPINGTYPE_VALUE
DESCRIPTOR.message_types_by_name['HyperparameterTuningJob'] = _HYPERPARAMETERTUNINGJOB
DESCRIPTOR.message_types_by_name['HyperparameterTuningObjectiveType'] = _HYPERPARAMETERTUNINGOBJECTIVETYPE
DESCRIPTOR.message_types_by_name['HyperparameterTuningObjective'] = _HYPERPARAMETERTUNINGOBJECTIVE
DESCRIPTOR.message_types_by_name['HyperparameterTuningStrategy'] = _HYPERPARAMETERTUNINGSTRATEGY
DESCRIPTOR.message_types_by_name['TrainingJobEarlyStoppingType'] = _TRAININGJOBEARLYSTOPPINGTYPE
DESCRIPTOR.message_types_by_name['HyperparameterTuningJobConfig'] = _HYPERPARAMETERTUNINGJOBCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HyperparameterTuningJob = _reflection.GeneratedProtocolMessageType('HyperparameterTuningJob', (_message.Message,), dict(
  DESCRIPTOR = _HYPERPARAMETERTUNINGJOB,
  __module__ = 'flyteidl.plugins.sagemaker.hyperparameter_tuning_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.HyperparameterTuningJob)
  ))
_sym_db.RegisterMessage(HyperparameterTuningJob)

HyperparameterTuningObjectiveType = _reflection.GeneratedProtocolMessageType('HyperparameterTuningObjectiveType', (_message.Message,), dict(
  DESCRIPTOR = _HYPERPARAMETERTUNINGOBJECTIVETYPE,
  __module__ = 'flyteidl.plugins.sagemaker.hyperparameter_tuning_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.HyperparameterTuningObjectiveType)
  ))
_sym_db.RegisterMessage(HyperparameterTuningObjectiveType)

HyperparameterTuningObjective = _reflection.GeneratedProtocolMessageType('HyperparameterTuningObjective', (_message.Message,), dict(
  DESCRIPTOR = _HYPERPARAMETERTUNINGOBJECTIVE,
  __module__ = 'flyteidl.plugins.sagemaker.hyperparameter_tuning_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.HyperparameterTuningObjective)
  ))
_sym_db.RegisterMessage(HyperparameterTuningObjective)

HyperparameterTuningStrategy = _reflection.GeneratedProtocolMessageType('HyperparameterTuningStrategy', (_message.Message,), dict(
  DESCRIPTOR = _HYPERPARAMETERTUNINGSTRATEGY,
  __module__ = 'flyteidl.plugins.sagemaker.hyperparameter_tuning_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.HyperparameterTuningStrategy)
  ))
_sym_db.RegisterMessage(HyperparameterTuningStrategy)

TrainingJobEarlyStoppingType = _reflection.GeneratedProtocolMessageType('TrainingJobEarlyStoppingType', (_message.Message,), dict(
  DESCRIPTOR = _TRAININGJOBEARLYSTOPPINGTYPE,
  __module__ = 'flyteidl.plugins.sagemaker.hyperparameter_tuning_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.TrainingJobEarlyStoppingType)
  ))
_sym_db.RegisterMessage(TrainingJobEarlyStoppingType)

HyperparameterTuningJobConfig = _reflection.GeneratedProtocolMessageType('HyperparameterTuningJobConfig', (_message.Message,), dict(
  DESCRIPTOR = _HYPERPARAMETERTUNINGJOBCONFIG,
  __module__ = 'flyteidl.plugins.sagemaker.hyperparameter_tuning_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.HyperparameterTuningJobConfig)
  ))
_sym_db.RegisterMessage(HyperparameterTuningJobConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
