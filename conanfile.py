#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile, tools, CMake

def get_version():
    git = tools.Git()
    try:
        tag = git.get_tag()
        return tag if tag else "1.0.0"
    except:
        return None

class DemoConan(ConanFile):
    name = "demo"
    version = get_version()
    url = "http://gitlab.com/aivero/public/conan/conan-" + name
    license = "MIT"
    description = ("Demo conan package")
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = ["CMakeLists.txt", "src/*"]
    generators = "env"

    def build_requirements(self):
        self.build_requires("env-generator/0.1@%s/stable" % self.user)
        self.build_requires("cmake/3.15.3@%s/stable" % self.user)

    def build(self):
        cmake = CMake(self, generator="Ninja")
        cmake.configure()
        cmake.install()

    def package(self):
        if self.settings.build_type == "Debug":
            self.copy("*.cpp", "src")
            self.copy("*.hpp", "src")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.srcdirs.append("src")
