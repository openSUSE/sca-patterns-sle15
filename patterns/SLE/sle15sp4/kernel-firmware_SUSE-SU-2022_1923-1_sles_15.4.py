#!/usr/bin/python3
#
# Title:       Important Security Announcement for kernel-firmware SUSE-SU-2022:1923-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP4
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-June/011226.html
# Source:      Security Announcement Generator (sagen.py) v2.0.0-beta4
# Modified:    2022 Oct 05
#
##############################################################################
# Copyright (C) 2022 SUSE LLC
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

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "kernel-firmware"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-June/011226.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kernel-firmware'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:1923-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'kernel-firmware-all': '20220509-150400.4.5.1',
			'kernel-firmware-amdgpu': '20220509-150400.4.5.1',
			'kernel-firmware-ath10k': '20220509-150400.4.5.1',
			'kernel-firmware-ath11k': '20220509-150400.4.5.1',
			'kernel-firmware-atheros': '20220509-150400.4.5.1',
			'kernel-firmware-bluetooth': '20220509-150400.4.5.1',
			'kernel-firmware-bnx2': '20220509-150400.4.5.1',
			'kernel-firmware-brcm': '20220509-150400.4.5.1',
			'kernel-firmware-chelsio': '20220509-150400.4.5.1',
			'kernel-firmware-dpaa2': '20220509-150400.4.5.1',
			'kernel-firmware-i915': '20220509-150400.4.5.1',
			'kernel-firmware-intel': '20220509-150400.4.5.1',
			'kernel-firmware-iwlwifi': '20220509-150400.4.5.1',
			'kernel-firmware-liquidio': '20220509-150400.4.5.1',
			'kernel-firmware-marvell': '20220509-150400.4.5.1',
			'kernel-firmware-media': '20220509-150400.4.5.1',
			'kernel-firmware-mediatek': '20220509-150400.4.5.1',
			'kernel-firmware-mellanox': '20220509-150400.4.5.1',
			'kernel-firmware-mwifiex': '20220509-150400.4.5.1',
			'kernel-firmware-network': '20220509-150400.4.5.1',
			'kernel-firmware-nfp': '20220509-150400.4.5.1',
			'kernel-firmware-nvidia': '20220509-150400.4.5.1',
			'kernel-firmware-platform': '20220509-150400.4.5.1',
			'kernel-firmware-prestera': '20220509-150400.4.5.1',
			'kernel-firmware-qcom': '20220509-150400.4.5.1',
			'kernel-firmware-qlogic': '20220509-150400.4.5.1',
			'kernel-firmware-radeon': '20220509-150400.4.5.1',
			'kernel-firmware-realtek': '20220509-150400.4.5.1',
			'kernel-firmware-serial': '20220509-150400.4.5.1',
			'kernel-firmware-sound': '20220509-150400.4.5.1',
			'kernel-firmware-ti': '20220509-150400.4.5.1',
			'kernel-firmware-ueagle': '20220509-150400.4.5.1',
			'kernel-firmware-usb-network': '20220509-150400.4.5.1',
			'ucode-amd': '20220509-150400.4.5.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

