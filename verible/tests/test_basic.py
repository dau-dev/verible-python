def test_import():
    import verible

    assert verible.__version__


def test_cli_import():
    from verible.cli import VERIBLE_TOOLS

    assert len(VERIBLE_TOOLS) > 0
