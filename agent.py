from actions import restart_pipeline, fix_schema, scale_resources

def agentic_loop(log):

    pipeline = log["pipeline"]
    error = log["error"].lower()

    if "connection" in error:
        decision="Restart"
        action=restart_pipeline(pipeline)

    elif "schema" in error:
        decision="Schema Fix"
        action=fix_schema(pipeline)

    elif "memory" in error:
        decision="Scale Resources"
        action=scale_resources(pipeline)

    else:
        decision="Manual"
        action="Manual investigation"

    return decision,action
