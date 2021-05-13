#!/usr/bin/python
#
# Title:       Pattern for TID000019571
# Description: Activation of multiple namespaces simultaneously may lead to an activation failure
# Source:      Basic Python Pattern Template v0.3.4
# Options:     SLE,Kernel,Namespace,namespace,000019571,1157778,1,1,0
# Distro:      SLES15 SP1
# Modified:    2021 May 13
#
##############################################################################
# Copyright (C) 2021 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record <jason.record@suse.com>
#
##############################################################################

import re
import os
import Core
import SUSE

META_CLASS = "SLE"
META_CATEGORY = "Kernel"
META_COMPONENT = "Namespace"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019571|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1157778"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

PACKAGE = "ndctl"
AFFECTED_ARCH = 'ppc'

SERVER = SUSE.getHostInfo()
if( AFFECTED_ARCH in SERVER['Architecture'].lower() ):
	if( SUSE.packageInstalled(PACKAGE) ):
		KERNEL_VERSION = '4.12.14-197.29'
		INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION)
		if( INSTALLED_VERSION < 0 ):
			Core.updateStatus(Core.WARN, "Activating multiple namespaces may fail, update to apply fixes")
		else:
			Core.updateStatus(Core.IGNORE, "Bug fixes applied in kernel version " + KERNEL_VERSION + " or higher")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: RPM package " + PACKAGE + " not installed")
else:
	Core.updateStatus(Core.ERROR, "ERROR: Invalid architecture, only " + AFFECTED_ARCH + " affected")

Core.printPatternResults()

