from inspect_ai.solver import solver
from inspect_ai.solver._task_state import TaskState
from inspect_ai.solver._solver import Generate
@solver
def use_sample_tools(TOOL_REGISTRY):
    """
    Inject tools based on the current sample's metadata.
    Only exposes tools listed in 'harmful_tools' and 'benign_tools' for each sample.
    """
    async def solve(state: TaskState, generate: Generate) -> TaskState:
        harmful_tools = state.metadata.get("harmful_tools", [])
        benign_tools = state.metadata.get("benign_tools", [])
        
        sample_tool_names = set(harmful_tools + benign_tools)
        
        sample_tools = [TOOL_REGISTRY[name] for name in sample_tool_names if name in TOOL_REGISTRY]
        
        state.tools = sample_tools
        state.tool_choice = "auto"
        
        return state
    
    return solve