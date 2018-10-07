# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Stc(AutotoolsPackage):
    """STC: The Swift-Turbine Compiler"""

    homepage = 'http://swift-lang.org/Swift-T'
    url      = 'http://swift-lang.github.io/swift-t-downloads/stc-0.7.3.tar.gz'

    version('0.7.3', '6bf769f406f6c33d1c134521373718d3')

    depends_on('java')
    depends_on('ant')
    depends_on('turbine')
    depends_on('zsh', type='run')

    def configure_args(self):
        args = ['--with-turbine=' + self.spec['turbine'].prefix]
        return args
