#!/usr/bin/python3
#
# Title:       Pattern for TID000020688
# Description: kernel crashes at nfs4_get_valid_delegation function
# Source:      Kernel Package Version Pattern Template v1.0.0
# Options:     SLE,NFS,Crash,nfs4delegation,000020688,0,5.3.18-24.9,0,1
# Modified:    2022 Jul 06
#
##############################################################################
# Copyright (C) 2022, SUSE LLC
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
META_CATEGORY = "NFS"
META_COMPONENT = "Crash"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020688"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def nfsModuleLoaded():
	DRIVER_INFO = SUSE.getDriverInfo('nfsv4')
	if( DRIVER_INFO['loaded'] ):
		return True
	return False

def nfsCrashFound():
	fileOpen = "boot.txt"
	section = "dmesg -T"
	content = []
	CONFIRMED = re.compile("RIP:.*nfs4_get_valid_delegation.*[nfsv4]")
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

KERNEL_VERSION_FIXED = '5.3.18-24.9'

INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION_FIXED)
if( INSTALLED_VERSION >= 0 ):
	Core.updateStatus(Core.IGNORE, "IGNORE: Bug fixes applied in kernel version " + KERNEL_VERSION_FIXED + " or higher")
else:
	if( nfsModuleLoaded() ):
		if( nfsCrashFound() ):
			Core.updateStatus(Core.CRIT, "Detected nfs4_get_valid_delegation kernel crash, update system to resolve")
		else:
			Core.updateStatus(Core.WARN, "Susceptible to nfs4_get_valid_delegation kernel crash, update system to avoid")
	else:
		Core.updateStatus(Core.IGNORE, "IGNORE: NFSv4 driver not loaded")

Core.printPatternResults()

