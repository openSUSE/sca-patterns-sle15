#!/usr/bin/python

# Title:       Amavis Virus Scanner failed start
# Description: amavis.service failed to start after upgrade
# Modified:    2021 Mar 25
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

##############################################################################
# Module Definition
##############################################################################

import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Services"
META_COMPONENT = "Amavis"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019709"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'amavisd-new'
SERVICE_NAME = 'amavis.service'
SERVICE_INFO = SUSE.getServiceDInfo(SERVICE_NAME)

if( SUSE.packageInstalled(RPM_NAME) ):
	if( SERVICE_INFO['UnitFileState'] == 'enabled' ):
		if( SERVICE_INFO['SubState'] == 'failed' ):
			if 'sa-update' in SERVICE_INFO['StatusText']:
				Core.updateStatus(Core.CRIT, "The " + str(SERVICE_NAME) + " has failed, run sa-update")
			else:
				Core.updateStatus(Core.WARN, "The " + str(SERVICE_NAME) + " has failed, consider running sa-update")
		else:
			Core.updateStatus(Core.ERROR, "Service did not fail: " + str(SERVICE_NAME))
	else:
		Core.updateStatus(Core.ERROR, "Service is disabled: " + str(SERVICE_NAME))
else:
	Core.updateStatus(Core.ERROR, "ERROR: RPM package " + RPM_NAME + " not installed")

Core.printPatternResults()
