{
  'targets': [
    {
      'target_name': 'native',
      'include_dirs': [
        '<(node_root_dir)/deps/openssl/openssl/include'
      ],
      'sources': [
        'src/main.cc',
        'src/eckey.cc'
      ],
    }
  ]
}
