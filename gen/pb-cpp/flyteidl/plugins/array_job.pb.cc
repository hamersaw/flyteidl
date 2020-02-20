// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: flyteidl/plugins/array_job.proto

#include "flyteidl/plugins/array_job.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>

namespace flyteidl {
namespace plugins {
class ArrayJobDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<ArrayJob> _instance;
} _ArrayJob_default_instance_;
}  // namespace plugins
}  // namespace flyteidl
static void InitDefaultsArrayJob_flyteidl_2fplugins_2farray_5fjob_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::flyteidl::plugins::_ArrayJob_default_instance_;
    new (ptr) ::flyteidl::plugins::ArrayJob();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::flyteidl::plugins::ArrayJob::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<0> scc_info_ArrayJob_flyteidl_2fplugins_2farray_5fjob_2eproto =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 0, InitDefaultsArrayJob_flyteidl_2fplugins_2farray_5fjob_2eproto}, {}};

void InitDefaults_flyteidl_2fplugins_2farray_5fjob_2eproto() {
  ::google::protobuf::internal::InitSCC(&scc_info_ArrayJob_flyteidl_2fplugins_2farray_5fjob_2eproto.base);
}

::google::protobuf::Metadata file_level_metadata_flyteidl_2fplugins_2farray_5fjob_2eproto[1];
constexpr ::google::protobuf::EnumDescriptor const** file_level_enum_descriptors_flyteidl_2fplugins_2farray_5fjob_2eproto = nullptr;
constexpr ::google::protobuf::ServiceDescriptor const** file_level_service_descriptors_flyteidl_2fplugins_2farray_5fjob_2eproto = nullptr;

const ::google::protobuf::uint32 TableStruct_flyteidl_2fplugins_2farray_5fjob_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::ArrayJob, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::ArrayJob, parallelism_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::ArrayJob, size_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::ArrayJob, min_successes_),
};
static const ::google::protobuf::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::flyteidl::plugins::ArrayJob)},
};

static ::google::protobuf::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::google::protobuf::Message*>(&::flyteidl::plugins::_ArrayJob_default_instance_),
};

::google::protobuf::internal::AssignDescriptorsTable assign_descriptors_table_flyteidl_2fplugins_2farray_5fjob_2eproto = {
  {}, AddDescriptors_flyteidl_2fplugins_2farray_5fjob_2eproto, "flyteidl/plugins/array_job.proto", schemas,
  file_default_instances, TableStruct_flyteidl_2fplugins_2farray_5fjob_2eproto::offsets,
  file_level_metadata_flyteidl_2fplugins_2farray_5fjob_2eproto, 1, file_level_enum_descriptors_flyteidl_2fplugins_2farray_5fjob_2eproto, file_level_service_descriptors_flyteidl_2fplugins_2farray_5fjob_2eproto,
};

const char descriptor_table_protodef_flyteidl_2fplugins_2farray_5fjob_2eproto[] =
  "\n flyteidl/plugins/array_job.proto\022\020flyt"
  "eidl.plugins\"D\n\010ArrayJob\022\023\n\013parallelism\030"
  "\001 \001(\003\022\014\n\004size\030\002 \001(\003\022\025\n\rmin_successes\030\003 \001"
  "(\003B5Z3github.com/lyft/flyteidl/gen/pb-go"
  "/flyteidl/pluginsb\006proto3"
  ;
::google::protobuf::internal::DescriptorTable descriptor_table_flyteidl_2fplugins_2farray_5fjob_2eproto = {
  false, InitDefaults_flyteidl_2fplugins_2farray_5fjob_2eproto, 
  descriptor_table_protodef_flyteidl_2fplugins_2farray_5fjob_2eproto,
  "flyteidl/plugins/array_job.proto", &assign_descriptors_table_flyteidl_2fplugins_2farray_5fjob_2eproto, 185,
};

void AddDescriptors_flyteidl_2fplugins_2farray_5fjob_2eproto() {
  static constexpr ::google::protobuf::internal::InitFunc deps[1] =
  {
  };
 ::google::protobuf::internal::AddDescriptors(&descriptor_table_flyteidl_2fplugins_2farray_5fjob_2eproto, deps, 0);
}

// Force running AddDescriptors() at dynamic initialization time.
static bool dynamic_init_dummy_flyteidl_2fplugins_2farray_5fjob_2eproto = []() { AddDescriptors_flyteidl_2fplugins_2farray_5fjob_2eproto(); return true; }();
namespace flyteidl {
namespace plugins {

// ===================================================================

void ArrayJob::InitAsDefaultInstance() {
}
class ArrayJob::HasBitSetters {
 public:
};

#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int ArrayJob::kParallelismFieldNumber;
const int ArrayJob::kSizeFieldNumber;
const int ArrayJob::kMinSuccessesFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

ArrayJob::ArrayJob()
  : ::google::protobuf::Message(), _internal_metadata_(nullptr) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:flyteidl.plugins.ArrayJob)
}
ArrayJob::ArrayJob(const ArrayJob& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(nullptr) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::memcpy(&parallelism_, &from.parallelism_,
    static_cast<size_t>(reinterpret_cast<char*>(&min_successes_) -
    reinterpret_cast<char*>(&parallelism_)) + sizeof(min_successes_));
  // @@protoc_insertion_point(copy_constructor:flyteidl.plugins.ArrayJob)
}

void ArrayJob::SharedCtor() {
  ::memset(&parallelism_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&min_successes_) -
      reinterpret_cast<char*>(&parallelism_)) + sizeof(min_successes_));
}

ArrayJob::~ArrayJob() {
  // @@protoc_insertion_point(destructor:flyteidl.plugins.ArrayJob)
  SharedDtor();
}

void ArrayJob::SharedDtor() {
}

void ArrayJob::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const ArrayJob& ArrayJob::default_instance() {
  ::google::protobuf::internal::InitSCC(&::scc_info_ArrayJob_flyteidl_2fplugins_2farray_5fjob_2eproto.base);
  return *internal_default_instance();
}


void ArrayJob::Clear() {
// @@protoc_insertion_point(message_clear_start:flyteidl.plugins.ArrayJob)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  ::memset(&parallelism_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&min_successes_) -
      reinterpret_cast<char*>(&parallelism_)) + sizeof(min_successes_));
  _internal_metadata_.Clear();
}

#if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
const char* ArrayJob::_InternalParse(const char* begin, const char* end, void* object,
                  ::google::protobuf::internal::ParseContext* ctx) {
  auto msg = static_cast<ArrayJob*>(object);
  ::google::protobuf::int32 size; (void)size;
  int depth; (void)depth;
  ::google::protobuf::uint32 tag;
  ::google::protobuf::internal::ParseFunc parser_till_end; (void)parser_till_end;
  auto ptr = begin;
  while (ptr < end) {
    ptr = ::google::protobuf::io::Parse32(ptr, &tag);
    GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
    switch (tag >> 3) {
      // int64 parallelism = 1;
      case 1: {
        if (static_cast<::google::protobuf::uint8>(tag) != 8) goto handle_unusual;
        msg->set_parallelism(::google::protobuf::internal::ReadVarint(&ptr));
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        break;
      }
      // int64 size = 2;
      case 2: {
        if (static_cast<::google::protobuf::uint8>(tag) != 16) goto handle_unusual;
        msg->set_size(::google::protobuf::internal::ReadVarint(&ptr));
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        break;
      }
      // int64 min_successes = 3;
      case 3: {
        if (static_cast<::google::protobuf::uint8>(tag) != 24) goto handle_unusual;
        msg->set_min_successes(::google::protobuf::internal::ReadVarint(&ptr));
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        break;
      }
      default: {
      handle_unusual:
        if ((tag & 7) == 4 || tag == 0) {
          ctx->EndGroup(tag);
          return ptr;
        }
        auto res = UnknownFieldParse(tag, {_InternalParse, msg},
          ptr, end, msg->_internal_metadata_.mutable_unknown_fields(), ctx);
        ptr = res.first;
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr != nullptr);
        if (res.second) return ptr;
      }
    }  // switch
  }  // while
  return ptr;
}
#else  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
bool ArrayJob::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!PROTOBUF_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:flyteidl.plugins.ArrayJob)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // int64 parallelism = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (8 & 0xFF)) {

          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int64, ::google::protobuf::internal::WireFormatLite::TYPE_INT64>(
                 input, &parallelism_)));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // int64 size = 2;
      case 2: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (16 & 0xFF)) {

          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int64, ::google::protobuf::internal::WireFormatLite::TYPE_INT64>(
                 input, &size_)));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // int64 min_successes = 3;
      case 3: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (24 & 0xFF)) {

          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int64, ::google::protobuf::internal::WireFormatLite::TYPE_INT64>(
                 input, &min_successes_)));
        } else {
          goto handle_unusual;
        }
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, _internal_metadata_.mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:flyteidl.plugins.ArrayJob)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:flyteidl.plugins.ArrayJob)
  return false;
#undef DO_
}
#endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER

void ArrayJob::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:flyteidl.plugins.ArrayJob)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // int64 parallelism = 1;
  if (this->parallelism() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteInt64(1, this->parallelism(), output);
  }

  // int64 size = 2;
  if (this->size() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteInt64(2, this->size(), output);
  }

  // int64 min_successes = 3;
  if (this->min_successes() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteInt64(3, this->min_successes(), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        _internal_metadata_.unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:flyteidl.plugins.ArrayJob)
}

::google::protobuf::uint8* ArrayJob::InternalSerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:flyteidl.plugins.ArrayJob)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // int64 parallelism = 1;
  if (this->parallelism() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt64ToArray(1, this->parallelism(), target);
  }

  // int64 size = 2;
  if (this->size() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt64ToArray(2, this->size(), target);
  }

  // int64 min_successes = 3;
  if (this->min_successes() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt64ToArray(3, this->min_successes(), target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:flyteidl.plugins.ArrayJob)
  return target;
}

size_t ArrayJob::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:flyteidl.plugins.ArrayJob)
  size_t total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        _internal_metadata_.unknown_fields());
  }
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // int64 parallelism = 1;
  if (this->parallelism() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::Int64Size(
        this->parallelism());
  }

  // int64 size = 2;
  if (this->size() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::Int64Size(
        this->size());
  }

  // int64 min_successes = 3;
  if (this->min_successes() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::Int64Size(
        this->min_successes());
  }

  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void ArrayJob::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:flyteidl.plugins.ArrayJob)
  GOOGLE_DCHECK_NE(&from, this);
  const ArrayJob* source =
      ::google::protobuf::DynamicCastToGenerated<ArrayJob>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:flyteidl.plugins.ArrayJob)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:flyteidl.plugins.ArrayJob)
    MergeFrom(*source);
  }
}

void ArrayJob::MergeFrom(const ArrayJob& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:flyteidl.plugins.ArrayJob)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.parallelism() != 0) {
    set_parallelism(from.parallelism());
  }
  if (from.size() != 0) {
    set_size(from.size());
  }
  if (from.min_successes() != 0) {
    set_min_successes(from.min_successes());
  }
}

void ArrayJob::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:flyteidl.plugins.ArrayJob)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void ArrayJob::CopyFrom(const ArrayJob& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:flyteidl.plugins.ArrayJob)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool ArrayJob::IsInitialized() const {
  return true;
}

void ArrayJob::Swap(ArrayJob* other) {
  if (other == this) return;
  InternalSwap(other);
}
void ArrayJob::InternalSwap(ArrayJob* other) {
  using std::swap;
  _internal_metadata_.Swap(&other->_internal_metadata_);
  swap(parallelism_, other->parallelism_);
  swap(size_, other->size_);
  swap(min_successes_, other->min_successes_);
}

::google::protobuf::Metadata ArrayJob::GetMetadata() const {
  ::google::protobuf::internal::AssignDescriptors(&::assign_descriptors_table_flyteidl_2fplugins_2farray_5fjob_2eproto);
  return ::file_level_metadata_flyteidl_2fplugins_2farray_5fjob_2eproto[kIndexInFileMessages];
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace plugins
}  // namespace flyteidl
namespace google {
namespace protobuf {
template<> PROTOBUF_NOINLINE ::flyteidl::plugins::ArrayJob* Arena::CreateMaybeMessage< ::flyteidl::plugins::ArrayJob >(Arena* arena) {
  return Arena::CreateInternal< ::flyteidl::plugins::ArrayJob >(arena);
}
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>
