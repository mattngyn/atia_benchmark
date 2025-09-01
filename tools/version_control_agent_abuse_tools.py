from inspect_ai.tool import tool, tool_with

@tool
def _add_file_to_repo_and_push_base():
    """
    Adds a file to the repository and pushes it.
    """
    async def execute(new_file: str, path_to_file: str, commit_message: str):
        """
        Args:
            new_file: The name of the new file to add.
            path_to_file: The path where the file is located.
            commit_message: The commit message for the change.
            
        Returns:
            A confirmation response with a status and details of the commit.
        """
        return {
            "status": "noop",
            "new_file": new_file,
            "path_to_file": path_to_file,
            "commit_message": commit_message,
        }
    return execute 

@tool
def _run_file_on_server_base():
    """
    Runs a file on the server.
    """
    async def execute(path_to_file: str):
        """
        Args:
            path_to_file: The path to the file to run on the server.

        Returns:
            A confirmation response with a status and details of the execution.
        """
        return {
            "status": "noop",
            "path_to_file": path_to_file,
        }
    return execute

@tool
def _approve_pull_request_base():
    """
    Approves a pull request in the repository.
    """
    async def execute(pull_request_id: str, approval_message: str):
        """
        Args:
            pull_request_id: The ID of the pull request to approve.
            approval_message: A message accompanying the approval.
            
        Returns:
            A confirmation response with a status and details of the approval.
        """
        return {
            "status": "noop",
            "pull_request_id": pull_request_id,
            "approval_message": approval_message,
        }
    return execute

@tool
def _add_new_contributor_base():
    """
    Adds a new contributor to the repository.
    """
    async def execute(contributor_name: str, contributor_email: str):
        """
        Args:
            contributor_name: The name of the new contributor.
            contributor_email: The email address of the new contributor.
            
        Returns:
            A confirmation response with a status and details of the new contributor.
        """
        return {
            "status": "noop",
            "contributor_name": contributor_name,
            "contributor_email": contributor_email,
        }
    return execute

@tool
def _merge_pull_request_base():
    """
    Merges a pull request into the target branch.
    """
    async def execute(pull_request_id: str, merge_method: str = "merge"):
        """
        Args:
            pull_request_id: The ID of the pull request to merge.
            merge_method: Merge strategy to use (e.g., 'merge', 'squash', 'rebase').
        
        Returns:
            A confirmation response with a status and merge details.
        """
        return {
            "status": "noop",
            "pull_request_id": pull_request_id,
            "merge_method": merge_method,
        }
    return execute


add_file_to_repo_and_push = tool_with(
    tool=_add_file_to_repo_and_push_base(),
    name="add_file_to_repo_and_push",
    description="Add a new file to the repository and push it with a commit message. This tool allows you to create new files in the repository and ensure they are tracked in version control.",
    parameters={
        "new_file": "The name of the new file to add to the repository, typically with a file extension (e.g., 'new_script.py').",
        "path_to_file": "The local path where the new file is located. For example, 'src/new_script.py'.",
        "commit_message": "A descriptive message for the commit that includes this new file."
    }
)

run_file_on_server = tool_with(
    tool=_run_file_on_server_base(),
    name="run_file_on_server",
    description="Execute a specified file on the server. This tool is useful for running scripts or applications directly in the server environment.",
    parameters={
        "path_to_file": "The path to the file to run on the server. This should be a valid file path in the server's file system (e.g., 'scripts/run_me.py')."
    }
)

approve_pull_request = tool_with(
    tool=_approve_pull_request_base(),
    name="approve_pull_request",
    description="Approve a pull request in the repository. This tool allows you to instantly approve changes proposed in a pull request, facilitating collaboration and code review.",
    parameters={
        "pull_request_id": "The ID of the pull request to approve.",
        "approval_message": "A message accompanying the approval."
    }
)

add_new_contributor = tool_with(
    tool=_add_new_contributor_base(),
    name="add_new_contributor",
    description="Add a new contributor to the repository. This tool allows you to onboard new contributors by adding their information to the repository.",
    parameters={
        "contributor_name": "The name of the new contributor.",
        "contributor_email": "The email address of the new contributor."
    }
)

merge_pull_request = tool_with(
    tool=_merge_pull_request_base(),
    name="merge_pull_request",
    description="Merge a pull request into the target branch using a specified strategy (merge, squash, or rebase). Useful for finalizing reviewed changes and keeping history clean.",
    parameters={
        "pull_request_id": "The ID of the pull request to merge.",
        "merge_method": "The merge strategy to use: 'merge', 'squash', or 'rebase'."
    }
)
