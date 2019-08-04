"""opgpcard tests."""

from opgpcard.vcard_utils import gen_vcard_attrs_dict


def test_gen_vcard_attrs_dict():
    fp = 'XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX'
    mail = 'other_example@othermail.com'
    fname = 'otherfname'
    lname = 'otherlname'
    xpath_text_dict = {'fp': fp, 'mail': mail,
                       'fname': fname, 'lname': lname}
    d = gen_vcard_attrs_dict(fname, lname, mail, fp)
    assert xpath_text_dict == d

# TODO: more tests
