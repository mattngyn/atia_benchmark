from inspect_ai import Task, task
from inspect_ai.solver import generate
from scorer_methods.default import harmful_tool_invoked
from solver_methods.default import use_sample_tools
from utils.get_tool_registry import get_tool_registry
from utils.get_dataset import get_dataset

@task(category="account_takeover")
def account_takeover_suite():
    """
    One Task covering all account takeover samples.
    Each sample dynamically loads its own tools based on metadata.
    """
    TOOL_REGISTRY = get_tool_registry("account_takeover")
    return Task(
        dataset=get_dataset("account_takeover"),
        solver=[use_sample_tools(TOOL_REGISTRY), generate()],
        scorer=harmful_tool_invoked(),
    )