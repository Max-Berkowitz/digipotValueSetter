{
  "targets": [
    { 
      "target_name": "getCode",
      "include_dirs": [ "<(module_root_dir)/server/app/util" ],
      "sources": [ "<(module_root_dir)/server/app/util/getCode.cpp", "<(module_root_dir)/server/app/util/StdAfx.cpp" ],
      "link_settings": { "libraries": [ "-lVCAIOUSB64" ], "library_dirs" : [ "<(module_root_dir)/server/app/util" ] }
    },
    { 
      "target_name": "incrimentCode",
      "include_dirs": [ "<(module_root_dir)/server/app/util" ],
      "sources": [ "<(module_root_dir)/server/app/util/incrimentCode.cpp", "<(module_root_dir)/server/app/util/StdAfx.cpp" ],
      "link_settings": { "libraries": [ "-lVCAIOUSB64" ], "library_dirs" : [ "<(module_root_dir)/server/app/util" ] }
    },
    { 
      "target_name": "decrimentCode",
      "include_dirs": [ "<(module_root_dir)/server/app/util" ],
      "sources": [ "<(module_root_dir)/server/app/util/decrimentCode.cpp", "<(module_root_dir)/server/app/util/StdAfx.cpp" ],
      "link_settings": { "libraries": [ "-lVCAIOUSB64" ], "library_dirs" : [ "<(module_root_dir)/server/app/util" ] }
    },
    { 
      "target_name": "saveCode",
      "include_dirs": [ "<(module_root_dir)/server/app/util" ],
      "sources": [ "<(module_root_dir)/server/app/util/saveCode.cpp", "<(module_root_dir)/server/app/util/StdAfx.cpp" ],
      "link_settings": { "libraries": [ "-lVCAIOUSB64" ], "library_dirs" : [ "<(module_root_dir)/server/app/util" ] }
    },
    { 
      "target_name": "setCode",
      "include_dirs": [ "<(module_root_dir)/server/app/util" ],
      "sources": [ "<(module_root_dir)/server/app/util/setCode.cpp", "<(module_root_dir)/server/app/util/StdAfx.cpp" ],
      "link_settings": { "libraries": [ "-lVCAIOUSB64" ], "library_dirs" : [ "<(module_root_dir)/server/app/util" ] }
    },
    { 
      "target_name": "configure",
      "include_dirs": [ "<(module_root_dir)/server/app/util" ],
      "sources": [ "<(module_root_dir)/server/app/util/configure.cpp", "<(module_root_dir)/server/app/util/StdAfx.cpp" ],
      "link_settings": { "libraries": [ "-lVCAIOUSB64" ], "library_dirs" : [ "<(module_root_dir)/server/app/util" ] }
    }
  ]
}