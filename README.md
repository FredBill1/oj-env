Online Judge Environment
===

- [Online Judge Environment](#online-judge-environment)
- [1 Setup](#1-setup)
  - [1.1 Requirements](#11-requirements)
  - [1.2 Clone the Repository](#12-clone-the-repository)
  - [1.3 Configure VSCode](#13-configure-vscode)
    - [1.3.1 Install Extensions](#131-install-extensions)
    - [1.3.2 Configure Keybindings](#132-configure-keybindings)
    - [1.3.3 Generate Source Files and Configure `CMake Tools` Extension](#133-generate-source-files-and-configure-cmake-tools-extension)
- [2 Usage](#2-usage)
  - [2.1 Generate Source Files and Reconfigure CMake](#21-generate-source-files-and-reconfigure-cmake)
  - [2.2 Build and Debug](#22-build-and-debug)
  - [2.3 Expand `atcoder/ac-library` Headers](#23-expand-atcoderac-library-headers)
  - [2.4 Customize the Settings](#24-customize-the-settings)

# 1 Setup

## 1.1 Requirements

- [CMake](https://cmake.org/download/)
- [Ninja](https://ninja-build.org/)
- A Working C++ Compiler. For Windows, MSVC from [Visual Studio](https://visualstudio.microsoft.com/) is recommended (a `bits/stdc++.h` is copied from [GCC](https://gcc.gnu.org/), which can be included directly); if you want to use g++, [MSYS2](https://www.msys2.org/) is recommended.
- [clangd](https://clangd.llvm.org/installation.html), which will be prompted to be automatically installed when installing the `clangd` extension in VSCode (see [1.3.1](#131-install-extensions)), but you can also install it manually.
- Python ([Miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/) is recommended)
- [VSCode](https://code.visualstudio.com/)

## 1.2 Clone the Repository

```bash
git clone https://github.com/FredBill1/oj-env.git --depth=1
cd oj-env
git submodule update --init --depth=1
```

## 1.3 Configure VSCode

### 1.3.1 Install Extensions

Press `F1` or `Ctrl+Shift+P` to open the command palette, type and select `Extensions: Show Recommended Extensions `. Then install the extensions shown in `WORKSPACE RECOMMENDATIONS` (which are specified in [`.vscode/extensions.json`](.vscode/extensions.json)).

Note that the clangd executable will be prompted to be automatically installed when installing the `clangd` extension. If missed, you can still use `F1` or `Ctrl+Shift+P` to open the command palette, type and select `clangd: Download language server` to install it.

### 1.3.2 Configure Keybindings

Beacuse VSCode cannot have independent keybindings for different workspaces according to a configuration file, you need to manually configure the keybindings globally.

Press `F1` or `Ctrl+Shift+P` to open the command palette, type and select `Preferences: Open Keyboard Shortcuts (JSON)`. Then paste the content of [`.vscode/keybindings.json`](.vscode/keybindings.json) into the opened file.

### 1.3.3 Generate Source Files and Configure `CMake Tools` Extension

Run the following command to generate the source files:

```bash
python generate_src.py
```

The command will create two folders `src` and `pysrc`, and a text file `input.txt` for `stdin` redirect; where `src` contains the C++ source files and `pysrc` contains the python source files based on the templates in the [`templates`](templates) folder.

Then press `F1` or `Ctrl+Shift+P` to open the command palette, type and select `CMake: Select a Kit`, and select the compiler you want to use. Then type and select `CMake: Configure` to generate the build files.

Press `F1` or `Ctrl+Shift+P` to open the command palette, type and select `CMake: Set Build Target`, and select the target named `dummy`. Because every time when debugging with the `CMake Tools` extension, it will always build a selected target no matter what, so we set an emtpy dummy target to avoid redundant builds.

Press `F1` or `Ctrl+Shift+P` to open the command palette, type and select `CMake: Set Debug Target`, and select `A`, which represents the file `src/A.cpp`. After that, the debug target will appear in the status bar at the bottom of the window, and you can click it to change the target to debug later, without the need to open the command palette.

# 2 Usage

## 2.1 Generate Source Files and Reconfigure CMake

You can run `generate_src.py` to regenerate the source files. The files are copied from the `templates` folder, so you can modify the templates to customize the generated files.

> **Important:** When running `generate_src.py`, the contents of the `src` and `pysrc` folders will be **wiped** and regenerated, make sure to move away the files you want to keep before running the script.

When adding new source files for C++ in the `src` folder, you need to call `CMake: Configure` again to update the build files.

## 2.2 Build and Debug

Press `F5` to debug, `Ctrl+F5` to run without debugging. When focusing on a `.py` source file, `F5` or `Ctrl+F5` will run the current focused python file; otherwise it will run the current selected CMake debug target, which will first be built automatically if necessary.

By default, the `stdin` is redirected from `input.txt` generated by `generate_src.py`, which means you do not need to type the inputs mannually to the program every time it runs. You can disable the redirection:

- for Python, by comment out the `args` section containing `"<", "input.txt"` in the [`.vscode/launch.json`](.vscode/launch.json) file.
- for C++, by comment out the `agrs` section in `cmake.debugConfig` in the [`.vscode/settings.json`](.vscode/settings.json) file.

> Note: the `<` operator in the `args` section is not supported by powershell, so the default terminal is set to `cmd.exe` on Windows in the [`.vscode/settings.json`](.vscode/settings.json) via `"terminal.integrated.defaultProfile.windows": "Command Prompt"`.

## 2.3 Expand [`atcoder/ac-library`](https://github.com/atcoder/ac-library.git) Headers

You can use the [`atcoder/ac-library`](https://github.com/atcoder/ac-library.git) library by directly including the headers in C++ source files, e.g.:

```cpp
#include <atcoder/all>
```

Before submitting the code to an online judge, you need to expand the headers by running the following command:

```bash
python aclib_expand.py
```

The command will **inplacely** expand the headers for all the C++ source files in the `src` folder.

## 2.4 Customize the Settings

- `Format On Save` can be disabled by setting `"editor.formatOnSave": false` in [`.vscode/settings.json`](.vscode/settings.json).
- C++ formatting style can be customized by modifying [`.clang-format`](.clang-format).
