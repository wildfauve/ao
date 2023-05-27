def selection_fn_caller(team_module, draws):
    for draw in draws:
        [getattr(team_module, f)(draw) for f in dir(team_module) if draw.fn_symbol in f]
