"""
application
    __init__.py
    settings.py
    logging.py
    constants.py

core
    models
        __init__.py
        flights.py
        towing.py

    managers
        __init__.py
        flights.py
        towing.py

    storages
        __init__.py
        redis
            __init__.py
            client.py

        postgres
            __init__.py
            client.py

    __init__.py
    broadcaster.py

router
    __init__.py
    http
        __init__.py
        health_check.py
        docs.py
    ws
        __init__.py
        create_manual_block.py
        update_bar.py
        update_linking.py
        get_stand_info.py

background_optimizations
    gluing
        __init__.py
        drop_gluing.py      (use_case)
        towing_gluing.py    (use_case)
    line_optimizations
        __init__.py
        recalculate_lines.py    (use_case)
    conflicts
        __init__.py
        recalculate_flight_conflicts.py     (use_case)

    __init__.py
    tasks.py

integrations
    __init__.py
    variations
        use_cases
            __init__.py
            save_body_colors.py
            save_stands.py
            save_flights.py

        structures
            __init__.py
            body_colors.py
            stand_colors.py

        __init__.py
        client.py

utils
    __init__.py
    http
        __init__.py
        base_client.py
        key_cloak_http_client.py
    time_utils.py
    init_application.py
"""