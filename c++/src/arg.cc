#include "arg.h"
#include "macro.h"

NAME_SPACE_BEGIN

template <typename InputType, typename TargetType>
inline bool IsCastLossless(const InputType &value) {
  return static_cast<InputType>(static_cast<TargetType>(value)) == value;
}


ProtoArgHelper::ProtoArgHelper(const OperatorDef &def) {
  for (auto &arg : def.arg()) {
    if (arg_map_.count(arg.name())) {
        LOG("Duplicated argument (%s) ,found in operator (%s)",arg.name().c_str(),def.name().c_str());
    }
    arg_map_[arg.name()] = arg;
  }
}

ProtoArgHelper::ProtoArgHelper(const NetDef &netdef) {
  for (auto &arg : netdef.arg()) {
      if(arg_map_.count(arg.name())){
          LOG("Duplicated argument(%s) found in net def.",arg.name().c_str());
      }
    arg_map_[arg.name()] = arg;
  }
}

#define GET_OPTIONAL_ARGUMENT_FUNC(T, fieldname, lossless_conversion)     \
  template <>                                                                  \
  T ProtoArgHelper::GetOptionalArg<T>(const std::string &arg_name,             \
                                      const T &default_value) const {          \
    if (arg_map_.count(arg_name) == 0) {                                       \
      return default_value;                                                    \
    }                                                                          \
    auto value = arg_map_.at(arg_name).fieldname();                            \
    if (lossless_conversion) {                                                 \
      const bool castLossless = IsCastLossless<decltype(value), T>(value);     \
      if(!castLossless){\
          LOG("cannot be casted losslessly to a target type");\
      }  \
    }                                                                          \
    return value;                                                              \
  }

GET_OPTIONAL_ARGUMENT_FUNC(float, f, false)
GET_OPTIONAL_ARGUMENT_FUNC(bool, i, false)
GET_OPTIONAL_ARGUMENT_FUNC(int, i, true)
GET_OPTIONAL_ARGUMENT_FUNC(std::string, s, false)
#undef GET_OPTIONAL_ARGUMENT_FUNC

#define GET_REPEATED_ARGUMENT_FUNC(T, fieldname, lossless_conversion) \
  template <>                                                              \
  std::vector<T> ProtoArgHelper::GetRepeatedArgs<T>(                       \
      const std::string &arg_name, const std::vector<T> &default_value)    \
      const {                                                              \
    if (arg_map_.count(arg_name) == 0) {                                   \
      return default_value;                                                \
    }                                                                      \
    std::vector<T> values;                                                 \
    for (const auto &v : arg_map_.at(arg_name).fieldname()) {              \
      if (lossless_conversion) {                                           \
        const bool castLossless = IsCastLossless<decltype(v), T>(v);       \
       if(!castLossless){\
          LOG("cannot be casted losslessly to a target type");\
        }  \
      }                                                                    \
      values.push_back(v);                                                 \
    }                                                                      \
    return values;                                                         \
  }

GET_REPEATED_ARGUMENT_FUNC(float, floats, false)
GET_REPEATED_ARGUMENT_FUNC(int, ints, true)
GET_REPEATED_ARGUMENT_FUNC(int64_t, ints, true)
#undef GET_REPEATED_ARGUMENT_FUNC
NAME_SPACE_END