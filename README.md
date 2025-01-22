# Welcome to Siting Lab Tutorials!

[![Release Documentation](https://github.com/NREL/SitingLab/actions/workflows/docs.yml/badge.svg)](https://nrel.github.io/SitingLab)
![Static Badge](https://img.shields.io/badge/SWR--24--95_%E2%80%9CSiting%20Lab%E2%80%9D-blue?label=NREL)
[![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)


This repository contains a collection of user-friendly tutorials and guides for working with the [Siting Lab](https://data.openei.org/siting_lab)
data within the context of the `reV` model. The python code examples demonstrate the creation and transformation of
Siting Lab data into `reV` compliant format as well as working with the `reV` model inputs and outputs.


# Getting Started

To interactively access the tutorial notebooks in this repository,
first grab a copy of the repository by cloning it from GitHub:

    $ git clone git@github.com:NREL/SitingLab.git

Before running any of the notebook tutorials, you should set up a Python environment that contains all the
required dependencies and can launch jupyter for you.

## Environment Setup

All instructions below assume you are executing the commands from the root directory
of the Siting Lab Tutorial code repository you just downloaded.

### Using Pixi (recommended)

We use [pixi](https://pixi.sh/latest/) to manage cross-platform Siting Lab Tutorial
environments. This tool allows developers to install libraries and dependencies in a
compatible and reproducible way. We keep a version-controlled ``pixi.lock``
in the repository to allow locking with the full requirements tree so that
behaviors and results can easily be reproduced.

To use pixi, simply install it using the link above and then run the following
command in the root directory of the Siting Lab Tutorial code repository:

    $ pixi run jupyter lab


### Using Pip

You can install all the packages required for Siting Lab Tutorials using Python's
native package installer `pip`. We strongly recommend using an environment manager
like `conda` or  `mamba` in this case. The steps below assume you have installed
`conda` on your machine.

   1) Create a conda env: `conda create --name slt python=3.11`.

   2) Activate the newly-created conda env: `conda activate slt`.

   3) Install Siting Lab Tutorial dependencies using `pip`: `pip install .`


## Running the notebooks

Once your environment is installed and activate, you can run the following command to
launch the jupyter server:

    $ jupyter lab

Once the server starts, you can navigate to the URL shown on the terminal and access
any notebook tutorial you wish!
