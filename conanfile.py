from conans import CMake, ConanFile, Meson, tools


class DemoConan(ConanFile):
    name = "demo"
    version = tools.get_env("GIT_TAG", "1.0.0")
    url = "http://gitlab.com/aivero/public/conan/conan-" + name
    license = "MIT"
    description = "Demo conan package"
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = ("meson.build", "CMakeLists.txt", "src/*")
    options = {"build_system": ["meson", "cmake"]}
    default_options = "build_system=meson"
    generators = "env"

    def build_requirements(self):
        self.build_requires("env-generator/1.0.0@%s/stable" % self.user)
        if self.options.build_system == "meson":
            self.build_requires("meson/[>=0.51.2]@%s/stable" % self.user)
        elif self.options.build_system == "cmake":
            self.build_requires("cmake/[>=3.15.3]@%s/stable" % self.user)

    def build(self):
        if self.options.build_system == "meson":
            meson = Meson(self)
            meson.configure(build_folder="build")
            meson.install()
        elif self.options.build_system == "cmake":
            cmake = CMake(self, generator="Ninja")
            cmake.configure()
            cmake.install()
