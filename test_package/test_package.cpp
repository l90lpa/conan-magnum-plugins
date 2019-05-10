#include <cstdlib>

#include <Magnum/Primitives/Icosphere.h>
#include <Magnum/Trade/MeshData3D.h>

#include <Corrade/PluginManager/PluginManager.h>
#include <Corrade/Utility/Debug.h>
#include <Magnum/Trade/AbstractImporter.h>

#include <memory>

using namespace Magnum;
using namespace Corrade;

int main() {
  PluginManager::Manager<Trade::AbstractImporter> manager;
  // std::unique_ptr<Trade::AbstractImporter> importer =
  //     manager.instantiate("AssimpImporter");

  return EXIT_SUCCESS;
}
