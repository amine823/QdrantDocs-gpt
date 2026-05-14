---
title: Permission Reference
---
# Permission Reference
This document outlines the permissions available in Qdrant Cloud.
> 💡 When enabling `write:` permissions in the UI, the corresponding `read:` permission will also be enabled and non-actionable. This guarantees access to resources after creating and/or updating them.
## Identity and Access Management
Permissions for users, user roles, management keys, and invitations.
`read:roles` — View roles in the Access Management page.
`write:roles` — Create and modify roles in the Access Management page.
`delete:roles` — Remove roles in the Access Management page.
`read:management_keys` — View Cloud Management Keys in the Access Management page.
`write:management_keys` — Create and manage Cloud Management Keys.
`delete:management_keys` — Remove Cloud Management Keys in the Access Management page.
`write:invites` — Invite new users to an account and revoke invitations.
`read:invites` — View pending invites in an account.
`delete:invites` — Remove an invitation.
`read:users` — View user details in the profile page. Also applicable in User Management and Role details (User tab).
`delete:users` — Remove users from an account. Applicable in User Management and Role details (User tab).
## Cluster
Permissions for API Keys, backups, clusters, and backup schedules.
### API Keys
`read:api_keys` — View Database API Keys for Managed Cloud clusters.
`write:api_keys` — Create new Database API Keys for Managed Cloud clusters.
`delete:api_keys` — Remove Database API Keys for Managed Cloud clusters.
### Backups
`read:backups` — View backups in the Backups page and Cluster details > Backups tab.
`write:backups` — Create backups from the Backups page and Cluster details > Backups tab.
`delete:backups` — Remove backups from the Backups page and Cluster details > Backups tab.
### Clusters
`read:clusters` — View cluster details.
`write:clusters` — Modify cluster settings.
`delete:clusters` — Delete clusters.
### Cluster Data
`read:cluster_data` — View cluster data, used for the Cluster UI button on Cluster Details. Maps to global `read-only` JWT access for the cluster.
`write:cluster_data` — View and modify cluster data, used for the Cluster UI button on Cluster Details. Maps to global `read-write` JWT access for the cluster.
### Backup Schedules
`read:backup_schedules` — View backup schedules in the Backups page and Cluster details > Backups tab.
`write:backup_schedules` — Create backup schedules from the Backups page and Cluster details > Backups tab.
`delete:backup_schedules` — Remove backup schedules from the Backups page and Cluster details > Backups tab.
## Hybrid Cloud
Permissions for Hybrid Cloud environments.
`read:hybrid_cloud_environments` — View Hybrid Cloud environment details.
`write:hybrid_cloud_environments` — Modify Hybrid Cloud environment settings.
`delete:hybrid_cloud_environments` — Delete Hybrid Cloud environments.
## Payment & Billing
Permissions for payment methods and billing information.
`read:payment_information` — View payment methods and billing details.
`write:payment_information` — Modify or remove payment methods and billing details.
## Account Management
Permissions for managing user accounts.
`read:account` — View account details that the user is a part of.
`write:account` — Modify account details such as: Editing the account name Setting an account as default Leaving an account (Only available to Owners)
`delete:account` — Remove an account from: The Profile page (list of user accounts). The active account (if the user is an owner/admin).
## Profile
Permissions for accessing personal profile information.
`read:profile` — View the user’s own profile information. (Assigned to all users by default)
