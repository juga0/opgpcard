"""Unit tests for opgpcard.cli"""
from opgpcard.cli import create_args_parser
from opgpcard.opgpcard import validate_args


def test_validate_args():
    """Test validate_args in cases that succed and fail.

    It does not test cases in which validate_args would succed because there
    are keys in the default keyring.
    """
    parser = create_args_parser()
    args = parser.parse_args([])
    # Cases that fail
    # This case might succeed if there'l a default keyring.
    # args = validate_args(args)
    # assert not args
    args = parser.parse_args(['-f', 'somefnamenotinlocalkeyring'])
    args = validate_args(args)
    assert not args
    args = parser.parse_args(['-l', 'somelnamenotinlocalkeyring'])
    args = validate_args(args)
    assert not args
    args = parser.parse_args(['-m', 'someemailnotinlocalkeyring'])
    args = validate_args(args)
    assert not args
    args = parser.parse_args(['-p', 'somefpnotinlocalkeyring'])
    args = validate_args(args)
    assert not args
    args = parser.parse_args(['-f', 'somefnamenotinlocalkeyring',
                              '-m', 'someemailnotinlocalkeyring'])
    args = validate_args(args)
    assert not args
    args = parser.parse_args(['-f', 'somefnamenotinlocalkeyring',
                              '-p', 'somefpnotinlocalkeyring'])
    args = validate_args(args)
    assert not args
    args = parser.parse_args(['-l', 'somelnamenotinlocalkeyring',
                              '-m', 'someemailnotinlocalkeyring'])
    args = validate_args(args)
    assert not args
    args = parser.parse_args(['-l', 'somelnamenotinlocalkeyring',
                              '-p', 'somefpnotinlocalkeyring'])
    args = validate_args(args)
    assert not args
    # Cases that succeed
    args = parser.parse_args(['-f', 'somefnamenotinlocalkeyring',
                              '-m', 'someemailnotinlocalkeyring',
                              '-p', 'somefpnotinlocalkeyring'])
    args = validate_args(args)
    assert args
    args = parser.parse_args(['-l', 'somelnamenotinlocalkeyring',
                              '-m', 'someemailnotinlocalkeyring',
                              '-p', 'somefpnotinlocalkeyring'])
    args = validate_args(args)
    assert args
    args = parser.parse_args(['-f', 'somefnamenotinlocalkeyring',
                              '-l', 'somelnamenotinlocalkeyring',
                              '-m', 'someemailnotinlocalkeyring',
                              '-p', 'somefpnotinlocalkeyring'])
    args = validate_args(args)
    assert args
