def test_import():
    import verible

    assert isinstance(verible.__version__, str)


def test_cli_import():
    from verible.cli import VERIBLE_TOOLS

    assert len(VERIBLE_TOOLS) > 0
