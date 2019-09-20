#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os

from conans import CMake, ConanFile


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if (
            self.options["magnum-plugins"].build_plugins_static
            and self.options["magnum-plugins"].with_assimpimporter
        ):
            cmake.build(target="test-assimp-plugin")
        if (
            self.options["magnum-plugins"].build_plugins_static
            and self.options["magnum-plugins"].with_freetypefont
        ):
            cmake.build(target="test-freetype-plugin")

    def test(self):
        bin_path = os.path.join("bin", "test-package")
        self.run(bin_path, run_environment=True)
        if (
            self.options["magnum-plugins"].build_plugins_static
            and self.options["magnum-plugins"].with_assimpimporter
        ):
            self.run(os.path.join("bin", "test-assimp-plugin"), run_environment=True)
        if (
            self.options["magnum-plugins"].build_plugins_static
            and self.options["magnum-plugins"].with_freetypefont
        ):
            bin_path = os.path.join("bin", "test-freetype-plugin")
            font_path = os.path.join(
                os.path.dirname(__file__), "data", "DejaVuSansMono.ttf"
            )
            self.run(f"{bin_path} {font_path}", run_environment=True)
