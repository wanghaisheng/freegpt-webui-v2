# https://github.com/Futura-Py/TimerX/tree/master
import sys

from cx_Freeze import Executable, setup

base = None

if sys.platform == "win32":
    base = "Win32GUI"

    icon = "./client/assets/icon.ico"
    executables = [
        Executable(
            "run.py",
            base=base,
            icon=icon,
            shortcut_name="FreeGPT",
            target_name="FreeGPT.exe",
            shortcut_dir="ProgramMenuFolder",
        )
    ]
elif sys.platform == "darwin":

    # icon = "./client/assets/logo_new.icns"
    icon = "./client/assets/icon.ico"

    executables = [
        Executable(
            "run.py",
            base=base,
            icon=icon,
            shortcut_name="FreeGPT",
            target_name="FreeGPT",
        )
    ]
else:
    # icon = "./client/assets/logo_new.png"
    icon = "./client/assets/icon.ico"

    executables = [
        Executable(
            "run.py",
            base=base,
            icon=icon,
            shortcut_name="FreeGPT",
            target_name="FreeGPT.exe",
        )
    ]

# directory_table = [
#     ("ProgramMenuFolder", "TARGETDIR", "."),
#     ("MyProgramMenu", "ProgramMenuFolder", "MYPROG~1|My Program"),
# ]

# msi_data = {
#     "Directory": directory_table,
#     "ProgId": [
#         ("FreeGPT", None, None, "A simple, lightweight, & beautiful timer app built in Python and tkinter.ttk using rdbende's Sun Valley TTk Theme", "IconId", None),
#     ],
#     "Icon": [
#         ("IconId", "assets/logo.ico"),
#     ],
# }
import uuid

upgradeid = (
    "{" + str(uuid.uuid3(uuid.NAMESPACE_DNS, "FreeGPT-App.FreeGPT.org")).upper() + "}"
)

build_exe_options = {
    "include_msvcr": True,
    # "packages":["server"],
    "include_files": [
         ( './client/', 'client' ),
         ( './g4f/', 'g4f' ),
         ( './server/', 'server' ),
         ( './conf/', 'conf' ),
         ( './translations/', 'translations' )

         ],
#     'includes': [
# "websocket-client","requests","tls-client","pypasser","names",
# "colorama",
# "curl_cffi",
# "aiohttp",
# "flask",
# "flask_cors",
# "flask-babel",
# "streamlit",
# "selenium",
# "fake-useragent",
# "twocaptcha",
# "pydantic",
# "pymailtm",
# "Levenshtein",
# "retrying",
# "mailgw_temporary_email",
# "pycryptodome",
# "random-password-generator",
# "numpy",
# "tornado",
# "PyExecJS",
# "browser_cookie3",
# "js2py",
# "platformdirs",
# "undetected_chromedriver",
# "py_arkose_generator",
# "asyncstdlib",
# "async_property"
#         ], # list of extra modules to include (from your virtualenv of system path),


}

bdist_rpm_options = {"icon": icon}

bdist_msi_options = {
    "add_to_path": False,
    "install_icon": "assets/icon.ico",
    "upgrade_code": upgradeid,
    "target_name": "FreeGPT",
}
bdist_mac_options = {"bundle_name": "FreeGPT", "iconfile": "./client/assets/icon.ico",

"include_resources":[

         ( './client/', 'client' ),
         ( './g4f/', 'g4f' ),
         ( './conf/', 'conf' ),

         ( './translations/', 'translations' )
]

                     }

bdist_dmg_options = {
    "volume_label": "FreeGPT",
    "applications_shortcut": True,
}

version = "0.1.0"

setup(
    name="FreeGPT",
    version=version,
    description="The only FreeGPT tool you'll ever need",
    executables=executables,
    options={
        "build_exe": build_exe_options,
        "bdist_mac": bdist_mac_options,
        "bdist_dmg": bdist_dmg_options,
        "bdist_msi": bdist_msi_options,
        "bdist_rpm": bdist_rpm_options,
    },
)