import re

pattern = r'[^,\s]+[\s,]+.*[\s,]+([^,\s]+)'

text = '''{
  "_url": "https://source.android.com/docs/security/bulletin/2023-07-01",
  "text": "\n<em>Published July 5, 2023 | Updated July 10, 2023</em>\n<p>The Android Security Bulletin contains details of security vulnerabilities\n  affecting Android devices. Security patch levels of\n  2023-07-05 or later address all of these issues.\n  To learn how to check a device's security patch level, see\n  <a href=\"https://support.google.com/pixelphone/answer/4457705\" rel=\"noreferrer\">Check and update your Android version</a>.</p>\n<p>Android partners are notified of all issues at least a month before\n  publication.\n  Source code patches for these issues have been released to the Android Open\n  Source Project (AOSP) repository and linked from this bulletin. This bulletin\n  also includes links to patches outside of AOSP.\n </p>\n<p>\n  The most severe of these issues is a critical security vulnerability in the\n  System component that could lead to remote code execution with no additional\n  execution privileges needed. User interaction is not needed for exploitation.\n  The <a href=\"/docs/security/overview/updates-resources#severity\" rel=\"noreferrer\">severity assessment</a> is based on the effect that\n  exploiting the vulnerability would possibly have on an affected device,\n  assuming the platform and service mitigations are turned off for development\n  purposes or if successfully bypassed.\n </p>\n<p>Refer to the <a href=\"#mitigations\">Android and Google Play Protect\n   mitigations</a> section for details on the\n  <a href=\"/security/enhancements\" rel=\"noreferrer\">Android security platform\n   protections</a>\n  and Google Play Protect, which improve the security of the Android platform.</p>\n<aside class=\"note\"><b>Note</b>: Information on the latest over-the-air\n  update (OTA) and firmware images for Google devices is available in the\n  <a href=\"/security/bulletin/pixel/2023-07-01\" rel=\"noreferrer\">July 2023\n   Pixel Update Bulletin</a>.\n </aside>\n<h2 data-text=\"Android and Google service   mitigations\" id=\"Android-and-Google-service-mitigations\" tabindex=\"-1\">Android and Google service\n  mitigations</h2>\n<p>This is a summary of the mitigations provided by the\n  <a href=\"/security/enhancements\" rel=\"noreferrer\">Android security platform</a>\n  and service\n  protections such as\n  <a href=\"https://developers.google.com/android/play-protect\" rel=\"noreferrer\">Google Play\n   Protect</a>. These capabilities reduce the likelihood that security\n  vulnerabilities could be successfully exploited on Android.</p>\n<ul>\n<li>Exploitation for many issues on Android is made more difficult by\n   enhancements in newer versions of the Android platform. We encourage all\n   users\n   to update to the latest version of Android where possible.</li>\n<li>The Android security team actively monitors for abuse through\n   <a href=\"https://developers.google.com/android/play-protect\" rel=\"noreferrer\">Google Play\n    Protect</a> and warns users about\n   <a href=\"/static/security/reports/Google_Android_Security_PHA_classifications.pdf\" rel=\"noreferrer\">Potentially\n    Harmful Applications</a>. Google Play Protect is enabled by default on\n   devices\n   with <a href=\"http://www.android.com/gms\" rel=\"noreferrer\">Google\n    Mobile\n    Services</a>, and is especially important for users who install apps from\n   outside of Google Play.</li>\n</ul>\n<aside class=\"note\">\n<b>Note</b>: There are indications that the following may be under limited,\n  targeted exploitation.\n  <ul>\n<li>CVE-2023-26083</li>\n<li>CVE-2023-2136</li>\n<li>CVE-2021-29256</li>\n</ul>\n</aside>\n<h2 data-text=\"2023-07-01   security patch level vulnerability details\" id=\"2023-07-01-security-patch-level-vulnerability-details\" tabindex=\"-1\">2023-07-01\n  security patch level vulnerability details</h2>\n<p>\n  In the sections below, we provide details for each of the security\n  vulnerabilities that apply to the 2023-07-01 patch level.\n  Vulnerabilities are grouped under the component they affect.\n  Issues are described in the tables below and include CVE ID, associated\n  references, <a href=\"#type\">type of vulnerability</a>,\n  <a href=\"/security/overview/updates-resources#severity\" rel=\"noreferrer\">severity</a>,\n  and updated AOSP versions (where applicable).\n  When available, we link the public change that addressed the issue to the\n  bug ID, like the AOSP change list.\n  When multiple changes relate to a single bug, additional references are\n  linked to numbers following the bug ID.\n  Devices with Android 10 and later may receive security updates as well as\n  <a href=\"https://support.google.com/android/answer/7680439\" rel=\"noreferrer\">Google\n   Play system updates</a>.\n </p>\n<h3 data-text=\"Framework\" id=\"framework\" tabindex=\"-1\">Framework</h3>\n<p>The most severe vulnerability in this section could allow possible\n  elevation\n  of privilege due to a confused deputy with no additional execution privileges\n  needed. User interaction is not needed for exploitation.</p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"21%\"/>\n<col width=\"21%\"/>\n<col width=\"14%\"/>\n<col width=\"14%\"/>\n<col width=\"30%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>CVE</th>\n<th>References</th>\n<th>Type</th>\n<th>Severity</th>\n<th scope=\"col\">Updated AOSP versions</th>\n</tr>\n<tr>\n<td>CVE-2023-20918</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/base/+/16c604aa7c253ce5cf075368a258c0b21386160d\" rel=\"noreferrer\">A-243794108</a>\n     [<a href=\"https://android.googlesource.com/platform/frameworks/base/+/8418e3a017428683d173c0c82b0eb02d5b923a4e\" rel=\"noreferrer\">2</a>]\n     [<a href=\"https://android.googlesource.com/platform/frameworks/base/+/51051de4eb40bb502db448084a83fd6cbfb7d3cf\" rel=\"noreferrer\">3</a>]</td>\n<td>EoP</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-20942</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/av/+/bae3b00a5873d1562679a1289fd8490178cfe064\" rel=\"noreferrer\">A-258021433</a>\n     [<a href=\"https://android.googlesource.com/platform/frameworks/av/+/b072419650958c41c87d2baa572dc2fe6da9ea6b\" rel=\"noreferrer\">2</a>]\n     [<a href=\"https://android.googlesource.com/platform/frameworks/av/+/770b45c3c1619cf4008b89e7a0f4392bf2224bbc\" rel=\"noreferrer\">3</a>]</td>\n<td>EoP</td>\n<td>High</td>\n<td>12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21145</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/base/+/44aeef1b82ecf21187d4903c9e3666a118bdeaf3\" rel=\"noreferrer\">A-265293293</a></td>\n<td>EoP</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21251</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/base/+/57946e2bb73850e817b3c01fa5350d705e178e39\" rel=\"noreferrer\">A-204554636</a></td>\n<td>EoP</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21254</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/base/+/fa539c85503dc63bfb53c76b6f12b3549f14a709\" rel=\"noreferrer\">A-254736794</a></td>\n<td>EoP</td>\n<td>High</td>\n<td>13</td>\n</tr>\n<tr>\n<td>CVE-2023-21257</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/base/+/1aec7feaf07e6d4568ca75d18158445dbeac10f6\" rel=\"noreferrer\">A-257443065</a></td>\n<td>EoP</td>\n<td>High</td>\n<td>13</td>\n</tr>\n<tr>\n<td>CVE-2023-21262</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/av/+/2c8973c39478cd3c8cf11d9f27cc0556a106d006\" rel=\"noreferrer\">A-279905816</a></td>\n<td>EoP</td>\n<td>High</td>\n<td>12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21238</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/base/+/91bfcbbd87886049778142618a655352b16cd911\" rel=\"noreferrer\">A-277740848</a></td>\n<td>ID</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21239</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/base/+/c451aa5710e1da19139eb3716e39a5d6f04de5c2\" rel=\"noreferrer\">A-274592467</a></td>\n<td>ID</td>\n<td>High</td>\n<td>12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21249</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/base/+/c00b7e7dbc1fa30339adef693d02a51254755d7f\" rel=\"noreferrer\">A-217981062</a></td>\n<td>ID</td>\n<td>High</td>\n<td>13</td>\n</tr>\n<tr>\n<td>CVE-2023-21087</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/base/+/4c2c027334672bb4a5fba4880a5536a3bce4e085\" rel=\"noreferrer\">A-261723753</a></td>\n<td>DoS</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n</tbody>\n</table></div>\n<h3 data-text=\"System\" id=\"system\" tabindex=\"-1\">System</h3>\n<p>The most severe vulnerability in this section could lead to remote code\n  execution with no additional execution privileges needed. User interaction is\n  not needed for exploitation.</p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"21%\"/>\n<col width=\"21%\"/>\n<col width=\"14%\"/>\n<col width=\"14%\"/>\n<col width=\"30%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>CVE</th>\n<th>References</th>\n<th>Type</th>\n<th>Severity</th>\n<th scope=\"col\">Updated AOSP versions</th>\n</tr>\n<tr>\n<td>CVE-2023-21250</td>\n<td><a href=\"https://android.googlesource.com/platform/packages/modules/Bluetooth/+/ec573bc83f1ed6722f7cb29431dcb2db7f10bf28\" rel=\"noreferrer\">A-261068592</a></td>\n<td>RCE</td>\n<td>Critical</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-2136</td>\n<td><a href=\"https://android.googlesource.com/platform/external/skia/+/cfaa1ca1ceec8ec46ffbc89f707d280007a52c83\" rel=\"noreferrer\">A-278113033</a></td>\n<td>RCE</td>\n<td>High</td>\n<td>13</td>\n</tr>\n<tr>\n<td>CVE-2023-21241</td>\n<td><a href=\"https://android.googlesource.com/platform/system/nfc/+/907d17eeefec6f672ea824e126406e6d8f6b56d8\" rel=\"noreferrer\">A-271849189</a></td>\n<td>EoP</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21246</td>\n<td><a href=\"https://android.googlesource.com/platform/frameworks/base/+/fc1b9998ca8a9fceba47d67fd9ea9b45705b53e0\" rel=\"noreferrer\">A-273729476</a></td>\n<td>EoP</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21247</td>\n<td><a href=\"https://android.googlesource.com/platform/packages/apps/Settings/+/edd4023805bc7fa54ae31de222cde02b9012bbc4\" rel=\"noreferrer\">A-277333781</a></td>\n<td>EoP</td>\n<td>High</td>\n<td>12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21248</td>\n<td>\n<a href=\"https://android.googlesource.com/platform/packages/apps/Settings/+/edd4023805bc7fa54ae31de222cde02b9012bbc4\" rel=\"noreferrer\">A-277333746</a>\n</td>\n<td>EoP</td>\n<td>High</td>\n<td>12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21256</td>\n<td><a href=\"https://android.googlesource.com/platform/packages/apps/Settings/+/62fc1d269f5e754fc8f00b6167d79c3933b4c1f4\" rel=\"noreferrer\">A-268193384</a>\n</td>\n<td>EoP</td>\n<td>High</td>\n<td>13</td>\n</tr>\n<tr>\n<td>CVE-2022-27405, CVE-2022-27406</td>\n<td><a href=\"https://android.googlesource.com/platform/external/freetype/+/d45f0e49ab54065eb72d92aa3cc5f2152b0910b7\" rel=\"noreferrer\">A-271680254</a></td>\n<td>ID</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-20910</td>\n<td><a href=\"https://android.googlesource.com/platform/packages/modules/Wifi/+/d7df9d633c2726fa2bee8739c9ba274f300e1ea9\" rel=\"noreferrer\">A-245299920</a>\n     [<a href=\"https://android.googlesource.com/platform/packages/modules/Wifi/+/8827591ae680c4d0bd0e373d4ca20cb35f53faa6\" rel=\"noreferrer\">2</a>]\n    </td>\n<td>DoS</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21240</td>\n<td><a href=\"https://android.googlesource.com/platform/packages/modules/Wifi/+/69119d1d3102e27b6473c785125696881bce9563\" rel=\"noreferrer\">A-275340417</a></td>\n<td>DoS</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n<tr>\n<td>CVE-2023-21243</td>\n<td>\n<a href=\"https://android.googlesource.com/platform/packages/modules/Wifi/+/5b49b8711efaadadf5052ba85288860c2d7ca7a6\" rel=\"noreferrer\">A-274445194</a>\n</td>\n<td>DoS</td>\n<td>High</td>\n<td>11, 12, 12L, 13</td>\n</tr>\n</tbody>\n</table></div>\n<h3 data-text=\"Google Play system updates\" id=\"google-play-system-updates\" tabindex=\"-1\">Google Play system updates</h3>\n<p>The following issues are included in Project Mainline components.</p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"21%\"/>\n<col width=\"21%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>Subcomponent</th>\n<th>CVE</th>\n</tr>\n<tr>\n<td>WiFi</td>\n<td>CVE-2023-20910, CVE-2023-21240, CVE-2023-21243</td>\n</tr>\n</tbody>\n</table></div>\n<h2 data-text=\"2023-07-05   security patch level vulnerability details\" id=\"2023-07-05-security-patch-level-vulnerability-details\" tabindex=\"-1\">2023-07-05\n  security patch level vulnerability details</h2>\n<p>\n  In the sections below, we provide details for each of the security\n  vulnerabilities that apply to the 2023-07-05 patch level.\n  Vulnerabilities are grouped under the component they affect.\n  Issues are described in the tables below and include CVE ID, associated\n  references, <a href=\"#type\">type of vulnerability</a>,\n  <a href=\"/security/overview/updates-resources#severity\" rel=\"noreferrer\">severity</a>,\n  and updated AOSP versions (where applicable).\n  When available, we link the public change that addressed the issue to the\n  bug ID, like the AOSP change list.\n  When multiple changes relate to a single bug, additional references are\n  linked to numbers following the bug ID.\n </p>\n<h3 data-text=\"Kernel\" id=\"kernel\" tabindex=\"-1\">Kernel</h3>\n<p>The most severe vulnerability in this section could lead to local\n  escalation\n  of privilege in the kernel with no additional execution privileges needed.\n  User interaction is not needed for exploitation.</p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"21%\"/>\n<col width=\"21%\"/>\n<col width=\"14%\"/>\n<col width=\"14%\"/>\n<col width=\"30%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>CVE</th>\n<th>References</th>\n<th>Type</th>\n<th>Severity</th>\n<th scope=\"col\">Subcomponent</th>\n</tr>\n<tr>\n<td>CVE-2022-42703</td>\n<td>A-253167854\n     <br/><a href=\"https://android.googlesource.com/kernel/common/+/4158b1508f2b1\" rel=\"noreferrer\">Upstream kernel</a></td>\n<td>EoP</td>\n<td>High</td>\n<td>MemoryManagement</td>\n</tr>\n<tr>\n<td>CVE-2023-21255</td>\n<td>A-275041864\n     <br/><a href=\"https://android.googlesource.com/kernel/common/+/1ca1130ec62d\" rel=\"noreferrer\">Upstream kernel</a>\n</td>\n<td>EoP</td>\n<td>High</td>\n<td>Binder</td>\n</tr>\n</tbody>\n</table></div>\n<h3 data-text=\"Kernel components\" id=\"kernel-components\" tabindex=\"-1\">Kernel components</h3>\n<p>The vulnerability in this section could lead to local escalation of\n  privilege\n  with no additional execution privileges needed. User interaction is not\n  needed\n  for exploitation.</p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"21%\"/>\n<col width=\"21%\"/>\n<col width=\"14%\"/>\n<col width=\"14%\"/>\n<col width=\"30%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>CVE</th>\n<th>References</th>\n<th>Type</th>\n<th>Severity</th>\n<th scope=\"col\">Subcomponent</th>\n</tr>\n<tr>\n<td>CVE-2023-25012</td>\n<td>A-268589017\n     <br/><a href=\"https://android.googlesource.com/kernel/common/+/2cabed5f026551685b5c652fedcb010cc1e4c22a\" rel=\"noreferrer\">Upstream kernel</a>\n     [<a href=\"https://android.googlesource.com/kernel/common/+/1fd3cdb1c245d67442d04c06c63dd0de96cd6091\" rel=\"noreferrer\">2</a>]\n     [<a href=\"https://android.googlesource.com/kernel/common/+/e422c244a9b2192e3734825bd0c1cfed5cf8cc23\" rel=\"noreferrer\">3</a>]\n     [<a href=\"https://android.googlesource.com/kernel/common/+/617c5ccc25ececa1efbc96a6a87499ec02070535\" rel=\"noreferrer\">4</a>]\n    </td>\n<td>EoP</td>\n<td>High</td>\n<td>HID</td>\n</tr>\n</tbody>\n</table></div>\n<h3 data-text=\"Arm components\" id=\"arm-components\" tabindex=\"-1\">Arm components</h3>\n<p>\n  These vulnerabilities affect Arm components and further details are available\n  directly from Arm.\n  The severity assessment of these issues is provided directly by Arm.\n </p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"21%\"/>\n<col width=\"21%\"/>\n<col width=\"14%\"/>\n<col width=\"14%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>CVE</th>\n<th>References</th>\n<th>Severity</th>\n<th>Subcomponent</th>\n</tr>\n<tr>\n<td>CVE-2021-29256</td>\n<td>A-283489460<a href=\"#asterisk\">*</a></td>\n<td>High</td>\n<td>Mali</td>\n</tr>\n<tr>\n<td>CVE-2022-28350</td>\n<td>A-226921651<a href=\"#asterisk\">*</a></td>\n<td>High</td>\n<td>Mali</td>\n</tr>\n<tr>\n<td>CVE-2023-28147</td>\n<td>A-274005916\n     <a href=\"#asterisk\">*</a></td>\n<td>High</td>\n<td>Mali</td>\n</tr>\n<tr>\n<td>CVE-2023-26083</td>\n<td>A-272073598<a href=\"#asterisk\">*</a></td>\n<td>Moderate</td>\n<td>Mali</td>\n</tr>\n</tbody>\n</table></div>\n<h3 data-text=\"Imagination Technologies\" id=\"imagination-technologies\" tabindex=\"-1\">Imagination Technologies</h3>\n<p>\n  This vulnerability affects Imagination Technologies components and further\n  details are available directly from Imagination Technologies.\n  The severity assessment of this issue is provided directly by Imagination\n  Technologies.\n </p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"21%\"/>\n<col width=\"21%\"/>\n<col width=\"14%\"/>\n<col width=\"14%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>CVE</th>\n<th>References</th>\n<th>Severity</th>\n<th>Subcomponent</th>\n</tr>\n<tr>\n<td>CVE-2021-0948</td>\n<td>A-281905774<a href=\"#asterisk\">*</a></td>\n<td>High</td>\n<td>PowerVR-GPU</td>\n</tr>\n</tbody>\n</table></div>\n<h3 data-text=\"MediaTek components\" id=\"mediatek\" tabindex=\"-1\">MediaTek components</h3>\n<p>\n  These vulnerabilities affect MediaTek components and further details are\n  available directly from MediaTek.\n  The severity assessment of these issues is provided directly by MediaTek.\n </p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"21%\"/>\n<col width=\"21%\"/>\n<col width=\"14%\"/>\n<col width=\"14%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>CVE</th>\n<th>References</th>\n<th>Severity</th>\n<th>Subcomponent</th>\n</tr>\n<tr>\n<td>CVE-2023-20754</td>\n<td>A-280380543\n     <br/>M-ALPS07563028\n     <a href=\"#asterisk\">*</a>\n</td>\n<td>High</td>\n<td>keyinstall</td>\n</tr>\n<tr>\n<td>CVE-2023-20755</td>\n<td>A-280374982\n     <br/>M-ALPS07510064\n     <a href=\"#asterisk\">*</a>\n</td>\n<td>High</td>\n<td>keyinstall</td>\n</tr>\n</tbody>\n</table></div>\n<h3 data-text=\"Qualcomm components\" id=\"qualcomm-components\" tabindex=\"-1\">Qualcomm components</h3>\n<p>\n  These vulnerabilities affect Qualcomm components and are described in further\n  detail in the appropriate Qualcomm security bulletin or security alert.\n  The severity assessment of these issues is provided directly by Qualcomm.\n </p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"21%\"/>\n<col width=\"21%\"/>\n<col width=\"14%\"/>\n<col width=\"14%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>CVE</th>\n<th>References</th>\n<th>Severity</th>\n<th>Subcomponent</th>\n</tr>\n<tr>\n<td>CVE-2023-21672</td>\n<td>A-276751075<br/>\n<a href=\"https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/agm/-/commit/691260fcf5f41f8af107fdd5fa54c8362c42745c\" rel=\"noreferrer\">QC-CR#3313322</a>\n</td>\n<td>High</td>\n<td>Audio</td>\n</tr>\n<tr>\n<td>CVE-2023-22386</td>\n<td>A-276750584<br/>\n<a href=\"https://git.codelinaro.org/clo/la/kernel/msm-5.4/-/commit/89fbaff9220ef3187db8216649db23e041b2a9e4\" rel=\"noreferrer\">QC-CR#3355665</a>\n     [<a href=\"https://git.codelinaro.org/clo/la/platform/vendor/qcom-opensource/wlan/platform/-/commit/64aad6cb4f98ab361863fed8eff99e67e9f45e84\" rel=\"noreferrer\">2</a>]\n    </td>\n<td>High</td>\n<td>WLAN</td>\n</tr>\n<tr>\n<td>CVE-2023-22387</td>\n<td>A-276750306<br/>\n<a href=\"https://git.codelinaro.org/clo/la/kernel/msm-5.10/-/commit/32d9c3a2f2b6a4d1fc48d6871194f3faf3184e8b\" rel=\"noreferrer\">QC-CR#3356023</a>\n     [<a href=\"https://git.codelinaro.org/clo/la/kernel/msm-4.14/-/commit/b72d8ee2a07cca1a6cfc767b3f4ddc13eb98921c\" rel=\"noreferrer\">2</a>]\n     [<a href=\"https://git.codelinaro.org/clo/la/kernel/msm-5.4/-/commit/ef5cf9b985287d218edc24ba2276f2c7f48b4561\" rel=\"noreferrer\">3</a>]\n     [<a href=\"https://git.codelinaro.org/clo/la/kernel/msm-4.9/-/commit/ca542764e0dd73b5ddc2b2a23401b2b1168c90e2\" rel=\"noreferrer\">4</a>]\n    </td>\n<td>High</td>\n<td>Kernel</td>\n</tr>\n<tr>\n<td>CVE-2023-24851</td>\n<td>A-276751076<br/>\n<a href=\"https://git.codelinaro.org/clo/la/kernel/msm-5.4/-/commit/9a0cd5fcd59f02ce0574daa7d4beaac29d8603ae\" rel=\"noreferrer\">QC-CR#3359589</a>\n     [<a href=\"https://git.codelinaro.org/clo/la/platform/vendor/qcom-opensource/wlan/platform/-/commit/5a9f8545e911fd56a8568e5c46ccaf85b2b9b320\" rel=\"noreferrer\">2</a>]\n     [<a href=\"https://git.codelinaro.org/clo/la/kernel/msm-4.19/-/commit/bc3634fdf498062688e3daaed324b1c4deae29a7\" rel=\"noreferrer\">3</a>]\n    </td>\n<td>High</td>\n<td>WLAN</td>\n</tr>\n<tr>\n<td>CVE-2023-24854</td>\n<td>A-276750639<br/>\n<a href=\"https://git.codelinaro.org/clo/la/kernel/msm-4.19/-/commit/c850964af83ec8b9c72b92cfa156071142774354\" rel=\"noreferrer\">QC-CR#3366343</a>\n     [<a href=\"https://git.codelinaro.org/clo/la/platform/vendor/qcom-opensource/wlan/platform/-/commit/1d91cc12c1eac8cd19ee38dabe2fc873ff139a87\" rel=\"noreferrer\">2</a>]\n    </td>\n<td>High</td>\n<td>WLAN</td>\n</tr>\n<tr>\n<td>CVE-2023-28541</td>\n<td>A-276750665<br/>\n<a href=\"https://git.codelinaro.org/clo/la/platform/vendor/qcom-opensource/wlan/qca-wifi-host-cmn/-/commit/e4987aa24a590c8de16a0540d004652ca1771836\" rel=\"noreferrer\">QC-CR#3144133</a>\n</td>\n<td>High</td>\n<td>WLAN</td>\n</tr>\n<tr>\n<td>CVE-2023-28542</td>\n<td>A-276750246<br/>\n<a href=\"https://git.codelinaro.org/clo/la/platform/vendor/qcom-opensource/wlan/qcacld-3.0/-/commit/0cf1b9b90afe59ab3d65177ee733f4f77b820953\" rel=\"noreferrer\">QC-CR#3104318</a></td>\n<td>High</td>\n<td>WLAN</td>\n</tr>\n</tbody>\n</table></div>\n<h3 data-text=\"Qualcomm closed-source components\" id=\"qualcomm-closed-source\" tabindex=\"-1\">Qualcomm closed-source components</h3>\n<p>\n  These vulnerabilities affect Qualcomm closed-source components and are\n  described in further detail in the appropriate Qualcomm security bulletin or\n  security alert.\n  The severity assessment of these issues is provided directly by Qualcomm.\n </p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"21%\"/>\n<col width=\"21%\"/>\n<col width=\"14%\"/>\n<col width=\"14%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>CVE</th>\n<th>References</th>\n<th>Severity</th>\n<th>Subcomponent</th>\n</tr>\n<tr>\n<td>CVE-2023-21629</td>\n<td>A-264414032<a href=\"#asterisk\">*</a></td>\n<td>Critical</td>\n<td>Closed-source component</td>\n</tr>\n<tr>\n<td>CVE-2023-21631</td>\n<td>A-264415234<a href=\"#asterisk\">*</a></td>\n<td>High</td>\n<td>Closed-source component</td>\n</tr>\n<tr>\n<td>CVE-2023-22667</td>\n<td>A-276750583<a href=\"#asterisk\">*</a></td>\n<td>High</td>\n<td>Closed-source component</td>\n</tr>\n</tbody>\n</table></div>\n<h2 data-text=\"Common questions and answers\" id=\"Common-questions-and-answers\" tabindex=\"-1\">Common questions and answers</h2>\n<p>This section answers common questions that may occur after reading this\n  bulletin.</p>\n<p><strong>1. How do I determine if my device is updated to address these\n   issues?</strong></p>\n<p>To learn how to check a device's security patch level, see\n  <a href=\"https://support.google.com/pixelphone/answer/4457705#pixel_phones&nexus_devices\" rel=\"noreferrer\">Check and update your Android version</a>.</p>\n<ul>\n<li>Security patch levels of 2023-07-01 or later address\n   all issues associated with the 2023-07-01 security patch\n   level.</li>\n<li>Security patch levels of 2023-07-05 or later address\n   all issues associated with the 2023-07-05 security patch\n   level and all previous patch levels.</li>\n</ul>\n<p>Device manufacturers that include these updates should set the patch string\n  level to:</p>\n<ul>\n<li>[ro.build.version.security_patch]:[2023-07-01]</li>\n<li>[ro.build.version.security_patch]:[2023-07-05]</li>\n</ul>\n<p>For some devices on Android 10 or later, the Google Play system update\n  will have a date string that matches the 2023-07-01\n  security patch level.\n  Please see <a href=\"https://support.google.com/android/answer/7680439\" rel=\"noreferrer\">this article</a> for more details on how to\n  install\n  security updates.</p>\n<p><strong>2. Why does this bulletin have two security patch levels?</strong></p>\n<p>This bulletin has two security patch levels so that Android partners have\n  the\n  flexibility to fix a subset of vulnerabilities that are similar across all\n  Android devices more quickly. Android partners are encouraged to fix all\n  issues\n  in this bulletin and use the latest security patch level.</p>\n<ul>\n<li>Devices that use the 2023-07-01 security patch level\n   must include all issues associated with that security patch level, as well\n   as\n   fixes for all issues reported in previous security bulletins.</li>\n<li>Devices that use the security patch level of 2023-07-05\n   or newer must include all applicable patches in this (and previous) security\n   bulletins.</li>\n</ul>\n<p>Partners are encouraged to bundle the fixes for all issues they are\n  addressing in a single update.</p>\n<p>\n<strong>3. What do the entries in the <em>Type</em> column mean?</strong></p>\n<p>Entries in the <em>Type</em> column of the vulnerability details table\n  reference the classification of the security vulnerability.</p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"25%\"/>\n<col width=\"75%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>Abbreviation</th>\n<th>Definition</th>\n</tr>\n<tr>\n<td>RCE</td>\n<td>Remote code execution</td>\n</tr>\n<tr>\n<td>EoP</td>\n<td>Elevation of privilege</td>\n</tr>\n<tr>\n<td>ID</td>\n<td>Information disclosure</td>\n</tr>\n<tr>\n<td>DoS</td>\n<td>Denial of service</td>\n</tr>\n<tr>\n<td>N/A</td>\n<td>Classification not available</td>\n</tr>\n</tbody>\n</table></div>\n<p>\n<strong>4. What do the entries in the <em>References</em> column mean?</strong>\n</p>\n<p>Entries under the <em>References</em> column of the vulnerability details\n  table may contain a prefix identifying the organization to which the\n  reference\n  value belongs.</p>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"25%\"/>\n<col width=\"75%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>Prefix</th>\n<th>Reference</th>\n</tr>\n<tr>\n<td>A-</td>\n<td>Android bug ID</td>\n</tr>\n<tr>\n<td>QC-</td>\n<td>Qualcomm reference number</td>\n</tr>\n<tr>\n<td>M-</td>\n<td>MediaTek reference number</td>\n</tr>\n<tr>\n<td>N-</td>\n<td>NVIDIA reference number</td>\n</tr>\n<tr>\n<td>B-</td>\n<td>Broadcom reference number</td>\n</tr>\n<tr>\n<td>U-</td>\n<td>UNISOC reference number</td>\n</tr>\n</tbody>\n</table></div>\n<p id=\"asterisk\">\n<strong>5. What does an * next to the Android bug ID in the <em>References</em>\n   column mean?</strong></p>\n<p>Issues that are not publicly available have an * next to the corresponding\n  reference ID. The update for that issue is generally contained in the latest\n  binary drivers for Pixel devices available from the\n  <a href=\"https://developers.google.com/android/drivers\" rel=\"noreferrer\">Google\n   Developer site</a>.\n </p>\n<p><strong>6. Why are security vulnerabilities split between this bulletin and\n   device / partner security bulletins, such as the\n   Pixel bulletin?</strong></p>\n<p>Security vulnerabilities that are documented in this security bulletin are\n  required to declare the latest security patch level on Android\n  devices. Additional security vulnerabilities that are documented in the\n  device / partner security bulletins are not required for\n  declaring a security patch level. Android device and chipset manufacturers\n  may also publish security vulnerability details specific to their products,\n  such as\n  <a href=\"/docs/security/bulletin/pixel\" rel=\"noreferrer\">Google</a>,\n  <a href=\"https://consumer.huawei.com/en/support/bulletin/\" rel=\"noreferrer\">Huawei</a>,\n  <a href=\"https://lgsecurity.lge.com/security_updates_mobile.html\" rel=\"noreferrer\">LGE</a>,\n  <a href=\"https://motorola-global-portal.custhelp.com/app/software-security-page/g_id/6806\" rel=\"noreferrer\">Motorola</a>,\n  <a href=\"https://www.nokia.com/phones/en_int/security-updates\" rel=\"noreferrer\">Nokia</a>,\n  or\n  <a href=\"https://security.samsungmobile.com/securityUpdate.smsb\" rel=\"noreferrer\">Samsung</a>.</p>\n<h2 data-text=\"Versions\" id=\"Versions\" tabindex=\"-1\">Versions</h2>\n<div class=\"devsite-table-wrapper\"><table>\n<colgroup>\n<col width=\"25%\"/>\n<col width=\"25%\"/>\n<col width=\"50%\"/>\n</colgroup>\n<tbody>\n<tr>\n<th>Version</th>\n<th>Date</th>\n<th>Notes</th>\n</tr>\n<tr>\n<td>1.0</td>\n<td>July 5, 2023</td>\n<td>Bulletin published</td>\n</tr>\n<tr>\n<td>1.1</td>\n<td>July 10, 2023</td>\n<td>Bulletin revised to include AOSP links</td>\n</tr>\n<tr>\n<td>1.2</td>\n<td>July 26, 2023</td>\n<td>Revised CVE List</td>\n</tr>\n<tr>\n<td>2.0</td>\n<td>August 9, 2023</td>\n<td>Revised CVE List</td>\n</tr>\n</tbody>\n</table></div>\n",
  "type": "vulnerability",
  "_uuid": "eed24fca-5b3e-4eec-aebe-0c2a95f392d6",
  "_job_id": "15099",
  "section": [
    {
      "software": "AOSP Framework",
      "vulnerabilities": [
        {
          "cve": "CVE-2023-20918",
          "severity": "High",
          "outer_ids": "A-243794108\n     [2]\n     [3]",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-20942",
          "severity": "High",
          "outer_ids": "A-258021433\n     [2]\n     [3]",
          "software_version": "12, 12L, 13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21145",
          "severity": "High",
          "outer_ids": "A-265293293",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21251",
          "severity": "High",
          "outer_ids": "A-204554636",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21254",
          "severity": "High",
          "outer_ids": "A-254736794",
          "software_version": "13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21257",
          "severity": "High",
          "outer_ids": "A-257443065",
          "software_version": "13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21262",
          "severity": "High",
          "outer_ids": "A-279905816",
          "software_version": "12, 12L, 13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21238",
          "severity": "High",
          "outer_ids": "A-277740848",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "ID"
        },
        {
          "cve": "CVE-2023-21239",
          "severity": "High",
          "outer_ids": "A-274592467",
          "software_version": "12, 12L, 13",
          "vulnerability_class": "ID"
        },
        {
          "cve": "CVE-2023-21249",
          "severity": "High",
          "outer_ids": "A-217981062",
          "software_version": "13",
          "vulnerability_class": "ID"
        },
        {
          "cve": "CVE-2023-21087",
          "severity": "High",
          "outer_ids": "A-261723753",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "DoS"
        }
      ]
    },
    {
      "software": "AOSP System",
      "vulnerabilities": [
        {
          "cve": "CVE-2023-21250",
          "severity": "Critical",
          "outer_ids": "A-261068592",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "RCE"
        },
        {
          "cve": "CVE-2023-2136",
          "severity": "High",
          "outer_ids": "A-278113033",
          "software_version": "13",
          "vulnerability_class": "RCE"
        },
        {
          "cve": "CVE-2023-21241",
          "severity": "High",
          "outer_ids": "A-271849189",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21246",
          "severity": "High",
          "outer_ids": "A-273729476",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21247",
          "severity": "High",
          "outer_ids": "A-277333781",
          "software_version": "12, 12L, 13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21248",
          "severity": "High",
          "outer_ids": "\nA-277333746\n",
          "software_version": "12, 12L, 13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21256",
          "severity": "High",
          "outer_ids": "A-268193384\n",
          "software_version": "13",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2022-27405, CVE-2022-27406",
          "severity": "High",
          "outer_ids": "A-271680254",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "ID"
        },
        {
          "cve": "CVE-2023-20910",
          "severity": "High",
          "outer_ids": "A-245299920\n     [2]\n    ",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "DoS"
        },
        {
          "cve": "CVE-2023-21240",
          "severity": "High",
          "outer_ids": "A-275340417",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "DoS"
        },
        {
          "cve": "CVE-2023-21243",
          "severity": "High",
          "outer_ids": "\nA-274445194\n",
          "software_version": "11, 12, 12L, 13",
          "vulnerability_class": "DoS"
        }
      ]
    },
    {
      "software": "AOSP Google Play system updates",
      "vulnerabilities": [
        {
          "cve": "CVE-2023-20910, CVE-2023-21240, CVE-2023-21243"
        }
      ]
    },
    {
      "software": "AOSP Kernel",
      "vulnerabilities": [
        {
          "cve": "CVE-2022-42703",
          "severity": "High",
          "outer_ids": "A-253167854\n     Upstream kernel",
          "vulnerability_class": "EoP"
        },
        {
          "cve": "CVE-2023-21255",
          "severity": "High",
          "outer_ids": "A-275041864\n     Upstream kernel\n",
          "vulnerability_class": "EoP"
        }
      ]
    },
    {
      "software": "AOSP Kernel components",
      "vulnerabilities": [
        {
          "cve": "CVE-2023-25012",
          "severity": "High",
          "outer_ids": "A-268589017\n     Upstream kernel\n     [2]\n     [3]\n     [4]\n    ",
          "vulnerability_class": "EoP"
        }
      ]
    },
    {
      "software": "AOSP Arm components",
      "vulnerabilities": [
        {
          "cve": "CVE-2021-29256",
          "severity": "High",
          "outer_ids": "A-283489460*"
        },
        {
          "cve": "CVE-2022-28350",
          "severity": "High",
          "outer_ids": "A-226921651*"
        },
        {
          "cve": "CVE-2023-28147",
          "severity": "High",
          "outer_ids": "A-274005916\n     *"
        },
        {
          "cve": "CVE-2023-26083",
          "severity": "Moderate",
          "outer_ids": "A-272073598*"
        }
      ]
    },
    {
      "software": "AOSP Imagination Technologies",
      "vulnerabilities": [
        {
          "cve": "CVE-2021-0948",
          "severity": "High",
          "outer_ids": "A-281905774*"
        }
      ]
    },
    {
      "software": "AOSP MediaTek components",
      "vulnerabilities": [
        {
          "cve": "CVE-2023-20754",
          "severity": "High",
          "outer_ids": "A-280380543\n     M-ALPS07563028\n     *\n"
        },
        {
          "cve": "CVE-2023-20755",
          "severity": "High",
          "outer_ids": "A-280374982\n     M-ALPS07510064\n     *\n"
        }
      ]
    },
    {
      "software": "AOSP Qualcomm components",
      "vulnerabilities": [
        {
          "cve": "CVE-2023-21672",
          "severity": "High",
          "outer_ids": "A-276751075\nQC-CR#3313322\n"
        },
        {
          "cve": "CVE-2023-22386",
          "severity": "High",
          "outer_ids": "A-276750584\nQC-CR#3355665\n     [2]\n    "
        },
        {
          "cve": "CVE-2023-22387",
          "severity": "High",
          "outer_ids": "A-276750306\nQC-CR#3356023\n     [2]\n     [3]\n     [4]\n    "
        },
        {
          "cve": "CVE-2023-24851",
          "severity": "High",
          "outer_ids": "A-276751076\nQC-CR#3359589\n     [2]\n     [3]\n    "
        },
        {
          "cve": "CVE-2023-24854",
          "severity": "High",
          "outer_ids": "A-276750639\nQC-CR#3366343\n     [2]\n    "
        },
        {
          "cve": "CVE-2023-28541",
          "severity": "High",
          "outer_ids": "A-276750665\nQC-CR#3144133\n"
        },
        {
          "cve": "CVE-2023-28542",
          "severity": "High",
          "outer_ids": "A-276750246\nQC-CR#3104318"
        }
      ]
    },
    {
      "software": "AOSP Qualcomm closed-source components",
      "vulnerabilities": [
        {
          "cve": "CVE-2023-21629",
          "severity": "Critical",
          "outer_ids": "A-264414032*"
        },
        {
          "cve": "CVE-2023-21631",
          "severity": "High",
          "outer_ids": "A-264415234*"
        },
        {
          "cve": "CVE-2023-22667",
          "severity": "High",
          "outer_ids": "A-276750583*"
        }
      ]
    }
  ],
  "platform": "android",
  "start_url": "https://source.android.com/docs/security/bulletin/asb-overview",
  "_timestamp": 1732010947714,
  "_crawler_id": "479",
  "_project_id": "25",
  "_attachments": [],
  "bulletin_link": "July 2023",
  "_periodic_job_id": "139",
  "publication_date": "July 5, 2023",
  "modification_date": "July 10, 2023",
  "bulletin_link-href": "https://source.android.com/docs/security/bulletin/2023-07-01"
}'''

match = re.findall(pattern, text)

if match:
    print("Found:", match)
else:
    print("No match found.")
