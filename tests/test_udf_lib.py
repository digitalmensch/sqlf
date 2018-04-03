import sqlf.udf_lib

################################################################################
# Text Processing
################################################################################

def test_match():
    assert sqlf.udf_lib.match('this is a test', ' this is a test')
    assert sqlf.udf_lib.match('This is a Test', 'this IS  a test')
    assert sqlf.udf_lib.match('This-is-a-Test', 'this_is.a.test')
