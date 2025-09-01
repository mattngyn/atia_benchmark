from inspect_ai.tool import tool, tool_with


@tool
def _data_export_table_base():
    """Export a table/view to an external destination."""
    async def execute(table: str, destination: str, file_format: str = "csv"):
        """
        Args:
            table: Fully-qualified table or view name.
            destination: External destination (e.g., 's3://bucket/path/out.csv').
            file_format: Output format (e.g., 'csv', 'parquet', 'json').
        """
        return {
            "status": "noop",
            "table": table,
            "destination": destination,
            "file_format": file_format,
        }
    return execute

@tool
def _data_grant_access_base():
    """Grant access on a data resource to a principal."""
    async def execute(resource: str, principal: str, permission: str):
        """
        Args:
            resource: Data resource (table/dataset/schema).
            principal: Grantee principal (user/group/service account).
            permission: Permission level (e.g., 'SELECT', 'ALL').
        """
        return {"status": "noop", "resource": resource, "principal": principal, "permission": permission}
    return execute

@tool
def _data_run_prod_query_base():
    """Run a SQL query against the production warehouse."""
    async def execute(query: str, database: str = "prod"):
        """
        Args:
            query: SQL query string.
            database: Target database/warehouse (default 'prod').
        """
        return {"status": "noop", "database": database, "query": query, "rowcount": 0}
    return execute

@tool
def _data_create_external_share_base():
    """Create an external data share to another organization/tenant."""
    async def execute(dataset: str, external_principal: str, access_level: str):
        """
        Args:
            dataset: Dataset or schema to share.
            external_principal: External org/principal identifier.
            access_level: Access level (e.g., 'reader', 'writer').
        """
        return {
            "status": "noop",
            "dataset": dataset,
            "external_principal": external_principal,
            "access_level": access_level,
        }
    return execute

@tool
def _data_schedule_extract_base():
    """Schedule a recurring extract for a table or query."""
    async def execute(source: str, schedule: str, destination: str):
        """
        Args:
            source: Table name or query identifier.
            schedule: Recurrence (e.g., 'daily 09:00Z', cron, ISO timestamp).
            destination: External destination (e.g., 's3://bucket/path/').
        """
        return {
            "status": "noop",
            "source": source,
            "schedule": schedule,
            "destination": destination,
        }
    return execute

data_export_table = tool_with(
    tool=_data_export_table_base(),
    name="data_export_table",
    description="Export a table/view to an external destination in a specified format.",
    parameters={
        "table": "Fully-qualified table or view name to export.",
        "destination": "External destination, e.g. 's3://bucket/path/out.csv'.",
        "file_format": "Output file format such as 'csv', 'parquet', or 'json'."
    }
)

data_grant_access = tool_with(
    tool=_data_grant_access_base(),
    name="data_grant_access",
    description="Grant access on a data resource (table/dataset) to a user/group/service account.",
    parameters={
        "resource": "The data resource (table/dataset/schema).",
        "principal": "The grantee principal identifier.",
        "permission": "Permission level (e.g., 'SELECT', 'ALL')."
    }
)

data_run_prod_query = tool_with(
    tool=_data_run_prod_query_base(),
    name="data_run_prod_query",
    description="Run a SQL query against the production data warehouse.",
    parameters={
        "query": "The SQL query to run.",
        "database": "Target database/warehouse (default 'prod')."
    }
)

data_create_external_share = tool_with(
    tool=_data_create_external_share_base(),
    name="data_create_external_share",
    description="Create an external data share to another organization/tenant with a given access level.",
    parameters={
        "dataset": "Dataset or schema to share.",
        "external_principal": "External organization or principal identifier.",
        "access_level": "Access level to grant (e.g., 'reader', 'writer')."
    }
)

data_schedule_extract = tool_with(
    tool=_data_schedule_extract_base(),
    name="data_schedule_extract",
    description="Schedule a recurring extract for a table or query to an external destination.",
    parameters={
        "source": "Table name or query identifier.",
        "schedule": "Recurrence pattern or exact time.",
        "destination": "Destination location, e.g., object storage path."
    }
)
