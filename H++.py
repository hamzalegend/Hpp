import os

solutionName = input("SolutionName: ").strip()
# projectName = input(f"ProjectName: [ENTER FOR DEFAULT ('{solutionName}')]").strip()
cppstd = input("C++ Standard: [ENTER FOR DEFAULT (17)]").strip()

# if projectName == "": projectName = solutionName

if cppstd == "": cppstd = 17 
else: cppstd = int(cppstd)

os.system(f"mkdir {solutionName}")
# os.system(f"mkdir {solutionName}/{projectName}")
os.system(f"mkdir {solutionName}/Build")
os.system(f"mkdir {solutionName}/src")
os.system(f"mkdir {solutionName}/vendor")

os.system(f"touch {solutionName}/CMakeLists.txt")
os.system(f"touch {solutionName}/src/main.cpp")
os.system(f"touch {solutionName}/Build/Build.bat")

cmakesrc = f'''
cmake_minimum_required(VERSION 3.0.0)

set(CMAKE_CXX_STANDARD {cppstd})
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project({solutionName} VERSION 0.1.0 LANGUAGES CXX)

file(GLOB_RECURSE srcFiles
    "src/*.h"
    "src/*.cpp"
)

add_executable({solutionName} ${{srcFiles}})


target_include_directories({solutionName} PUBLIC ${{CMAKE_CURRENT_SOURCE_DIR}}/src)
target_include_directories({solutionName} PUBLIC ${{CMAKE_CURRENT_SOURCE_DIR}}/vendor)

# add another cmakelists.txt as a sub-project in a child dir 
# add_subdirectory(dir)

# create and add a lib to your Proj:
# add_library(my_lib STATIC mylib.cpp)
# target_link_libraries(my_exec PUBLIC mylib)
'''
mainsrc = f'''#include <iostream>

int main()
{{
    std::cout << "Hello {solutionName}" << std::endl;
    return 0;
}};
'''
Buildsrc = f'''pwd
cd {solutionName}/Build/
cmake ..
make
./{solutionName}
'''


with open(f"{solutionName}/CMakeLists.txt", "w") as f:
    f.write(cmakesrc)
with open(f"{solutionName}/src/main.cpp", "w") as f:
    f.write(mainsrc)
with open(f"{solutionName}/Build/Build.bat", "w") as f:
    f.write(Buildsrc)

os.system(f"chmod +x {solutionName}/Build/Build.bat")
os.system(f"./{solutionName}/Build/Build.bat")

