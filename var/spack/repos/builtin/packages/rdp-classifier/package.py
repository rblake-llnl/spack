# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RdpClassifier(Package):
    """The RDP Classifier is a naive Bayesian classifier that can rapidly and
       accurately provides taxonomic assignments from domain to genus, with
       confidence estimates for each assignment. """

    homepage = "http://rdp.cme.msu.edu/"
    url      = "https://downloads.sourceforge.net/project/rdp-classifier/rdp-classifier/rdp_classifier_2.12.zip"

    version('2.12', '7fdfa33512629810f0ff06b905642ddd')

    depends_on('java', type=('build', 'run'))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path('dist', 'classifier.jar'), prefix.bin)
        install_tree(join_path('dist', 'lib'), prefix.bin.lib)
        install(join_path('lib', 'junit-4.8.2.jar'), prefix.bin.lib)
        install_tree('src', prefix.src)
