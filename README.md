### custom management command
`python manage.py create_feature tenancy tenants create`

### Get forlder structure
`tree -L 3 modules`

### Get all file paths
`find modules -name "*.py"`

### Creates the whole sub-domain skeleton.
`python manage.py create_subdomain tenancy domains`

### Remove all migrations
`find modules -path "*/migrations/*.py" ! -name "__init__.py" -delete`
`find modules -path "*/migrations/*.pyc" -delete`