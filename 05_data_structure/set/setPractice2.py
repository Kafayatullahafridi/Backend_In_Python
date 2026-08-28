python_users = {"Ali", "Sara", "Ahmed"}
javascript_users = {"Sara", "Zain", "Ahmed"}
know_each = python_users | javascript_users
print(know_each)
know_python = python_users-javascript_users#reverse of this will be JS
print(know_python)
symmetric_diff = python_users ^javascript_users
print(symmetric_diff)
user_permissions = {"read", "write"}
required_permissions = {"read", "write", "delete"}
user_missing =  required_permissions-user_permissions
print(user_missing)

basic = {"read", "write"}
admin = {"read", "write", "delete", "manage_users"}
print(basic<=admin)
print(admin<=basic)
frontend_team = {"Ali", "Sara"}
backend_team = {"Ahmed", "Zain"}
print(frontend_team.isdisjoint(backend_team))
old_permissions = {
    "read",
    "write",
    "delete"
}

new_permissions = {
    "read",
    "write",
    "export",
    "api_access"
}
removed = old_permissions-new_permissions
added = new_permissions-old_permissions
unchanged = old_permissions & new_permissions
print("Removed permissions:", removed)
print("Added permissions:", added)
print("Unchanged permissions:", unchanged)