# To link your .gyp file to the libsqlite.so shared library, you'll need to modify the dependencies and linker flags appropriately.
# Below is an example of how you can link the better_sqlite3 target to libsqlite.so:

{
  'includes': ['deps/common.gypi'],
  'targets': [
    {
      'target_name': 'better_sqlite3',
      'dependencies': [
        'deps/sqlite3.gyp:sqlite3',
        'your_path_to_libsqlite_so/libsqlite.so',  # Add the path to libsqlite.so
      ],
      'sources': ['src/better_sqlite3.cpp'],
      'cflags_cc': ['-std=c++17'],
      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': ['-std=c++17', '-stdlib=libc++'],
      },
      'msvs_settings': {
        'VCCLCompilerTool': {
          'AdditionalOptions': [
            '/std:c++17',
          ],
        },
      },
      'conditions': [
        ['OS=="linux"', {
          'ldflags': [
            '-shared',
            '-Wl,-Bsymbolic',
            '-Wl,--exclude-libs,ALL',
          ],
        }],
      ],
    },
    {
      'target_name': 'test_extension',
      'dependencies': ['deps/sqlite3.gyp:sqlite3'],
      'conditions': [['sqlite3 == ""', { 'sources': ['deps/test_extension.c'] }]],
    },
  ],
}


# In the dependencies section of the better_sqlite3 target, add the path to the libsqlite.so file.

# Replace 'your_path_to_libsqlite_so/libsqlite.so' with the actual path to the library file on your system.

# Remember to adjust the path based on your project's directory structure and the location of the libsqlite.so file on your system.

# Also, ensure that the header paths and other necessary build settings are correctly configured to work with the dynamic linking to libsqlite.so.