# Siting Lab Tutorial Notebooks

This directory contains tutorials in the form of Jupyter Notebooks to help you work with
Siting Lab data.

## Jupyter Notebooks

The tutorial notebooks are split into categories based on the underlying
code repository: `reV`, and `reVX`.

Some notebooks define other notebooks as requirements. In that case, following
the recommended order helps to build the required concepts and make it an
easier learning process.


> [!NOTE]
> Jupyter Notebooks are a fantastic analysis tool. They allow you to run
> bits and pieces of python code, check the results, and interactively
> re-run with changes if need be. If you have never used Jupyter Notebooks,
> check out some of the many guides available online
> (e.g. [this one](https://www.codecademy.com/article/how-to-use-jupyter-notebooks)).

### reVX

This set of tutorials helps introduce you to [`reVX`](https://github.com/NREL/reVX/) tools. The tutorials are listed by recommended order:

- [Working with GeoTIFFs](reVX/01_geotiff_tutorial.ipynb): Introduction to the ``Geotiff`` handler, which provides a simple interface to load, extract, and write various information to and from GeoTIFF files.
- [GeoTIFFs to reV HDF5 Files](reVX/02_layered_h5_tutorial.ipynb): Introduction to the ``LayeredH5`` handler, which provides a simple interface to create and write to an HDF5 file formatted for `reV` exclusion data.


### reV

This set of tutorials helps introduce you to [`reV`](https://github.com/NREL/reV/) tools. The tutorials are listed by recommended order:

- [Supply Curve + Temporal Profiles](reV/01_temporal_profiles.ipynb): Demonstrates how to link Supply Curve outputs with temporal profiles.
