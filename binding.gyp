{
    'variables': {
       'use_ffmpeg%': 0,
    },
    'targets': [
        {
            'target_name': 'openssl',
            'type': 'none',
            'variables': {
               'openssl_cflags%': '<!(pkg-config --cflags openssl)',
               'openssl_ldflags%': '<!(pkg-config --libs-only-L --libs-only-other openssl)',
               'openssl_libraries%': '<!(pkg-config --libs-only-l openssl)',
            },
            'direct_dependent_settings': {
                'cflags': [
                    '<@(openssl_cflags)',
                ],
            },
            'link_settings': {
                'ldflags': [
                    '<@(openssl_ldflags)',
                ],
                'libraries': [
                    '<@(openssl_libraries)',
                ],
            },
        },
        {
            'target_name': 'libmediaserver',
            'type': '<(library)',
            'cflags_cc': [
                '-std=c++17',
            ],
            'dependencies': [
                'openssl',
                'ext/mp4v2/libmp4v2.gyp:mp4v2',
                'ext/srtp/libsrtp.gyp:libsrtp',
            ],
            'export_dependent_settings': [
                'ext/mp4v2/libmp4v2.gyp:mp4v2',
                'ext/srtp/libsrtp.gyp:libsrtp',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    'include',
                    'src',
                    'ext/libdatachannels/src/',
                    'ext/libdatachannels/src/internal/',
                ],
            },
            'include_dirs': [
                'include',
                'src',
                'ext/libdatachannels/src/',
                'ext/libdatachannels/src/internal/',
            ],
            'sources': [
                'src/utf8.cpp',
            ],
            'conditions': [
                ['use_ffmpeg==1', {
                    'dependencies': [
                        'libavcodec',
                    ],
                }],
            ]
        },
    ],
    'conditions': [
        ['use_ffmpeg==1', {
            'targets': [
                {
                    'target_name': 'libavcodec',
                    'type': 'none',
                    'variables': {
                       'libavcodec_cflags%': '<!(pkg-config --cflags libavcodec)',
                       'libavcodec_ldflags%': '<!(pkg-config --libs-only-L --libs-only-other libavcodec)',
                       'libavcodec_libraries%': '<!(pkg-config --libs-only-l libavcodec)',
                    },
                    'direct_dependent_settings': {
                        'cflags': [
                            '<@(libavcodec_cflags)',
                        ],
                    },
                    'link_settings': {
                        'ldflags': [
                            '<@(libavcodec_ldflags)',
                        ],
                        'libraries': [
                            '<@(libavcodec_libraries)',
                        ],
                    },
                },
            ],
        }],
    ],
}
