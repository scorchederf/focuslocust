---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Liferay

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cheatsheets-liferay` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/liferay.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Liferay](../../topics/cheatsheets/liferay.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cheatsheets-liferay |
| name | Liferay |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cheatsheets/liferay.md |

## Preserved Source Material

````yaml
_body: "# Liferay\n\n> Liferay Portal is an open-source enterprise portal platform used for building web applications and\
  \ digital experiences. It provides features like content management, user authentication, collaboration tools, and customizable\
  \ dashboards. - [liferay/liferay-portal](https://github.com/liferay/liferay-portal)\n\n## Summary\n\n* [Portlets](#portlets)\n\
  * [Login Page](#login-page)\n* [Register Page](#register-page)\n* [User Profile](#user-configuration)\n* [User Configuration](#user-configuration)\n\
  * [Control Panel](#control-panel)\n* [API](#api)\n* [Vulnerabilities](#vulnerabilities)\n    * [Open Redirect](#open-redirect)\n\
  \    * [Code Execution on Administrator Control Panel](#code-execution-on-administrator-control-panel)\n    * [Resource\
  \ Leakage Through I18nServlet](#resource-leakage-through-i18nservlet)\n    * [Remote Code Execution via JSON web services](#remote-code-execution-via-json-web-services)\n\
  * [References](#references)\n\n## Portlets\n\n```ps1\n/?p_p_id=<portlet_ID>&p_p_lifecycle=0&p_p_state=<window_state>&p_p_mode=<mode>\n\
  ```\n\n* **portlet_ID**: ID of the portlet to be executed. Can be a numeric ID, which is an incremental number for each\
  \ portlet, or a [liferay.com/Fully-Qualified-Portlet-IDs](https://help.liferay.com/hc/en-us/articles/360018511712-Fully-Qualified-Portlet-IDs),\
  \ which is a string.\n\n* **window_state**: Amount of space a portlet takes up on a page. Values are: normal, maximized\n\
  minimized\n\n* **mode**: Portlet's current function. Values are: view, edit, help\n\n| Name                | Portlet ID\
  \ |\n| ------------------- | ---------- |\n| Asset Publisher     | com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet\
  \ |\n| Documents and Media | com_liferay_document_library_web_portlet_DLPortlet |\n| Navigation Menu     | com_liferay_site_navigation_menu_web_portlet_SiteNavigationMenuPortlet\
  \ |\n| Site Map            | com_liferay_site_navigation_site_map_web_portlet_SiteNavigationSiteMapPortlet |\n| Web Content\
  \ Display | com_liferay_journal_content_web_portlet_JournalContentPortlet |\n| Search Bar          | com_liferay_portal_search_web_search_bar_portlet_SearchBarPortlet\
  \ |\n| Search              | com_liferay_portal_search_web_portlet_SearchPortlet |\n\n## Login Page\n\n```ps1\n/login\n\
  /c/portal/login\n/?p_p_id=58&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view\n/?p_p_id=58&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&saveLastPath=false&_58_struts_action=%2Flogin%2Flogin\n\
  /?p_p_id=com_liferay_login_web_portlet_LoginPortlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view\n/?p_p_id=com_liferay_login_web_portlet_LoginPortlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&saveLastPath=false&_58_struts_action=%2Flogin%2Flogin\n\
  ```\n\n## Register Page\n\n```ps1\n/?p_p_id=58&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&_com_liferay_login_web_portlet_LoginPortlet_mvcRenderCommandName=%2Flogin%2Fcreate_account\n\
  /?p_p_id=58&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&saveLastPath=false&_58_struts_action=%2Flogin%2Flogin&_com_liferay_login_web_portlet_LoginPortlet_mvcRenderCommandName=%2Flogin%2Fcreate_account\n\
  /?p_p_id=com_liferay_login_web_portlet_LoginPortlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&_com_liferay_login_web_portlet_LoginPortlet_mvcRenderCommandName=%2Flogin%2Fcreate_account\n\
  /?p_p_id=com_liferay_login_web_portlet_LoginPortlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&saveLastPath=false&_58_struts_action=%2Flogin%2Flogin&_com_liferay_login_web_portlet_LoginPortlet_mvcRenderCommandName=%2Flogin%2Fcreate_account\n\
  ```\n\n## User Profile\n\n```ps1\n/web/<user>\n/web/<user>/home\n/user/<other_user>/control_panel/manage\n/user/<other_user>/~/control_panel/manage\n\
  /web/guest\n/web/guest/home\n```\n\n## User Configuration\n\n```ps1\n/user/<user>\n/user/<user>/manage\n/user/<user>/manage?p_p_id=com_liferay_my_account_web_portlet_MyAccountPortlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view\n\
  /group/control_panel/manage?p_p_id=com_liferay_my_account_web_portlet_MyAccountPo\n```\n\n## Control Panel\n\nEndpoints\
  \ reachable by authenticated users.\n\n```ps1\n/group/control_panel/manage\n/group/guest/control_panel/manage\n/group/guest/~/control_panel/manage\n\
  /group/<user>/control_panel/manage\n/group/<user>/~/control_panel/manage\n/user/<user>/control_panel/manage\n/user/<user>/~/control_panel/manage\n\
  ```\n\n## API\n\n* [nuclei-templates/http/misconfiguration/liferay/liferay-axis.yaml](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/misconfiguration/liferay/liferay-axis.yaml)\n\
  * [nuclei-templates/http/misconfiguration/liferay/liferay-jsonws.yaml](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/misconfiguration/liferay/liferay-jsonws.yaml)\n\
  * [nuclei-templates/http/misconfiguration/liferay/liferay-api.yaml](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/misconfiguration/liferay/liferay-api.yaml)\n\
  \n| Name              | Path          |\n| ----------------- | ------------- |\n| JSON Web Services | `/api/jsonws` |\n\
  | SOAP              | `/api/axis`   |\n| GraphQL           | `/o/graphql`  |\n| JSON and GraphQL  | `/o/api`      |\n\n\
  ## Vulnerabilities\n\n* [liferay.dev/known-vulnerabilities](https://liferay.dev/portal/security/known-vulnerabilities)\n\
  * [ilmila/J2EEScan](https://github.com/ilmila/J2EEScan/blob/master/src/main/java/burp/j2ee/issues/impl/LiferayAPI.java)\n\
  \n### Open Redirect\n\n```ps1\n/html/common/referer_jsp.jsp?referer=<url>\n/html/common/referer_js.jsp?referer=<url>\n/html/common/forward_jsp.jsp?FORWARD_URL=<url>\n\
  /html/common/forward_js.jsp?FORWARD_URL=<url>\n```\n\n### Code Execution on Administrator Control Panel\n\nGogo shell, read\
  \ files\n\n```ps1\n/group/control_panel/manage?p_p_id=com_liferay_gogo_shell_web_internal_portlet_GogoShellPortlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&_com_liferay_gogo_shell_web_internal_portlet_GogoShellPortlet_javax.portlet.action=executeCommand\n\
  ```\n\nGroovy Interpreter\n\n```ps1\n/group/control_panel/manage?p_p_id=com_liferay_server_admin_web_portlet_ServerAdminPortlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&_com_liferay_server_admin_web_portlet_ServerAdminPortlet_mvcRenderCommandName=%2Fserver_admin%2Fview&_com_liferay_server_admin_web_portlet_ServerAdminPortlet_tabs1=script\n\
  ```\n\n### Resource Leakage Through I18nServlet\n\nLiferay is vulnerable to local file inclusion in the I18n Servlet because\
  \ it leaks information via sending an HTTP request to /[language]/[resource];.js (also .jsp works). [nuclei-templates/http/vulnerabilities/j2ee/liferay-resource-leak.yaml](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/vulnerabilities/j2ee/liferay-resource-leak.yaml)\n\
  \n* Liferay Portal 7.3.0 GA1\n* Liferay Portal 7.0.2 GA3\n\n### Remote Code Execution via JSON web services\n\n* [nuclei-templates/http/cves/2020/CVE-2020-7961.yaml](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2020/CVE-2020-7961.yaml)\n\
  \n## References\n\n* [Pentesting Liferay Applications - Víctor Fresco - February 6, 2025](https://www.tarlogic.com/blog/pentesting-liferay-applications/)\n\
  * [How to exploit Liferay CVE-2020-7961 : quick journey to PoC - Thomas Etrillard - March 30, 2020](https://www.synacktiv.com/en/publications/how-to-exploit-liferay-cve-2020-7961-quick-journey-to-poc.html)"
_relative_path: cheatsheets/liferay.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/liferay.md
````
