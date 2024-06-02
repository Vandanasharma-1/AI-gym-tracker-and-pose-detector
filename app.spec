# app.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Import collect_data_files
from PyInstaller.utils.hooks import collect_data_files

# Collect MediaPipe data files
mediapipe_data_files = collect_data_files('mediapipe')

a = Analysis(
    ['app.py'],
    pathex=['C:\\Users\\Lenovo\\OneDrive\\Desktop\\p'],
    binaries=[],
    datas=mediapipe_data_files,  # Include MediaPipe data files
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to False for a windowed application
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
