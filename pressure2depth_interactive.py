#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pressure2depth_interactive.py
Interactive CLI – i18n ready (zh_CN / en_US auto-switch)
"""

import os
import locale
import gettext
import numpy as np
import pandas as pd

# ---------- 国际化 ----------
localedir = os.path.join(os.path.dirname(__file__), 'locale')
lang = locale.getdefaultlocale()[0] or 'en_US'
_ = gettext.translation('messages', localedir,
                        languages=[lang], fallback=True).gettext

# ---------- 算法 ----------
def pressure_to_depth(p, lat_deg):
    phi = np.deg2rad(lat_deg)
    x = np.sin(phi) ** 2
    g = 9.780318 * (1.0 + (5.2788e-3 + 2.36e-5 * x) * x) + 1.092e-6 * p
    numerator = (((-1.82e-15 * p + 2.279e-10) * p - 2.2512e-5) * p + 9.72659)
    return numerator * p / g

# ---------- 主程序 ----------
def main():
    print(_("=== Pressure→Depth Converter ==="))
    print(_("Please drag or paste the CSV file path and press Enter:"))
    file_path = input("> ").strip('"')

    if not os.path.isfile(file_path):
        print(_("❌ File not found – please check the path."))
        return

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(_("❌ Read failed: {}").format(e))
        return

    if df.shape[1] < 2:
        print(_("❌ CSV must contain at least two columns: pressure & latitude."))
        return

    # 自动识别列
    p_col, lat_col = df.columns[0], df.columns[1]
    print(_("Detected:"))
    print(_("  Pressure column : {}").format(p_col))
    print(_("  Latitude column : {}").format(lat_col))

    df = df.dropna(subset=[p_col, lat_col])
    df["Depth_m"] = df.apply(
        lambda row: pressure_to_depth(row[p_col], row[lat_col]), axis=1
    )

    base, ext = os.path.splitext(file_path)
    out_path = f"{base}_depth{ext}"
    df.to_csv(out_path, index=False)

    print(_("✅ Processing complete."))
    print(_("Result saved to: {}").format(out_path))
    print(df.head())

if __name__ == "__main__":
    main()