#include <Corrade/PluginManager/PluginManager.h>
#include <Corrade/Utility/Debug.h>
#include <Magnum/Trade/AbstractImporter.h>

#include <MagnumPlugins/AssimpImporter/AssimpImporter.h>
#include <MagnumPlugins/AssimpImporter/importStaticPlugin.cpp>

#include <iostream>
#include <memory>

using namespace Magnum;
using namespace Corrade;

int main() {
  PluginManager::Manager<Trade::AbstractImporter> manager;
  std::unique_ptr<Trade::AbstractImporter> importer =
      manager.loadAndInstantiate("AssimpImporter");

  if (!importer) {
    std::cout << "Failed to load assimp importer" << std::endl;
    return 1;
  }

  std::cout << "Successfully loaded assimp importer" << std::endl;

  return 0;
}
