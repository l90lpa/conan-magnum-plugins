#include <Corrade/PluginManager/PluginManager.h>
#include <Corrade/Utility/Debug.h>

#include <MagnumPlugins/FreeTypeFont/FreeTypeFont.h>
#include <MagnumPlugins/FreeTypeFont/importStaticPlugin.cpp>

#include <iostream>
#include <memory>

using namespace Magnum;
using namespace Corrade;

int main(int argc, char **argv) {
  if (argc < 2) {
    std::cerr << "Must provide test with path to font" << std::endl;
    return 1;
  }
  Text::FreeTypeFont::initialize();
  Text::FreeTypeFont font;

  if (!font.openFile(argv[1], 16.0)) {
    std::cerr << "Failed to open " << argv[1] << std::endl;
    return 1;
  }

  std::cout << "Successfully opened font " << argv[1] << std::endl;
  return 0;
}
