# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class XercesC(AutotoolsPackage):
    """Xerces-C++ is a validating XML parser written in a portable subset of
    C++. Xerces-C++ makes it easy to give your application the ability to read
    and write XML data. A shared library is provided for parsing, generating,
    manipulating, and validating XML documents using the DOM, SAX, and SAX2
    APIs."""

    homepage = "https://xerces.apache.org/xerces-c"
    url      = "https://archive.apache.org/dist/xerces/c/3/sources/xerces-c-3.2.1.tar.bz2"

    version('3.2.1', '8f98a81a3589bbc2dad9837452f7d319')
    version('3.1.4', 'd04ae9d8b2dee2157c6db95fa908abfd')

    depends_on('libiconv')

    def setup_environment(self, spack_env, run_env):
        spack_env.append_flags('LDFLAGS', self.spec['libiconv'].libs.ld_flags)

    def configure_args(self):
        return ['--disable-network']
