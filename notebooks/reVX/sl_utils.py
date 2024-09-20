"""Siting Lab reV tutorial utility functions."""

import urllib.request
from pathlib import Path

import rasterio
from rasterio.windows import Window


def crop_raster(
    raster_fp, x_size=2000, y_size=2000, x_offset=47000, y_offset=10000
):
    window = Window(x_offset, y_offset, x_size, y_size)
    with rasterio.open(raster_fp) as src:
        transform = src.window_transform(window)

        profile = src.profile
        profile.update(
            {"height": y_size, "width": x_size, "transform": transform}
        )
        if "crs" in profile:
            profile["crs"] = str(profile["crs"]).replace("+init=", "")

        data = src.read(window=window)

    with rasterio.open(raster_fp, "w", **profile) as dst:
        dst.write(data)


def download_tiff_file(file_url, local_filepath, crop=True):
    if Path(local_filepath).exists():
        print(f"{str(local_filepath)!r} already exists!")
        return

    urllib.request.urlretrieve(file_url, local_filepath)
    if crop:
        crop_raster(local_filepath)
    print(f"Downloaded {str(local_filepath)!r}!")
