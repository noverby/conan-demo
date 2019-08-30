#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile, tools, CMake

def get_version():
    git = tools.Git()
    try:
        if git.get_tag() and git.get_branch().endswith("(no branch)"):
            return git.get_tag()
        else:
            return git.get_branch()
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

    def requirements(self):
        self.requires("env-generator/0.1@%s/stable" % self.user)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package(self):
        if self.settings.build_type == "Debug":
            self.copy("*.c*", "src")
            self.copy("*.h*", "src")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.srcdirs.append("src")
