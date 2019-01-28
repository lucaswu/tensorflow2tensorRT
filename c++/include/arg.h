#ifndef ARG_H_
#define ARG_H_
#include "tensorrt.pb.h"
#include "macro.h"
NAME_SPACE_BEGIN
using namespace tensorrt;

class ProtoArgHelper {
    public:
        template <typename Def, typename T>
        static T GetOptionalArg(const Def &def,
                          const std::string &arg_name,
                          const T &default_value) {
            return ProtoArgHelper(def).GetOptionalArg<T>(arg_name, default_value);
        }

        template <typename Def, typename T>
        static std::vector<T> GetRepeatedArgs(
            const Def &def,
            const std::string &arg_name,
            const std::vector<T> &default_value = std::vector<T>()) {
            return ProtoArgHelper(def).GetRepeatedArgs<T>(arg_name, default_value);
        }

        explicit ProtoArgHelper(const OperatorDef &def);
        explicit ProtoArgHelper(const NetDef &netdef);

        template <typename T>
        T GetOptionalArg(const std::string &arg_name, const T &default_value) const;
        template <typename T>
        std::vector<T> GetRepeatedArgs(
            const std::string &arg_name,
            const std::vector<T> &default_value = std::vector<T>()) const;

    private:
    std::map<std::string, Argument> arg_map_;
};

NAME_SPACE_END

#endif