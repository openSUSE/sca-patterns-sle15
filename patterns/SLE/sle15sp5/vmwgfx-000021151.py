#!/usr/bin/python3
#
# Title:       kernel crashes due to NULL pointer dereference when system runs in graphical mode
# Description: Pattern for TID000021151
# Template:    SCA Tool Python Pattern Generator v2.0.2
# Modified:    2023 Aug 29
#
##############################################################################
# Copyright (C) 2023 SUSE LLC
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

meta_class = "SLE"
meta_category = "Kernel"
meta_component = "Driver"
pattern_id = os.path.basename(__file__)
primary_link = "META_LINK_TID"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000021151|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1213632"
Core.init(meta_class, meta_category, meta_component, pattern_id, primary_link, overall, overall_info, other_links)

##############################################################################
# Local Function Definitions
##############################################################################

def graphical_target():
	service = 'graphical.target'
	service_info = SUSE.getServiceDInfo(service)
	if( service_info['SubState'] == 'active' ):
		return True
	elif( "default" in service_info['Names']):
		return True
	else:
		return False

def vmware_guest():
	virtualization = SUSE.getBasicVirtualization()
	vmhyp = re.compile("VMware", re.IGNORECASE)
	vmid = re.compile("Virtual Machine", re.IGNORECASE)
	if vmhyp.search(virtualization['Hypervisor']):
		if vmid.search(virtualization['Identity']):
			return True
	return False

##############################################################################
# Main
##############################################################################

def main():
	kernel_version_fixed = '5.14.21-150500.55.19'

	kernel_version_installed = SUSE.compareKernel(kernel_version_fixed)
	if( kernel_version_installed >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied in kernel version " + kernel_version_fixed + " or higher")
	else:
		if( graphical_target() ):
			if( vmware_guest() ):
				Core.updateStatus(Core.WARN, "Consider upgrading the kernel for graphical login stability")
			else:
				Core.updateStatus(Core.ERROR, "Error: Not a VMware Virtual Machine")
		else:
			Core.updateStatus(Core.ERROR, "Error: Not in graphical.target")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

