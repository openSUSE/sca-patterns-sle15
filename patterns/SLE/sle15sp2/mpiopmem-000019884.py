#!/usr/bin/python
#
# Title:       Pattern for TID000019884
# Description: Executing multipath -ll on Optane memory based pmem devices returns HDIO_GETGEO failed with 25
# Source:      Package Version Pattern Template v0.3.8
# Options:     SLE,DM,MPIO,mpiopmem,000019884,0,multipath-tools,0.8.2+166.7501a27-4.9.1,0,1
# Modified:    2021 Jun 16
#
##############################################################################
# Copyright (C) 2021, SUSE LLC
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
META_CATEGORY = "DM"
META_COMPONENT = "MPIO"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019884"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def mpioPmemErrors():
	fileOpen = "mpio.txt"
	section = "bin/multipath -ll"
	content = []
	CONFIRMED = re.compile("pmem.*HDIO_GETGEO failed with 25", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

IN_SCOPE = False
RPM_NAME = 'multipath-tools'
RPM_VERSION_FIXED = ''

SERVER = SUSE.getHostInfo()
if( SERVER['DistroVersion'] == 15 ):
	if( SERVER['DistroPatchLevel'] == 2 ):
		RPM_VERSION_FIXED = '0.8.2+166.7501a27-4.9.1'
		IN_SCOPE = True

if( IN_SCOPE ):
	if( SUSE.packageInstalled(RPM_NAME) ):
		INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION_FIXED)
		if( INSTALLED_VERSION >= 0 ):
			Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME + "")
		else:
			if( mpioPmemErrors() ):
				Core.updateStatus(Core.WARN, "Optane memory based devices with multipath errors")
			else:
				Core.updateStatus(Core.IGNORE, "Optane memory based device errors not found")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")
else:
	Core.updateStatus(Core.ERROR, "ERROR: Outside distro scope")


Core.printPatternResults()

