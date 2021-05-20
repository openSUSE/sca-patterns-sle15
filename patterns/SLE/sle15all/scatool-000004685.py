#!/usr/bin/python
#
# Title:       Pattern for TID000004685
# Description: scatool fails with traceback
# Source:      Package Version Pattern Template v0.3.8
# Options:     SLE,Monitoring,SCA,scatool,000004685,0,sca-server-report,1.0.1-4.3.1,0,0
# Modified:    2021 May 20
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

import os
import Core
import SUSE

META_CLASS = "SLE"
META_CATEGORY = "Monitoring"
META_COMPONENT = "SCA"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000004685"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'sca-server-report'
RPM_WORKAROUND = 'python'
RPM_VERSION_FIXED = '1.0.1-4.3'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION_FIXED)
	if( INSTALLED_VERSION >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME + "")
	else:
		if( SUSE.packageInstalled(RPM_WORKAROUND) ):
			Core.updateStatus(Core.WARN, "SCA Tool work around in place, update " + RPM_NAME + " package for complete fix")
		else:
			Core.updateStatus(Core.CRIT, "SCA Tool will fail with import errors, update " + RPM_NAME + " package to resolve")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")


Core.printPatternResults()

