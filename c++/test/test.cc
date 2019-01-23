#include "net.h"

using namespace parser;

int main(int argc, char*argv[])
{
    Net *net = new Net();
    auto enginer = net->getEnginer(100,100,3);
}