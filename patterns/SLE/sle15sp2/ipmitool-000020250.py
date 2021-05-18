#!/usr/bin/python
#
# Title:       Pattern for TID000020250
# Description: ipmitool: lanplus: hanging on getting cipher suites
# Source:      Package Version Pattern Template v0.3.8
# Options:     SLE,Monitoring,IPMI,ipmitool,000020250,1185684,ipmitool,0,ipmitool-1.8.18+git20200204.7ccea28-1.22,0
# Distro:      SLES15 SP2
# Modified:    2021 May 18
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
META_COMPONENT = "IPMI"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020250|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1185684"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'ipmitool'
RPM_VERSION_BROKE = '1.8.18+git20200204.7ccea28-1.22'
RPM_VERSION_FIXED = RPM_VERSION_BROKE
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION_FIXED)
	if( INSTALLED_VERSION > 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME + "")
	else:
#		INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION_BROKE)
		if( INSTALLED_VERSION == 0 ):
			Core.updateStatus(Core.WARN, "The ipmitool may hang on ipmi devices without using the ciphersuite option")
		else:
			Core.updateStatus(Core.IGNORE, "Previously unaffected version of " + RPM_NAME + " installed")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")


Core.printPatternResults()

