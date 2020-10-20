# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Wcs(CMakePackage):
    """Simulates whole cell models using discrete event simulation."""

    homepage = "https://github.com/LLNL/wcs.git"
    git      = "https://github.com/LLNL/wcs.git"
    maintainers = ['rblake-llnl']

    version('master', branch='master')
    version('develop', branch='devel')

    variant("des", default='none', 
            description='Discrete event simulation engine to use',
            values=('ross','none'), multi=False)
    variant("exprtk", default=True, description="Use exprtk for inputs")

    depends_on('boost+graph+filesystem+regex+system')
    depends_on('sbml@5.18.0:+cpp')
    depends_on('cmake@3.12:', type='build')
    depends_on('cereal', type='build')
    depends_on('ross', when="des=ross")
    depends_on('mpi', when="des=ross")

    def cmake_args(self):
        spec = self.spec
        args = [
            "-DBOOST_ROOT:PATH=" + spec['boost'].prefix,
            "-DCEREAL_ROOT:PATH=" + spec['cereal'].prefix,
            "-DSBML_ROOT:PATH=" + spec['sbml'].prefix,
            "-DWCS_WITH_SBML:BOOL=ON",
        ]
        if "+exprtk" in spec:
            args.append("-DWCS_WITH_EXPRTK:BOOL=ON")
        if "des=ross" in spec:
            args.append("-DWCS_WITH_ROSS:BOOL=ON")
        return args
