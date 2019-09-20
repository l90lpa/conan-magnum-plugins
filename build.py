#!/usr/bin/env python
import copy
from collections import defaultdict

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="magnum-plugins:build_plugins_static")

    # add c++17 build configs
    named_builds = defaultdict(list)
    for settings, options, env_vars, build_requires, reference in builder.items:
        settings["compiler.cppstd"] = "17"
        settings["compiler.libcxx"] = "libstdc++11"

        # the options we'll be varying
        options["magnum-plugins:with_assimpimporter"] = False
        options["magnum-plugins:with_freetypefont"] = False

        # magnum non-default settings
        options["magnum:with_sdl2application"] = False
        options["magnum:with_glfwapplication"] = True
        options["magnum:with_tgaimporter"] = True
        options["magnum:with_anysceneimporter"] = True
        options["magnum:with_meshtools"] = True

        named_builds[
            f"{settings['build_type']}-"
            f"{'static' if options['magnum-plugins:build_plugins_static'] else 'shared'}"
        ].append([settings, options, env_vars, build_requires, reference])

        assimp_options = copy.copy(options)
        assimp_options["magnum-plugins:with_assimpimporter"] = True
        named_builds[
            f"{settings['build_type']}-"
            f"{'static' if options['magnum-plugins:build_plugins_static'] else 'shared'}-assimp"
        ].append([settings, assimp_options, env_vars, build_requires, reference])

        freetype_options = copy.copy(options)
        freetype_options["magnum-plugins:with_freetypefont"] = True
        named_builds[
            f"{settings['build_type']}-"
            f"{'static' if options['magnum-plugins:build_plugins_static'] else 'shared'}-freetype"
        ].append([settings, freetype_options, env_vars, build_requires, reference])

        assimp_and_freetype_options = copy.copy(options)
        assimp_and_freetype_options["magnum-plugins:with_assimpimporter"] = True
        assimp_and_freetype_options["magnum-plugins:with_freetypefont"] = True
        named_builds[
            f"{settings['build_type']}-"
            f"{'static' if options['magnum-plugins:build_plugins_static'] else 'shared'}"
            "-assimp-freetype"
        ].append(
            [settings, assimp_and_freetype_options, env_vars, build_requires, reference]
        )

    builder.builds = []
    builder.named_builds = named_builds

    builder.run()
